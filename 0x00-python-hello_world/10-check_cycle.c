#include "lists.h"
/**
 * check_cycle - prototype
 * @list: prototype
 * Description: checks if linked list has cycle
 * Return: 0 if no cycle 1 if there
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = list;
	second = list;
	while (first != NULL && second != NULL)
	{
		first = first->next;
		if (second->next)
			second = second->next->next;

		if (first == second)
			return (1);
	}
	return (0);
}
