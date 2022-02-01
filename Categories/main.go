package main

import(
	"fmt"
	"net/http"
	"resources/db"
)

func main(){

	db = getDB()

	http.HandleFunc("/get", func(w http.ResponseWriter, r *http.Request){
		token := r.URL.Query()["token"]
		user_id := r.URL.Query()["user_id"]

		query := 'SELECT * FROM category WHERE user_id = $1;'
		row := db.Conn.QueryRow(query, user_id)
		row.Scan()
	
		fmt.Fprintf(w, "get: %s %s",token,user_id)
	})

	http.HandleFunc("/add", func(w http.ResponseWriter, r *http.Request){
		token := r.URL.Query()["token"]
		user_id := r.URL.Query()["user_id"]
		name := r.URL.Query()["name"]
		color := r.URL.Query()["color"]
		fmt.Fprintf(w, "add: %s %s %s %s",token,user_id, name, color)
	})

	http.HandleFunc("/edit", func(w http.ResponseWriter, r *http.Request){
		token := r.URL.Query()["token"]
		user_id := r.URL.Query()["user_id"]
		name := r.URL.Query()["name"]
		color := r.URL.Query()["color"]
		fmt.Fprintf(w, "edit: %s %s %s %s",token,user_id, name, color)
	})

	http.HandleFunc("/delete", func(w http.ResponseWriter, r *http.Request){
		token := r.URL.Query()["token"]
		user_id := r.URL.Query()["user_id"]
		name := r.URL.Query()["name"]
		fmt.Fprintf(w, "delete: %s %s %s",token,user_id, name)
	})

	http.ListenAndServe(":5000", nil)
}