import matplotlib.pyplot as plt

# Данные для круговой диаграммы
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [20, 30, 25, 25]
explode = (0, 0.1, 0, 0)  # Величина смещения для второго сектора
plt.pie(sizes, labels=labels, autopct='%1.1f%%', wedgeprops=dict(width=0.3))
plt.title('Donut Chart')
plt.show()