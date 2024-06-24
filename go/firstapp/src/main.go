/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.go                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: phenriq2 <phenriq2@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/17 18:47:29 by phenriq2          #+#    #+#             */
/*   Updated: 2024/06/18 13:31:24 by phenriq2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

package main

import (
	"io"
	"net/http"
	"os"
	"log"
)

func main() {
	http.HandleFunc("/", func (w http.ResponseWriter, r *http.Request) {
		f, err := os.Open("index.html")
		if err != nil {
			http.Error(w, "file not found", 404)
			log.Println(err)
			return
		}
		defer f.Close()
		io.Copy(w, f)
		})	
	http.ListenAndServe(":8000", nil)
}