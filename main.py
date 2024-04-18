import os

from flask import Flask, redirect, request, session, url_for


from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler




app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETKEY'


client_id = 'c19a284481e4415c8ae7f7ba9cf5c794'
client_secret = '20a8453aee554ab0b0ec13945f92bb0d'
redirect_uri = 'http://localhost:5500/callback'

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


@app.route('/')
def home():
  if not sp_oauth.validate_token(cache_handler.get_cached_token()):
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)
  return redirect(url_for('get_playlists'))



@app.route('/callback')
def callback():
  sp_oauth.get_access_token(request.args['code'])
  return redirect(url_for('get_playlists'))


@app.route('/get_playlists')
def get_playlists():
  if not sp_oauth.validate_token(cache_handler.get_cached_token()):
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


  playlists = sp.current_user_playlists()
  playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']]
  
  # print data (fix format for self) (play with to get selection)
  playlists_html = '<br>' .join([f'{name}: {url}' for name, url in playlists_info])

  return playlists_html


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug = True)
