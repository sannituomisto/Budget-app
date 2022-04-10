from dotenv import load_dotenv
import os

dirname = os.path.dirname(__file__)
try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

BUDGET_FILENAME = os.getenv('BUDGET_FILENAME') or 'budget.csv'
BUDGET_FILE_PATH = os.path.join(dirname, '..', 'data', BUDGET_FILENAME)
DB_FILENAME = os.getenv('DB_FILENAME') or 'database.sqlite'
DB_FILE_PATH = os.path.join(dirname, '..', 'data', DB_FILENAME)
