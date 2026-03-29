#!/bin/bash
# Run via
# sh dockerfiles/download_maps.sh
set -e

# Create maps directory if it doesn't exist
mkdir -p dockerfiles/maps
cd dockerfiles/maps

# Download function with retries
download_with_retry() {
    local url=$1
    local output=$2
    curl --retry 5 --retry-delay 5 -C - -L "$url" -o "$output"
}

# Download and process sc2ai.net ladder maps
download_with_retry "https://sc2ai.net/wiki/184/plugin/attachments/download/9/" "1.zip"
download_with_retry "https://sc2ai.net/wiki/184/plugin/attachments/download/14/" "2.zip"
download_with_retry "https://sc2ai.net/wiki/184/plugin/attachments/download/21/" "3.zip"
download_with_retry "https://sc2ai.net/wiki/184/plugin/attachments/download/35/" "4.zip"
download_with_retry "https://sc2ai.net/wiki/184/plugin/attachments/download/36/" "5.zip"
download_with_retry "https://sc2ai.net/wiki/184/plugin/attachments/download/38/" "6.zip"
download_with_retry "https://sc2ai.net/wiki/184/plugin/attachments/download/39/" "7.zip"
unzip -q -o '*.zip'
rm *.zip

# Download and process official blizzard maps
download_with_retry "http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2019Season3.zip" "Ladder2019Season3.zip"
unzip -q -P iagreetotheeula -o "Ladder2019Season3.zip"
mv Ladder2019Season3/* .
rm "Ladder2019Season3.zip"
rmdir Ladder2019Season3

# Download and process v5.0.6 maps
download_with_retry "https://github.com/shostyn/sc2patch/raw/4987d4915b47c801adbc05e297abaa9ca2988838/Maps/506.zip" "506.zip"
unzip -q -o "506.zip"
rm "506.zip"

# Download and process flat/empty maps
download_with_retry "http://blzdistsc2-a.akamaihd.net/MapPacks/Melee.zip" "Melee.zip"
unzip -q -P iagreetotheeula -o "Melee.zip"
mv Melee/* .
rm "Melee.zip"
rmdir Melee

# Remove LE suffix from file names
for f in *LE.SC2Map; do 
    mv -- "$f" "${f%LE.SC2Map}.SC2Map"; 
done
