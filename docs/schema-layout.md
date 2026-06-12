# Schema Layout Document

## Enum Types
| Name  | Values            |
|-------|-------------------|
| roles | 'owner', 'member' |

## Users
| Column          | Type         | Constraints                   |
|-----------------|--------------|-------------------------------|
| id              | UUID         | PK, DEFAULT gen_random_uuid() |
| email           | VARCHAR(255) | NOT NULL, UNIQUE              |
| hashed_password | TEXT         | NOT NULL                      |
| display_name    | VARCHAR(100) | NOT NULL                      |
| created_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |
| updated_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |

## Memberships
| Column          | Type         | Constraints                   |
|-----------------|--------------|-------------------------------|
| id              | UUID         | PK, DEFAULT gen_random_uuid() |
| user_id         | UUID         | FK > users.id, NOT NULL       |
| household_id    | UUID         | FK > households.id, NOT NULL  |
| role            | roles        | NOT NULL                      |
| created_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |
| updated_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |
**Table constraints:** UNIQUE (user_id, household_id)

## Households
| Column          | Type         | Constraints                   |
|-----------------|--------------|-------------------------------|
| id              | UUID         | PK, DEFAULT gen_random_uuid() |
| name            | VARCHAR(100) | NOT NULL                      |
| invite_code     | VARCHAR(8)   | NOT NULL, UNIQUE              |
| created_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |
| updated_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |

## Expenses
| Column          | Type         | Constraints                   |
|-----------------|--------------|-------------------------------|
| id              | UUID         | PK, DEFAULT gen_random_uuid() |
| household_id    | UUID         | FK > households.id, NOT NULL  |
| paid_by         | UUID         | FK > users.id, NOT NULL       |
| title           | VARCHAR(100) | NOT NULL                      |
| total           | INTEGER      | NOT NULL, CHECK (total > 0)   |
| created_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |
| updated_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |

## Expense Splits
| Column          | Type         | Constraints                   |
|-----------------|--------------|-------------------------------|
| id              | UUID         | PK, DEFAULT gen_random_uuid() |
| expense_id      | UUID         | FK > expenses.id, NOT NULL    |
| user_id         | UUID         | FK > users.id, NOT NULL       |
| amount          | INTEGER      | NOT NULL, CHECK (amount > 0)  |
| created_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |
| updated_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |

## Settlements
| Column          | Type         | Constraints                   |
|-----------------|--------------|-------------------------------|
| id              | UUID         | PK, DEFAULT gen_random_uuid() |
| household_id    | UUID         | FK > households.id, NOT NULL  |
| paid_by_user_id | UUID         | FK > users.id, NOT NULL       |
| paid_to_user_id | UUID         | FK > users.id, NOT NULL       |
| amount          | INTEGER      | NOT NULL, CHECK (amount > 0)  |
| created_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |
| updated_at      | TIMESTAMPTZ  | NOT NULL, DEFAULT now()       |

## Indexes
| Table          | Column(s)              | Type   | Reason                              |
|----------------|------------------------|--------|-------------------------------------|
| users          | email                  | UNIQUE | Login lookup                        |
| households     | invite_code            | UNIQUE | Join via invite code lookup         |
| memberships    | user_id                | INDEX  | FK lookup                           |
| memberships    | household_id           | INDEX  | FK lookup                           |
| memberships    | (user_id, household_id)| UNIQUE | Composite unique constraint         |
| expenses       | household_id           | INDEX  | Tenant scoping on all expense reads |
| expense_splits | expense_id             | INDEX  | FK lookup                           |
| expense_splits | user_id                | INDEX  | FK lookup                           |
| settlements    | household_id           | INDEX  | Tenant scoping                      |
| settlements    | paid_by_user_id        | INDEX  | FK lookup                           |
| settlements    | paid_to_user_id        | INDEX  | FK lookup                           |