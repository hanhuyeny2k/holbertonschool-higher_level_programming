#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: double pointer that points to the head
 *
 * Return: the copy of the pointer
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy = *head;

	return (recurse(&copy, copy));
}

/**
 * recurse - loop through the linked list to compare each value
 * @left: double pointer
 * @right: single pointer
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int recurse(listint_t **left, listint_t *right)
{
	int result;

	if (right == NULL)
		return (1);
	result = recurse(left, right->next)
		&& (*left)->n == right->n;
	*left = (*left)->next;
	return (result);
}
