from pathlib import Path
import csv
import random

rng = random.Random(42)
data_dir = Path(__file__).resolve().parent / "data"
data_dir.mkdir(parents=True, exist_ok=True)

# 1. user.csv (10 записів)
users = []
for i in range(1, 11):
    users.append({
        "id": i,
        "email": f"user_{i:03d}@example.com",
        "username": f"alex_dev_{i}",
        "created_at": f"2026-01-10 10:{i:02d}:00+00"
    })
with open("data/user.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "email", "username", "created_at"])
    writer.writeheader()
    writer.writerows(users)

# 2. category.csv (6 записів)
categories = [
    {"id": 1, "name": "Зарплата", "type": "income", "created_at": "2026-01-01 00:00:00+00"},
    {"id": 2, "name": "Фриланс", "type": "income", "created_at": "2026-01-01 00:00:00+00"},
    {"id": 3, "name": "Продукти", "type": "expense", "created_at": "2026-01-01 00:00:00+00"},
    {"id": 4, "name": "Кафе та ресторани", "type": "expense", "created_at": "2026-01-01 00:00:00+00"},
    {"id": 5, "name": "Транспорт", "type": "expense", "created_at": "2026-01-01 00:00:00+00"},
    {"id": 6, "name": "Підписки та софт", "type": "expense", "created_at": "2026-01-01 00:00:00+00"},
]
with open("data/category.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "type", "created_at"])
    writer.writeheader()
    writer.writerows(categories)

# 3. wallet.csv (15 записів)
wallets = []
for i in range(1, 16):
    u_id = ((i - 1) % 10) + 1
    wallets.append({
        "id": i,
        "user_id": u_id,
        "name": f"Гаманець #{i}",
        "balance": f"{rng.randint(1500, 45000)}.00",
        "currency": "UAH"
    })
with open("data/wallet.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "user_id", "name", "balance", "currency"])
    writer.writeheader()
    writer.writerows(wallets)

# 4. budget.csv (15 записів)
budgets = []
b_id = 1
for u_id in range(1, 6):
    for c_id in [3, 4, 5]:
        budgets.append({
            "id": b_id,
            "user_id": u_id,
            "category_id": c_id,
            "limit_amount": f"{rng.randint(2000, 8000)}.00",
            "month": "2026-10-01"
        })
        b_id += 1
with open("data/budget.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "user_id", "category_id", "limit_amount", "month"])
    writer.writeheader()
    writer.writerows(budgets)

# 5. transaction.csv (100 записів - більше 50)
transactions = []
for i in range(1, 101):
    w_id = rng.randint(1, 15)
    c_id = rng.randint(1, 6)
    day = (i % 28) + 1
    transactions.append({
        "id": i,
        "wallet_id": w_id,
        "category_id": c_id,
        "amount": f"{rng.randint(50, 2500)}.00",
        "transaction_date": f"2026-10-{day:02d}",
        "description": f"Платіж #{i}"
    })
with open("data/transaction.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "wallet_id", "category_id", "amount", "transaction_date", "description"])
    writer.writeheader()
    writer.writerows(transactions)

# 6. audit_log.csv (20 записів)
logs = []
for i in range(1, 21):
    u_id = ((i - 1) % 10) + 1
    logs.append({
        "id": i,
        "user_id": u_id,
        "action": f"USER_LOGIN_SESSION_{i}",
        "created_at": f"2026-10-15 14:{i:02d}:00+00"
    })
with open("data/audit_log.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "user_id", "action", "created_at"])
    writer.writeheader()
    writer.writerows(logs)

print("Дані успішно згенеровано в project/data/ (разом понад 165 рядків).")