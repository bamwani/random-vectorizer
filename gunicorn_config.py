bind = '0.0.0.0:5000'  # Bind to all network interfaces on port 8000
workers = 4  # Number of worker processes
threads = 2  # Number of worker threads per process
worker_class = 'gevent'  # Use the Gevent worker class for improved concurrency

# SSL/TLS Configuration
# certfile = '/path/to/certificate.crt'
# keyfile = '/path/to/private.key'
# ssl_version = 'TLSv1_2'  # Specify the desired SSL/TLS version