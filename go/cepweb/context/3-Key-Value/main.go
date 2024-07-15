package main

import (
	"context"
	"fmt"
)

func main() {
	ctx := context.Background()
	ctx = context.WithValue(ctx, "Token", "senha")
	err := bookHotel(ctx)
	if err != nil {
		panic(err)
	}
}

func bookHotel(ctx context.Context) error {
	token := ctx.Value("Token")
	fmt.Println("Token:", token)
	if token == nil {
		return fmt.Errorf("Token not found")
	}
	return nil
}
