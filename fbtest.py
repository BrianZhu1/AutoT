from firebase import firebase

firebase = firebase.FirebaseApplication('https://autotapp.firebaseio.com', None)
result = firebase.post('/users', 'asdfasdfasdf')
print result