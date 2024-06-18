# MediaPlayer
A simple media player for macOS and Windows, based on Python 3, PyQt5 (portable to PyQt6 or PySide6) and a custom video widget that uses native system multimedia frameworks directly ([AVFoundation](https://developer.apple.com/av-foundation/) in macOS, DirectShow and [LAV Filters](https://github.com/Nevcairiel/LAVFilters) in Windows).

## Supported video containers
### Windows
3gp asx avi f4v flv hevc m2ts m2v mjpeg mkv mov mp4 mpeg mts mxf ogv rm ts vob webm wmv wtv
### macOS
3gp avi m2ts m2v mov mp4 mpg mpeg mts mxf ts vob   
(mxf only when free [Pro Video Formats](https://support.apple.com/en-us/106396) are installed)  

## Screenshots

*MediaPlayer in Windows 11*  
![MediaPlayer in Windows 11](screenshots/mediaplayer_win11.jpg)

*MediaPlayer in macOS 13*  
![MediaPlayer in macOS 13](screenshots/mediaplayer_macos13.jpg)
