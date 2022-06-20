#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *current, *comp;
	current = comp = *head;
	int n = 0;

	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	int arr[n], arr2[n];
	int i = 0, j = 0;

	while (comp != NULL)
	{
		arr[i] = comp->n;
		comp = comp->next;
		printf("arr[%d] = %d  ", i, arr[i]);
		i = i + 1;
	}
	printf("\n");

	i = n - 1;

	while (i != -1)
	{
		arr2[i] = arr[j];
		printf("arr2[%d] = %d  ", i, arr2[i]);
		i = i - 1;
		j += 1;
	}

	printf("\n\nthe elements ~ %d, %d\n", arr[0], arr[2]);
	printf("\n\nthe elements ~ %d, %d\n", arr2[0], arr2[2]);


	if (n == 10)
	{
		printf("correct - %d\n", n);
		return (10);
	}
	
	else
	{
		printf("not correct - %d\n", n);
		return (1);
	}

}
