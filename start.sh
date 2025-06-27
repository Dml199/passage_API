
source bin/activate

pip install -r requirements.txt

sudo -u postgres psql -c "CREATE DATABASE mydatabase;" 2>/dev/null

python3 app/test.py

cd app

uvicorn main:app --reload
