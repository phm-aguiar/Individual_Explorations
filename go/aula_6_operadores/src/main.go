/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.go                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/13 09:01:54 by phenriq2          #+#    #+#             */
/*   Updated: 2024/06/16 10:19:40 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

package main

func main() {
	soma := 1 + 1
	subtracao := 1 - 1
	multiplicacao := 1 * 1
	divisao := 1 / 1
	modulo := 1 % 1
	
	println(soma)
	println(subtracao)
	println(multiplicacao)
	println(divisao)
	println(modulo)
	// incremento e decremento
	soma++
	println(soma)
	soma--
	println(soma)
	soma += 10
	println(soma)
}