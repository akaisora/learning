import dataclasses      
                        
@dataclasses.dataclass  
class Person:           
    name: str           
    age: int = 0             
                        
                        
@dataclasses.dataclass  
class Employee:         
    name: str           
    id: int =0          
                 
@dataclasses.dataclass
class PersonEmployee:
	name:str
	age: int=0
	id: int = 0
						
persons = [Person("bahar", 33), Person("tamas", 43), Person("Chiara", 25)]
employees = [Employee("tamas", 65987), Employee("bahar", 65235), Employee("Chiara", 66985)]

#generator = map(PersonEmployee(x.name,x.age,y.id), filter(lambda x,y: x.name==y.name, ((x,y) for x in persons for y in employees)))
#generator = filter(lambda record: record[0].name==record[1].name, ((x,y) for x in persons for y in employees))
generator = map(lambda record: PersonEmployee(record[0].name,record[0].age,record[1].id), filter(lambda record: record[0].name==record[1].name, ((x,y) for x in persons for y in employees)))

generator = map(lambda record: PersonEmployee(record[0].name,record[0].age,record[1].id), filter(lambda record: record[0].name==record[1].name, zip(persons,employees)))
generator = map(lambda record: PersonEmployee(record[0].name,record[0].age,record[1].id), filter(lambda x: x.name==y.name, itertools.chain(persons,employees)))

source = iter([1,2,3,4,5])
#avg = reduce(