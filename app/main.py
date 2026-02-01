class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(p["name"], p["age"]) for p in people]
    for p in people:
        person = Person.people[p["name"]]
        wife_name = p.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        husband_name = p.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]
    return person_list
