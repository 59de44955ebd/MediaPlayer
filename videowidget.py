import sys

IS_WIN = sys.platform == 'win32'
IS_MAC = sys.platform == 'darwin'
if not IS_WIN and not IS_MAC:
    sys.exit(1)

if IS_WIN:
    from dsplayer import VideoWidget
else:
    from avplayer import VideoWidget
