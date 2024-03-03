/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pointer.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/24 19:38:45 by phenriq2          #+#    #+#             */
/*   Updated: 2024/02/24 21:00:09 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef POINTER_H
# define POINTER_H

# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <unistd.h>

typedef struct s_cmd
{
	int					is_builtin;
	char				*cmd;
	char				**args;
	char				**envp;
	int					cmd_pos;
}						t_cmd;

typedef struct s_builtin
{
	char				*cmd;
	void				(*builtin)(char);
	struct s_builtin	*next;
}						t_builtin;

#endif

