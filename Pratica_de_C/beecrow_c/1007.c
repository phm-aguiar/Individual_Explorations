/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   1007.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/15 09:02:58 by phenriq2          #+#    #+#             */
/*   Updated: 2023/08/15 09:07:40 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	main(void)
{
	int	a;
	int	b;
	int	c;
	int	d;

	scanf("%d %d %d %d", &a, &b, &c, &d);
	a = (a * b) + (c * d) * -1;
	printf("DIFERENCA = %d\n", a);
	return (0);
}
