## 🧠 API Basics

## What is API?

- API = Application Programming Interface
- A way to request data or service from another system 
- It allows different programs to communicate

## How it works?

- You send a request
- API acts as a middleman between:
  - Client (your app)
  - Server (data source)
- You get a response  

---

## Endpoint

- A specific URL where API receives requests  

Examples:
- /users  
- /products  
- /login  

---

## Request

- What you send to the API  

Includes:
- URL  
- Method  
- Data (optional)  

---

## Response

- What API returns  

Contains:
- Data  
- Status  

---

## Request Methods

- GET → fetch data  
- POST → send/create data  
- PUT → update data  
- DELETE → remove data  

---

## Status Codes

- 200 → Success  
- 404 → Not found  
- 500 → Server error  
- 401 → Unauthorized  

---

## Real Flow

Your Python code  
↓  
Create request  
↓  
Send over internet  
↓  
Server receives  
↓  
Server sends to AI  
↓  
AI generates response  
↓  
Response comes back  
↓  
You use it  

---

## Simple Thinking

`input() → send to API → get response → print()`



---

## 🌐 HTTP / HTTPS Basics

- HTTP = HyperText Transfer Protocol  
- Used to send data between client and server  

---

### What is HTTPS?

- HTTPS = Secure version of HTTP  
- Data is encrypted (protected)  

---

### What are Headers?

- Metadata sent with request and response  
- Helps with:
  - Authentication  
  - Caching  
  - Managing state  

---

### Types of Headers

- Request headers → from client  
- Response headers → from server  
- Representation headers → encoding / compression  
- Payload headers → actual data  

---

### Common Headers

- Accept → application/json  
- User-Agent  
- Authorization  
- Content-Type  
- Cookie  
- Cache-Control  

---

### HTTP Methods

- GET → retrieve data  
- POST → send data  
- PUT → replace data  
- DELETE → remove data  
- PATCH → update part of data  
- OPTIONS → check available operations  
- HEAD → headers only  
- TRACE → loopback test  

---

### Status Codes

- 1xx → Informational  
- 2xx → Success  
- 3xx → Redirection  
- 4xx → Client error  
- 5xx → Server error  

Examples:
- 100 → Continue
- 102 → Processing
- 200 → OK  
- 201 → Created  
- 202 → Accepted
- 307 → Temporary redirect
- 308 → Permanent redirect
- 400 → Bad request  
- 401 → Unauthorized  
- 402 → Payment required
- 404 → Not found  
- 500 → Server error  
- 504 → Gateway timeout  


---

## 📦 JSON Basics

### What is JSON?

- JSON = JavaScript Object Notation  
- Used to store and exchange data  

---

### Why JSON?

- Easy to read  
- Easy to write  
- Used in APIs everywhere  

---

### Basic Structure

{
  "name": "Khushan",
  "age": 19
}

- Key: Value format
  - "name" → key
  - "khushan" → vlue

# Rules of JSON

- Keys must be in double quotes ""
- Data is in key: value pairs
- Use {} for objects
- Use [] for lists

# Data types in JSON

{
    "name": "khushan",  // String
    "age": 19,  // Number
    "is_student: true,  // Boolean
    "skills": ["python", "fitness"],  // Lists
    "city": null  // Empty value
}    

# JSON objects vs JSON arrays

- Object → A collection of key-value pairs inside {}.
{
    "name": "khushan",
    "age": 19
}

- Array → A special type of object used to store multiple values under a single variable name.
[ "Tony", "Robert", "Max"]

# Nested JSON (JSON inside JSON)

{
    "name": "khushan",
    "skills": ["Python", "Gym"],
    "details": {
        "age": 19,
        "city": "Jaipur"
    }
}

# Common Mistakes

- Using single quotes
- Missing commas
- Keys without quotes

# Real Understanding

- JSON is NOT code
- JSON is just a data format