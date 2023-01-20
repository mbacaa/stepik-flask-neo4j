from src.config.db_connector import driver
import json

class EmployeesService:
    async def get_employees(self):
        with driver.session() as session:
            employees = session.run("MATCH (e:Employee) RETURN e").data()
            return json.dumps([employee['e'] for employee in employees])

    async def create_employee(self, employee):
        with driver.session() as session:
            session.run("CREATE (e:Employee {employee})", employee=employee)
            return json.dumps(employee)

    async def delete_employee(self, id):
        with driver.session() as session:
            session.run("MATCH (e:Employee) WHERE e.id = $id DETACH DELETE e", id=id)
            return json.dumps({"id": id})
            
    async def get_subordinates(self, id):
        with driver.session() as session:
            subordinates = session.run("MATCH (e:Employee)-[:MANAGES]->(s:Employee) WHERE e.id = $id RETURN s", id=id).data()
            return json.dumps([subordinate['s'] for subordinate in subordinates])

    async def get_department(self, id):
        with driver.session() as session:
            department = session.run("MATCH (e:Employee)-[:WORKS_IN]->(d:Department) WHERE e.id = $id RETURN d", id=id).data()
            return json.dumps(department[0]['d'])
