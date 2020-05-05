package main 
import "fmt"

/*
	for i := n-1 ; i >= 0; i--{
		arr[i + 1] = arr[i]
	}
	arr[0] = new_data
	
	

*/
func main() { 
	var arr [10]int
	new_data := 4
	n := 5
	
	fmt.Printf("Please insert %d element in array\n",n)
	for i:=0; i<n; i++{
		fmt.Scanln(&arr[i])
	}
	
	fmt.Print("before insert new data\n")
	for i:=0; i<=n; i++{
		fmt.Print(arr[i])
	}
	
	arr1 := insertAtFirst(arr,new_data,n)

	fmt.Print("\nafter insert new data\n")
	for i :=0 ; i <= n; i++{
		fmt.Print(arr1[i])
	}
}

func insertAtFirst(arr [10]int ,new_data int, n int) [10]int{
	for i := n-1 ; i >= 0; i--{
		arr[i + 1] = arr[i]
	}
	arr[0] = new_data
	return arr
}

func insertAtIndex(arr [10]int ,new_data int, n int, index int) [10]int{
	for i := n-1 ; i >= index; i--{
		arr[i + 1] = arr[i]
	}
	arr[index] = new_data
	return arr
}