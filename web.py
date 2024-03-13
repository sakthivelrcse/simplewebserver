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