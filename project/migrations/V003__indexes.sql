-- V003: Додавання індексів на зовнішні ключі для прискорення JOIN та каскадних операцій
CREATE INDEX "idx_wallet_user_id" ON "wallet"("user_id");
CREATE INDEX "idx_budget_user_category" ON "budget"("user_id", "category_id");
CREATE INDEX "idx_transaction_wallet_id" ON "transaction"("wallet_id");
CREATE INDEX "idx_transaction_category_id" ON "transaction"("category_id");
CREATE INDEX "idx_audit_log_user_id" ON "audit_log"("user_id");