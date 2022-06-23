## Python Cowsay

A small Python Flask app to display text using cowsay library.

## How to Run

Make sure you've Docker installed on your machine. Clone or download this repository.

```sh
git clone https://github.com/rioastamal-examples/python-cowsay.git
```

```sh
cd python-cowsay
```

Run pip command using Docker to install all dependencies.

```sh
docker run -v $(pwd):/app --rm -it \
public.ecr.aws/docker/library/python:3.8-slim \
pip install -r /app/requirements.txt --target=/app/libs
```

Then run the server. It should be available on port `8080`.

```sh
docker run -v $(pwd):/app --rm -it -p 8080:8080 \
public.ecr.aws/docker/library/python:3.8-slim \
bash /app/run-server.sh
```

Use cURL to test the app.

```sh
curl -s 'localhost:8080/?text=Hello%20people!'
```

```
  _____________
| Hello people! |
  =============
             \
              \
                ^__^
                (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
My Local IP: 172.26.44.245
```

You can use other character as well such as `milk`.

```sh
curl -s 'localhost:8080/?text=Hello%20people!&char=milk'
```

```
  _____________
| Hello people! |
  =============
             \
              \
               \
                \
                    ____________
                    |__________|
                   /           /\
                  /           /  \
                 /___________/___/|
                 |          |     |
                 |  ==\ /== |     |
                 |   O   O  | \ \ |
                 |     <    |  \ \|
                /|          |   \ \
               / |  \_____/ |   / /
              / /|          |  / /|
             /||\|          | /||\/
                 -------------|
                     | |    | |
                    <__/    \__>
My Local IP: 172.26.44.245
```

Available characters: 'beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux'.

## Running Test

Install development package first.

```sh
docker run -v $(pwd):/app --rm -it \
public.ecr.aws/docker/library/python:3.8-slim \
pip install -r /app/requirements.dev.txt --target=/app/libs.dev 
```

To run unit test issue following command.

```sh
docker run -v $(pwd):/app --rm -it \
-w /app -e PYTHONPATH=/app/libs.dev \
public.ecr.aws/docker/library/python:3.8-slim \
/app/libs.dev/bin/pytest -v
```

```
================================================= test session starts =================================================
platform linux -- Python 3.8.13, pytest-7.1.2, pluggy-1.0.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /app
collected 2 items                                                                                                     

tests/test_cowsay.py::test_root_path PASSED                                                                     [ 50%]
tests/test_cowsay.py::test_text_param PASSED                                                                    [100%]

================================================== 2 passed in 0.56s ==================================================
```

## License

This project is licensed under MIT License.
