import os

## Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///infra/tmp/olatcg.db'

## Paths
API_PATH = '/api'

## Global Alignment
DEFAULT_MATCH_SCORE = 2
DEFAULT_MISMATCH_SCORE = -1

## Exe paths
CLUSTALW2_PATH = os.getcwd() + '/web_app/infra/exe/clustalw2'