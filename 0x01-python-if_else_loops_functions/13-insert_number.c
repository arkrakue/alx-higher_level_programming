#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted singly linked list.
 * @head: Pointer to a pointer to the first node of the list.
 * @number: Index to be inserted into the list.
 * Return: Pointer to the new node, or NULL on failure.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!*head || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current_node = *head;

	while (current_node->next && current_node->next->n < number)
		current_node = current_node->next;

	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}
