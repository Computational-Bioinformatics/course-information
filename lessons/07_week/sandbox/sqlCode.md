# SQL code

## Build a table to contain data

```
CREATE TABLE mySeq(
ID VARCHAR,
name VARCHAR,
seq VARCHAR);
```

## Add data to the table

```
INSERT INTO mySeq VALUES
(
"gene101",
"x-gene",
"ATATCG"
);
```

## A basic query to get all data from the table

```
SELECT * FROM mySeq;
```

## Add more data to table

```
INSERT INTO mySeq VALUES (
"gene210",
"a-gene",
"GATATCG");

INSERT INTO mySeq VALUES (
"gene300",
"b-gene",
"GTATCG");
```

## A specific query to get ID and seq information from the table

```
SELECT ID,seq FROM mySeq;
```
