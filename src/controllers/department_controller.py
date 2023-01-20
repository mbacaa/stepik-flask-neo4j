from fastapi import APIRouter, Request, Response
from src.services.department_service import DepartmentService

department_router = APIRouter(prefix="/department", tags=["department"])
service = DepartmentService()

@department_router.get("/{id}")
async def get_department(id: str):
    try:
      response = await service.get_department(id)
      return Response(content=response, status_code=200, media_type="application/json")
    except Exception as e:
      return Response(content={"error": str(e)}, status_code=500, media_type="application/json")

@department_router.get("/{id}/details")
async def get_department_details(id: str):
    try:
      response = await service.get_department_details(id)
      return Response(content=response, status_code=200, media_type="application/json")
    except Exception as e:
      return Response(content={"error": str(e)}, status_code=500, media_type="application/json")

@department_router.get("/{id}/employees")
async def get_department_employees(id: str):
    try:
      response = await service.get_department_employees(id)
      return Response(content=response, status_code=200, media_type="application/json")
    except Exception as e:
      return Response(content={"error": str(e)}, status_code=500, media_type="application/json")

@department_router.get("/")
async def get_departments():
    try:
      response = await service.get_departments()
      return Response(content=response, status_code=200, media_type="application/json")
    except Exception as e:
      return Response(content={"error": str(e)}, status_code=500, media_type="application/json")

