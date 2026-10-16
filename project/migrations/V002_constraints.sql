-- V002: Додавання бізнес-обмежень CHECK
ALTER TABLE "category" 
    ADD CONSTRAINT "ck_category_type" 
    CHECK (type IN ('income', 'expense'));

ALTER TABLE "wallet" 
    ADD CONSTRAINT "ck_wallet_balance_positive" 
    CHECK (balance >= 0.00);

ALTER TABLE "budget" 
    ADD CONSTRAINT "ck_budget_limit_positive" 
    CHECK (limit_amount > 0.00);

ALTER TABLE "transaction" 
    ADD CONSTRAINT "ck_transaction_amount_not_zero" 
    CHECK (amount <> 0.00);