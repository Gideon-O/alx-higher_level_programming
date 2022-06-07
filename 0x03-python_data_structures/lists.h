#ifndef _LISTS_H_
#define _LISTS_H_

/**
  * @n: Integer
  * @next: points to next node
  * 
  * Description: Singly linked node structure
  * for project
  */

typedef struct listint_s
{
    int n;
    struct listint_s;
}listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int h);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
