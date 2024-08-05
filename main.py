pip install pybullet
import pybullet as p
import time

# Подключаемся к физическому движку
p.connect(p.GUI)

# Загружаем плоскость и наш манипулятор
p.loadURDF("plane.urdf")
robot_id = p.loadURDF("path/to/your/robot.urdf")  # Замените на путь к вашему URDF файлу

# Получаем количество суставов в роботе
num_joints = p.getNumJoints(robot_id)

# Устанавливаем начальные положения суставов
initial_positions = [0, 0]  # Замените на нужные углы для вашего манипулятора
for i in range(num_joints):
    p.resetJointState(robot_id, i, initial_positions[i])

# Основной цикл симуляции
while True:
    p.stepSimulation()
    time.sleep(1./240.)  # Задержка для управления частотой обновления

# Отключаемся от симулятора
p.disconnect()
