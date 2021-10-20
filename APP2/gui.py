import tkinter as tk
from tkinter.filedialog import askopenfilename
from main import shuffle, coter, obtenir_cote_max

def show_result():
	result_frame = tk.Frame(root)
	result_frame.pack()
	result_frame.tkraise()
	result_frame.place(relheight=1, relwidth=1)

	global réponses
	global qcm_questions
	cote = coter(réponses, qcm_questions, "1" if mode.get() == "Cool" else "2")
	max_cote = obtenir_cote_max(qcm_questions)

	grade = tk.Label(result_frame, text=f"Vous avez obtenu {cote}/{max_cote}!", font=("Courier", 30, "bold"))
	grade.place(relx=.1, rely=.4)

réponses = []
def submit_answers(answers):
	global réponses
	réponses.append([str(i+1) for i in range(len(answers.keys())-1) if answers["vars"][i].get() == 1])
	global qcm_questions
	global qcm_index
	qcm_index += 1
	if qcm_index < len(qcm_questions):
		setup_question(qcm_questions[qcm_index])
	else:
		show_result()

def setup_question(question):
	for widget in question_frame.winfo_children():
		widget.destroy()
	question_label = tk.Label(question_frame, text=question[0], font=("Courier", 18, "bold"), wraplength=600, justify="center")
	question_label.place(rely=0.1, relx=0.15)
	answers = {"vars":[]}
	i = 0
	for answer in question[1]:
		answers["vars"].append(tk.IntVar())
		answers[str(i)] = tk.Checkbutton(question_frame, text=answer[0], font=("Courier", 14), variable=answers["vars"][i], onvalue=1, offvalue=0, wraplength=600, justify="center")
		answers[str(i)].place(rely=0.3 + i*0.1, relx = 0.1)
		i += 1

	submit_btn = tk.Button(question_frame, text="Soumettre", command=lambda: submit_answers(answers))
	submit_btn.place(rely=0.8, relx=0.35, relwidth=0.3, relheight=0.2)

import qcm as builder
qcm_questions = []
qcm_index = 0
def start_qcm(qcm):
	if not qcm:
		return
	question_frame.tkraise()
	question_frame.place(relheight=1, relwidth=1)

	questions = builder.build_questionnaire(qcm)
	randomised_questions = shuffle(questions)
	
	global qcm_questions
	qcm_questions = randomised_questions
	setup_question(qcm_questions[0])

qcm_file = ""
def set_qcm():
	global qcm_file
	qcm_file = askopenfilename()

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)
question_frame = tk.Frame(root)
question_frame.pack()

main_h1 = tk.Label(text="Bienvenu(e) dans le programme de QCM!", font=("Courier", int(root.winfo_width()/40), "bold"))
main_h1.place(rely= 0.1, relx=0.125)
start_btn = tk.Button(text="Commencer", command=lambda:start_qcm(qcm_file))
start_btn.place(rely= 0.8, relx=0.4, relwidth=0.2, relheight=0.1)
file_btn = tk.Button(text="Sélectionner le QCM", command=set_qcm)
file_btn.place(rely= 0.4, relx=0.3, relwidth=0.4, relheight=0.2)
choices = ['Cool', 'Sévère']
mode = tk.StringVar(root)
mode.set('Cool')

from tkinter.ttk import Combobox
mode_label = tk.Label(text="mode de cotation")
mode_label.place(rely=.65, relx=0.2)
mode_box = Combobox(root, values = choices, state='readonly', textvariable=mode)
mode_box.current(0)
mode_box.place(rely=.65, relx=0.4, relwidth=0.2)

def update(event):
	main_h1.config(font=("Courier", int(root.winfo_width()/40), "bold"))

root.minsize(width=800, height=500)
root.bind("<Configure>", update)
root.mainloop()