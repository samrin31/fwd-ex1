from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>student info</title>
</head>
<body>
<h1>student details</h1>
<table border="1" cellipadding="8">
  <tr>
    <th>name</th>
    <th>roll</th>
    <th>department</th>
  </tr>
  <tr>
    <td>arun</td>
    <td>101</td>
    <td>cse</td>
  </tr>
  <tr>
    <td>banu</td>
    <td>102</td>
    <td>ece</td>
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
server_address = ('',80)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()