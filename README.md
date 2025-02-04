# sentiment-analysis-backend-task

Install Python3
upgrade pip to pip3
create virtual env
python3 -m venv .venv
activate virtual env
. .venv/bin/activate

install the packages that are required
pip3 install -r requirements.txt

run the project 
python3 main.py 
or
flask --app main.py --debug run
flask --app main.py run

pm2 start wsgi.py --name sentiment-api --interpreter python3
pm2 save
pm2 startup
