/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pointer.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/24 19:38:24 by phenriq2          #+#    #+#             */
/*   Updated: 2024/02/24 20:59:08 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "pointer.h"

t_builtin	*new_builtin(char *name, void *function)
{
	t_builtin	*new_builtin;

	new_builtin = malloc(sizeof(t_builtin));
	new_builtin->cmd = name;
	new_builtin->builtin = function;
	new_builtin->next = NULL;
	return (new_builtin);
}

void	add_back(t_builtin **lst, t_builtin *new)
{
	t_builtin	*last;

	if (!*lst)
	{
		*lst = new;
		return ;
	}
	if (*lst)
	{
		last = *lst;
		while (last->next)
			last = last->next;
		last->next = new;
	}
}

void	ft_putchar1(char c)
{
	write(1, &c, 1);
}
void	ft_putchar2(char c)
{
	write(1, &c, 1);
}

void	ft_putchar3(char c)
{
	write(1, &c, 1);
}

void	ft_putchar4(char c)
{
	write(1, &c, 1);
}

int	main(void)
{
	t_builtin	*builtin;

	builtin = NULL;
	add_back(&builtin, new_builtin("put_char1", ft_putchar1));
	add_back(&builtin, new_builtin("put_char2", ft_putchar2));
	add_back(&builtin, new_builtin("put_char3", ft_putchar3));
	add_back(&builtin, new_builtin("put_char4", ft_putchar4));
	while (builtin)
	{
		if (!strcmp(builtin->cmd, "put_char1"))
			builtin->builtin('a');
		if (!strcmp(builtin->cmd, "put_char2"))
			builtin->builtin('b');
		if (!strcmp(builtin->cmd, "put_char3"))
			builtin->builtin('c');
		if (!strcmp(builtin->cmd, "put_char4"))
			builtin->builtin('d');
		builtin = builtin->next;
	}
	return (0);
}
