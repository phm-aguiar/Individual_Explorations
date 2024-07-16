/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.go                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/13 09:01:54 by phenriq2          #+#    #+#             */
/*   Updated: 2024/06/17 17:14:00 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	var tamanho int

	fmt.Println("gerador de senhas")
	fmt.Println("Digite o tamanho da senha")
	_, err := fmt.Scanf("%v", &tamanho)
	if err != nil {
		fmt.Println("Erro ao ler o tamanho da senha")
		return
	}

	rand.New(rand.NewSource(time.Now().UnixNano()))
	fmt.Printf("Senha gerada: %v\n", randomPass(tamanho))
}

func randomPass(tamanho int) string {
	var senha string
	var caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%¨&*()_+-/*"

	for i := 0; i < tamanho; i++ {
		senha += string(caracteres[rand.Intn(len(caracteres))])
	}

	return senha
}