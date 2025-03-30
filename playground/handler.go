// handler for api to accept name as input and return hello name message
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

// Response represents the API response structure
type Response struct {
	Message string `json:"message"`
}

// Server holds the server configuration
type Server struct {
	port string
}

// NewServer creates a new server instance
func NewServer(port string) *Server {
	return &Server{
		port: port,
	}
}

// helloHandler handles the /hello endpoint
func (s *Server) helloHandler(w http.ResponseWriter, r *http.Request) {
	// Only allow GET requests
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	// Get name from query parameters
	name := r.URL.Query().Get("name")
	if name == "" {
		http.Error(w, "Name parameter is required", http.StatusBadRequest)
		return
	}

	// Create response
	response := Response{
		Message: fmt.Sprintf("Hello, %s!", name),
	}

	// Set response headers
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	// Encode and send response
	if err := json.NewEncoder(w).Encode(response); err != nil {
		log.Printf("Error encoding response: %v", err)
		http.Error(w, "Internal server error", http.StatusInternalServerError)
		return
	}
}

// Start initializes and starts the HTTP server
func (s *Server) Start() error {
	// Register routes
	http.HandleFunc("/hello", s.helloHandler)

	// Start server
	log.Printf("Starting server at port %s", s.port)
	return http.ListenAndServe(":"+s.port, nil)
}

func main() {
	server := NewServer("8080")
	if err := server.Start(); err != nil {
		log.Fatalf("Server failed to start: %v", err)
	}
}

