# HTTP & HTTPS — Task 1

## 1. Consume Data from an API Using Command Line Tools (`curl`)

### Introduction

`curl` is a command-line tool used to transfer data between a client and a server. It supports multiple protocols, including HTTP and HTTPS, and is commonly used to test APIs, inspect server responses, and send requests directly from the terminal.

This task focuses on using `curl` to interact with a public API and understand how API requests and responses work from the command line.

---

## 1. Checking That `curl` Is Installed

To confirm that `curl` is installed and available on your system, run:

```bash
curl --version

Expected result

This command should display:

the installed version of curl

supported protocols such as HTTP and HTTPS

supported features such as SSL, IPv6, and others

Example:

curl 7.81.0 (x86_64-pc-linux-gnu) libcurl/7.81.0 OpenSSL/3.0.2 ...
Protocols: dict file ftp ftps gopher http https ...
Features: alt-svc AsynchDNS HSTS HTTPS-proxy IPv6 Largefile SSL ...
2. Fetching a Web Page

A basic curl request can be used to retrieve the content of a web page.

Command
curl http://example.com
What it does

Sends a GET request to the server

Retrieves the body of the response

Displays the HTML content directly in the terminal

Expected result

The terminal should display the HTML source of the page.

3. Fetching Data from an API

A common use of curl is retrieving data from an API endpoint.

Command
curl https://jsonplaceholder.typicode.com/posts
What it does

Sends a GET request to the JSONPlaceholder API

Retrieves a list of posts in JSON format

Expected result

The output should be a JSON array containing multiple post objects.

Each object typically includes:

userId

id

title

body

Example:

[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit..."
  }
]
4. Fetching Only the Response Headers

Sometimes it is useful to inspect only the headers returned by a server.

Command
curl -I https://jsonplaceholder.typicode.com/posts
What it does

Sends a request to the server

Returns only the response headers

Does not display the response body

Expected result

The output should include:

the HTTP status code

content type

cache-related headers

server information

Example:

HTTP/2 200
content-type: application/json; charset=utf-8
cache-control: max-age=43200
...
Why this is useful

This helps identify:

whether the request succeeded

the type of content returned

caching behavior

other server configuration details

5. Sending Data with a POST Request

curl can also be used to send data to an API using a POST request.

Command
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
What it does

uses -X POST to specify the HTTP method

uses -d to send data in the request body

simulates the creation of a new post

Expected result

The API should return a JSON object representing the created post.

Example:

{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
Note

JSONPlaceholder does not actually store the new post. It only simulates a successful creation and returns a fake new id.

6. Useful curl Options Used in This Task
-I

Fetches only the response headers

Useful for checking status codes and server metadata

-X

Specifies the HTTP method to use

Example: POST, PUT, DELETE

-d

Sends data in the request body

Commonly used with POST, PUT, and PATCH

7. Summary

Using curl, it is possible to:

verify that the tool is installed

retrieve web pages and API data

inspect response headers

send data through POST requests

This makes curl a powerful and practical tool for testing and interacting with RESTful APIs directly from the command line.

8. Example Commands Recap
curl --version
curl http://example.com
curl https://jsonplaceholder.typicode.com/posts
curl -I https://jsonplaceholder.typicode.com/posts
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

Conclusion

This task shows that curl is a simple but powerful tool for interacting with web servers and APIs from the command line. By using basic requests such as GET and POST, and by inspecting headers with options like -I, it becomes easier to understand how clients and servers communicate. Learning to use curl is an important step toward testing, debugging, and working efficiently with RESTful APIs.
