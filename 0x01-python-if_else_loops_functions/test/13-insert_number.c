#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert a new node into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *temp;

	current = malloc(sizeof(listint_t));


	if (!current)
	{
		return (NULL);
	}

	current = *head;

	while (current != NULL || number > current->n)
	{
		current = current->next;
	}

	temp = malloc(sizeof(listint_t));
	
	if (temp == NULL)
	{
		return (NULL);
	}

	temp->next = current->next;
	current->n = number;
	current->next = temp;

	return (*head);
}
