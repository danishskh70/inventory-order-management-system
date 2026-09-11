# Inventory & Order Management System (IOMS)

Backend ERP system for tracking inventory, orders, customers, and suppliers, with role-based access control (RBAC) and JWT authentication.

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

## Auth Flow

1. User registers → password hashed (Argon2) before storing
2. User logs in (`POST /auth/login`) → credentials verified → JWT issued
3. JWT sent as `Authorization: Bearer <token>` on protected routes
4. `get_current_user` dependency decodes token, fetches user from DB
5. `require_permission` dependency checks user's role against required permission for that route

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

Actively in development. Core auth + RBAC wired; extending permission checks across all routes, adding ownership-level access control next.

## Author

Danish Shaikh — [GitHub](https://github.com/danishskh70)