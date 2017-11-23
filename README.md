# Restaurant Menu System
A restaurant menu system that allows for restaurants and menu items to be created, viewed, and modified on a python web server.

## Setup
1. You must have python and flask installed.
2. To setup the database run `python database_setup.py`. This will create a sqlite database. 
3. If you would like to insert dummy data into the database for testing, run `python lotsofmenus.py`.
4. To enable Google sign in create new credentials and download client_secrets.json from your [Google Developer Dashboard](https://console.developers.google.com).
5. To enable Facebook sign in login to [Facebook Developers](https://developers.facebook.com/), create a new api key if you don't have one. Next create a file named fb_client_secrets.json with your app_id and app_secret key. The file should look like the snippet below.

```json
{
  "web": {
    "app_id": "YOUR_APP_ID",
    "app_secret": "YOUR_APP SECRET"
  }
}
```

## Usage
To start the web server run `python server.py`