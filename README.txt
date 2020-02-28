# I. No Docker

# Activate env
$ pipenv shell

# Install dependencies
$ pipenv install

./run.sh
python app2.py

# II. With Docker

$ (sudo) docker build -t fastapi:latest .
$ (sudo) docker run -it -d -p 5001:5001 fastapi