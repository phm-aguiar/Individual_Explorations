package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx := context.Background()
	ctx, cancel := context.WithTimeout(ctx, 3*time.Second)
	defer cancel()
	err := bookHotel(ctx)
	if err != nil {
		panic(err)
	}
}

func bookHotel(ctx context.Context) error {
	select {
	case <-ctx.Done():
		fmt.Println("booking hotel was canceled. Reason:", ctx.Err())
		return ctx.Err()
	case <-time.After(1 * time.Second):
		fmt.Println("hotel booked")
	}
	return nil
}
