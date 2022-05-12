#!/bin/bash
# https://cancer.sanger.ac.uk/cosmic/register
# Please replace email and pass variables with your own credentials.
email=CORREO
pass=CONTRASENA
auth=$(echo "$email:$pass" | base64)
jp2a public/welcome.jpg
sleep 2
jp2a public/dna.jpg
sleep 1
cd tests
sudo chmod +x test.sh
cd ..
# Installing dependencies
sudo apt-get install python3-pip curl jp2a jq python3-tk
pip install autopep8 virtualenv python-decouple tk

# Getting cosmic variants.
mkdir data
cd data
if [ -e cosmic_variants.tsv ]; then
    echo "cosmic_variants.tsv already exist"
    sleep 1
    cd ../views
    python3 interface.py
else
    url=$(curl -H "Authorization: Basic $auth" https://cancer.sanger.ac.uk/cosmic/file_download/GRCh38/cosmic/v95/CosmicMutantExport.tsv.gz | jq -r '.url')
    wait
    jp2a ../public/chromosome.jpg
    echo "Downloading variants from cosmos database..."
    curl "$url" --output cosmic_variants.tsv
    if [ -e cosmic_variants.tsv ]; then
        jp2a ../public/inmegen_logo.jpg
        echo "The file cosmic_variants.tsv was correctly loaded you can now run the tests of the program using ./test"
        sleep 3
        cd ../views
        python3 interface.py
    else
        echo "The file cosmic_variants.tsv was not loaded correctly"
    fi
fi

cd ..

# For more info on extracting the cosmos database look at:
# https://cancer.sanger.ac.uk/cosmic/help/file_download
# https://cancer.sanger.ac.uk/cosmic/download
