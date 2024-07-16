/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.go                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/13 09:01:54 by phenriq2          #+#    #+#             */
/*   Updated: 2024/06/17 13:53:26 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

package main

import "fmt"

func main() {
	
	num := 10
	// declaração de variável com valor condicional
	if  num > 5 {
		println("O número é maior que 5")
	} else {
		println("O número é menor ou igual a 5")
	}
	switch {
		case num == 1:
			println("O número é 1")
		case num == 2:
			println("O número é 2")
		case num == 3:
			println("O número é 3")
		case num == 10:
			println("O número é 10")
	}

	// for

	for i := 0; i < 10; i++ {
		println(i)
	}

	for{
		println(num)
		num--
		if num == 0 {
			break
		}
	}
	array := make([]int, 10)

	for i := 0; i < 10; i++ {
		array[i] = i
		println(array[i])
	}
	fmt.Println(array)
	
	lista:= []string{"a", "b", "c", "d", "e"}

	for index, v := range lista {
		fmt.Println("array {",index,"} = ",v)
	}
	
	dicionario := make(map[string]int)
	dicionario["a"] = 1
	dicionario["b"] = 2
	dicionario["c"] = 3
	for k, v := range dicionario {
		fmt.Println("map {",k,"} = ",v)
	}
}