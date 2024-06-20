# MediaPlayer
A simple media player for macOS and Windows, based on Python 3, PyQt5 (portable to PyQt6 or PySide6) and a custom video widget that uses native system multimedia frameworks directly ([AVFoundation](https://developer.apple.com/av-foundation/) in macOS, DirectShow and [LAV Filters](https://github.com/Nevcairiel/LAVFilters) in Windows).

## Supported video containers
* **Windows**: 3gp asf asx avi dv f4v flv gif hevc m2ts m2v m4v mjpeg mkv mov mp4 mpeg mts mxf ogv rm ts vob webm wmv wtv
* **macOS**: 3gp avi m2ts m2v m4v mov mp4 mpg mpeg mts mxf ts vob  
(mxf only when free [Pro Video Formats](https://support.apple.com/en-us/106396) are installed)  

## Supported audio containers
* **Windows**: aac ac3 aiff ape caf flac mp3 ogg sox wav
* **macOS**: aac ac3 aiff caf flac mp3 wav

## Supported video codecs (selection)
* **Windows**: bink cinepak dirac dvvideo flash fraps h264 hevc indeo mjpeg mpeg1 mpeg2 mpeg4 msrle msvideo1 qtrle vp4 vp6 vp7 wmv12 wmv3
* **macOS**: cinepak dvvideo h264 hevc mjpeg mpeg1 mpeg2 prores422 prores4444  
(+ [Pro Video Formats](https://support.apple.com/en-us/106396), if installed)

## Supported audio codecs (selection)
* **Windows**: aac ac3 alac dts flac mp2 mp3 nellymoser opus pcm realaudio truespeech vorbis wavpack wma
* **macOS**: aac ac3 alac flac mp2 mp3 pcm

## Screenshots

*MediaPlayer in Windows 11*  
![MediaPlayer in Windows 11](screenshots/mediaplayer_win11.jpg)

*MediaPlayer in macOS 13*  
![MediaPlayer in macOS 13](screenshots/mediaplayer_macos13.jpg)
