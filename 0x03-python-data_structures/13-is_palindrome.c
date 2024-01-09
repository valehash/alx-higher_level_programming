#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: The start of the linked list.
 *
 * Return: If is palindrome, 1. Otherwise, 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head, *past = NULL, *second = NULL;

	while (curr != second || curr != past)
	{
		second = curr;
		while (second->next != past)
			second = second->next;

		if (curr->n != second->n)
			return (0);

		if (curr == second)
			break;

		past = second;
		curr = curr->next;
	}

	return (1);
}
