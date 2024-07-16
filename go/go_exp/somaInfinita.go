package main

func somaInfinita(n ... int) int {
	
	var soma int
	for _, v := range n { // _ is the index, v is the value
		soma += v
	}
	return soma
	
}