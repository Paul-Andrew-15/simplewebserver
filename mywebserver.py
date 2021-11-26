from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>MY WEBSERVER</title>
</head>
<body>
<h1>TOP FIVE PROGRAMMING LANGUAGES</h1> 
1.Python<p>
2.Java<p>
3.Javascript<p>
4.C programming<p>
5.C++ programming<p>


<h1>1.PYTHON</h1>
Python is an interpreted high-level general-purpose programming language.
Its design philosophy emphasizes code readability with its use of significant indentation. 
Its language constructs as well as its object-oriented approach aim to help programmers write clear,
logical code for small and large-scale projects.<p>

<h1>2.JAVA</h1>
Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.
It is a general-purpose programming language intended to let programmers write once, run anywhere (WORA), meaning that compiled Java code can 
run on all platforms that support Java without the need for recompilation.<p>

<h1>3.JAVASCRIPT</h1>
JavaScript often abbreviated as JS, is a programming language that conforms to the ECMAScript specification.
JavaScript is high-level, often just-in-time compiled and multi-paradigm. It has dynamic typing, 
prototype-based object-orientation and first-class functions.<p>

<h1>4.C PROGRAMMING</h1>
C is a general-purpose, procedural computer programming language supporting structured programming, lexical variable scope,
and recursion, with a static type system. By design, C provides constructs that map efficiently to typical machine instructions.
It has found lasting use in applications previously coded in assembly language.<p>

<h1>5.C++ PROGRAMMING</h1>
C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or "C with Classes".
The language has expanded significantly over time, and modern C++ now has object-oriented, generic, and functional features in addition to facilities 
for low-level memory manipulation.<p>
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