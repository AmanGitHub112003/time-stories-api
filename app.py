import urllib.request
import xml.etree.ElementTree as ET
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Function to fetch and parse latest 6 stories
def get_latest_stories():
    url = "https://time.com/feed"
    response = urllib.request.urlopen(url)
    xml_data = response.read().decode("utf-8")

    root = ET.fromstring(xml_data)
    stories = []

    for item in root.findall("./channel/item")[:6]:
        title = item.find("title").text
        link = item.find("link").text
        stories.append({"title": title, "link": link})

    return stories


# HTTP request handler
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/getTimeStories":
            stories = get_latest_stories()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(stories, indent=2).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()


# Run the server
if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), MyHandler)
    print("✅ Server running at http://localhost:8000/getTimeStories")
    server.serve_forever()
