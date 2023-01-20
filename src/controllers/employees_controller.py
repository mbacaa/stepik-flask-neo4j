from fastapi import APIRouter, Request, Response
from src.services.employees_service import EmployeesService

employees_router = APIRouter(prefix="/employees", tags=["employees"])
service = EmployeesService()

@employees_router.get("/")
async def get_employees(request: Request):
    try:
      response = await service.get_employees()
      return Response(content=response, status_code=200, media_type="application/json")
    except Exception as e:
      return Response(content={"error": str(e)}, status_code=500, media_type="application/json")

@employees_router.post("/")
async def create_employee(request: Request):
    try:
      response = await service.create_employee(request.json())
      return Response(content=response, status_code=201, media_type="application/json")
    except Exception as e:
      return Response(content={"error": str(e)}, status_code=500, media_type="application/json")

@employees_router.delete("/{id}")
async def delete_employee(id: str):
    try:
      response = await service.delete_employee(id)
      return Response(content=response, status_code=200, media_type="application/json")
    except Exception as e:
      return Response(content={"error": str(e)}, status_code=500, media_type="application/json")
    
@employees_router.put("/{id}")
async def update_employee(id: str, request: Request):
    try:
      response = await service.update_employee(id, request.json())
      return Response(content=response, status_code=200, media_type="application/json")
    except Exception as e:
      return Response(content={"error": str(e)}, status_code=500, media_type="application/json")

@employees_router.get("/{id}/subordinates")
async def get_subordinates(id: str):
    try:
      response = await service.get_subordinates(id)
      return Response(content=response, status_code=200, media_type="application/json")
    except Exception as e:
      return Response(content={"error": str(e)}, status_code=500, media_type="application/json")

@employees_router.get("/{id}/department")
async def get_department(id: str):
    try:
      response = await service.get_department(id)
      return Response(content=response, status_code=200, media_type="application/json")
    except Exception as e:
      return Response(content={"error": str(e)}, status_code=500, media_type="application/json")



      
 

