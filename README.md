# SQL GPT
SQL **GPT** Generative Pre-trained Transformer for SQL migration with different SQL dialects between Oracle/Mysql/SQL Server/PostgreSQL... etc. 

## The Data Mirgation Challenge
**SQL DPT is trying to solve the most difficult step in 5th Mirgration.**

Migrating a database(Oracle) to another database(Postgresql) can be a complex process that requires careful planning and execution.

1. **Plan the migration**: Before you start migrating your database, you need to plan the migration process. You should determine which tables, views, indexes, stored procedures, and other database objects you need to migrate. You should also plan how you will transfer the data from Oracle to PostgreSQL.

2. **Set up PostgreSQL**: You need to install PostgreSQL on the server where you want to migrate your Oracle database. You can download PostgreSQL from the official website and follow the installation instructions for your operating system.
 
3. **Create the database schema**: You need to create the database schema in PostgreSQL to match the Oracle database schema. You can use the pgloader tool to automatically create the schema in PostgreSQL.

4. **Migrate the data**: You need to transfer the data from Oracle to PostgreSQL. There are several ways to do this, including using the pgloader tool, using an ETL (Extract, Transform, Load) tool, or exporting the data from Oracle to a CSV file and importing it into PostgreSQL.
 
5. **Migrate functions and stored procedures**: You need to migrate the stored procedures from Oracle to PostgreSQL. 

6. **Test the migration**: Once you have migrated the data and stored procedures, you need to test the migration to ensure that everything is working correctly.

7. **Deploy the migration**: After testing, you can deploy the migration by pointing your applications to the PostgreSQL database instead of the Oracle database.

Note that migrating a database can be a complex process, and it is important to take appropriate precautions and perform thorough testing before deploying the migration to production. Overall, the key to transforming Oracle SQL into PostgreSQL SQL is to understand the differences between the two database systems and adjust your queries accordingly. It's always a good idea to consult the relevant documentation or resources to ensure that your transformed SQL statements are accurate and effective.


## Marketing And Analytics

Oralce into Postgresql marking analytics in a sample explaination, definitely there are deep anlaytics of all the features. 

YES=Meet Need, X=Not at All, P=Partially

| Solution      | Schema | Function | Store Procedure |
|:-----------|:------:|:---------:|:--------------:|
| [AWS DMS](https://aws.amazon.com/dms/)    |   Y    |        X | X               |
|[ GOOGLE DMS ](https://cloud.google.com/database-migration)|   Y    |        X | X|
| [Azure DMS](https://azure.microsoft.com/en-us/products/database-migration)  |   Y    |       X|X|
| [Ora2pg](https://ora2pg.darold.net/)     |   Y    |        P | P               |
| [Jooq](https://www.jooq.org/translate/)     |   Y    |        P | P               |

Ora2Pg, first release on May 2001 (last version: 15.1) 14 years of development, Near 10,000 lines of Perl code. recommend by Google [link](https://cloud.google.com/blog/products/databases/migrating-oracle-to-postgresql-just-got-a-lot-easier), AWS Cloud [Blog link](https://aws.amazon.com/blogs/database/migrating-blob-and-clob-tables-from-oracle-to-postgresql-using-ora2pg-and-aws-dms/). But there are still many procedure and function transformming failed. 

## The Solution And Features

**The solution** is inspired by OpenAI GPT model. Converting the problem from Database Domain Special Programming Language Compiler Issue into General NLP problem by AI power.

![Problem Converting](./docs/Problem.drawio.svg)

### Features
* No Coding for SQL complier or Converter.
* Based on Large language models (LLMs), like OpenAI GPT or Google T5.
* SQL GPT be adapted into different databases with different datasets.
* Support any data objects: Tables, Views, Indexs, Packages, Partitions, Procedures, Functions, Triggers, Types, Sequences, Meterialized View, Sznozms, Database Links, Scheduler, GIS, etc...
* Reinforcement learning from Human Feedback(DBA) for language model. [OpenAI Paper](https://cdn.openai.com/papers/Training_language_models_to_follow_instructions_with_human_feedback.pdf) 

## Roadmap

**Version 1**: SQL GPT is verifying the possibility of this design by OpenAI GPT model.  And current OpenAI model(Algorithm + Training data) is not opensource, we can't train the model. 

**Version 2**: to extend model like open-source model like Google T5 model + clean dataset to build for enterprise demand.

## Overview of Architecture

* There are serveral components like SQLcollector, Dummy-Data-Generator, SQLGPT service ...
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

## References

* Huggingface rlhf: [https://huggingface.co/blog/rlhf](https://huggingface.co/blog/rlhf)
* OpenAI Paper:  [https://cdn.openai.com/papers/Training_language_models_to_follow_instructions_with_human_feedback.pdf](https://cdn.openai.com/papers/Training_language_models_to_follow_instructions_with_human_feedback.pdf)
* CarperAI trlx: [https://github.com/CarperAI/trlx ](https://github.com/CarperAI/trlx)
* Ora2pg: [https://ora2pg.darold.net/](https://ora2pg.darold.net/)
* Joop Translate: [https://www.jooq.org/translate/](https://www.jooq.org/translate/)
* Google T5: [ https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html]()
* OpenAI GPT: [https://openai.com/product]()


