const express = require('express');

class Server {
    constructor(port = 8080) {
        this.port = port;
        this.app = express();
        this.setupRoutes();
    }

    setupRoutes() {
        // Hello endpoint
        this.app.get('/hello', (req, res) => {
            const name = req.query.name;
            
            if (!name) {
                return res.status(400).json({
                    error: 'Name parameter is required'
                });
            }

            const response = {
                message: `Hello, ${name}!`
            };

            res.status(200).json(response);
        });
    }

    start() {
        this.app.listen(this.port, () => {
            console.log(`Starting server at port ${this.port}`);
        });
    }
}

// Create and start server
const server = new Server(8080);
server.start(); 