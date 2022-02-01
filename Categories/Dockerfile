FROM golang:latest

RUN mkdir /app

ADD main.go /app

ADD db.go /app/resources

WORKDIR /app

RUN apt -y update && apt -y install git

RUN go env -w GO111MODULE=off

RUN go get github.com/lib/pq

RUN go build -o main .

EXPOSE 5000

CMD /app/main