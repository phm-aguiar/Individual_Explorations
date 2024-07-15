package main

import (
	"fmt"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

type Category struct {
	ID  int    `gorm:"primary_key" json:"id"`
	Name string `gorm:"type:varchar(100)" json:"name"`
}

type Product struct {
	ID    int     `gorm:"primary_key" json:"id"`
	Name  string  `gorm:"type:varchar(100)" json:"name"`
	Price float64 `gorm:"type:decimal" json:"price"`
	CategoryID int `json:"category_id"`
	Category Category
	gorm.Model
}

// func main() {
// 	dsn := "root:root@tcp(localhost:3307)/goexpert?charset=utf8mb4&parseTime=True&loc=Local"
// 	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
// 	if err != nil {
// 		panic(err)
// 	}
// db.AutoMigrate(&Product{})
// product := Product{Name: "camisa", Price: 100.0}
// db.Create(&product)
// products := []Product{
// 	{Name: "camiseta", Price: 100.0},
// 	{Name: "calca", Price: 200.0},
// 	{Name: "sapato", Price: 300.0},
// 	{Name: "meia", Price: 400.0},
// }
// db.Create(&products)

// var products []Product
// // db.First(&product, 2)
// // fmt.Println(product)
// // db.First(&product, "name = ?", "camiseta")
// // fmt.Println(product)
// db.Find(&products)

// for _, v := range products {
// 	fmt.Println(v)
// }
// db.Limit(2).Find(&products)
// fmt.Println("testando com limit 2")
// for _, v := range products {
// 	fmt.Println(v)
// }
// db.Limit(2).Offset(2).Find(&products)
// fmt.Println("testando com limit 2 e offset 2")
// for _, v := range products {
// 	fmt.Println(v)
// }
// fmt.Println("testando com where")
// db.Where("price > ?", 200).Find(&products)
// for _, v := range products {
// 	fmt.Println(v)
// }
// fmt.Println("testando o like")
// db.Where("name LIKE ?", "%i%").Find(&products)
// for _, v := range products {
// 	fmt.Println(v)
// }

// var p Product
// db.First(&p, 1)
// p.Name = "camisa 2"
// db.Save(&p)
// db.Delete(&p)
// var p2 Product
// db.First(&p2, 1)
// fmt.Println(p2)
// db.Delete(&p2)
// db.AutoMigrate(&Product{})
// db.Create(&Product{Name: "camisa", Price: 100.0})
// }

func main() {
	dsn := "root:root@tcp(localhost:3307)/goexpert?charset=utf8mb4&parseTime=True&loc=Local"
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		panic(err)
	}
	db.AutoMigrate(&Product{}, &Category{})

	// category := Category{Name: "roupas"}
	// db.Create(&category)

	db.Create(&Product{Name: "tenis", Price: 100.0, CategoryID: 1})
	var products []Product
	db.Preload("Category").Find(&products)
	for _, v := range products {
		fmt.Println(v.Name, v.Category.Name)
	}
}
