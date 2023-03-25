import GeneratePerson

person1 = GeneratePerson.generate_person()

print(person1)
print(person1["name"]["first_name"])
print(person1["name"]["last_name"])
print(person1["gender"])
print(person1["birthday"]["year"])
print(person1["birthday"]["month"])
print(person1["birthday"]["day"])
print(person1["country"])
print(person1["address"]["street"])
print(person1["address"]["city"])
print(person1["address"]["zip"])
print(person1["address"]["full_state"])
print(person1["address"]["short_state"])
print("")