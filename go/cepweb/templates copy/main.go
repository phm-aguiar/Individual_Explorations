package main

import (
	"os"
	"text/template"
)

type Curso struct {
	Nome         string
	CargaHoraria int
}

func main() {
	curso := Curso{"go", 40}
	tmp := template.New("Curso sobre templates")

	tmp, _ = tmp.Parse("O curso de {{.Nome}} tem carga horária de {{.CargaHoraria}} horas")
	err := tmp.Execute(os.Stdout, curso)
	if err != nil {
		panic(err)
	}
}
