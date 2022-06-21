## Python Cowsay

A small Python Flask app to display text using cowsay library.

## How to Run

Make sure you've Docker installed on your machine. Run pip command using Docker to install all dependencies.

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

## License

This project is licensed under MIT License.
