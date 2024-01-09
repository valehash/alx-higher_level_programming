int is_palindrome(listint_t **head)
{
	listint_t *curr = *head, *past = NULL, *second = NULL;

	while (curr != second || curr != past)
	{
		second = curr;
		while (second->next != past)
			second = second->next;

		if (curr->n != second->n)
			return (0)

		past = second;
		curr = curr->next;
	}

	return (1);
}
