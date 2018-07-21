# Download unseen files from a folder in Google Drive
Example:
~~~
cd ~/Documents
drive-download scanbot
~~~

The script only downloads files it hasn't seen before.

## Configuring
1. Get Google Drive API id and secret from the Google API console.
2. Create and edit `.config/drive-download/settings.yaml`:

~~~
client_config_backend: settings
client_config:
  client_id: XXX.apps.googleusercontent.com
  client_secret: _s3cr3deadc4fef00baR

  save_credentials: True
  save_credentials_backend: file
  save_credentials_file: /home/USERNAME/.cache/drive-download/credentials.json
~~~
