from fastapi import FastAPI

from app.router import audit_log, category, customer, department, order, order_item, permission, product, role, role_permission, stock_movement, supplier, user
from app.model import user as user_model
from app.model import role as role_model
from app.model import permission as permission_model
from app.model import role_permission as role_permission_model

app = FastAPI()

app.include_router(user.router)
app.include_router(role.router)
app.include_router(permission.router)
app.include_router(role_permission.router)
app.include_router(category.router)
app.include_router(product.router)
app.include_router(customer.router)
app.include_router(supplier.router)
app.include_router(order.router)
app.include_router(order_item.router)
app.include_router(stock_movement.router)
app.include_router(audit_log.router)
app.include_router(department.router)

@app.get("/")
def root():
    return {"message": "root"}