import json
import os
import time

# just for testing with string playlist name from dataset
def getPlaylistTracklist(data, name):
    for playlist in data['playlists']:
        if(playlist['name'] == name):
            list = []
            for track in playlist['tracks']:
                list.append(track['track_uri'])

            return list
        





def GetTrackSet(playlist):
    setA = set()

    for track in playlist['tracks']:
        setA.add(track['track_uri'])

    return setA


def TracksToDictionary(tracks, NumFiles): # passes in numfiles for testing
    files = os.listdir('MPD/data')

    # not use this?
    # tracks_size = len(tracks) 
    setA = set(tracks)
    dictionary = {}

    # num_playlists = 0 
    
    for i in range(NumFiles):
        with open('MPD/data/' + files[i], 'r') as f:
            data = json.load(f)

        for playlist in data['playlists']:
            # num_playlists += 1 
            setB = GetTrackSet(playlist)
            num_matches = len(setA.intersection(setB))
            match_percent = (float(num_matches) / len(setA)) * 100
            dictionary[playlist['pid']] = match_percent


    return list(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    # print()
    # print(num_playlists) 
    # print()
    # return dictionary


# with open('Downloads/spotify_million_playlist_dataset/data/mpd.slice.0-999.json', 'r') as f:
#     data = json.load(f)

# track_list = getPlaylistTracklist(data, "Throwbacks")
# print(len(track_list))

# start_time = time.time()

# dict = TheActualThing(track_list, 10)
# print(dict.items())
# #print(dict)

# print("--- %s seconds ---" % (time.time() - start_time))
'''
track_list = [
   "spotify:track:2MvIMgtWyK88OiPi0J8Dg3"
]


print(len(track_list))
start_time = time.time()

dict = TracksToDictionary(track_list, 10)
#print(dict.items())
print(dict)

print("--- %s seconds ---" % (time.time() - start_time))
'''