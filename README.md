# podmena-ip
Просматривать список сетевых подключений.
Выбирать нужный интерфейс.
Указывать IP, маску и шлюз.
Менять IP в один клик или возвращаться к DHCP.
Как использовать:
Сохраните код в файл change_ip_gui.py.
Убедитесь, что у вас установлен Python и библиотека tkinter (обычно она уже встроена).
Запустите скрипт от имени администратора
python change_ip_gui.py
Советы:
Чтобы сделать из этого .exe, используйте pyinstaller:
bash
pip install pyinstaller
pyinstaller --onefile --windowed change_ip_gui.py

1
2
pip install pyinstaller
pyinstaller --onefile --windowed change_ip_gui.py
Это создаст автономный исполняемый файл без консольного окна.
Все команды требуют запуска от имени администратора!
