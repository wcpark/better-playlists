# BetterPlaylists

BetterPlaylists is an application that allows users to discover playlists similar to ones they already enjoy, crafted by other users. The application is built using Flask and utilizes the Spotify API, along with Python, JavaScript, and HTML/CSS.

## Table of Contents

- [Setup](#setup)
	- [Downloading Dataset](#downloading-dataset)
	- [Accessing Spotify API](#accessing-spotify-api)
	- [Installing Dependencies](#installing-dependencies)
- [Usage](#usage)
- [Resources](#resources)

## Setup

### Downloading Dataset
[Navigate to the dataset website](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge), make an account, and download the dataset from the Resources tab. Extract the downloaded zip file to a folder named "MPD", and place the folder in the project root directory.

### Accessing Spotify API
In order to access the Spotify API, you need the necessary environment variables.

Create an app on the [Spotify for Developers dashboard](https://developer.spotify.com/dashboard). When asked, "Which API/SDKs are you planning to use?" check the "Web API" box.

Navigate to the settings, note the Client ID and Client Secret, and set the Redirect URI to http://localhost:5000/callback.

Replace those values in the variables located in app.py.
```python
client_id = 'example'
client_secret = 'example'
```

### Installing Dependencies
In the terminal, set up a virtual environment while in the project root directory:
```bash
python -m venv {virtual environment name of choice}
source {virtual environment name of choice}/scripts/activate
```

If using Powershell, the command to activate is instead:
```bash
{virtual environment name of choice}/scripts/activate.
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#install-flask) and [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/):

```bash
pip install Flask
pip install spotipy
```

## Usage
Now, in the terminal run:
```bash
python src/app.py
```

Open a browser of choice, and navigate to the localhost URL shown in the terminal.
After successfully opening the webpage, follow the instructions to authenticate with your Spotify account.
Then, select one of your playlists to match against the dataset.

The application will return the top ten playlists with the highest match percentages, each accompanied by 15 songs. Additionally, it will display the execution times for the sorting process of all of the playlists used for comparison.


## Resources
[Link to the dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge)
