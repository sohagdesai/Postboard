# Postboard
This project enables a user to post and edit articles. It stores the article's title and content in a database and caches the content for later retrieval. It provides a simple GUI interface to support the following API calls:

| Endpoint | HTTP Protocol    |  Request Payload                                                                  | Result                       |
| :------- | :--------------  | :-------------------------------------------------------------------------------- | :--------------------------  |
| /signup  | POST             | User details: name, email, password. User ID and user create time auto-generated. | User created.                |
| /login   | POST             | User credentials: email, password.                                                | User authenticated.          | 
| /add     | POST             | Article data: title, body. Article ID, article create time auto-generated.        | Article created.             |
| /fetch   | GET              | Authenticated user.                                                               | List of articles with article ID, title, body, create time, update time. |
| /edit    | GET              | Authenticated user, article ID to be edited.                                      | Article data: title, body.   |
| /edit    | POST             | Authenticated user, article data: title, body. Article update time auto-generated.| Article created.             |
| /logout  | POST             | Authenticated user.                                                               | User logged out. |

## Installation

**Installation**:

```shell
$ git clone https://github.com/sohagdesai/Postboard.git
$ cd Postboard
$ docker build -t postboard .
$ docker-compose up
```
## Usage
1. Browse to http://localhost:5000/login
2. Click "Signup".
3. Enter user details such as name, email address and passsword.
4. Click "Submit".
5. Login with credentials provided.
6. Enter title and article body.
7. Click "Submit". 
8. Click "Get My Articles" to see list of articles posted for this user sorted by creation date.
9. From Show Articles screen, enter ID of article to be edited. 
10. Click "Submit".
11. From Post Article screen, edit title and body.
12. Click "Submit"
13. Click "Get My Articles" and observe edited article among list of articles posted for this user sorted by creation date.
14. Click "Logout".

# Data Verification

## Verifying Postgres DB entries

```shell
$ docker container ls
$ docker exec -it <ID of postgres container from above command> bash
root@<ID of postgres container>:/# psql -U postgres
postgres=#  \c Postboard
postgres=#  SELECT * FROM "PB_Article";
postgres=#  SELECT * FROM "PB_User";
```

## Verifying Redis cache entries

```shell
$ docker container ls
$ docker exec -it <ID of redis container from above command> bash
root@<ID of redis container>:/data# redis-cli
127.0.0.1:6379> hgetall <stringified ID of any article>
```
