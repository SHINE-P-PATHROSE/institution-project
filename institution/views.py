from django.shortcuts import render

def index (request):
    return render(request, 'home.html')
def course(request) :
    data ={
         'cse': 'subject: ' 'computer science and engineering',
         "duration": 'course duration: ' '4 years',
         "seats": 'Available seats: ' '100',
         "fee": 'Course fee: ' '50000/-',
         "Eligibility": 'Eligibility: ' ' Based on 12th mark and Entrance mark',
    }
    main = {
        'mech': 'subject: ' 'Mechanical engineering',
        "duration": 'course duration: ' '4 years',
        "seats": 'Available seats: ' '70',
        "fee": 'Course fee: ' '50000/-',
        "Eligibility": 'Eligibility: ' ' Based on 12th mark and Entrance mark',
    }
    fun ={
        'ece': 'subject: ' 'Electronics and Communication Engineering',
        "duration": 'course duration: ' '4 years',
        "seats": 'Available seats: ' '100',
        "fee": 'Course fee: ' '50000/-',
        "Eligibility": 'Eligibility: ' ' Based on 12th mark and Entrance mark',
    }
    df = {
        'eee': 'subject: ' 'Electrical and Electronics Engineering',
        "duration": 'course duration: ' '4 years',
        "seats": 'Available seats: ' '100',
        "fee": 'Course fee: ' '50000/-',
        "Eligibility": 'Eligibility: ' ' Based on 12th mark and Entrance mark',
    }
    return render(request, 'courses.html', {'data': data, 'main': main, 'fun': fun, 'df': df})
def faculty(request):
    staff1 = {
        "Professor name": "Asher",
        "Subject": "Mechanical Engineering",
        "Prof. Asher": "He teaches mechanical engineering",
    }
    staff2 = {
        "Professor name": 'Olivia',
        "Subject": "Computer Science and Engineering",
        "Prof. Olivia": "She teaches computer science and engineering",
    }
    staff3 = {
        "Professor name": 'Evelyn',
        "Subject": "Electronics and Communication Engineering",
        "Prof. Evelyn": "She Electronics and Communication Engineering",
    }
    staff4 = {
        "Professor name": 'Jack',
        "Subject": "Electrical and Electronics Engineering",
        "Prof. jack": "He teaches Electrical and Electronics Engineering",
    }
    return render(request, "faculty.html", {"staff1": staff1,"staff2": staff2,'staff3': staff3,'staff4': staff4})

def contact(request):
    data = {
         'phone': 'phone no: ''64743283737',
         'Email': 'Email id: ''Shineppathrose@gmail.com',
         'Location': 'Location: ''New york',
    }
    return render(request, "contact.html", {'data': data})

def new(request):
    return render(request,'new.html')