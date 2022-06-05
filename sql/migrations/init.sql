create type CAPEC_TYPE as enum (
  'high',
  'medium',
  'low',
  'no_chance'
);

create table bdu (
  id serial primary key,
  name varchar(12) not null,
  cve varchar(100) not null,
  cwe varchar(255) not null,
  capec_high varchar(255) not null,
  capec_medium varchar(255) not null,
  capec_low varchar(255) not null,
  capec_no_chance varchar(255) not null
);

create table cwe (
  id serial primary key,
  value int not null unique
);

create table bdu_cwe (
  id serial primary key,
  bdu_id int not null references bdu(id),
  cwe_id int not null references cwe(id)
);

create table capec (
  id serial primary key,
  value int not null unique,
  type CAPEC_TYPE
);

create table cwe_capec (
  id serial primary key,
  cwe_id int not null references cwe(id),
  capec_id int not null references capec(id)
);
