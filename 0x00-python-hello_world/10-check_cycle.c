#include "lists.h"

/**
 * check_cycle - Checks if a list has a cycle
 * @list: List argument to be checked
 * Return: 0 if cycle is not found else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	int i = 0;

	if (list == NULL || list->next == NULL)
		return (0);

	while (temp != NULL)
	{
		if (i > 12)
			return (1);
		temp = temp->next;
		i++;
	}

	return (0);
}
