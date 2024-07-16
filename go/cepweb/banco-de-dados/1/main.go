package main

import (
	"context"
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
	"github.com/google/uuid"
)

type Product struct {
	Id    string
	Name  string
	Price float64
}

func NewProduct(name string, price float64) *Product {
	return &Product{
		Id:    uuid.New().String(),
		Name:  name,
		Price: price}
}

func main() {
	ctx := context.Background()
	db, err := sql.Open("mysql", "root:root@tcp(localhost:3307)/goexpert")
	if err != nil {
		panic(err)
	}
	defer db.Close()
	product := NewProduct("camisa2", 100.0)
	err = insertProduct(db, product)
	if err != nil {
		panic(err)
	}
	product.Price = 200.0
	err = updateProduct(db, product)
	if err != nil {
		panic(err)
	}
	p, err := selectProduct(ctx, db, product.Id)
	if err != nil {
		panic(err)
	}
	err = deleteProduct(db, p.Id)
	if err != nil {
		panic(err)
	}
	fmt.Printf("All products:\n")
	products, err := selectAllProducts(db)
	if err != nil {
		panic(err)
	}
	// delete all products
	for _, v := range products {
		fmt.Printf("Product: %v\nPreço: %.2f\n", v.Name, v.Price)
	}
}

func insertProduct(db *sql.DB, product *Product) error {
	stmt, err := db.Prepare("insert into products(id, name, price) values(?, ?, ?)")
	if err != nil {
		return err
	}
	defer stmt.Close()
	_, err = stmt.Exec(product.Id, product.Name, product.Price)
	if err != nil {
		return err
	}
	return nil
}

func updateProduct(db *sql.DB, product *Product) error {
	stmt, err := db.Prepare("update products set name = ?, price = ? where id = ?")
	if err != nil {
		return err
	}
	defer stmt.Close()
	_, err = stmt.Exec(product.Name, product.Price, product.Id)
	if err != nil {
		return err
	}
	return nil
}

func selectProduct(ctx context.Context, db *sql.DB, id string) (*Product, error) {
	stmt, err := db.Prepare("select id, name, price from products where id = ?")
	if err != nil {
		return nil, err
	}
	defer stmt.Close()
	var p Product

	err = stmt.QueryRowContext(ctx, id).Scan(&p.Id, &p.Name, &p.Price)
	if err != nil {
		return nil, err
	}
	return &p, nil
}

func selectAllProducts(db *sql.DB) ([]Product, error) {
	rows, err := db.Query("select id, name, price from products")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var products []Product
	for rows.Next() {
		var p Product
		err = rows.Scan(&p.Id, &p.Name, &p.Price)
		if err != nil {
			return nil, err
		}
		products = append(products, p)
	}
	return products, nil
}

func deleteProduct(db *sql.DB, id string) error {
	stmt, err := db.Prepare("delete from products where id = ?")
	if err != nil {
		return err
	}
	defer stmt.Close()
	_, err = stmt.Exec(id)
	if err != nil {
		return err
	}
	return nil
}
