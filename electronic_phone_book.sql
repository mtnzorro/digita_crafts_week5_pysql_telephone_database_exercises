CREATE TABLE phonebook (
  id serial PRIMARY KEY,
  name varchar NOT NULL UNIQUE,
  phone_number varchar,
  email varchar UNIQUE
);
