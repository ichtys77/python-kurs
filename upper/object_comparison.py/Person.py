class Person:
  def __init__(self, name, surname, email, nickname):
    self.name = name
    self.surname = surname
    self.email = email
    self.nickname = nickname
  
  def printInfo(self):
    print(f'name: {self.name}, surname: {self.surname} \nemail: {self.email}, nickname: {self.nickname}')