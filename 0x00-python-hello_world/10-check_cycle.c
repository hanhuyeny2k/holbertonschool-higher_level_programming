#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *tort;
	listint_t *hare;

	tort = list;
	hare = list;
	while(hare != NULL && hare->next != NULL)
	{
		tort = tort->next;
		hare = hare->next->next;
		if (hare == tort)
			return(1);
	}
	return (0);
}
