import json
import os
import time



def get_playlist_data(entries):
    # Create dictionaries to store playlist data
    playlist_names = {}
    track_sets = {}

    # Iterate over each entry in the list
    for entry in entries:
        playlist_id, _ = entry
        
        # Extract the filename based on the playlist ID range
        filename = f"mpd.slice.{playlist_id // 1000 * 1000}-{(playlist_id // 1000 + 1) * 1000 - 1}.json"
        
        # Check if the file exists
        if not os.path.isfile(os.path.join('MPD/data', filename)):
            print(f"File not found for playlist ID {playlist_id}")
            continue

        # Open the file and load its JSON data
        with open(os.path.join('MPD/data', filename), 'r') as f:
            data = json.load(f)
        
        # Search for the playlist with the given ID
        for playlist in data['playlists']:
            if playlist['pid'] == playlist_id:
                # Store playlist name
                playlist_names[playlist_id] = playlist['name']
                # Get track set
                track_sets[playlist_id] = GetTrackSetNames(playlist)[:15]
                break  # Stop searching once the playlist is found
    
    return playlist_names, track_sets


# just for testing with string playlist name from dataset
def getPlaylistTracklist(data, name):
    for playlist in data['playlists']:
        if(playlist['name'] == name):
            list = []
            for track in playlist['tracks']:
                list.append(track['track_uri'])

            return list
        

# gets track uri's for comparison
def GetTrackSet(playlist):
    setA = set()

    for track in playlist['tracks']:
        setA.add(track['track_uri'])

    return setA

# gets track names for final output
def GetTrackSetNames(playlist):
    trackSet = []

    for track in playlist['tracks']:
        trackSet.append(track['track_name'])

    return trackSet


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

    return list(dictionary.items())
    #return list(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)) #automatic sorted return for testing




# example usage
# with open('Downloads/spotify_million_playlist_dataset/data/mpd.slice.0-999.json', 'r') as f:
#     data = json.load(f)

# track_list = getPlaylistTracklist(data, "Throwbacks")
# print(len(track_list))

# start_time = time.time()
# dict = TracksToDictionary(track_list, 10)
# print("--- %s seconds ---" % (time.time() - start_time))



#example usage of get_playlist_names function
'''
entries = [(17491, 100.0), (17089, 100.0), (121, 100.0), (11209, 100.0), (15011, 100.0), (10161, 100.0), (13381, 100.0), (13034, 100.0), (16994, 100.0), (11981, 50.0)]

playlist_names, track_sets = get_playlist_data(entries)

for index, (playlist_id, match_percent) in enumerate(entries, start=1):
    playlist_name = playlist_names.get(playlist_id)
    track_set = track_sets.get(playlist_id)
    if playlist_name:
        print(f"list entry {index}: Playlist Name: {playlist_name}, Match Percentage: {match_percent}")
    else:
        print(f"list entry {index}: No playlist found for ID {playlist_id}")

    if track_set:
        print(f"    Track Set for Playlist ID {playlist_id}: {track_set}")
'''