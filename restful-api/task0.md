# HTTP & HTTPS — Task 0

## 0. Basics of HTTP/HTTPS

### Introduction

HTTP (Hypertext Transfer Protocol) is the foundation of communication on the web. It allows clients such as browsers and API consumers to communicate with servers and exchange data. HTTPS is the secure version of HTTP, adding SSL/TLS encryption to protect data during transmission.

---

## 1. HTTP vs HTTPS: Key Security Differences

### 1. Encryption

- **HTTP**
  - No encryption
  - Data travels in plain text
  - Usernames, passwords, cookies, and other sensitive data can be exposed

- **HTTPS**
  - Uses SSL/TLS to encrypt communication
  - Data is protected while in transit
  - Intercepted data cannot be easily read without the proper decryption keys

---

### 2. Data Integrity

- **HTTP**
  - Data can be modified during transmission without the client or server noticing

- **HTTPS**
  - Helps ensure that data is not altered during transmission
  - Protects against tampering and man-in-the-middle attacks

---

### 3. Authentication

- **HTTP**
  - Does not verify the identity of the website
  - Users may connect to a fake or malicious server without knowing it

- **HTTPS**
  - Uses digital certificates issued by trusted Certificate Authorities (CAs)
  - Confirms that the client is communicating with the legitimate server

---

### 4. Default Ports

- **HTTP**
  - Uses port **80** by default

- **HTTPS**
  - Uses port **443** by default

---

### 5. Typical Use Cases

- **HTTP**
  - Suitable only for non-sensitive communication
  - Rarely recommended for modern production websites

- **HTTPS**
  - Required for websites that handle logins, payments, personal data, or APIs
  - Standard choice for modern websites and web services

---

## 2. Structure of an HTTP Request and Response

### 1. Example of an HTTP Request

#```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html

Parts of the request:

Method: GET

Path: /index.html

HTTP Version: HTTP/1.1

Headers:

Host

User-Agent

Accept

2. Example of an HTTP Response

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256

<html>
 <body>Hello</body>
</html>
Parts of the response

HTTP Version: HTTP/1.1

Status Code: 200

Status Message: OK

Headers:

Content-Type

Content-Length

Body: the content returned by the server

3. Common HTTP Methods
1. GET

Description: Retrieves data from the server

Use case: Loading a web page or fetching information from an API

2. POST

Description: Sends data to the server to create a new resource

Use case: Submitting a form or creating a new account

3. PUT

Description: Updates an existing resource

Use case: Editing user profile information or updating stored data

4. DELETE

Description: Removes a resource from the server

Use case: Deleting a user, post, or item from a database

4. Common HTTP Status Codes
1. 200 OK

Description: The request was successful

Scenario: A web page loads correctly or an API returns data successfully

2. 201 Created

Description: A new resource was successfully created

Scenario: A new user account is created through an API

3. 400 Bad Request

Description: The server could not process the request because it was invalid

Scenario: A form is submitted with missing or incorrect data

4. 404 Not Found

Description: The requested resource could not be found

Scenario: A page or API endpoint does not exist

5. 500 Internal Server Error

Description: The server encountered an unexpected error

Scenario: The application crashes or fails while processing a request

Conclusion

HTTP and HTTPS are both used for communication between clients and servers, but HTTPS adds encryption, authentication, and data integrity. Understanding HTTP methods, request and response structure, and common status codes is essential for working with RESTful APIs and web services.
