#!/usr/bin/env bash

exit on error
set -o errexit

pip install -r requirements.txt

python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4'); nltk.download('punkt');"