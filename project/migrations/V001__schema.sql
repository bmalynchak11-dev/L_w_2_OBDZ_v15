-- V001: Базова схема таблиць (створення сутностей)
CREATE TABLE "user" (
    "id" integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "email" text NOT NULL UNIQUE,
    "username" text NOT NULL,
    "created_at" timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE "category" (
    "id" integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "name" text NOT NULL,
    "type" text NOT NULL,
    "created_at" timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE "wallet" (
    "id" integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "user"("id") ON DELETE CASCADE,
    "name" text NOT NULL,
    "balance" numeric(12, 2) NOT NULL DEFAULT 0.00,
    "currency" text NOT NULL DEFAULT 'UAH'
);

CREATE TABLE "budget" (
    "id" integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "user"("id") ON DELETE CASCADE,
    "category_id" integer NOT NULL REFERENCES "category"("id") ON DELETE CASCADE,
    "limit_amount" numeric(12, 2) NOT NULL,
    "month" date NOT NULL
);

CREATE TABLE "transaction" (
    "id" integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "wallet_id" integer NOT NULL REFERENCES "wallet"("id") ON DELETE CASCADE,
    "category_id" integer NOT NULL REFERENCES "category"("id") ON DELETE RESTRICT,
    "amount" numeric(12, 2) NOT NULL,
    "transaction_date" date NOT NULL,
    "description" text
);

CREATE TABLE "audit_log" (
    "id" integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "user_id" integer REFERENCES "user"("id") ON DELETE SET NULL,
    "action" text NOT NULL,
    "created_at" timestamptz NOT NULL DEFAULT now()
);