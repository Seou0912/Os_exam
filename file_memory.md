<img width="1247" alt="Screenshot 2024-03-20 at 3 12 00 PM" src="https://github.com/Seou0912/Os_exam/assets/151927766/b86e330f-0e23-4f14-b253-a1c30a35d623">

## 연결 리스트 (Linked List) 설명

연결 리스트는 노드(Node)들이 포인터로 연결된 자료구조로, 각 노드는 데이터와 다음 노드를 가리키는 포인터로 구성됩니다. 이 자료구조에서 삽입과 삭제가 효율적으로 이루어집니다. 다음은 연결 리스트의 특징입니다:

1. **동적 할당:** 연결 리스트는 동적으로 메모리를 할당하여 노드를 추가하거나 제거할 수 있습니다. 이로써 메모리의 효율적인 사용이 가능합니다.

2. **삽입 및 삭제의 용이성:** 중간에 노드를 추가하거나 삭제할 때 배열과는 달리 데이터를 이동시키지 않고도 가능합니다. 이는 삽입 및 삭제 연산이 빠르고 효율적으로 이루어질 수 있음을 의미합니다.

3. **불연속할당과의 관계:** 연결 리스트는 파일의 내용에 순차적으로 접근할 수 있도록 해줍니다. 불연속할당으로 인해 메모리 위치가 불연속적일지라도, 각 노드가 다음 노드를 가리키는 포인터로 연결되어 있으므로 순차적인 접근이 가능합니다.

## C언어를 이용한 연결 리스트 구현 예제

아래는 C언어로 단일 연결 리스트를 구현한 예제입니다:

```c
#include <stdio.h>
#include <stdlib.h>

// 노드 구조체 정의
struct Node {
    int data;
    struct Node* next;
};

// 새로운 노드 생성
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;
    return node;
}

// 연결 리스트에 노드 추가
void appendNode(struct Node** head, int data) {
    struct Node* newNode = createNewNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

// 연결 리스트 출력
void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
}

int main() {
    struct Node* head = NULL;
    appendNode(&head, 1);
    appendNode(&head, 2);
    appendNode(&head, 3);
    printf("Linked List: ");
    printList(head);
    return 0;
}
```

이 예제에서는 단일 연결 리스트를 구현하고, 몇 가지 기본적인 함수를 사용하여 노드를 추가하고 출력합니다.
