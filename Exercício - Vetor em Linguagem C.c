#include <stdio.h>
#include <stdlib.h>

int main()
{

    int *ponteiro = (int*) malloc(22*sizeof(int));

    ponteiro = (int*) realloc(ponteiro, 22*sizeof(int));
    
    if(ponteiro == NULL) {
        printf("Erro: Sem Memória!\n");
        exit(1);
    }


    free(ponteiro);

    system("pause");
    return 0;
}