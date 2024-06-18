@echo off
setlocal EnableDelayedExpansion
cd /d %~dp0

:: config
set APP_NAME=MediaPlayer
set APP_ICON=app.ico
set DIR=%CD%
set APP_DIR=%CD%\dist\%APP_NAME%\

:: cleanup
rmdir /s /q "dist\%APP_NAME%" 2>nul
del "dist\%APP_NAME%-x64-setup.exe" 2>nul
del "dist\%APP_NAME%-x64-portable.7z" 2>nul

echo.
echo ****************************************
echo Checking requirements...
echo ****************************************

pip install -r requirements_windows.txt
pip install -r requirements_dist.txt

echo.
echo ****************************************
echo Running pyinstaller...
echo ****************************************

:: pyinstaller --noupx -w -i "%APP_ICON%" -n "%APP_NAME%" --version-file=version_res.txt --hidden-import videowidget -D main.py
pyinstaller %APP_NAME%_win.spec

echo.
echo ****************************************
echo Copying resources...
echo ****************************************

:: xcopy /e resources "dist\%APP_NAME%\_internal\resources\" >nul
mkdir "dist\%APP_NAME%\_internal\resources"
copy resources\main.ui "dist\%APP_NAME%\_internal\resources\"
copy resources\main.rcc "dist\%APP_NAME%\_internal\resources\"
copy resources\style.css "dist\%APP_NAME%\_internal\resources\"
xcopy /e resources\filters "dist\%APP_NAME%\_internal\resources\filters\"

echo.
echo ****************************************
echo Optimizing dist folder...
echo ****************************************

del "dist\%APP_NAME%\_internal\libssl-3.dll"
del "dist\%APP_NAME%\_internal\unicodedata.pyd"
del "dist\%APP_NAME%\_internal\_bz2.pyd"
del "dist\%APP_NAME%\_internal\_decimal.pyd"
del "dist\%APP_NAME%\_internal\_elementtree.pyd"
del "dist\%APP_NAME%\_internal\_hashlib.pyd"
del "dist\%APP_NAME%\_internal\_lzma.pyd"
del "dist\%APP_NAME%\_internal\_ssl.pyd"
del "dist\%APP_NAME%\_internal\_wmi.pyd"

del "dist\%APP_NAME%\_internal\api-ms-win-core-console-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-datetime-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-debug-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-errorhandling-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-file-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-file-l1-2-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-file-l2-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-handle-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-heap-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-interlocked-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-libraryloader-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-localization-l1-2-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-memory-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-namedpipe-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-processenvironment-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-processthreads-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-processthreads-l1-1-1.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-profile-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-rtlsupport-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-string-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-synch-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-synch-l1-2-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-sysinfo-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-timezone-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-util-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-conio-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-convert-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-environment-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-filesystem-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-heap-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-locale-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-math-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-process-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-runtime-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-stdio-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-string-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-time-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-crt-utility-l1-1-0.dll"
del "dist\%APP_NAME%\_internal\api-ms-win-core-fibers-l1-1-0.dll

del "dist\%APP_NAME%\_internal\libcrypto-3.dll"
del "dist\%APP_NAME%\_internal\ucrtbase.dll"

del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\d3dcompiler_47.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\libEGL.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\libGLESv2.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\opengl32sw.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\Qt5DBus.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\Qt5Network.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\Qt5Qml.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\Qt5QmlModels.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\Qt5Quick.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\Qt5Svg.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\bin\Qt5WebSockets.dll"

::MSVCP140.dll
::MSVCP140_1.dll
::Qt5Core.dll
::Qt5Gui.dll
::Qt5Widgets.dll
::VCRUNTIME140.dll
::VCRUNTIME140_1.dll

rmdir /s /q "dist\%APP_NAME%\_internal\PyQt5\uic"
rmdir /s /q "dist\%APP_NAME%\_internal\PyQt5\Qt5\translations"

rmdir /s /q "dist\%APP_NAME%\_internal\PyQt5\Qt5\plugins\generic"
rmdir /s /q "dist\%APP_NAME%\_internal\PyQt5\Qt5\plugins\iconengines"
rmdir /s /q "dist\%APP_NAME%\_internal\PyQt5\Qt5\plugins\imageformats"
rmdir /s /q "dist\%APP_NAME%\_internal\PyQt5\Qt5\plugins\platformthemes"

del "dist\%APP_NAME%\_internal\PyQt5\Qt5\plugins\platforms\qminimal.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\plugins\platforms\qoffscreen.dll"
del "dist\%APP_NAME%\_internal\PyQt5\Qt5\plugins\platforms\qwebgl.dll"


::del "dist\%APP_NAME%\_internal\_ssl.pyd"
::del "dist\%APP_NAME%\_internal\libssl-3.dll"

call :create_7z
call :create_installer

:done
echo.
echo ****************************************
echo Done.
echo ****************************************
echo.
pause

endlocal
goto :eof


:create_7z
if not exist "C:\Program Files\7-Zip\" (
	echo.
	echo ****************************************
	echo 7z.exe not found at default location, omitting .7z creation...
	echo ****************************************
	exit /B
)
echo.
echo ****************************************
echo Creating .7z archive...
echo ****************************************
cd dist
set PATH=C:\Program Files\7-Zip;%PATH%
7z a "%APP_NAME%-x64-portable.7z" "%APP_NAME%\*"
cd ..
exit /B


:create_installer
if not exist "C:\Program Files (x86)\NSIS\" (
	echo.
	echo ****************************************
	echo NSIS not found at default location, omitting installer creation...
	echo ****************************************
	exit /B
)
echo.
echo ****************************************
echo Creating installer...
echo ****************************************

:: get length of APP_DIR
set TF=%TMP%\x
echo %APP_DIR%> %TF%
for %%? in (%TF%) do set /a LEN=%%~z? - 2
del %TF%

call :make_abs_nsh nsis\uninstall_list.nsh

del "%NSH%" 2>nul

cd "%APP_DIR%"

for /F %%f in ('dir /b /a-d') do (
	echo Delete "$INSTDIR\%%f" >> "%NSH%"
)

for /F %%d in ('dir /s /b /aD') do (
	cd "%%d"
	set DIR_REL=%%d
	for /F %%f IN ('dir /b /a-d 2^>nul') do (
		echo Delete "$INSTDIR\!DIR_REL:~%LEN%!\%%f" >> "%NSH%"
	)
)

cd "%APP_DIR%"

for /F %%d in ('dir /s /b /ad^|sort /r') do (
	set DIR_REL=%%d
	echo RMDir "$INSTDIR\!DIR_REL:~%LEN%!" >> "%NSH%"
)

cd "%DIR%"
set PATH=C:\Program Files (x86)\NSIS;%PATH%
makensis nsis\make-installer.nsi
exit /B


:make_abs_nsh
set NSH=%~dpnx1%
exit /B