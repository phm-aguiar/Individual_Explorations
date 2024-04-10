/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   garbage.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/22 12:23:04 by phenriq2          #+#    #+#             */
/*   Updated: 2024/03/22 12:44:19 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

t_list	*garbage_add(void **data, t_list *garbage)
{
	t_list	*new;

	new = malloc(sizeof(t_list));
	if (!new)
		return (NULL);
	new->data = data;
	new->next = garbage;
	return (new);
}
t_list	*garbage_clear(t_list *garbage)
{
	t_list	*current;
	t_list	*next_node;

	current = garbage;
	next_node = NULL;
	while (current)
	{
		next_node = current->next;
		if (current->data && *current->data)
		{
			free(*current->data);
			*current->data = NULL;
		}
		free(current);
		current = next_node;
	}
	return (NULL);
}

int	main(void)
{
	t_list *garbage;
	int *data;
	char *str;
	char *str2;

	garbage = NULL;
	data = malloc(sizeof(int));
	if (!data)
		return (1);
	str = malloc(sizeof(char) * 10);
	if (!str)
		return (1);
	str2 = malloc(sizeof(char) * 10);
	if (!str2)
		return (1);
	while (*str2)
		*str2 = '\0';
	while (*str)
		*str = '\0';
	*data = 42;
	garbage = garbage_add((void **)&data, garbage);
	garbage = garbage_add((void **)&str, garbage);
	garbage = garbage_add((void **)&str2, garbage);
	free(str2);
	str2 = NULL;
	garbage = garbage_clear(garbage);
	return (0);
}