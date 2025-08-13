import streamlit as st
import dropbox
import requests
from urllib.parse import urlencode
import os

DROPBOX_APP_KEY = st.secrets["dropbox"]["app_key"]
DROPBOX_APP_SECRET = st.secrets["dropbox"]["app_secret"]
DROPBOX_REFRESH_TOKEN = st.secrets["dropbox"]["refresh_token"]
DROPBOX_FOLDER = '/ReportesBPM/'

# 1. Obtener refresh token (solo la primera vez, localmente)
def obtener_refresh_token():
    params = {
        'response_type': 'code',
        'client_id': DROPBOX_APP_KEY,
        'redirect_uri': 'http://localhost:8501/',
        'token_access_type': 'offline',
    }
    url = f'https://www.dropbox.com/oauth2/authorize?{urlencode(params)}'
    print('Abre esta URL en tu navegador e inicia sesión:')
    print(url)
    code = input('Pega aquí el código de autorización: ')
    data = {
        'code': code,
        'grant_type': 'authorization_code',
        'client_id': DROPBOX_APP_KEY,
        'client_secret': DROPBOX_APP_SECRET,
        'redirect_uri': 'http://localhost:8501/',
    }
    resp = requests.post('https://api.dropbox.com/oauth2/token', data=data)
    resp.raise_for_status()
    tokens = resp.json()
    print('Pon este refresh_token en secrets.toml:')
    print(tokens['refresh_token'])

# 2. Obtener access token usando refresh token
def get_access_token():
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': DROPBOX_REFRESH_TOKEN,
        'client_id': DROPBOX_APP_KEY,
        'client_secret': DROPBOX_APP_SECRET,
    }
    resp = requests.post('https://api.dropbox.com/oauth2/token', data=data)
    resp.raise_for_status()
    return resp.json()['access_token']

# 3. Subir archivo a Dropbox usando access token válido
def subir_a_dropbox(archivo):
    access_token = get_access_token()
    dbx = dropbox.Dropbox(oauth2_access_token=access_token)
    nombre_archivo = os.path.basename(archivo)
    ruta_destino = DROPBOX_FOLDER + nombre_archivo
    with open(archivo, 'rb') as f:
        dbx.files_upload(f.read(), ruta_destino, mode=dropbox.files.WriteMode.overwrite)
    shared_link_metadata = dbx.sharing_create_shared_link_with_settings(ruta_destino)
    return shared_link_metadata.url