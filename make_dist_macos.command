APP_NAME=MediaPlayer
APP_ICON=app.icns

cd "$(dirname "$0")"

rm -R dist/$APP_NAME 2>/dev/null
rm -R dist/$APP_NAME.app 2>/dev/null
rm -R dist/$APP_NAME.dmg 2>/dev/null

echo
echo '****************************************'
echo 'Checking requirements...'
echo '****************************************'

pip install -r requirements_macos.txt
pip install -r requirements_dist.txt

echo
echo '****************************************'
echo 'Running pyinstaller...'
echo '****************************************'

# pyinstaller --noupx -w -i "$APP_ICON" -n "$APP_NAME" -D main.py --exclude-module _bootlocale
pyinstaller MediaPlayer_macos.spec

echo
echo '****************************************'
echo 'Copying resources...'
echo '****************************************'

cp resources/main.ui "dist/$APP_NAME.app/Contents/Resources/"
cp resources/main.rcc "dist/$APP_NAME.app/Contents/Resources/"
cp resources/style.css "dist/$APP_NAME.app/Contents/Resources/"

echo
echo '****************************************'
echo 'Optimizing dist folder...'
echo '****************************************'

rm dist/$APP_NAME.app/Contents/Frameworks/libcrypto.3.dylib
rm dist/$APP_NAME.app/Contents/Frameworks/libssl.3.dylib
rm dist/$APP_NAME.app/Contents/Resources/libcrypto.3.dylib
rm dist/$APP_NAME.app/Contents/Resources/libssl.3.dylib

rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/uic
rm -R dist/$APP_NAME.app/Contents/Resources/PyQt5/uic

rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/translations
rm -R dist/$APP_NAME.app/Contents/Resources/PyQt5/Qt5/translations

rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/lib/QtQml.framework
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/lib/QtQmlModels.framework
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/lib/QtQuick.framework
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/lib/QtSvg.framework
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/lib/QtWebSockets.framework
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/lib/QtNetwork.framework

rm dist/$APP_NAME.app/Contents/Frameworks/QtNetwork
rm dist/$APP_NAME.app/Contents/Frameworks/QtQml
rm dist/$APP_NAME.app/Contents/Frameworks/QtQmlModels
rm dist/$APP_NAME.app/Contents/Frameworks/QtQuick
rm dist/$APP_NAME.app/Contents/Frameworks/QtSvg
rm dist/$APP_NAME.app/Contents/Frameworks/QtWebSockets

rm dist/$APP_NAME.app/Contents/Resources/QtNetwork
rm dist/$APP_NAME.app/Contents/Resources/QtQml
rm dist/$APP_NAME.app/Contents/Resources/QtQmlModels
rm dist/$APP_NAME.app/Contents/Resources/QtQuick
rm dist/$APP_NAME.app/Contents/Resources/QtSvg
rm dist/$APP_NAME.app/Contents/Resources/QtWebSockets

#rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/plugins/bearer
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/plugins/generic
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/plugins/iconengines
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/plugins/imageformats
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/plugins/platformthemes

rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/plugins/platforms/libqminimal.dylib
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/plugins/platforms/libqoffscreen.dylib
rm -R dist/$APP_NAME.app/Contents/Frameworks/PyQt5/Qt5/plugins/platforms/libqwebgl.dylib

# echo
# echo '****************************************'
# echo 'Creating ZIP...'
# echo '****************************************'
# cd dist
# rm $APP_NAME-macos.zip 2>/dev/null
# zip -q -r $APP_NAME-macos.zip $APP_NAME.app
# cd ..

echo
echo '****************************************'
echo 'Creating DMG...'
echo '****************************************'
mkdir dist/dmg
mv dist/$APP_NAME.app dist/dmg/
python make_dmg.py "dist/dmg" "dist/$APP_NAME.dmg" "$APP_NAME"
mv dist/dmg/$APP_NAME.app dist/
rm -R dist/dmg

echo
echo '****************************************'
echo 'Done.'
echo '****************************************'
echo
