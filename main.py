from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from io import BytesIO
from PIL import Image
import numpy as np
import time

global LTIME
LTIME = cur_time = time.monotonic()

class RequestHandler(BaseHTTPRequestHandler):
    MATRIX_SIZE = (800, 1024)
    COLORS = {
        'w': (255, 255, 255),
        'b': (0, 0, 0),
        'r': (255, 0, 0),
        'g': (0, 255, 0),
    }

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()

        matrix = self.get_matrix()
        matrix = np.flip(matrix, axis=0)
        self.send_image(matrix)

    def do_POST(self):
        global LTIME
        cur_time = time.monotonic()
        address = self.client_address[0]
        print("IP: ", address)

        if cur_time - LTIME <= 0.01:
            self.send_error(429, 'Too Many Requests')
            self.send_response(429)
            return 0
        else:
            LTIME = time.monotonic()
        
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            params = parse_qs(body.decode('utf-8'))

            y = int(params['y'][0])
            x = int(params['x'][0])
            color = params['color'][0]

            matrix = self.get_matrix()
            matrix[x][y] = self.COLORS[color]

            self.save_matrix(matrix)
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()

    def get_matrix(self):
        try:
            with open('matrix.npy', 'rb') as f:
                matrix = np.load(f)
        except FileNotFoundError:
            matrix = np.full(shape=(*self.MATRIX_SIZE, 3), fill_value=255, dtype=np.uint8)
            self.save_matrix(matrix)
    
        return matrix

    def save_matrix(self, matrix):
        with open('matrix.npy', 'wb') as f:
            np.save(f, matrix)

    def send_image(self, matrix):
        image = Image.fromarray(matrix)
        buffer = BytesIO()
        image.save(buffer, format='PNG')
        self.wfile.write(buffer.getvalue())


def run():
    server = HTTPServer(('127.0.0.1', 3333), RequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    run()






