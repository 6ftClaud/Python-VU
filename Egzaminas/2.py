# Sukuriama Tasks klase
class Tasks:

    # __init__ funkcija issaukiama sukuriant klases objekta
    # klasei ne visada perduodami name ir till_datetime kintamieji,
    # del to naudojama =None nurodyti default reiksme
    def __init__(self, name=None, till_datetime=None):
        # Inicializuojamas tasks kintamasis
        self.tasks = []
        # Jei name ir till_datetime nera lygus None, pridedamas
        # task prie tasks
        if name != None and till_datetime != None:
            self.add_task(name, till_datetime)

    # add_task funkcija priima name ir till_datetime kintamuosius
    def add_task(self, name, till_datetime):
        # task pridedeama prie tasks su .append() funkcija
        self.tasks.append((name, till_datetime))

    # remove_task funkcija priima name ir till_datetime kintamuosius
    def remove_task(self, name, till_datetime):
        # Sukuriamas task tuple is name ir till_datetime
        task = (name, till_datetime)
        # enumerate() naudojamas sekti indeksa
        for i, t in enumerate(self.tasks):
            # Jei task randama
            if t == task:
                # task istrinama
                self.tasks.pop(i)
                # break tam, kad nebeieskotu
                break

    # Iteruoja per sarasa ir spausdina visus kintamuosius sarase
    def display_tasks(self):
        for task in self.tasks:
            print(task)


# Testavimas
tasks = Tasks()
tasks.add_task("pirma", "2021-06-01 12:00:00")
tasks.add_task("antra", "2021-06-01 13:00:00")
tasks.add_task("trecia", "2021-06-01 14:00:00")
tasks.display_tasks()

tasks.remove_task("antra", "2021-06-01 13:00:00")
tasks.display_tasks()

tasks = Tasks("susitikimas", "2021-06-03 15:00:00")
tasks.display_tasks()
