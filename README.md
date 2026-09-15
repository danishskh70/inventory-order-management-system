# Inventory & Order Management System (IOMS)

Backend ERP system for tracking inventory, orders, customers, and suppliers, with role-based access control (RBAC) and JWT authentication.

## Motivation

This is a self-directed learning project, not a client requirement or a deployed business system. Most beginner backend tutorials stop at single-table CRUD and never touch the patterns that actually matter in real systems — relational depth, access control, and security. I built this specifically to move past that: a realistic domain (inventory/order management) that naturally requires every relationship type (one-to-many, many-to-many, self-referential, audit logging) at a scope small enough to actually finish.

The goal wasn't the ERP itself — it was learning to design, secure, and defend a real multi-table backend system end-to-end, including the mistakes and fixes along the way (see commit history for a few real bugs caught and corrected, not just a clean final state).

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Auth:** JWT (PyJWT), Argon2 password hashing (pwdlib)

## Features

- JWT-based authentication (login, token creation, token verification)
- Role-based access control — roles, permissions, and role-permission mapping, fully API-manageable
- 14 relational tables: users, roles, permissions, categories, products, customers, suppliers, orders, order items, stock movements, audit logs, departments, warehouses
- Alembic-managed schema migrations
- Server-side calculation of order totals from order items (not trusted from client input)

## Auth Flow

1. User registers → password hashed (Argon2) before storing
2. User logs in (`POST /auth/login`) → credentials verified → JWT issued
3. JWT sent as `Authorization: Bearer <token>` on protected routes
4. `get_current_user` dependency decodes token, fetches user from DB
5. `require_permission` dependency checks user's role against the required permission for that route

## Setup

```bash
git clone https://github.com/danishskh70/inventory-order-management-system.git
cd inventory-order-management-system
pip install -r requirements.txt
cp .env.example .env  # fill in your own values
alembic upgrade head
uvicorn app.main:app --reload
```

## Environment Variables

See `.env.example` for required variables (database URL, JWT secret key, algorithm, token expiry).

## Status

Core learning goals complete: JWT auth, full RBAC enforcement across all routes (every read requires login, every sensitive write requires a specific permission), and correct server-side calculation of order totals.

Not yet built, known gaps:
- No pagination on list endpoints
- No automated tests — verified manually via Swagger/Postman
- Stock movements are a separate manual endpoint, not auto-triggered by the order flow
- A few legacy/generic permission names from early testing remain unused alongside the newer, specific ones

This is a learning artifact, not a production-hardened system — treat it as a demonstration of backend architecture and security patterns, not a deploy-ready product.

## Author

Danish Shaikh — [GitHub](https://github.com/danishskh70)