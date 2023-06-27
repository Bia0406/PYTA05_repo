
class TodoList:

    def __init__(self):
        self.todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        if nume in self.todo:
            del self.todo[nume]
        else:
            print('Nu a sters!')

    def afiseaza_todo_list(self):
        for key in self.todo.keys():
            print(key)

    # varianta 2
    # def afiseaza_todo_list(self):
    #         print(list(self.todo.keys()))

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo:
            input("Doriti sa adaugam task-ul?")
            if nume_task is False:
                print("La revedere!")
            else:
                detalii = input("Detaliile taskului: ")
                self.todo = nume_task + detalii


task = TodoList()
task.adauga_task('curatenie', 'la ora 10')
print(task.todo)
task.adauga_task('cumparaturi', 'la salar')
print(task.todo)
task.finalizeaza_task('curatenie')
print(task.todo)
task.finalizeaza_task('bani')
print(task.todo)
task.adauga_task('sedinta', 'strada Primaverii')
task.adauga_task('zi de nastere', 'la George')
task.afiseaza_todo_list()

task.afiseaza_detalii_suplimentare("cumparaturi")