from dotenv import load_dotenv
load_dotenv()

from datetime import datetime, date, time

from app import app, db
from app.models import User, AppointmentCategory, Appointment, ToDoType, ToDo
from app.api.user_routes import set_password

hashed1 = set_password('password1')
hashed2 = set_password('password2')
hashed3 = set_password('password3')
hashed4 = set_password('password4')
hashed5 = set_password('password5')
hashed6 = set_password('password6')
hashed7 = set_password('password7')
hashed8 = set_password('password8')
hashed9 = set_password('password9')

with app.app_context():
  db.drop_all()
  db.create_all()

  ian = User(username = 'Ian', email = 'ian@aa.io', hashed_password=hashed1)
  javier = User(username = 'Javier', email = 'javier@aa.io', hashed_password=hashed2)
  dean = User(username = 'Dean', email = 'dean@aa.io', hashed_password=hashed3)
  angela = User(username = 'Angela', email = 'angela@aa.io', hashed_password=hashed4)
  soonmi = User(username = 'Soon-Mi', email = 'soonmi@aa.io', hashed_password=hashed5)
  alissa = User(username = 'Alissa', email = 'alissa@aa.io', hashed_password=hashed6)
  mrAnderson = User(username='mranderson', email='Mr@Anderson.com', hashed_password=hashed7)
  mrSmith = User(username='mrsmith', email='Mr@Smith.com', hashed_password=hashed8)
  demouser = User(username='demouser', email='demo@user.org', hashed_password=hashed9)

  db.session.add(ian)
  db.session.add(javier)
  db.session.add(dean)
  db.session.add(angela)
  db.session.add(soonmi)
  db.session.add(alissa)
  db.session.add(mrAnderson)
  db.session.add(mrSmith)
  db.session.add(demouser)

  apptC1 = AppointmentCategory(category='doctor')
  apptC2 = AppointmentCategory(category='salon')
  apptC3 = AppointmentCategory(category='grooming')
  apptC4 = AppointmentCategory(category='spa')
  apptC5 = AppointmentCategory(category='vet')
  apptC6 = AppointmentCategory(category='pet groomers')
  apptC7 = AppointmentCategory(category='interview')
  apptC8 = AppointmentCategory(category='meeting')
  apptC9 = AppointmentCategory(category='conference')
  apptC10 = AppointmentCategory(category='social')

  db.session.add(apptC1)
  db.session.add(apptC2)
  db.session.add(apptC3)
  db.session.add(apptC4)
  db.session.add(apptC5)
  db.session.add(apptC6)
  db.session.add(apptC7)
  db.session.add(apptC8)
  db.session.add(apptC9)
  db.session.add(apptC10)

  appt1 = Appointment(categoryId=1, userId=9, date=date(2020, 10, 30), time=time(hour=15, minute=2), notes='Dr Weiler')
  appt2 = Appointment(categoryId=5, userId=9, date=date(2020, 10, 30), time=time(hour=13, minute=15), notes='Rocky/Dr. Bianca')
  appt3 = Appointment(categoryId=7, userId=9, date=date(2020, 10, 30), time=time(hour=12, minute=30), notes='Phone Interview with App Academy 1 888 888 8888')
  appt4 = Appointment(categoryId=2, userId=9, date=date(2020, 11, 2), time=time(hour=11, minute=45), notes='Hair and Nail Salon')
  appt5 = Appointment(categoryId=3, userId=9, date=date(2020, 11, 2), time=time(hour=14, minute=45), notes='Barber Bob')
  appt6 = Appointment(categoryId=4, userId=9, date=date(2020, 11, 5), time=time(hour=10, minute=15), notes='Massage Therapist Monica')
  appt7 = Appointment(categoryId=6, userId=9, date=date(2020, 11, 6), time=time(hour=13, minute=15), notes='Rocky Stinks')
  appt8 = Appointment(categoryId=8, userId=9, date=date(2020, 11, 6), time=time(hour=15, minute=30), notes='Google Meeting')
  appt9 = Appointment(categoryId=10, userId=9, date=date(2020, 10, 30), time=time(hour=22, minute=0), notes='PARTY AT MY HOUSE!!!!')

  db.session.add(appt1)
  db.session.add(appt2)
  db.session.add(appt3)
  db.session.add(appt4)
  db.session.add(appt5)
  db.session.add(appt6)
  db.session.add(appt7)
  db.session.add(appt8)
  db.session.add(appt9)

  toDoType1 = ToDoType(type='To Do (General)')
  toDoType2 = ToDoType(type='Groceries')
  toDoType3 = ToDoType(type='High Priority')
  toDoType4 = ToDoType(type='Low Priority')
  toDoType5 = ToDoType(type='Extra Curricular Projects')
  toDoType6 = ToDoType(type='Bucket List')

  db.session.add(toDoType1)
  db.session.add(toDoType2)
  db.session.add(toDoType3)
  db.session.add(toDoType4)
  db.session.add(toDoType5)
  db.session.add(toDoType6)

  toDo1 = ToDo(userId=9, typeId=1, item='Rocky Bath')
  toDo2 = ToDo(userId=9, typeId=1, item='Grocery Shopping')
  toDo3 = ToDo(userId=9, typeId=1, item='Laundry')
  toDo4 = ToDo(userId=9, typeId=1, item='Deposit money into bank account')
  toDo5 = ToDo(userId=9, typeId=1, item='Tend to plants/garden')
  toDo6 = ToDo(userId=9, typeId=1, item='Rocky bath')
  toDo7 = ToDo(userId=9, typeId=6, item='Cliff Diving')
  toDo8 = ToDo(userId=9, typeId=3, item='Carve a punkin')
  toDo9 = ToDo(userId=9, typeId=5, item='Paint a portrait of Rocky')
  toDo10 = ToDo(userId=9, typeId=5, item='Make Rocky a cat condo')
  toDo11 = ToDo(userId=9, typeId=6, item='Sky diving Again')
  toDo12 = ToDo(userId=9, typeId=6, item='DJ Again')

  db.session.add(toDo1)
  db.session.add(toDo2)
  db.session.add(toDo3)
  db.session.add(toDo4)
  db.session.add(toDo5)
  db.session.add(toDo6)
  db.session.add(toDo7)
  db.session.add(toDo8)
  db.session.add(toDo9)
  db.session.add(toDo10)
  db.session.add(toDo11)
  db.session.add(toDo12)





  db.session.commit()
