# iot-humid-temp
SENSE and PUB program to read DHT11 sensed data as temperature and humidity level and publish to google IOT

# Steps
PRE-REQUISITES:

Create new google project
Create topic/subscription/registry using google cloud console, in pubsub, google iot core module.
Create a service account under same project to be used for auth, under IAM & ADMIN=>Service Accounts


SETUP on Raspberry PI Device:

# create python virtual env
cd DHT/
python3 -m venv dhtvirutalenv
# Activate virtual env, should see command prompt as (dhtvirtualenv)
source ./dhtvirutalenv/bin/activate

# update virtual env
sudo apt-get update
sudo apt-get install build-essential python3-dev 
sudo apt-get install git

# get adafruit lib
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT/
python setup.py install

git clone https://github.com/adafruit/Adafruit_CircuitPython_DHT
cd Adafruit_CircuitPython_DHT
python setup.py install

# for google pub
mkdir API 
copy temp_humid_pub.py and test_pub.py to it.

# add google project id and topic to profile.
sudo nano /etc/profile
export PROJECT_ID="iot-explore"
export TOPIC_NAME="temp_humid_data_topic"
export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/google-iot/iot-certs-key/iot-explore-7b7e3d6f2a1a.json"

# sudo reboot now
# install google python pubsub lib in dhtvirutalenv
pip install google-cloud-pubsub

# cd API and excute pub program to publish data to Google Topic.
python temp_humid_pub.py 

# On google console use subscription object to pull data to view
gcloud auth login
gcloud config set project iot-explore
gcloud pubsub subscriptions pull temp_humid_data_subs
