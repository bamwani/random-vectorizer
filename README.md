# Random Vectorizer API

The Random Vectorizer API is a production-ready API endpoint that takes a sentence as input and returns a random 500-dimensional array of floats. This project has been developed with considerations for scalability, security, and performance to ensure it meets the requirements of a production environment.

## Pre-requisites (for Production deployment):
1. Docker installed in server.

## Installation - Development

1. Clone the repository:

   ```shell
   git clone https://github.com/bamwani/random-vectorizer.git

2. Navigate to the project directory:

    ```shell
    cd random-vectorizer
    
3. Run the following command to create a virtual environment for the application using Python3-venv:
    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```
    
4. Update pip and install the reuired libraries using the following command:
    ```shell
    pip3 install--upgrade pip
    pip3 install -r requirements.txt
    
## Usage - Development

1. Run the folling command to test and start the server:
    ```shell
    sh ./start_main_app.sh
    

This will create a docker image named "random_vectorizer", Run it by using the same name as container name and start the service


## Installation - Production (using Docker)

1. Clone the repository:

   ```shell
   git clone https://github.com/bamwani/random-vectorizer.git

2. Navigate to the project directory:

    ```shell
    cd random-vectorizer
    
3. Run the following command to install the application using docker:
    ```shell
    sh ./install.sh
    ```
This will create a docker image named "random_vectorizer", Run it by using the same name as container name and start the service


## Usage - Production (using Docker)

1. Start the docker container:
    ```shell
    sh ./start_docker.sh

2. Send a POST request to the API endpoint using your favorite HTTP client or tool (e.g., cURL, Postman).
    ```shell
    POST /vectorize HTTP/1.1
    Host: localhost:5000
    Content-Type: application/json
    
    {
      "sentence": "This is an example sentence"
    }
The API will respond with a JSON object containing the random 500-dimensional array of floats.


## Configuration

1. The application uses Gunicorn as the production-ready server. The Gunicorn configuration is defined in the gunicorn_config.py file. You can modify the configuration parameters to customize the server behavior according to your needs.

2. SSL/TLS: By default, the application runs over HTTP. If you want to enable SSL/TLS encryption, you can provide the appropriate SSL/TLS certificate and private key files and configure Gunicorn to use HTTPS. Refer to the Gunicorn documentation for detailed instructions.

## Running Tests:

1. To run the unit tests for the application, execute the following command:
    ```shell
    pytest

The tests ensure the functionality of the vectorization process and the expected behavior of the API endpoint.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.