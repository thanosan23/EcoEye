# EcoEye

## Inspiration
Ever since we were children, we enjoyed playing outside and being outdoors, but as we grew up, we noticed more and more trash around the places we played. We went on garbage pick ups annually, but this did little to counteract the billions of people littering worldwide. Because of the problem pollution poses to our environment, we designed EcoEye. EcoEye is an AI that can detect trash in images.

## What it does
Users can input an image and EcoEye AI will detect how many pieces of trash are in the given image.

## How we built it
For the AI, we used YoloV5, a state of the art artificial intelligence model, to detect garbage in a given image. We used Flask to create a web server. Additionally, we used Vanilla JavaScript, HTML, and CSS for the front-end of the website. The front-end of the website communicates with the web server.

## How to use it
The frontend website is hosted on `frontend/`. The server is on `serve.py`. Run `python serve.py` to start the server (if we had the resources, we would also host the backend as well, but as of right now, you have to start up the server locally). Then, go onto the website locally or using the website `https://ecoeye.vercel.app/`, and from there, you can start using the website. Enjoy!
