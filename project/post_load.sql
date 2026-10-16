SELECT setval(pg_get_serial_sequence('"user"', 'id'), coalesce(max("id"), 0) + 1, false) FROM "user";
SELECT setval(pg_get_serial_sequence('"category"', 'id'), coalesce(max("id"), 0) + 1, false) FROM "category";
SELECT setval(pg_get_serial_sequence('"wallet"', 'id'), coalesce(max("id"), 0) + 1, false) FROM "wallet";
SELECT setval(pg_get_serial_sequence('"budget"', 'id'), coalesce(max("id"), 0) + 1, false) FROM "budget";
SELECT setval(pg_get_serial_sequence('"transaction"', 'id'), coalesce(max("id"), 0) + 1, false) FROM "transaction";
SELECT setval(pg_get_serial_sequence('"audit_log"', 'id'), coalesce(max("id"), 0) + 1, false) FROM "audit_log";