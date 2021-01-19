def quastionnaire(name, surname, birth, city, email, phone):
    return f"{name} {surname}, {birth} года рождения, проживает в г.{city}, email: {email}, контактный телефон: {phone}"

print(quastionnaire(surname='Иванов', name='Иван', email='blablabla@mail.com',
              phone='890000000', city='Житомир', birth='1917'))