/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.go                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/13 09:01:54 by phenriq2          #+#    #+#             */
/*   Updated: 2024/06/17 14:25:00 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

package main

import "fmt"

func soma(a int, b int) int {
	return a + b
}

func saudacao(nome *string) string {
	*nome = "João"
	return "Olá " + *nome
}

func main() {
	fmt.Println(soma(1, 2))
	msg := "Pedro"
	// agora vou passar a referencia da variável
	// msg para a função saudacao
	fmt.Println(msg)
	fmt.Println(saudacao(&msg))
	fmt.Println(msg)
	resultado := somaNtermos(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
	fmt.Println(resultado)
}


func somaNtermos(n ... int) int {
	soma := 0
	for _, v := range n {
		soma += v
	}
	return soma
}