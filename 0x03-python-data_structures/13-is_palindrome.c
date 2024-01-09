#include "lists.h"

listint_t *second_hf(listint_t *second_p, listint_t *past_p);

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
		/*while (second->next != past)*/
			/*second = second->next;*/
		second = second_hf(second, past);

		if (curr->n != second->n)
			return (0);

		if (curr == second)
			break;

		past = second;
		curr = curr->next;
	}

	return (1);
}

/**
 * second_hf - helper function to return a pointer to the last element in list
 * @second_p: Pointer to starting point.
 * @past_p: Pointer to stopping point.
 *
 * Return: Pointer to current stopping point.
 */
listint_t *second_hf(listint_t *second_p, listint_t *past_p)
{
	while (second_p->next != past_p)
		second_p = second_p->next;

	return second_p;
}
