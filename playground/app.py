from flask import Flask, request, jsonify
import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Server:
    def __init__(self, port: int = 8080):
        self.port = port
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self) -> None:
        """Set up API routes"""
        self.app.route('/hello', methods=['GET'])(self.hello_handler)

    def hello_handler(self) -> tuple[Dict[str, str], int]:
        """
        Handle the /hello endpoint
        Returns a JSON response with a greeting message
        """
        # Get name from query parameters
        name = request.args.get('name')
        
        if not name:
            return jsonify({'error': 'Name parameter is required'}), 400

        # Create response
        response = {
            'message': f'Hello, {name}!'
        }

        return jsonify(response), 200

    def start(self) -> None:
        """Start the Flask server"""
        logger.info(f"Starting server at port {self.port}")
        self.app.run(host='0.0.0.0', port=self.port)

def main():
    server = Server(port=8080)
    server.start()

if __name__ == '__main__':
    main() 