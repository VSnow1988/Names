users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print 'Students:'
for r in range (0, len(users['Students'])):
    print users['Students'][r]['first_name'] + " " + users['Students'][r]['last_name']
print 'Instructors:'
for d in range (0, len(users['Instructors'])):
    print users['Instructors'][d]['first_name'] + " " + users['Instructors'][d]['last_name']
