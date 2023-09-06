#include "lists.h"

/**
 * insert_node - Inserts node
 * @head: Head of the linked list
 * @number: number to be added to the list
 * Return: Pointer to a node or null if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = NULL;
	listint_t *temp = NULL;

	(void)number;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	if (head == NULL || *head == NULL)
	{
		new_node->n = number;
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	if (current->n > number)
	{
		new_node->n = number;
		new_node->next = current;
		*head = new_node;
		return (*head);
	}

	/* Traverse the list to find where current->n > number*/
	while (current->n < number && current->next != NULL)
	{
		if (current->next->n >= number)
			break;
		current = current->next;
	}
	new_node->n = number;
	temp = current->next;
	current->next = new_node;
	new_node->next = temp;

	return (NULL);
}
