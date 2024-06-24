/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.go                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/13 09:01:54 by phenriq2          #+#    #+#             */
/*   Updated: 2024/06/17 16:21:16 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

package main

import "fmt"
import "time"

func main() {
	go abcGen() // go routine - executa a função abcGen em uma nova thread

	time.Sleep(60 * time.Millisecond) // tempo de espera para que a função abcGen seja executada
	// usado para substituir o join do c
}


func abcGen(){
	for l:= byte('a'); l <= byte('z'); l++ {
		fmt.Printf("%c ", l)
	}
}