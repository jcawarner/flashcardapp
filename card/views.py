from django.shortcuts import render
from random import randint

def home(request):
	return render(request, 'home.html', {})

def add(request):

	num_1 = randint(0,10)
	num_2 = randint(0,10)

	

	if request.method == 'POST':
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) + int(old_num_2)
		

		if int(answer) == correct_answer:
			my_answer = "Correct!"
		else:
			my_answer = "Incorrect!"

		return render(request, 'add.html', {
			'answer':answer,
			'my_answer':my_answer,
			'correct_answer': correct_answer,
			'num_1': num_1,
			'num_2': num_2,
			})

	return render(request, 'add.html', {
		'num_1': num_1,
		'num_2': num_2,
		})

def subtract(request):

	num_1 = randint(0,10)
	num_2 = randint(0,10)

	

	if request.method == 'POST':
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) - int(old_num_2)
		

		if int(answer) == correct_answer:
			my_answer = "Correct!"
		else:
			my_answer = "Incorrect!"

		return render(request, 'subtract.html', {
			'answer':answer,
			'my_answer':my_answer,
			'correct_answer': correct_answer,
			'num_1': num_1,
			'num_2': num_2,
			})

	return render(request, 'subtract.html', {
		'num_1': num_1,
		'num_2': num_2,
		})

	

def multiply(request):
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	

	if request.method == 'POST':
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) * int(old_num_2)
		

		if int(answer) == correct_answer:
			my_answer = "Correct!"
		else:
			my_answer = "Incorrect!"

		return render(request, 'multiply.html', {
			'answer':answer,
			'my_answer':my_answer,
			'correct_answer': correct_answer,
			'num_1': num_1,
			'num_2': num_2,
			})

	return render(request, 'multiply.html', {
		'num_1': num_1,
		'num_2': num_2,
		})

def divide(request):
	num_1 = randint(0,10)
	num_2 = randint(1,10)

	

	if request.method == 'POST':
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = float(old_num_1) / float(old_num_2)
		

		if float(answer) == round(correct_answer,1):
			my_answer = "Correct!"
		else:
			my_answer = "Incorrect!"

		return render(request, 'divide.html', {
			'answer':answer,
			'my_answer':my_answer,
			'correct_answer': correct_answer,
			'num_1': num_1,
			'num_2': num_2,
			})

	return render(request, 'divide.html', {
		'num_1': num_1,
		'num_2': num_2,
		})


def exponent(request):
	num_1 = randint(0,10)
	num_2 = randint(1,10)

	

	if request.method == 'POST':
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) ** int(old_num_2)
		

		if int(answer) == correct_answer:
			my_answer = "Correct!"
		else:
			my_answer = "Incorrect!"

		return render(request, 'exponent.html', {
			'answer':answer,
			'my_answer':my_answer,
			'correct_answer': correct_answer,
			'num_1': num_1,
			'num_2': num_2,
			})

	return render(request, 'exponent.html', {
		'num_1': num_1,
		'num_2': num_2,
		})


def squareroot(request):

	num_1 = randint(0,10)
	

	if request.method == 'POST':
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		

		correct_answer = int(old_num_1) ** 0.5
		

		if float(answer) == round(correct_answer,1):
			my_answer = "Correct!"
		else:
			my_answer = "Incorrect!"

		return render(request, 'squareroot.html', {
			'answer':answer,
			'my_answer':my_answer,
			'correct_answer': correct_answer,
			'num_1': num_1,
			})

	return render(request, 'squareroot.html', {
		'num_1': num_1,
		})
