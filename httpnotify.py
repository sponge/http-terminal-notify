import os, cgi, sys
import argparse, subprocess
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class notificationHTTPServer(BaseHTTPRequestHandler):
    """Handle requests to be passed onto notification-center"""

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        if not form.has_key('message'):
            self.send_response(400)
            return

        cmd = ['/Applications/terminal-notifier.app/Contents/MacOS/terminal-notifier']
        # workaround for https://github.com/alloy/terminal-notifier/issues/11
        cmd.extend( [ '-message', '"%s"' % form['message'].value.replace('"', '\\"') ] )

        # terminal-notifier supports 'activate' for bundles and 'command'
        # for executing commands but this is potentitally dangerous
        valid_args = ['title','subtitle','group','url']

        for field in form.keys():
            if field not in valid_args:
                continue
            cmd.extend( [ '-%s' % field, '"%s"' % form[field].value.replace('"', '\\"') ] )

        subprocess.call(cmd)

        self.send_response(200)

if __name__=='__main__':
    parser = argparse.ArgumentParser( description='HTTP server frontend to terminal-notifier: https://github.com/alloy/terminal-notifier' )
    parser.add_argument( '--port', type=int, default=8080, help='Port number to listen on.' )
    args = parser.parse_args()
    
    if not os.path.exists( '/Applications/terminal-notifier.app/Contents/MacOS/terminal-notifier' ):
        sys.exit( "Couldn't find terminal-notifier.app inside /Applications/" )
    
    print 'Starting notification center server on port %i' % args.port
    try:
        server = HTTPServer( ('',args.port), notificationHTTPServer )
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()  
