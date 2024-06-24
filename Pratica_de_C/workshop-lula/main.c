/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/23 17:35:22 by phenriq2          #+#    #+#             */
/*   Updated: 2024/01/23 20:11:02 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int	main(void)
{
	time_t		rawtime;
	struct tm	*info;
	int			ano;
	int			mes;
	int			meses;
	int			input_month;
	int			input_year;
	int			projects;
	int			ciclos;

	time(&rawtime);
	info = localtime(&rawtime);
	ano = info->tm_year + 1900;
	mes = info->tm_mon + 1;
	printf("que ano voce quer terminar a 42?(2024-2030) ");
	scanf(" %d", &input_year);
	if(input_year < 2024 || input_year > 2030)
	{
		printf("%d\n", input_year);
		printf("ano invalido\n");
		exit(0);
	}
	printf("que mes voce quer terminar a 42?(1-12) ");
	scanf(" %d", &input_month);
	if(input_month < 1 || input_month > 12)
	{
		printf("mes invalido\n");
		exit(0);
	}
	printf("voce ja fez quantos projetos? ");
	scanf(" %d", &projects);
	if(projects < 0 || projects > 15)
	{
		printf("numero de projetos invalido\n");
		exit(0);
	}
	ano = input_year - ano;
	mes = input_month - mes;
	meses = input_month - mes + ano * 12;
	ciclos = meses * 2;
	projects = 15 - projects;
	printf("voce tem %d anos e %d meses (%d ciclos) para terminar %d projetos\n", ano, mes, ciclos, projects);
	printf("no caso %d ciclo por projeto em média.\n", (ciclos / projects) + 1);
	if (((ciclos / projects) + 1) >= 3)
		printf("\nvoce vai conseguir terminar a 42 a tempo\n");
	else
		printf("\nvoce não vai conseguir terminar a 42 a tempo ... que peninha né\n");
	exit(0);
}
