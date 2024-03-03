/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   twosum.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/17 08:55:25 by phenriq2          #+#    #+#             */
/*   Updated: 2024/02/17 09:05:17 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	*twosum(int *nums, int numsSize, int target, int *returnSize)
{
	int	*sum;
	int	i;
	int	j;

	i = 0;
	j = 0;
	sum = (int *)malloc(2 * sizeof(int));
	while (i < numsSize)
	{
		j = i + 1;
		while (j < numsSize)
		{
			if (nums[i] + nums[j] == target)
			{
				sum[0] = nums[i];
				sum[1] = nums[j];
				*returnSize = 2;
				return (sum);
			}
			j++;
		}
		i++;
	}
	*returnSize = 0;
	return (sum);
}
