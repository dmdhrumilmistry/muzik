# Muzik

Music Downloader created using django framework
![Muzik Logo](https://github.com/dmdhrumilmistry/muzik/blob/main/static/images/logo/logo.png?raw=True)

## Installation

- Clone/Download repo

  ```bash
  git clone https://github.com/dmdhrumilmistry/muzik.git
  ```

- Change path to cloned directory

  ```bash
  cd muzik
  ```
  
- Install requirements

  ```bash
  python3 -m pip install -r requirements.txt 
  ```
  
- Make Migrations

  ```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

- Check for errors

  ```bash
  python3 manage.py check
  ```

- Run Server

  ```bash
  python3 manage.py runserver
  ```
  
## Heroku deployment

- Install Heroku CLI and clone `muzik` repo

- Login to acc

  ```bash
  heroku login
  ```

- Create app and add repo

- add heroku git to local repo

  ```bash
  heroku git:remote -a [app-name]
  ```

- Set Environment variable

  ```bash
  heroku config:set DJANGO_DEBUG=False --app [app-name]
  ```
  
- Commit changes (if any) and push repo.

  ```bash
  git push heroku main
  ```
