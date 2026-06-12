# Architectural Database Decisions Document

## Row-Level Multi-Tenancy
**Decision:** Store tenant_id at the row level rather than using separate schemas or databases per tenant.

**Considerations:** I evaluated several approaches including single database with schema-per-tenant, and separate databases per tenant as alternatives.

**Why:** Row-level tenancy allows it to serve each household with the same database while enforcing clear security boundaries at query time, while maintaining scalability and reducing infrastructure costs for operating databases. This approach also simplifies data backups and migrations compared to managing numerous separate databases.

## Global Users, Household-Scoped Roles
**Decision:** Users are global across all households, while roles (Owners, and Members) are scoped to specific household memberships.

**Considerations:** I considered storing users within each household vs. a unified user pool, and whether roles should be user-scoped or household-scoped.

**Why:** Global users enables connection to many different households while household-scoped roles maintain appropriate access control within each household. This separation prevents accidental cross-household data access while still allowing users to manage multiple households they belong to.

## UUID Primary Keys
**Decision:** All entities use UUIDs as primary keys instead of auto-incrementing integers.

**Considerations:** I compared UUIDs against sequential integers for database performance and API design.

**Why:** UUIDs prevent information leakage about row ordering and record counts, and provides better protection against enumeration attacks on the API specifically.They also offer greater randomness for high-concurrency scenarios and prevent potential timing attacks that could leak information about database state through sequential IDs.

## Integer Cents for Money
**Decision:** Store all monetary amounts as integers representing cents (e.g., $10.99 = 1099) rather than using decimal or floating-point types.

**Considerations:** I evaluated PostgreSQL DECIMAL types, BIGINT types, and floating-point numbers for monetary calculations.

**Why:** Integer cents eliminate floating-point precision errors entirely, are faster for database operations, and simplify calculations without needing arbitrary-precision libraries. This approach is well-suited for financial calculations where exact precision is mandatory and rounding errors could have legal or financial consequences.

## Token URL Safe for Invite Codes
**Decision:** Use secrets.token_urlsafe() to generate invite codes rather than random integers or UUIDs.

**Considerations:** I compared UUIDs, random integers, and secrets.token_urlsafe() for code generation.

**Why:** Token URL-safe base64 encoding produces compact, URL-friendly strings that are easier to share and less prone to truncation or encoding issues. Other options like using `pg_hashids` and `pgsodium` add extensions that cannot be guaranteed with free-tier hosting of the website. The token is designed to resist brute force attacks while being significantly shorter and more readable than a full UUID, making invite codes more user-friendly for sharing.

## Calculated Balances Rather Than Stored
**Decision:** Store only credit/debit transactions and calculate current balance dynamically rather than maintaining a stored balance field.

**Considerations:** I considered storing balances for performance vs. recalculating from transaction history.

**Why:** Calculating balances from transactions ensures data consistency without complex triggers or stored procedures that could fail silently. If transactions need adjustment, the system automatically recalculates the correct balance. While this requires computation, modern database queries can handle this efficiently, and the data integrity benefit outweighs the minimal performance cost.

## Membership Composite Unique Constraint
**Decision:** A composite unique constraint on (user_id, household_id) prevents duplicate memberships with different combinations.

**Considerations:** I evaluated whether to allow a user to hold multiple roles per household or enforce a single role per user-household pairing.

**Why:** This constraint ensures a user cannot hold multiple conflicting roles (e.g., both Owner and Member) within the same household, which would create access control ambiguities. It also prevents duplicate memberships that would complicate queries and data management, while still allowing a user to belong to a household with a specific role only once. 