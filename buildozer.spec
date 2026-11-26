#!/usr/bin/env bash
set -euo pipefail

export ACLOCAL_PATH="/usr/share/aclocal:${ACLOCAL_PATH:-}"
rm -rf .buildozer ~/.buildozer
mkdir -p ~/.buildozer/android/platform/android-sdk

curl -fL --retry 5 --retry-delay 5 \
  "https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip" \
  -o /tmp/cmdline-tools.zip

unzip -q /tmp/cmdline-tools.zip -d /tmp/cmdline-extracted
mkdir -p ~/.buildozer/android/platform/android-sdk/cmdline-tools/latest
mv /tmp/cmdline-extracted/cmdline-tools/* ~/.buildozer/android/platform/android-sdk/cmdline-tools/latest/

mkdir -p ~/.buildozer/android/platform/android-sdk/tools/bin
ln -sfn ~/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/sdkmanager \
  ~/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager
ln -sfn ~/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/avdmanager \
  ~/.buildozer/android/platform/android-sdk/tools/bin/avdmanager

(yes || true) | ~/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/sdkmanager \
  --sdk_root="$HOME/.buildozer/android/platform/android-sdk" \
  "platform-tools" "platforms;android-33" "build-tools;33.0.2" "ndk;27.2.12479018"

ln -sfn "$HOME/.buildozer/android/platform/android-sdk/ndk/27.2.12479018" \
  "$HOME/.buildozer/android/platform/android-ndk-r27.2.12479018"

set +e
buildozer android debug > /tmp/buildozer.log 2>&1
EXIT_CODE=$?
set -e

if [ "$EXIT_CODE" -ne 0 ]; then
  tail -n 120 /tmp/buildozer.log > error_tail.txt
  cat error_tail.txt
  exit "$EXIT_CODE"
fi

find . -maxdepth 4 -name "*.apk" -ls
