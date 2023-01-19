![image](https://user-images.githubusercontent.com/88645471/213474378-90b19ac3-f256-4947-ac33-fff83849c06e.png)

# Overview
This is a python script that saves all discover weekly playlists created by Spotify. It can be automated using PythonAnywhere (www.pythonanywhere.com) or the Windows Task Scheduler to run every week, or more specifically every Monday when Spotify updates this playlist.

# Installation
Clone the repository by `git clone https://github.com/dcsp3/discover-weekly-spotify.git`

# Usage
1. Create an app using the Spotify developer dashboard
2. Authorize this app using the documentation from Spotify
3. Get the refresh token and save it in secrets.py
4. Get the id of your discover weekly playlist and save it in secrets.py
5. Automate using python anywhere/task scheduler.

# References
- Spotify Developer Dashboard - https://developer.spotify.com/dashboard
- Spotify App Authorization - https://developer.spotify.com/documentation/general/guides/authorization/
- Creating Playlist - https://developer.spotify.com/documentation/web-api/reference/#/operations/create-playlist
- Getting Playlist Items - https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlists-tracks
- Adding Items to Playlist - https://developer.spotify.com/documentation/web-api/reference/#/operations/add-tracks-to-playlist
