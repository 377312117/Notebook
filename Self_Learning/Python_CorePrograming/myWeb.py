from wsgiref.simple_server import make_server

def application(environ,start_response):
    print(environ)
    start_response("200 OK",[("Content-Type",'text/html')])
    return [b'<h1>Hello web</h1>']

httpd = make_server('',8080,application)

print('Serving HTTP on port 8080...')

httpd.serve_forever()