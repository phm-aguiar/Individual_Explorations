package main

// na biblioteca fmt temos a função Println melhor que a função println
import "fmt"

func main() {
	lista := [3]int{}
	lista[0] = 1
	lista[1] = 2
	lista[2] = 42

	// o compilador do go consegue inferir o tamanho do array
	// então podemos usar o ... para que ele infira o tamanho
	// da lista
	lista2 := [...]int{1, 42, 42}


	// o print do go não aceita imprimir um array inteiro
	println(lista[0])
	// por isso usamos a biblioteca fmt
	fmt.Println(lista)
	fmt.Println(lista2)

	// o go não permite que um array seja atribuído a outro
	// array de tamanho diferente
	lista = lista2
	fmt.Println(lista)

	// funcoes de array
	fmt.Println(len(lista))
	fmt.Println(cap(lista))

	// slices
	// slices são como arrays, mas não tem tamanho fixo
	// slices são como ponteiros para arrays
	// slices são mais utilizados que arrays
	// slices são mais flexíveis que arrays
	// slices são mais eficientes que arrays
	// slices são mais seguros que arrays
	fatia := lista[0:2]
	fmt.Println(fatia)
	fatia = append(fatia, 42)
	fmt.Println(fatia)

	lista3 := []float32{1.2, 42.2, 42.3}
	fmt.Println(lista3)

	lista4 := make([]float32, 10)
	lista4[7] = 42.42
	fmt.Println(lista4)
	fmt.Println(len(lista4))

}