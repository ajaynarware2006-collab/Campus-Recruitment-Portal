CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    email VARCHAR(254) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    user_role TEXT NOT NULL check (user_role IN ('Student','Admim','Recruiter')),
    account_status TEXT NOT NULL CHECK (account_status IN ('Active','Inactive','Suspended')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
