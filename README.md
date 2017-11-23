# Restaurant Menu System
A restaurant menu system that allows for restaurants and menu items to be created, viewed, and modified on a python web server.

## Setup
1. You must have python and flask installed.
2. To setup the database run `python database_setup.py`. This will create a sqlite database. 
3. If you would like to insert dummy data into the database for testing, run `python lotsofmenus.py`.
4. To enable Google Sign In:
    1. Login to [Google Developer Dashboard](https://console.developers.google.com) 
    2. Create new credentials from (if you don't have them)  
    3. Download client_secrets.json from your [Google Developer Dashboard](https://console.developers.google.com).
    4. Update the data-clientid in login.html with your clientid.

5. To enable Facebook Login:
    1. Login to [Facebook Developers](https://developers.facebook.com/)
    2. Create a new api key if you don't have one. 
    3. Create a file named fb_client_secrets.json with your app_id and app_secret key. The file should look like the snippet below.

        ```json
        {
          "web": {
            "app_id": "YOUR_APP_ID",
            "app_secret": "YOUR_APP SECRET"
          }
        }
        ```

    4. Update the appId in login.html with your Facebook appId.

## Usage
To start the web server run `python server.py`