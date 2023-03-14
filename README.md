# SQL GPT
SQL **GPT** Generative Pre-trained Transformer for SQL migration with different SQL Oracle/Mysql/SQL Server/PostgreSQL... etc.

## The Problem
Database Mirgation is complicated task 

## Marketing And Analytics

## The Solution and Features
## Overview of Architecture

* There are serveral components like SQLcollector, Dummy-Data-Generator, SQLGPT service, ect...
* **SQLCollector**:  Web Service to receieve source SQL.
* **DataGenerator**: Generate Dummy Data for Schema.
* **SQLGPT Service**: Core Service to generate target SQL.
* **Models** : V1 from OpenAI model; V2 from Google T5 Model.
* **SQLTrainer**: training the model by new HumanFeedback Reinforcement learning.
![SQL GPT Architecture](./docs/sqlgbt.drawio.svg)

## Algorithm Explanation 
## Demonstration

**Example 1**:  select top 100 customer in Oracle PL/SQL

```oracle
SELECT id, client_id FROM customer 
WHERE rownum <= 100
ORDER BY create_time DESC;
```
Top 100 customer in Postgresql PG/SQL

```postgresql
SELECT id, client_id FROM customer
ORDER BY create_time DESC
LIMIT 100;
```

**Example 2**: A Transform SQL from Oracle PL/SQL into PostgreSQL PG/SQL: 

```oracle
-- A oracle PL/SQL Procedure
CREATE OR REPLACE PROCEDURE print_contact(
    in_customer_id NUMBER 
)
IS
  r_contact contacts%ROWTYPE;
BEGIN
  -- get contact based on customer id
  SELECT *
  INTO r_contact
  FROM contacts
  WHERE customer_id = p_customer_id;

  -- print out contact's information
  dbms_output.put_line( r_contact.first_name || ' ' ||
  r_contact.last_name || '<' || r_contact.email ||'>' );

EXCEPTION
   WHEN OTHERS THEN
      dbms_output.put_line( SQLERRM );
END;

```
Translate into PostgreSQL

```postgresql
-- A postgresql PG/SQL Procedure
create procedure print_contact(IN in_customer_id integer)
    language plpgsql
as
$$
DECLARE
    r_contact contacts%ROWTYPE;
BEGIN
  -- get contact based on customer id
  SELECT *
  INTO r_contact
  FROM contacts
  WHERE customer_id = in_customer_id;

  -- print out contact's information
  RAISE NOTICE '% %<%>', r_contact.first_name, r_contact.last_name, r_contact.email;
EXCEPTION
  WHEN OTHERS THEN
    RAISE EXCEPTION '%', SQLERRM;
END;
$$;


```
**Example 3**: A cursor in Oralce PL/SQL 

```oracle
DECLARE
  CURSOR c_product
  IS
    SELECT 
        product_name, list_price
    FROM 
        products 
    ORDER BY 
        list_price DESC;
BEGIN
  FOR r_product IN c_product
  LOOP
    dbms_output.put_line( r_product.product_name || ': $' ||  r_product.list_price );
  END LOOP;
END;
```

Transformed into Postgresql PG/SQL 

```postgresql
DO $$
DECLARE 
    r_product RECORD;
BEGIN
    FOR r_product IN 
        SELECT product_name, list_price 
        FROM products 
        ORDER BY list_price DESC
    LOOP
        RAISE NOTICE '%: $%', r_product.product_name, r_product.list_price;
    END LOOP;
END $$;

```

## Reference 


