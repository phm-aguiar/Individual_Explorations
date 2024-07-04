package main

import (
	"fmt"
	"os"
	"strconv"
)

type Stack struct {
	value int
	index int
	next  *Stack
}

func Push(A **Stack, value int) {
	node := &Stack{value: value, index: 0}
	node.next = *A
	*A = node
}

func Swap(A **Stack, msg string) {
	if *A == nil || (*A).next == nil {
		return
	}
	node := *A
	*A = node.next
	node.next = (*A).next
	(*A).next = node

	fmt.Printf(msg)
}

func Rotate(A **Stack, msg string) {
	if *A == nil || (*A).next == nil {
		return
	}
	first := *A
	*A = first.next
	node := *A
	for node.next != nil {
		node = node.next
	}
	node.next = first
	first.next = nil
	fmt.Printf(msg)
}

func ReverseRotate(A **Stack, msg string) {
	if *A == nil || (*A).next == nil {
		return
	}
	node := *A
	for node.next.next != nil {
		node = node.next
	}
	node.next.next = *A
	*A = node.next
	node.next = nil
	fmt.Printf(msg)
}

func SwapS(A **Stack, B **Stack) {
	Swap(A, "")
	Swap(B, "")
	fmt.Printf("ss\n")
}

func PushTo(A **Stack, B **Stack, msg string) {
	if *A == nil {
		return
	}
	value, _ := Pop(A)
	Push(B, value)
	fmt.Printf(msg)
}

func CreateStack(args []string, A **Stack) {
	for i := len(args) - 1; i >= 0; i-- {
		n, _ := strconv.Atoi(args[i])
		Push(A, n)
	}
}

func PrintStack(A *Stack) {
	for A != nil {
		fmt.Printf("A %v I %v \n", A.value, A.index)
		A = A.next
	}
}

func Pop(A **Stack) (int, error) {
	if *A == nil {
		return 0, fmt.Errorf("Stack is empty")
	}
	node := *A
	*A = node.next
	return node.value, nil
}

// Cria um array ordenado com os valores passados no argumento
func SortArray(args []string) []int {
	var array []int
	for i := 0; i < len(args); i++ {
		n, _ := strconv.Atoi(args[i])
		array = append(array, n)
	}
	for i := 0; i < len(array); i++ {
		for j := 0; j < len(array)-1; j++ {
			if array[j] > array[j+1] {
				aux := array[j]
				array[j] = array[j+1]
				array[j+1] = aux
			}
		}
	}
	return array
}

// Usa o array ordenado para setar o index de cada nó
func SetIndex(A **Stack, array []int) {
	for i := 0; i < len(array); i++ {
		node := *A
		for node != nil {
			if node.value == array[i] {
				node.index = i
			}
			node = node.next
		}
	}
}

func count_bits(max int) int {
	count := 0
	for max != 0 {
		max = max >> 1
		count++
	}
	return count
}

func push_back(A **Stack, B **Stack, size int) {
	for i := 0; i < size; i++ {
		PushTo(B, A, "pa\n")
	}
}

func radix_sort(A **Stack, B **Stack, bits int, size int) {
	for i := 0; i < bits; i++ {
		index := 0
		for index < size {
			if ((*A).index >> i) % 2 == 1 {
				Rotate(A, "ra\n")
			} else {
				PushTo(A, B, "pb\n")
			}
			index++
		}
		push_back(A, B, size)
	}
}

func ft_return_last(A **Stack) *Stack {
	node := *A
	for node.next != nil {
		node = node.next
	}
	return node
}



func main() {
	var A *Stack
	var B *Stack

	args := os.Args[1:]
	if len(args) < 1 {
		os.Exit(0)
	}
	CreateStack(args, &A)
	SetIndex(&A, SortArray(args))
	bits := count_bits(len(args))
	radix_sort(&A, &B, bits, len(args))
}
