#!/bin/bash

# Fetch the URL and find the positions of the Scheme Name and Asset Value fields in the content
content=$(wget -qO- https://www.amfiindia.com/spages/NAVAll.txt)
SCHEME_POS=$(echo "$content" | head -n 1 | awk -F ';' '{for(i=1; i<=NF; i++) if($i == "Scheme Name") print i}')
ASSET_POS=$(echo "$content" | head -n 1 | awk -F ';' '{for(i=1; i<=NF; i++) if($i == "Net Asset Value") print i}')

# Extract the Scheme Name and Asset Value fields based on their positions and remove empty rows
echo "$content" | awk -F ';' -v scheme_pos="$SCHEME_POS" -v asset_pos="$ASSET_POS" '{if (NF >= asset_pos) print $scheme_pos "," $asset_pos}' > output.csv

echo "Output saved in output.csv"


