import os
import json
import percentmatch
import quicksort
import mergesort
import time
from flask import Flask, render_template, redirect, request, session, url_for, jsonify
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler


app = Flask(__name__, template_folder='Templates', static_folder='Templates')
app.config['SECRET_KEY'] = 'SECRETKEY'


client_id = 'c19a284481e4415c8ae7f7ba9cf5c794'
client_secret = '20a8453aee554ab0b0ec13945f92bb0d'
redirect_uri = 'http://localhost:5000/callback'
scope = 'playlist-read-private'


cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(
  client_id = client_id,
  client_secret = client_secret,
  redirect_uri = redirect_uri,
  scope = scope,
  cache_handler = cache_handler,
  show_dialog = True
)

sp = Spotify(auth_manager = sp_oauth)

# global variables
stored_tracks_info = []
percentmatch_time = 0
quicksort_time = 0
mergesort_time = 0


@app.route('/')
def home():
  if not sp_oauth.validate_token(cache_handler.get_cached_token()):
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)
  return redirect(url_for('get_playlists'))



@app.route('/callback')
def callback():
  error = request.args.get('error')
  if error == 'access_denied':
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)
  else:
    print("Request URL:", request.url)
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('get_playlists'))


@app.route('/get_playlists')
def get_playlists():
  if not sp_oauth.validate_token(cache_handler.get_cached_token()):
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

  # get current users playlists
  playlists = sp.current_user_playlists()
  playlists_info = []

  for pl in playlists['items']:
    playlist_id = pl['id']
    playlist_name = pl['name']
    playlist_url = pl['external_urls']['spotify']

    # Retrieve tracks for the playlist
    playlist_tracks = sp.playlist_tracks(playlist_id)

    # Extract track names
    track_names = [track['track']['name'] for track in playlist_tracks['items']][:15]

    playlists_info.append((playlist_name, playlist_url, playlist_id, track_names))

  return render_template('get_playlists.html', playlists_info=playlists_info)



@app.route('/get_tracks/<playlist_id>')
def get_tracks(playlist_id):
  if not sp_oauth.validate_token(cache_handler.get_cached_token()):
      auth_url = sp_oauth.get_authorize_url()
      return redirect(auth_url)

  # get current playlist's tracks and grab the specific data for use
  tracks = sp.playlist_tracks(playlist_id)
  tracks_info = [track['track']['uri'] for track in tracks['items']]

  # Store tracks
  global stored_tracks_info
  stored_tracks_info = tracks_info

  return jsonify({'tracks_info' : tracks_info})



@app.route('/list_tracks_info')
def list_tracks_info():
  global stored_tracks_info, percentmatch_time, quicksort_time, mergesort_time

  start_time = time.time()
  track_list = percentmatch.TracksToDictionary(stored_tracks_info, 10)
  percentmatch_time = (time.time() - start_time)

  # duplicate list to allow for both sorts
  quicksorted_list = track_list
  start_time = time.time()
  quicksort.quickSort(quicksorted_list, 0, len(quicksorted_list) - 1)
  quicksort_time = (time.time() - start_time)
  quicksorted_list = quicksorted_list[-1:-11:-1]

  mergesorted_list = track_list
  start_time = time.time()
  mergesort.mergeSort(mergesorted_list, 0, len(mergesorted_list) - 1)
  mergesort_time = (time.time() - start_time)
  mergesorted_list =  mergesorted_list[-1:-11:-1]

  # Get playlist names and track sets for each entry (Note: both sorts return the same result so we only need to format one)
  playlist_names, track_sets = percentmatch.get_playlist_data(quicksorted_list)

  # format results
  formatted_results = []
  for index, entry in enumerate(quicksorted_list, start=1):
    playlist_id, match_percent = entry
    playlist_name = playlist_names.get(playlist_id)
    track_set = track_sets.get(playlist_id)
    if playlist_name and track_set:
      formatted_results.append({
        "list_entry": index,
        "playlist_name": playlist_name,
        "match_percentage": match_percent,
        "track_set": list(track_set)
      })


  json_data = {
    'quicksort_time': quicksort_time, 
    'mergesort_time': mergesort_time,
    'formatted_results': formatted_results
  }

  return render_template('list_track_info.html', json_data=json_data)



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))



if __name__ == '__main__':
  app.run(debug = True)
