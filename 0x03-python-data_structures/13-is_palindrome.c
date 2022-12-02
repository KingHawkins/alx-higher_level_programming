#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include "lists.h"

/**
 ** reverse_listint - reverses a linked list.
 ** @head: head of a list.
 **
 ** Return: pointer to the first node.
 **/
listint_t *reverse_listint(listint_t **head)
{
        listint_t *p;
        listint_t *n;

        p = NULL;
        n = NULL;

        while (*head != NULL)
        {
                n = (*head)->next;
                (*head)->next = p;
                p = *head;
                *head = n;
        }

        *head = p;
        return (*head);
}
/**
 ** is_palindrome - checks if all elements of a listint_t list
 ** are palindrome
 ** @head: pointer to head of list
 ** Return: number of nodes
 **/
int is_palindrome(listint_t **head)
{
        if (!head)
        {
                return 1;
        }
        else
        {
                if (reverse_listint(head) == print_listint(head))
                {
                        return 0
                }
                else
                {
                        return 1
                }
        }
}
