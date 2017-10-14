#!/bin/bash
cd ~/Development/cometcabs/backend/CabTracker
echo "Removing old zips"
rm scraper.zip
rm api.zip
mkdir lambda_package_scraper
mkdir lambda_package_scraper/lambda
mkdir lambda_package_scraper/utils
mkdir lambda_package_api
mkdir lambda_package_api/lambda
mkdir lambda_package_api/utils
echo "Installing peewee + requests + PyMySQL"
pip install peewee -t ./lambda_package_scraper/
pip install peewee -t ./lambda_package_api/
pip install requests -t ./lambda_package_scraper/
pip install PyMySQL -t ./lambda_package_scraper/
pip install PyMySQL -t ./lambda_package_api/
echo "Copying lambda files"
cp lambda/__init__.py ./lambda_package_scraper/lambda/
cp lambda/lambda_scraper.py ./lambda_package_scraper/lambda/
cp utils/lambda_utils.py ./lambda_package_scraper/utils/
cp lambda/__init__.py ./lambda_package_api/lambda/
cp lambda/lambda_cab_api.py ./lambda_package_api/lambda/
cp utils/lambda_utils.py ./lambda_package_api/utils/
echo "Copying DB Helper"
cp utils/__init__.py ./lambda_package_scraper/utils/
cp utils/DBHelper.py ./lambda_package_scraper/utils/
cp utils/__init__.py ./lambda_package_api/utils/
cp utils/DBHelper.py ./lambda_package_api/utils/
echo "Copying other utils"
cp utils/time_utils.py ./lambda_package_scraper/utils/
cp utils/time_utils.py ./lambda_package_api/utils/
echo "Copying cab_scraper"
cp cab_scraper.py ./lambda_package_scraper/
cd lambda_package_scraper
echo "Zipping scraper"
zip -r -9 -q scraper.zip .
mv scraper.zip ..
cd ..
echo "Zipping api"
cd lambda_package_api
zip -r -9 -q api.zip .
mv api.zip ..

cd ~/Development/cometcabs/backend/CabTracker
rm -rf lambda_package_scraper
rm -rf lambda_package_api
