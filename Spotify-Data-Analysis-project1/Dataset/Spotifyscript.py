import requests
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace with your actual Spotify credentials
CLIENT_ID = "b8f72275323741bbb190b8eb1bc2f672"
CLIENT_SECRET = "f5f69079eaa74a61ad9b8bea02f91566"

# Authenticate with Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load dataset with correct encoding
file_path = "F:/project da/spotify-2023.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Ensure track and artist columns exist
track_col = "track_name"
artist_col = "artist(s)_name"
if track_col not in df.columns or artist_col not in df.columns:
    print("Error: Missing required columns in the dataset.")
    exit()

# Add new columns for Spotify URL and Album Cover
df["spotify_url"] = None
df["album_cover"] = None

def get_spotify_data(track, artist):
    query = f"{track} {artist}"
    results = sp.search(q=query, limit=1, type="track")
    
    if results["tracks"]["items"]:
        track_info = results["tracks"]["items"][0]
        spotify_url = track_info["external_urls"]["spotify"]
        album_cover = track_info["album"]["images"][0]["url"]
        return spotify_url, album_cover
    return None, None

# Process each track
for index, row in df.iterrows():
    track = str(row[track_col])
    artist = str(row[artist_col])
    
    if pd.isna(track) or pd.isna(artist):
        continue  # Skip missing values
    
    try:
        spotify_url, album_cover = get_spotify_data(track, artist)
        df.at[index, "spotify_url"] = spotify_url
        df.at[index, "album_cover"] = album_cover
        print(f"Processed: {track} by {artist}")
    except Exception as e:
        print(f"Error processing {track} by {artist}: {e}")

# Save updated dataset
output_path = "F:/project da/spotify-2023-updated.csv"
df.to_csv(output_path, encoding="ISO-8859-1", index=False)
print(f"Updated file saved at: {output_path}")
