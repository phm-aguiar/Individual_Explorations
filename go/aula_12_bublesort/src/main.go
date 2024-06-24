/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.go                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/13 09:01:54 by phenriq2          #+#    #+#             */
/*   Updated: 2024/06/17 17:49:44 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

package main

import "fmt"

func main() {
	var numeros = []int{}

	for {
		var numero int
		_, err := fmt.Scanf("%v", &numero)
		if err != nil {
			break
		}
		numeros = append(numeros, numero)
	}

	fmt.Printf("%v", bubbleSort(numeros))
	fmt.Printf("%v", mergeSort(numeros))
}

func bubbleSort(numeros []int) []int {
	var movCounter int
	for i := 0; i < len(numeros); i++ {
		for j := 0; j < len(numeros)-1; j++ {
			if numeros[j] > numeros[j+1] {
				numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
				movCounter++
			}
		}
	}
	fmt.Printf("Movimentos: %v\n", movCounter)
	return numeros
}

func mergeSort(numeros []int) []int {
	if len(numeros) <= 1 {
		return numeros
	}
	if len(numeros) == 3 {
		return sortThree(numeros)
	}
	meio := len(numeros) / 2
	esquerda := mergeSort(numeros[:meio])
	direita := mergeSort(numeros[meio:])
	var ordened []int
	ordened = append(ordened, esquerda...)
	ordened = append(ordened, direita...)
	return ordened
		
}

func sortThree(numeros []int) []int {
	if(numeros[0] > numeros[1]){
		numeros[0], numeros[1] = numeros[1], numeros[0]
	}
	if(numeros[1] > numeros[2]){
		numeros[1], numeros[2] = numeros[2], numeros[1]
	}
	if(numeros[0] > numeros[1]){
		numeros[0], numeros[1] = numeros[1], numeros[0]
	}
	return numeros
}