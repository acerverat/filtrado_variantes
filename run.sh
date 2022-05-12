#!/bin/bash
# https://cancer.sanger.ac.uk/cosmic/register
# Please replace email and pass variables with your own credentials.
email=AQUI_PON_TU_EMAIL
pass=AQUI_PON_TU_PASSWORD
auth=$(echo "$email:$pass" | base64)
jp2a public/dna.jpg

# Installing dependencies
sudo apt-get install python3-pip curl jp2a jq
pip install autopep8 virtualenv python-decouple

# For more info on extracting the cosmos database look at:
# https://cancer.sanger.ac.uk/cosmic/help/file_download
# https://cancer.sanger.ac.uk/cosmic/download
url=$(curl -H "Authorization: Basic $auth" https://cancer.sanger.ac.uk/cosmic/file_download/GRCh38/cosmic/v95/CosmicMutantExport.tsv.gz | jq -r '.url')
wait
jp2a public/downloading.jpg
echo "Downloading from cosmos database..."
mkdir data
cd data
curl "$url" --output cosmic_variants.tsv

if [ -e cosmic_variants.tsv ]; then
    jp2a public/INMEGEN_logo.jpg
    echo "The file cosmic_variants.tsv was correctly loaded you can now run the tests of the program using python3 tests/e2e.py"
    sleep 5
    cd ../views
    python3 interface.py
else
    echo "The file cosmic_variants.tsv was not loaded correctly"
fi
