# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<table border=2>
<tr>
<th>Company</th> <th>Revenue</th> <th>Financial Year</th>
</tr>
<tr>
<td>Micro Soft</td> <td>$9034</td> <td>2014</td>
</tr>
<tr>
<td>Amazon</td> <td>$8904</td> <td>2014</td>
</tr>
<tr>
<td>Apple</td> <td>$1233</td> <td>2014</td>
</tr>
<tr>
<td>Flipkart</td> <td>$6789</td> <td>2014</td>
</tr>
<tr>
<td>Stofinex</td> <td>$9889</td> <td>2014</td>
</tr>
<tr>
<td>TCS</td> <td>$8589</td> <td>2014</td>
</tr>
<tr>
<td>Infy</td> <td>$8967</td> <td>2014</td>
</tr>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2024-03-13 155527.png>)
![alt text](<Screenshot 2024-03-13 155613.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
