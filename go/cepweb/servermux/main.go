package main

import "net/http"

func main() {
	// pq usar mux ao inves de http.ListenAndServe(":8080", nil)?
	// pq o mux é um roteador de requisições HTTP
	// ele é um objeto que implementa a interface http.Handler
	// se eu criasse outro mux e direcionasse para a porta 8081 por exemplo
	// eu poderia ter dois servidores rodando na mesma máquina
	// um na porta 8080 e outro na porta 8081

	mux := http.NewServeMux()

	mux.HandleFunc("/", HomeHandler)
	mux.Handle("/blog", &blog{title: "My Blog"})
	http.ListenAndServe(":8080", mux)

	// mux2 := http.NewServeMux()
	// mux2.HandleFunc("/", HomeHandler)
	// mux2.Handle("/blog", &blog{title: "My Blog number 2"})
	// http.ListenAndServe(":4000", mux2)

}


func HomeHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello World!"))
}


type blog struct {
	title string
}

func (b *blog) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Welcome to my blog: " + b.title))
}