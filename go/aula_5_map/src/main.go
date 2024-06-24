package main

import "fmt"

func main() {
	// map representa um conjunto de chave-valor
	// map é uma estrutura de dados nativa do go
	// onde a estrutura é definida por map[TipoDaChave]TipoDoValor
	myMap := make(map[string]int)
	myMap["one"] = 1
	myMap["two"] = 2
	myMap["three"] = 3

	fmt.Println(myMap)
}