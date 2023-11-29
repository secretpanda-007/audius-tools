import requests
import tkinter as tk
from tkinter import messagebox
import random
import os

host = random.choice((requests.get('https://api.audius.co')).json()['data'])
track_id = None  # Initialize track_id as None

# Function to resolve the Audius URL
def resolve_audius_url():
    global track_id  # Declare track_id as a global variable
    url = entry_url.get()

    headers = {
        'Accept': 'application/json'
    }

    resolve_url = 'https://discovery-au-02.audius.openplayer.org/v1/resolve'

    params = {
        'url': url,
        'app_name': 'secretPANDA007'
    }

    response = requests.get(resolve_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            track_data = data['data']
            if 'id' in track_data:
                track_id = track_data['id']
                result_label.config(text=f'Track ID: {track_id}')
            else:
                messagebox.showerror("Error", 'No "id" found in track data')
        else:
            messagebox.showerror("Error", 'No "data" found in the response')
    else:
        messagebox.showerror("Error", f"Request failed with status code {response.status_code}")

# Function to stream the Audius URL and save it to a file
def stream_audius_url():
    global track_id  # Declare track_id as a global variable
    if track_id is not None:
        url = f'{host}/v1/tracks/{track_id}/stream?app_name=secretPANDA007'
        
        response = requests.get(url)
        if response.status_code == 200:
            # Determine the file name and extension based on the track title
            track_title = f'Track_{track_id}.mp3'
            file_path = os.path.join(os.getcwd(), track_title)
            
            # Save the audio to the file
            with open(file_path, 'wb') as file:
                file.write(response.content)
            
            messagebox.showinfo("Success", f"Audio saved as {track_title}")
        else:
            messagebox.showerror("Error", f"Failed to fetch audio with status code {response.status_code}")
    else:
        messagebox.showerror("Error", "Please resolve an Audius URL first.")

# Create the main application window
root = tk.Tk()
root.title("Audius URL Resolver")

# Create a label and entry widget for the Audius URL
url_label = tk.Label(root, text="Enter the Audius URL:")
url_label.pack()

entry_url = tk.Entry(root, width=40)
entry_url.pack()

# Create a button to resolve the URL
resolve_button = tk.Button(root, text="Resolve", command=resolve_audius_url)
resolve_button.pack()

# Create a button to stream the URL and save to a file
stream_button = tk.Button(root, text="Stream to File", command=stream_audius_url)
stream_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

# testing notifications
