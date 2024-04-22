# BetterPlaylists

BetterPlaylists is an application that allows users to discover playlists similar to ones they already enjoy, crafted by other users. The application is built using Flask and utilizes the Spotify API, along with Python, JavaScript, and HTML/CSS.

## Table of Contents

- [Setup](#setup)
	- [Installing Dependencies](#installing-dependencies)
	- [Accessing Spotify API](#accessing-spotify-api)
- [Usage](#usage)
- [Resources](#resources)

## Setup
### Installing Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#install-flask) and [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/).

```bash
pip install Flask
pip install spotipy
```

### Accessing Spotify API
In order to access the Spotify API, you need the necessary environment variables.

Create an app on the [Spotify for Developers dashboard](https://developer.spotify.com/dashboard) and note the Client ID and Client Secret from the settings.

Replace those values in the variables located in app.py.
```python
client_id = 'example'
client_secret = 'example'
```

Now, in the terminal run:
```bash
python3 app.py
```
The localhost webpage should pop up:

## Usage
After successfully opening the webpage, follow the instructions to authenticate with your Spotify account.
Then, select one of your playlists to match against the dataset. The application will return the top ten playlists with the highest matches, along with 



## Resources
[Link to the dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge)

