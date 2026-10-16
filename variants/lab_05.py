import csv
import io
from copy import deepcopy
from datetime import date, timedelta
from decimal import Decimal


def generate_csv(spec: list, n: int) -> str:
    # Захист вхідних даних від модифікації
    spec_copy = deepcopy(spec)

    # 1. Перевірка n
    if n < 0:
        raise ValueError("n не може бути від'ємним")

    # 2. Перевірка на порожній опис
    if not spec_copy:
        raise ValueError("Порожній опис стовпців")

    # 3. Перевірка на дублювання імен стовпців
    seen_names = set()
    for col in spec_copy:
        name = col.get("name")
        if name in seen_names:
            raise ValueError(f"Дубльований стовпець: {name}")
        seen_names.add(name)

    # 4. Валідація видів генераторів та їхніх параметрів
    allowed_kinds = {"seq", "cycle", "template", "date", "decimal"}
    for col in spec_copy:
        kind = col.get("kind")
        if kind not in allowed_kinds:
            raise ValueError(f"Невідомий вид генератора: {kind}")
        if kind == "cycle":
            values = col.get("values")
            if not values:
                raise ValueError(f"Порожній список значень: {col.get('name')}")

    # Запис CSV через StringIO та csv.writer
    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")

    # Заголовок
    headers = [col["name"] for col in spec_copy]
    writer.writerow(headers)

    # Генерація рядків від i = 1 до n
    for i in range(1, n + 1):
        row = []
        for col in spec_copy:
            null_every = col.get("null_every")
            if null_every and (i % null_every == 0):
                row.append(None)
                continue

            kind = col["kind"]
            if kind == "seq":
                start = col.get("start", 1)
                step = col.get("step", 1)
                val = start + (i - 1) * step
                row.append(val)

            elif kind == "cycle":
                values = col["values"]
                val = str(values[(i - 1) % len(values)])
                row.append(val)

            elif kind == "template":
                pattern = col["pattern"]
                val = pattern.format(i=i)
                row.append(val)

            elif kind == "date":
                start_str = col["start"]
                step_days = col.get("step_days", 1)
                d = date.fromisoformat(start_str) + timedelta(days=(i - 1) * step_days)
                row.append(d.isoformat())

            elif kind == "decimal":
                start_d = Decimal(str(col["start"]))
                step_d = Decimal(str(col.get("step", "1")))
                val = start_d + Decimal(i - 1) * step_d
                row.append(f"{val:.2f}")

        writer.writerow(row)

    return output.getvalue()