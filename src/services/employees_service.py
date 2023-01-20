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

    async def update_employee(self,id,employee):
        with driver.session() as session:    
            employee_exists = await session.run("MATCH (e:Employee) WHERE e.id = $id RETURN e", id=id).data()
            if len(employee_exists) == 0:
                raise Exception('User not found')
            else:
                employee_exists['name'] = employee['name']
                employee_exists['salary'] = employee['salary']
                employee_exists['age'] = employee['age']
                
                session.run("MATCH (e:Employee) WHERE id(e) = $id SET e.name = $name, e.salary = $salary, e.age = $age", id=id, name=employee_exists['name'], salary=employee_exists['salary'], age=employee_exists['age'])
                if employee['new_department'] != None:
                    session.run("MATCH (e:Employee) WHERE id(e) = $id MATCH (d:Department) WHERE d.name = $department CREATE (e)-[:WORKS_IN]->(d)", id=id, department=employee['new_department'])
                return json.dumps({'message':'Updated succesfuly'}), 200

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
