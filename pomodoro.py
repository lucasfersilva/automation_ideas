import time


class pomodoro():
    def __init__(self):
        self.IV_TAREFA = ""
        self.IV_TIMER = 0
        self.IV_TASK_COUNT = 0

    def input_task(self):
        try:
            self.IV_TAREFA = input("Digite a Tarefa que esta trabalhando: ")
            if len(self.IV_TAREFA) > 0:
                print("Você está trabalhando na tarefa:", self.IV_TAREFA)
            while self.IV_TAREFA:
                time.sleep(1500)
                for i in range(4):
                    self.IV_TIMER += 1
                    if self.IV_TIMER == 4:
                        print("Você Completou seu Pomodoro, tire um intervalo longo!")
                        time.sleep(900)
                        self.IV_TIMER= 0
                    else:
                        print("Tire seu intervalo curto")
                        time.sleep(300)
                        print("Volte ao trabalho")
                        time.sleep(1500)
        except KeyboardInterrupt:
            print("Programa interrompido!")


a = pomodoro()
a.input_task()
