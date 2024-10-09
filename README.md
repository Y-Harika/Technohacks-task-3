# Pygame Music Player

## Description
This is a simple music player built using the Python `pygame` library. It allows users to:
- Add songs to a playlist.
- Play, pause, resume, and stop music.
- Navigate between songs in the playlist (next/previous).

## Features
- **Play**: Play the current song.
- **Pause**: Pause the current song.
- **Resume**: Resume playing the current song after pausing.
- **Stop**: Stop the music.
- **Next Song**: Move to the next song in the playlist.
- **Previous Song**: Go back to the previous song in the playlist.
- **Create Playlist**: Add multiple songs to the playlist and manage them.

## How to Use

1. **Add Songs to Playlist**: 
   - Songs can be added to the playlist using the `add_to_playlist()` method by specifying the path to the song file. 
   - Example:
     ```python
     player.add_to_playlist(r"c:\path\to\song1.mp3")
     ```

2. **Play Music**:
   - Use the `play()` method to start playing the first song in the playlist.
   
3. **Control Music Playback**:
   - Input commands like `play`, `pause`, `resume`, `stop`, `next`, and `previous` in the terminal to control the playback.

4. **Example**:
   ```bash
   Enter command (play/pause/resume/stop/next/previous): play
