### Project Title
## Concurrency Safe Banking Backend Service

Core Engineering Points

- Built secure banking backend using Django REST Framework with JWT authentication and role based access control.

- Designed custom user model with role hierarchy for customer, manager, and admin level authorization.

- Implemented bank account ownership enforcement to prevent horizontal privilege escalation.

- Developed immutable double entry ledger system ensuring financial correctness without storing balance state.

- Engineered atomic fund transfer service using database transactions and row level locking to prevent race condition induced double spending.

- Implemented idempotent transfer execution using unique idempotency keys to handle retries and network failures.

- Built deposit and transaction history APIs with pagination and filtering for financial transparency.

- Created concurrency simulation tests using multithreading and TransactionTestCase validating system money invariant under parallel transfers.

- Designed modular service layer architecture separating API, domain logic, and persistence layers.

- Enabled secure admin observability through Django admin dashboards with search, filters, and pagination.