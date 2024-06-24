/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   variaveis.go                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/15 13:15:11 by phenriq2          #+#    #+#             */
/*   Updated: 2024/06/16 09:49:14 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

package main

func main() {
	var number int
	number = 42
	println(number)

	var floatNumber float32 = 42.
	println(floatNumber)

	palavra := "Hello, World!"
	println(palavra)
	
	// Go não permite que variáveis sejam declaradas e não utilizadas
	
	myComplexNumber := complex(2, 3)
	println(myComplexNumber)
	println(real(myComplexNumber))
	println(imag(myComplexNumber))
}
