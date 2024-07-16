/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/14 09:25:42 by phenriq2          #+#    #+#             */
/*   Updated: 2024/05/30 19:15:30 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "exame.h"

int	err(char *msg)
{
	write(2, msg, strlen(msg));
	return (1);
}

int	cd(char **argv, int i)
{
	if (i != 2)
		return (err("error: cd: bad arguments\n"));
	if (chdir(argv[1]) == -1)
		return (err("error: cd: cannot change directory to "), err(argv[1]),
			err("\n"));
	return (0);
}

int	exec(char **argv, char **envp, int i)
{
	int	fd[2];
	int	status;
	int	has_pipe;
	int	pid;

	has_pipe = argv[i] && !strcmp(argv[i], "|");
	if (!has_pipe && !strcmp(*argv, "cd"))
		return (cd(argv, i));
	if (has_pipe && pipe(fd) == -1)
		return (err("error: fatal\n"));
	pid = fork();
	if (!pid)
	{
		argv[i] = 0;
		if (has_pipe && (dup2(fd[1], 1) == -1 || close(fd[0]) == -1
				|| close(fd[1]) == -1))
			return (err("error: fatal\n"));
		if (!strcmp(*argv, "cd"))
			return (cd(argv, i));
		execve(*argv, argv, envp);
		return (err("error: cannot execute "), err(*argv), err("\n"));
	}
	waitpid(pid, &status, 0);
	if (has_pipe && (dup2(fd[0], 0) == -1 || close(fd[0]) == -1
			|| close(fd[1]) == -1))
		return (err("error: fatal\n"));
	return (WIFEXITED(status) && WEXITSTATUS(status));
}

int	main(int argc, char **argv, char **envp)
{
	int	status;
	int	i;

	i = 0;
	status = 0;
	if (argc > 1)
	{
		while (argv[i] && argv[i++])
		{
			argv += i;
			i = 0;
			while (argv[i] && strcmp(argv[i], "|") && strcmp(argv[i], ";"))
				i++;
			if (i)
				status = exec(argv, envp, i);
		}
	}
	return (status);
}
