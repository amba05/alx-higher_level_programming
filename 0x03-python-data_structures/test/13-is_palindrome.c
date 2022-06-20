#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * NB = A palindrome is a list which when reversed has 
 * the same elements as its original
 *
 * Return: 1 if it is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;
	
	//check if it is an empty list or contains only 
	//one element and returns 1 (it is a palindrome)
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	//uses a while loop to ensure we create a 
	//duplicate of *head to use to reverse list
	//and then compare with the temp head
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	// reverse the linked list
	reverse_listint(&dup);

	//compares the reversed linked list with the 
	//original linked list (temp)
	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	//returns 1 cos it is a palindrome
	if (!dup)
		return (1);

	// it isn't a palindrome
	return (0);
}
