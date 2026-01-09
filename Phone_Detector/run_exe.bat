@echo off
echo Starting Phone Detector...
if exist "dist\PhoneDetector.exe" (
    "dist\PhoneDetector.exe"
) else (
    echo Could not find dist\PhoneDetector.exe.
    echo Please make sure the build completed successfully.
    pause
)
