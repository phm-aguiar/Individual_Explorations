package main

import (
	"log"
	"net/http"
	"time"
)

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)

}

func handler(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()
	log.Println("Request received")
	defer log.Println(`Request processed`)
	select {
	case <-time.After(5 * time.Second):
		log.Println("request processed in 5 seconds")
		w.Write([]byte("request processed in 5 seconds"))
	case <-ctx.Done():
		log.Println("request canceled:", ctx.Err())
		http.Error(w, ctx.Err().Error(), http.StatusRequestTimeout)
	}
}
