#include <stdio.h>
void push(int a[],int size,int data);
void insert(int a[],int size,int data, int index);
void pop(int a[], int size, int index);
void remove(int a[], int size, int data);
void traverse(int a[], int size);
int main()
{
    int arr[100] = {1,2,3,4,5,6,7,8,9,10};
    int size = 10, data = 8, i;
    
    printf("Before insert new data\n");
    traverse(arr, size+2);
    remove(arr,size,data);
    printf("\nAfter insert new data\n");
    traverse(arr, size+2);
    return 0;
}

void traverse(int a[], int size){
    int i;
    for (i = 0; i < size; i++){
        printf(" %d",a[i]);
    }  
}

void push(int a[],int size,int data){
    int i;
    for (i = size-1; i >= 0; i--){
        a[i+1] = a[i];
    }
    a[0] = data;

}

void insert(int a[],int size,int data, int index){
	if (index < 0){
		printf("\ninvalid index(negative) appending at start of array\n");
		index = 0;
	}
	else if (index > size){
		printf("\ninvalid index appending at end of array\n");
		index = size;
	}
    int i;
    for (i = size-1; i >= index; i--){
        a[i+1] = a[i];
    }
    a[index] = data;
}


void pop(int a[], int size, int index){
	if (index < 0 || index > size-1)
	{
		printf("\nInvalid index");
		return;
	}
	else{
		int i;
		for (i=index; i<size-1; i++){
			a[i] = a[i+1];
		}
		a[i] = 0;
	}
}


void remove(int a[], int size, int data){
    int i, found = -1;
    for (i = 0; i < size; i++){
        if(a[i] == key){
            found = i;
            break;
        }
    }
    if(found == -1){
        printf("\n%d does not exits in the array",key);
        return;
    }

    for (i=found; i<size-1; i++){
        a[i] = a[i+1];
    }
    a[i] = 0;
}