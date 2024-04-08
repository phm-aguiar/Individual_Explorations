/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/14 09:25:42 by phenriq2          #+#    #+#             */
/*   Updated: 2024/03/14 14:02:10 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#ifndef BUFFER_SIZE
# define BUFFER_SIZE 10
#endif

typedef struct s_char	t_char;
typedef struct s_list	t_list;
typedef struct s_gnl	t_gnl;

typedef struct s_char
{
	char				c;
	t_char				*next;
}						t_char;

typedef struct s_gnl
{
	t_char				*chars;
	char				*line;
	t_char				*avanced;
}						t_gnl;

char					*get_next_line(int fd);

t_char	*new_node(char c)
{
	t_char	*new;

	new = malloc(sizeof(t_char));
	new->c = c;
	new->next = NULL;
	return (new);
}

void	add_last(t_char **head, t_char *new)
{
	t_char	*current;

	if (!*head)
	{
		*head = new;
		return ;
	}
	current = *head;
	while (current->next)
		current = current->next;
	current->next = new;
}

void	clean_list(t_char *clear)
{
	t_char	*current;

	while (clear)
	{
		current = clear->next;
		free(clear);
		clear = current;
	}
	clear = NULL;
}

void	print_list(t_char *teste)
{
	t_char	*current;

	current = teste;
	while (current)
	{
		printf("%c", current->c);
		current = current->next;
	}
}

t_gnl	*get_gnl(void)
{
	static t_gnl	core = {0};

	return (&core);
}

int	find_raban(t_char *find)
{
	t_char	*current;
	int		len;

	len = 0;
	current = find;
	while (current)
	{
		len++;
		if (current->c == '\n')
			return (len);
		if (current->c == '\0')
			return (len);
		current = current->next;
	}
	return (-1);
}

void	readline(int fd)
{
	int		bytesread;
	char	readed[BUFFER_SIZE + 1];
	int		index;
	int		flag;

	bytesread = read(fd, readed, BUFFER_SIZE);
	flag = 0;
	while (bytesread)
	{
		flag = 1;
		index = -1;
		readed[bytesread] = '\0';
		while (readed[++index])
			add_last(&get_gnl()->chars, new_node(readed[index]));
		bytesread = read(fd, readed, BUFFER_SIZE);
	}
	if (flag)
		get_gnl()->avanced = get_gnl()->chars;
}

void	lsttostr(void)
{
	int		len;
	int		index;
	char	*line;

	index = -1;
	len = find_raban(get_gnl()->avanced);
	if (len == -1)
	{
		clean_list(get_gnl()->chars);
		get_gnl()->line = NULL;
		return ;
	}
	line = malloc((len + 1) * sizeof(char));
	line[len] = '\0';
	while (get_gnl()->avanced && ++index < len)
	{
		line[index] = get_gnl()->avanced->c;
		get_gnl()->avanced = get_gnl()->avanced->next;
	}
	get_gnl()->line = line;
	sleep(1);
}

char	*get_next_line(int fd)
{
	get_gnl()->line = NULL;
	if ((fd < 0 && !get_gnl()->chars) || BUFFER_SIZE <= 0 || read(fd, NULL,
			0) < 0)
		return (NULL);
	if ((fd < 0 && get_gnl()->chars))
		clean_list(get_gnl()->chars);
	readline(fd);
	lsttostr();
	return (get_gnl()->line);
}

int	main(void)
{
	int		fd;
	char	*line;

	fd = open("exemplo.txt", O_RDONLY);
	line = get_next_line(fd);
	while (line)
	{
		printf("%s", line);
		free(line);
		line = get_next_line(fd);
	}
	close(fd);
	return (0);
}
