from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
import cgi

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

def list_all(database):
    collective = session.query(database).all()
    return collective

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                places = list_all(Restaurant)

                output += "<html><body>"
                for p in places:
                    output += "<h2>%s</h2>" % p.name
                    output += "<a href='/restaurants/%s/edit'>Edit</a><br>" % p.id
                    output += "<a href='/restaurants/%s/delete'>Delete</a>" % p.id
                    output += "<br><br>"
                output += '''<a href="/restaurants/new"><h2>
                          Add New Restuarant</h2></a>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output =""
                output += "<html><body>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><h2>What ought this restaurant be called?</h2><input name='restaurant_name' type='text'><input type='submit' value=Submit></form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/edit"):
                restaurant_path = self.path.split("/")[2]
                rest = session.query(Restaurant).filter_by(id = restaurant_path).one()
                if rest:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurant_path
                    output += "<h2>What would you like to rename this restaurant?</h2>"
                    output += "<input name='restaurant_name' type='text'><input type='submit' value= 'Submit'>"
                    output += "</form></body></html>"
                    self.wfile.write(output)
                    print output
                    return

            if self.path.endswith("/delete"):
                restaurant_path = self.path.split("/")[2]
                rest = session.query(Restaurant).filter_by(id = restaurant_path).one()
                if rest:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurant_path
                    output += "<h2>Are you sure you want to delete this restaurant?</h2>"
                    output += "<input type='submit' value= 'Delete'>"
                    output += "</form></body></html>"
                    self.wfile.write(output)
                    print output
                    return

        except:
            self.send_error(404, "File not found %s" % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                restaurant = fields.get('restaurant_name')
                output =""
                output += "<html><body>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/new'><h2>What ought this restaurant be called?</h2><input name='restaurant_name' type='text'><input type='submit' value=Submit></form>'''
                output += "</body></html>"
                new_restaurant = Restaurant(name=restaurant[0])
                session.add(new_restaurant)
                session.commit()
                print output

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    new_name = fields.get('restaurant_name')
                    rest_id = self.path.split("/")[2]

                    restaurant = session.query(Restaurant).filter_by(id=rest_id).one()
                    if restaurant:
                        restaurant.name = new_name[0]
                        session.add(restaurant)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    rest_id = self.path.split("/")[2]

                    restaurant = session.query(Restaurant).filter_by(id=rest_id).one()
                    if restaurant:
                        session.delete(restaurant)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()
        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, you f***ed up now..."
        server.socket.close()

if __name__ == '__main__':
    main()
