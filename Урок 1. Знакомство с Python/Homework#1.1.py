"""
Я уверен, что эту задачу можно написать как-то изящнее, но пока не знаю как.
Буду рад получить рекомендации:)
"""

seconds = int(input("Введите время в секундах - "))
h = seconds // 3600
m = (seconds % 3600) // 60
s = seconds % 60

h_str = str(h)
m_str = str(m)
s_str = str(s)

if len(h_str) == 1:
    h_str = '0' + h_str
if len(m_str) == 1:
    m_str = '0' + m_str
if len(s_str) == 1:
    s_str = '0' + s_str

print("Итоговое время:")
print("%s:%s:%s" % (h_str, m_str, s_str))
