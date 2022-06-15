import os

## Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///infra/tmp/olatcg.db'

## Paths
API_PATH = '/api'

## External Urls
OLATCG_BACKEND = 'https://olatcg-backend.herokuapp.com/api'

## Global Alignment
DEFAULT_MATCH_SCORE = 2
DEFAULT_MISMATCH_SCORE = -1

## Exe paths
CLUSTALW2_PATH = os.getcwd() + '/web_app/infra/exe/clustalw2'

## System Constants
E_VALUE_THRESH_BLASTN = 0.00000000001