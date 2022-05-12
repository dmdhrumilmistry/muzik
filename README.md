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

# License

[MIT License](https://github.com/dmdhrumilmistry/muzik/blob/main/LICENSE)


### Have any Ideas 💡 or issue
- Create an issue
- Fork the repo, update script and create a Pull Request
       
       
### Connect with me on:

<p align ="center">
    <table>
      <tr>
        <td><a hrf = "https://github.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Github-dmdhrumilmistry-333"></a></td>
        <td><a href = "https://www.instagram.com/dmdhrumilmistry/" target="_blank"><img src = "https://img.shields.io/badge/Instagram-dmdhrumilmistry-833ab4"></a></td>
        <td><a href = "https://twitter.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Twitter-dmdhrumilmistry-4078c0"></a></td>
      </tr>
      <tr>
        <td><a href = "https://www.youtube.com/channel/UChbjrRvbzgY3BIomUI55XDQ" target="_blank"><img src = "https://img.shields.io/badge/YouTube-Dhrumil%20Mistry-critical"></a></td>
        <td><a href = "https://dhrumilmistrywrites.blogspot.com/ " target="_blank"><img src = "https://img.shields.io/badge/Blog-Dhrumil%20Mistry-bd2c00"></a></td>
        <td><a href = "https://www.linkedin.com/in/dmdhrumilmistry/" target="_blank"><img src = "https://img.shields.io/badge/LinkedIn-Dhrumil%20Mistry-4078c0"></a></td>
    </table>
</p>
