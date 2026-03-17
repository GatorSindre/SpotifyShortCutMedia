import spotipy
import keyboard
from spotipy.oauth2 import SpotifyOAuth
import win32gui
import win32process
import psutil
import time
import win32com.client

pause = False

playlist_chache = ""
empty_playlist_uri = "spotify:playlist:0qPxhnNbUnarfHV3mFs0Kq"

clash_playlist_uri = "spotify:playlist:7F9L88RCW9ZFrOrcAIK3ZP"
jjk_playlist_uri = "spotify:playlist:3PKsl9s7Tq4EKevC7oFcEz"
the80s_playlist_uri = "spotify:playlist:6RZb1CWCm9eAXJ1HioeFtP"
chill_playlist_uri = "spotify:playlist:2KfIiQaMujClh9wgRmSLWz"

# lambda: print(get_current_playlist_uri())         switch this with one of the hotkeys to get uri's

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="213ab4ad23dc414da133bdea6a3eaca1",
    client_secret="ac8230fb691540d19f7bb154f4b9f58c",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-modify-playback-state user-read-playback-state"
))

def pause_spot():
    try:
        print("Paused")
        sp.pause_playback()
    except:
        print("No active device")

def play_spot():
    try:
        print("Play")
        sp.start_playback()
    except:
        print("No active device")

def advanced_pause():
    global pause
    global playlist_chache 
    current_playlist_uri = get_current_playlist_uri()
    if current_playlist_uri != empty_playlist_uri:
        pause = False
    if pause == True:
        return
    try:
        playlist_chache = current_playlist_uri
        play_playlist(empty_playlist_uri)
        pause = True
        print("Advanced_Pause")
    except:
        print("No active device")

def advanced_play():
    global pause
    global playlist_chache 
    if pause == False:
        return
    try:
        play_playlist(playlist_chache)
        pause = False
        print("Advanced_Play")
    except:
        print("No active device")
    

def play_playlist(playlist_uri):
    try:
        global pause
        sp.start_playback(context_uri=playlist_uri)
        pause = False
        print("Switched to playlist!")
    except Exception as e:
        print("No active device or error:", e)

def get_current_playlist_uri():
    try:
        playback = sp.current_playback()
        if playback and playback['context']:
            context_type = playback['context']['type']  # 'playlist', 'album', 'artist', etc.
            context_uri = playback['context']['uri']    # e.g., 'spotify:playlist:37i9dQZF1DXcBWIGoYBM5M'
            
            if context_type == 'playlist':
                print("Current playlist URI:", context_uri)
                return context_uri  # You can pass this to start_playback later
            else:
                print(f"Currently playing from a {context_type}, not a playlist")
                return None
        else:
            print("No active playback or context")
            return None
    except Exception as e:
        print("Error:", e)
        return None



def play_force():
    
    current = win32gui.GetForegroundWindow()

    keyboard.press_and_release("win+3")

    time.sleep(0.5)

    keyboard.send("space")

    time.sleep(0.5)

    win32gui.SetForegroundWindow(current)

keyboard.add_hotkey('f13', advanced_play)
keyboard.add_hotkey('f14', advanced_pause)
keyboard.add_hotkey('f15', lambda: play_playlist("spotify:playlist:7F9L88RCW9ZFrOrcAIK3ZP"))
keyboard.add_hotkey('f16', lambda: play_playlist("spotify:playlist:6RZb1CWCm9eAXJ1HioeFtP"))
keyboard.add_hotkey('f17', lambda: play_playlist("spotify:playlist:2KfIiQaMujClh9wgRmSLWz"))
keyboard.add_hotkey('f18', lambda: play_playlist("spotify:playlist:3PKsl9s7Tq4EKevC7oFcEz"))
keyboard.add_hotkey('f19', play_force)


keyboard.wait()