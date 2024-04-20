import os
import percentmatch
import time
from flask import Flask, render_template, redirect, request, session, url_for, jsonify
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler


app = Flask(__name__)
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

stored_tracks_info = []


@app.route('/')
def home():
  if not sp_oauth.validate_token(cache_handler.get_cached_token()):
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)
  return redirect(url_for('get_playlists'))



@app.route('/callback')
def callback():
  print("Request URL:", request.url)
  sp_oauth.get_access_token(request.args['code'])
  return redirect(url_for('get_playlists'))


@app.route('/get_playlists')
def get_playlists():
  if not sp_oauth.validate_token(cache_handler.get_cached_token()):
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


  playlists = sp.current_user_playlists()
  playlists_info = [(pl['name'], pl['external_urls']['spotify'], pl['id']) for pl in playlists['items']]
  
  # print data (fix format for self) (play with to get selection)
  # base formatting
  #playlists_html = '<br>'.join([f'{name}: {url}: {href}' for name, url, href in playlists_info])

  playlists_html = '<br><br>'.join([f'{name}<br>&emsp;<a href="{url}">{url}</a><br>&emsp;{id}' for name, url, id in playlists_info])


  #return playlists_html
  return render_template('get_playlists.html', playlists_info=playlists_info)

'''
@app.route('/get_playlists')
def get_playlists():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)

    playlists = sp.current_user_playlists()
    playlists_info = [(pl['name'], pl['id']) for pl in playlists['items']]

    return render_template('get_playlists.html', playlists_info=playlists_info)
'''   

@app.route('/get_tracks/<playlist_id>')
def get_tracks(playlist_id):
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)

    tracks = sp.playlist_tracks(playlist_id)
    tracks_info = [track['track']['uri'] for track in tracks['items']]

    # Store tracks or perform any other operation
    global stored_tracks_info
    stored_tracks_info = tracks_info

    # Example: You can store the tracks in a database or a file

    return jsonify({'tracks_info' : tracks_info})


@app.route('/list_tracks_info')
def list_tracks_info():
    global stored_tracks_info
    jsonify({'tracks_info' : stored_tracks_info})

    start_time = time.time()
    track_dict = percentmatch.TracksToDictionary(stored_tracks_info, 10)[:10]
    print("--- %s seconds ---" % (time.time() - start_time))

    return render_template('list_track_info.html', track_names=stored_tracks_info, json_data=track_dict)




@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug = True)
