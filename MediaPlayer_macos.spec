# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['videowidget'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['_bootlocale'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MediaPlayer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['app.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='MediaPlayer',
)
app = BUNDLE(
    coll,
    name='MediaPlayer.app',
    icon='app.icns',
    bundle_identifier=None,
    info_plist={
        'CFBundleShortVersionString': '0.2.0',
        'Associations': 'mp4 avi mpg m2v mxf wav mp3 aif aiff',
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeExtensions': ['mp4', 'avi', 'mpg', 'm2v', 'mxf', 'wav', 'mp3', 'aif', 'aiff'],
                'CFBundleTypeRole': 'Viewer'
            }
        ]
    },
)
