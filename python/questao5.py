class TabelaDrones:
    def __init__(lista_drones=[]):
        self.lista_drones = lista_drones


    def add(self, drone):
        self.lista_drones.append(drone)

    def rankear(self):
        self.lista_drones = sorted(self.lista_drones, key=lambda x: x.ano_construcao)
    
    def __str__(self):
        s = ''
        for i in self.lista_drones:
            s += str(i)
        return s

class Drone:
    def __init__(n_motores, n_cameras, ano_construcao, nome, ultima_utilizacao):
        self.n_motores = n_motores
        self.n_cameras = n_cameras
        self.ano_construcao = ano_construcao
        self.nome = nome
        self.ultima_utilizacao = ultima_utilizacao
    
    def fale(self): # metodo de livre escolha
        print('bip bop')

    def __le__(self, outro_drone):
        return self.ano_construcao <= outro_drone.ano_construcao 

    def __repr__(self):
        return repr((self.nome, self.n_motores, self.n_cameras, self.ano_construcao, self.ultima_utilizacao))

    def __str__(self):
        return f"{nome}\t|\t#_motores: {self.n_motores}\t|\t#_cameras: {self.n_cameras}\t|\t{self.ano_construcao}\t|\t{self.ultima_utilizacao}\t|"

