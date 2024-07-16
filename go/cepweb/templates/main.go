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
	t := template.Must(template.New("Curso sobre templates").Parse("O curso de {{.Nome}} tem carga horária de {{.CargaHoraria}} horas"))
	err := t.Execute(os.Stdout, curso)
	if err != nil {
		panic(err)
	}
}

