## Installation

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/sohagdesai/Postboard.git
$ cd Postboard
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ flask run
```
## Usage

* `FLASK_APP`: Entry point of application (should be `wsgi.py`).
* `FLASK_ENV`: The environment to run app in (either `development` or `production`).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt app's data.
* `SQLALCHEMY_DATABASE_URI`: Connection URI of a SQL database.
* `LESS_BIN`: Path to local LESS installation via `which lessc` (optional for static assets).
* `ASSETS_DEBUG`: Debug asset creation and bundling in `development` (optional).
* `LESS_RUN_IN_DEBUG`: Debug LESS while in `development` (optional).
* `COMPRESSOR_DEBUG`: Debug asset compression while in `development` (optional).
-----
