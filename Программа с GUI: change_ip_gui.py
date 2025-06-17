import tkinter as tk
from tkinter import messagebox
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        messagebox.showerror("Ошибка", f"Не удалось выполнить команду:\n{result.stderr}")
    else:
        output_text.insert(tk.END, result.stdout + "\n")
        output_text.see(tk.END)

def list_interfaces():
    cmd = 'netsh interface ipv4 show interfaces'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Список сетевых интерфейсов:\n\n")
    output_text.insert(tk.END, result.stdout)

def set_static_ip():
    interface = interface_entry.get().strip()
    ip = ip_entry.get().strip()
    mask = mask_entry.get().strip()
    gateway = gateway_entry.get().strip()

    if not all([interface, ip, mask, gateway]):
        messagebox.showwarning("Внимание", "Заполните все поля!")
        return

    cmds = [
        f'netsh interface ipv4 set address name="{interface}" static {ip} {mask} {gateway}',
        f'netsh interface ipv4 set dns name="{interface}" static 8.8.8.8'
    ]
    for cmd in cmds:
        run_command(cmd)
    messagebox.showinfo("Готово", "IP успешно изменён!")

def reset_to_dhcp():
    interface = interface_entry.get().strip()
    if not interface:
        messagebox.showwarning("Внимание", "Введите имя интерфейса!")
        return

    cmds = [
        f'netsh interface ipv4 set address name="{interface}" dhcp',
        f'netsh interface ipv4 set dns name="{interface}" dhcp'
    ]
    for cmd in cmds:
        run_command(cmd)
    messagebox.showinfo("Готово", "Интерфейс переведён на DHCP!")

# === Создание окна ===
app = tk.Tk()
app.title("Смена IP-адреса в Windows")
app.geometry("600x500")
app.resizable(False, False)

# === Ввод имени интерфейса ===
tk.Label(app, text="Имя интерфейса (например, Ethernet или Wi-Fi):").pack(pady=5)
interface_entry = tk.Entry(app, width=40)
interface_entry.pack(pady=5)

# === IP ===
tk.Label(app, text="IP-адрес (например, 192.168.1.100):").pack(pady=5)
ip_entry = tk.Entry(app, width=40)
ip_entry.pack(pady=5)

# === Маска подсети ===
tk.Label(app, text="Маска подсети (например, 255.255.255.0):").pack(pady=5)
mask_entry = tk.Entry(app, width=40)
mask_entry.pack(pady=5)

# === Шлюз ===
tk.Label(app, text="Шлюз (например, 192.168.1.1):").pack(pady=5)
gateway_entry = tk.Entry(app, width=40)
gateway_entry.pack(pady=5)

# === Кнопки ===
btn_frame = tk.Frame(app)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Установить статический IP", command=set_static_ip, width=25).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Сбросить до DHCP", command=reset_to_dhcp, width=20).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Показать интерфейсы", command=list_interfaces, width=20).grid(row=0, column=2, padx=5)

# === Лог вывода ===
output_text = tk.Text(app, height=10, width=70, wrap=tk.WORD)
output_text.pack(pady=10)

# === Запуск приложения ===
app.mainloop()
