import json

with open('data/mpd.slice.1000-1999.json', 'r') as f:
    data = json.load(f)


def percentAinB(set1, playlist2):
    set2 = set()

    for track in playlist2['tracks']:
        set2.add(track['track_name'])

    set_intersection = set1.intersection(set2)

    percentAinB = float(len(set_intersection)) /  len(set2)

    return percentAinB

def getPlaylist(data, name):
    for playlist in data['playlists']:
        if(playlist['name'] == name):
            return playlist


########################

playlistA = getPlaylist(data, "New music")

setA = set()

for track in playlistA['tracks']:
    setA.add(track['track_name'])

dictionary = {}

for playlist in data['playlists']:
    if(playlist['num_tracks'] > playlistA['num_tracks']):
        dictionary[playlist['name']] = percentAinB(setA, playlist)

print(dictionary)