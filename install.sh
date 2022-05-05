#!/bin/bash
sudo apt-get install python3-pip curl jp2a jq

# https://cancer.sanger.ac.uk/cosmic/register
email=AQUI_PON_TU_EMAIL
pass=AQUI_PON_TU_PASSWORD
auth=$(echo "$email:$pass" | base64);
echo $auth

jp2a public/downloading.jpg
# Installing dependencies
pip install virtualenv
pip install python-decouple
pip install robotframework

# For more info on extracting the cosmos database look at: 
# https://cancer.sanger.ac.uk/cosmic/help/file_download
# https://cancer.sanger.ac.uk/cosmic/download
url=$(curl -H "Authorization: Basic $auth" https://cancer.sanger.ac.uk/cosmic/file_download/GRCh38/cosmic/v95/CosmicMutantExport.tsv.gz | jq -r '.url');
wait
jp2a public/dna.jpg
echo "Downloading from cosmos database..."
curl "$url" --output cosmic

jp2a public/inmegen_logo.jpg