#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle HTTP GET requests for a simple API."""

    def do_GET(self):
        """Handle GET requests and return the correct response."""
        # Check if the user is requesting the root endpoint
        if self.path == "/":
            # Send HTTP status code 200 (OK)
            self.send_response(200)

            # Specify that the response content is plain text
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            # Send the response body as bytes
            self.wfile.write(b"Hello, this is a simple API!")

        # Check if the user is requesting the /data endpoint
        elif self.path == "/data":
            # Create sample data as a Python dictionary
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            # Convert the dictionary into a JSON string
            json_data = json.dumps(data)

            # Send HTTP status code 200 (OK)
            self.send_response(200)

            # Specify that the response content is JSON
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # Send the JSON response encoded as bytes
            self.wfile.write(json_data.encode("utf-8"))

        # Check if the user is requesting the /status endpoint
        elif self.path == "/status":
            # Send HTTP status code 200 (OK)
            self.send_response(200)

            # Specify that the response content is plain text
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            # Send a simple status message
            self.wfile.write(b"OK")

        # Check if the user is requesting the /info endpoint
        elif self.path == "/info":
            # Create API information as a Python dictionary
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            # Convert the dictionary into a JSON string
            json_info = json.dumps(info)

            # Send HTTP status code 200 (OK)
            self.send_response(200)

            # Specify that the response content is JSON
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # Send the JSON response encoded as bytes
            self.wfile.write(json_info.encode("utf-8"))

        # Handle all undefined endpoints
        else:
            # Send HTTP status code 404 (Not Found)
            self.send_response(404)

            # Specify that the response content is plain text
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            # Send the error message
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    # Define the server address and port number
    server_address = ("", 8000)

    # Create the HTTP server using the handler class
    httpd = HTTPServer(server_address, SimpleAPIHandler)

    # Display a message showing that the server is running
    print("Server running on port 8000...")

    # Start the server and keep it running
    httpd.serve_forever()
