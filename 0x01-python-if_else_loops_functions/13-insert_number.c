#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	ptr = *head;
	if (ptr == NULL)
	{
		*head = new;
		return (new);
	}
	if (number < ptr->n)
		new->next = *head;
	for (; ptr->next != NULL && number > ptr->next->n; ptr = ptr->next)
		;
	new->next = ptr->next;
	ptr->next = new;
	return (new);
}
