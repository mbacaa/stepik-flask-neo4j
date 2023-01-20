from src.config.db_connector import driver
import json

class DepartmentService:
    async def get_department(self, id):
        with driver.session() as session:
            department = session.run("MATCH (e:Employee)-[:WORKS_IN]->(d:Department) WHERE e.id = $id RETURN d", id=id).data()
            return json.dumps(department[0]['d'])

    async def get_department_details(self, id):
        with driver.session() as session:
            department = session.run("MATCH (e:Employee)-[:WORKS_IN]->(d:Department) WHERE e.id = $id RETURN d", id=id).data()
            department_name = department[0]['d']['name']
            department_employees = session.run("MATCH (e:Employee)-[:WORKS_IN]->(d:Department) WHERE d.name = $department_name RETURN e", department_name=department_name).data()
            department_manager = session.run("MATCH (e:Employee)-[:WORKS_IN]->(d:Department) WHERE d.name = $department_name AND e.manager = true RETURN e", department_name=department_name).data()
            return json.dumps({
                "name": department_name,
                "employees": [employee['e'] for employee in department_employees],
                "manager": department_manager[0]['e']
            })

    async def get_departments(self, name=None, employees=None, manager=None):
        with driver.session() as session:
            departments = session.run("MATCH (d:Department) RETURN d").data()
            return json.dumps([department['d'] for department in departments])

    async def get_department_employees(self, id):
        with driver.session() as session:
            department = session.run("MATCH (e:Employee)-[:WORKS_IN]->(d:Department) WHERE e.id = $id RETURN d", id=id).data()
            department_name = department[0]['d']['name']
            department_employees = session.run("MATCH (e:Employee)-[:WORKS_IN]->(d:Department) WHERE d.name = $department_name RETURN e", department_name=department_name).data()
            return json.dumps([employee['e'] for employee in department_employees])