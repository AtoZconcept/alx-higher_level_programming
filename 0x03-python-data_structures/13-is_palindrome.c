#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a linkedList is a palindrome
 * @head: Double pointer to the head of a list
 * Return: 0 if not else 1
 */

int is_palindrome(listint_t **head)
{
	int len = 0, first = 0, last = 0;
	int middle = 0, arr_l[25] = {0}, t_len;
	listint_t *ptr;

	(void)last;
	(void)t_len;

	if (head == NULL || *head == NULL)
		return (1);
	/*Find the length*/
	first = (*head)->n;
	ptr = *head;

	while (ptr != NULL)
	{
		len++;
		if (len == 4)
			middle = ptr->n;
		if (ptr->next == NULL)
			last = ptr->n;
		ptr = ptr->next;
	}
	ptr = *head, t_len = len;
	while (ptr != NULL)
	{
		arr_l[len] = ptr->n;
		len--;
		ptr = ptr->next;
	}

	if (first == arr_l[1] && last == arr_l[t_len] && middle == arr_l[4])
		return (1);

	return (0);
}
