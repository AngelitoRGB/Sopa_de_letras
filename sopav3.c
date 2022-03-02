#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// numRandom: Int -> Int
// Devuelve un numero random entre 0 y U

int numRandom(int U){
    int aleatorio;
    aleatorio = (int)(((U+1.0)*rand())/(RAND_MAX+1.0));
    return aleatorio;
}

int main(){
    FILE *file, *file2;
    char **palabras = malloc(sizeof(char*));
    char buff[30], archivo[30];
    int cant_palabras, count = 0, numero_palabras = 1, valor = 1;
    int tamano, compl;
    printf("Ingrese el nombre del archivo: ");
    scanf("%s", archivo);
    while(valor){
        printf("Ingrese el tamano de la sopa de letras: ");
        scanf("%d", &tamano);
        if(tamano < 2){
            printf("Ingrese un tamaño mayor o igual a 2\n");
        }
        else{
            valor = 0;
        }
    }
    valor = 1;
    while(valor){
        printf("Ingrese la cantidad de palabras: ");
        scanf("%d", &cant_palabras);
        if(cant_palabras < 1){
            printf("La cantidad minima de palabras es 1\n");
        }
        else{
            valor = 0;
        }
    }
    valor = 1;
    while (valor)
    {
        printf("Ingrese la complejidad [0-3]: ");
        scanf("%d", &compl);
        if(compl < 0 || compl > 3){
            printf("No ha ingresado una complejidad correcta\n");
        }
        else{
            valor = 0;
        }
    } 
    int num_randoms[cant_palabras];
    file = fopen(archivo, "r");
    srand(time(NULL));

    // Se lee el archivo, se agregan las palabras a un arreglo y 
    // se cuentan las cantidad de palabras que hay en el archivo
    fgets(buff, 30, file); 
    palabras[count] = malloc(sizeof(char)* (strlen(buff)+1));
    strcpy(palabras[count], buff);
    while(feof(file) == 0){
        ++numero_palabras;
        ++count;
        fgets(buff, 30, file);
        palabras = realloc(palabras, sizeof(char*) * numero_palabras);
        palabras[count] = malloc(sizeof(char)* (strlen(buff)+1));
        strcpy(palabras[count],buff);
    }

    // Se eligen la misma cantidad de numeros que de palabras
    // aleatoriamente
    for(int i = 0; i < cant_palabras;i++){
        num_randoms[i] = numRandom(count);
    }
    
    fclose(file);
    file2 = fopen("salida.txt", "w");
    fprintf(file2, "DIMENSION\n");
    fprintf(file2, "%d\n", tamano);
    fprintf(file2, "PALABRAS\n");
    // Se eligen aleatoriamente palabras de nuestro arreglo, para
    // luego escribirlas en el archivo
    for(int i = 0; i < cant_palabras; i++){
        fprintf(file2, palabras[num_randoms[i]]);
    }
    fprintf(file2, "COMPLEJIDAD\n");
    fprintf(file2, "%d", compl);
    fclose(file2);
    printf("Archivo escrito con exito");

    return 0;
}

// No es posible hacer test ya que hay una unica funcion que retorna
// un numero aleatorio