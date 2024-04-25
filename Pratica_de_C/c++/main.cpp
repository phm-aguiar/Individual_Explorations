/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 10:28:54 by phenriq2          #+#    #+#             */
/*   Updated: 2024/04/17 11:07:47 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "operatings.hpp"

int	main(void)
{
	int num;
	int num2;
	operatings op;

	std::cout << "Hello, World!" << std::endl;
	std::cin >> num >> num2;
	std::cout << "Soma: " << op.soma(num, num2) << std::endl;
	std::cout << "Sub: " << op.sub(num, num2) << std::endl;
	std::cout << "Mult: " << op.mult(num, num2) << std::endl;
	std::cout << "Divi: " << op.divi(num, num2) << std::endl;

	std::cout << "Bye, World!" << std::endl;
	return (0);
}
