# Create docker image
docker build -t random_vectorizer .

# Build docker container from image
docker run -d -p 5000:5000 --name random_vectorizer random_vectorizer:latest