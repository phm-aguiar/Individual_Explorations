/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   exame.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/14 09:24:59 by phenriq2          #+#    #+#             */
/*   Updated: 2024/03/14 13:31:31 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef EXAME_H
# define EXAME_H

# include <fcntl.h>
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <unistd.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 10
# endif

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

t_char					*new_node(char c);
void					add_last(t_char **head, t_char *new);
void					clean_list(t_char *clear);
void					print_list(t_char *teste);
t_gnl					*get_gnl(void);

#endif // 42EXAME_H
