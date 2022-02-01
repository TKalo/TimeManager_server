package db

import(
	_ "github.com/lib/pq"
	"log"
	"fmt"
)

func getDB(){
	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s",os.Getenv("host"),5432,os.Getenv("user"),os.Getenv("password"),os.Getenv("database"))

	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {
	  log.Fatalf("Tidak Konek DB Errornya : %s", err)
	}

	return db
}