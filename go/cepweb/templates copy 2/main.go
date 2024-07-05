package main

import (
	"net/http"
	"text/template"
)

type Curso struct {
	Nome         string
	CargaHoraria int
}

type Cursos []Curso

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		t := template.Must(template.New("template.html").ParseFiles("template.html"))
		err := t.Execute(w, Cursos{
			Curso{"go", 40},
			Curso{"python", 10},
			Curso{"ruby", 46},
		})
		if err != nil {
			panic(err)
		}
	})
	http.ListenAndServe(":8282", nil)
}
