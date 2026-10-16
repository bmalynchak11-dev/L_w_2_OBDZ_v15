-- check: fk: транзакції без валідного гаманця
SELECT t.id, t.wallet_id FROM "transaction" t
LEFT JOIN "wallet" w ON t.wallet_id = w.id
WHERE w.id IS NULL;

-- check: fk: бюджети без валідної категорії
SELECT b.id, b.category_id FROM "budget" b
LEFT JOIN "category" c ON b.category_id = c.id
WHERE c.id IS NULL;

-- check: dup: дублікати категорій за назвою та типом
SELECT name, type, COUNT(*) FROM "category"
GROUP BY name, type
HAVING COUNT(*) > 1;

-- check: dup: дублювання бюджетів на одну категорію для одного користувача в один місяць
SELECT user_id, category_id, month, COUNT(*) FROM "budget"
GROUP BY user_id, category_id, month
HAVING COUNT(*) > 1;

-- check: null: транзакції з порожнім описом або відсутньою датою
SELECT id FROM "transaction"
WHERE transaction_date IS NULL OR description IS NULL;

-- check: rule: невідповідність між типом категорії доходу/витрати та сумою операції
SELECT t.id, t.amount, c.type FROM "transaction" t
JOIN "category" c ON t.category_id = c.id
WHERE (c.type = 'expense' AND t.amount < 0) OR (c.type = 'income' AND t.amount < 0);