import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import subprocess
import threading
import sys
import random
import time

# Variabili globali
processes = []
fake_threads = []

def start_test():
    target = entry_target.get()
    duration = entry_duration.get()
    concurrency = entry_concurrency.get()
    payload = "10KB"  # Imposta SEMPRE 10KB

    if not target:
        messagebox.showerror("Errore", "Inserisci un URL o IP valido.")
        return

    cmd = [
        sys.executable, "stress_core.py",
        target,
        "-d", duration,
        "-c", concurrency,
        "--payload-size", payload,    # Non più variabile, sempre 10KB
        "--log-level", "INFO"
    ]

    def run():
        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            processes.append(process)

            t2 = threading.Thread(target=lambda: fake_log(output_box_fake2), daemon=True)
            t3 = threading.Thread(target=lambda: fake_log(output_box_fake3), daemon=True)
            t2.start()
            t3.start()
            fake_threads.extend([t2, t3])

            for line in iter(process.stdout.readline, ''):
                output_box_main.insert(tk.END, line)
                output_box_main.see(tk.END)
            process.stdout.close()
        except Exception as e:
            output_box_main.insert(tk.END, f"Errore: {e}\n")
            output_box_main.see(tk.END)

    threading.Thread(target=run, daemon=True).start()

def fake_log(box):
    fake_msgs = [
        lambda: f"Inviata richiesta a {entry_target.get()}...",
        lambda: f"Ping risposta: {random.randint(30, 300)}ms",
        lambda: "Timeout dalla destinazione...",
        lambda: f"Connessione stabilita con {entry_target.get()}",
        lambda: f"Inviata sequenza dati di 10KB",    # Sempre 10KB
        lambda: "Connessione chiusa dal server.",
    ]
    while any(p.poll() is None for p in processes):
        time.sleep(random.uniform(0.4, 1.3))
        box.insert(tk.END, random.choice(fake_msgs)() + "\n")
        box.see(tk.END)

def stop_test():
    for p in processes:
        if p.poll() is None:
            p.terminate()
    output_box_main.insert(tk.END, "Test interrotto manualmente.\n")
    output_box_main.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("APOCALYPSE RED")
root.geometry("850x900")
root.configure(bg="#0d0d0d")

font_label = ("OCR A Extended", 11, "bold")
font_input = ("Consolas", 11)
font_title = ("OCR A Extended", 25, "bold")

tk.Label(root, text="A P O C A L Y P S E", font=font_title, fg="red", bg="#0d0d0d").pack(pady=10)

# Input frame
frame_options = tk.Frame(root, bg="#0d0d0d", highlightbackground="red", highlightthickness=2, padx=10, pady=10)
frame_options.pack(pady=10, fill="x", padx=20)

def add_entry(label_text, default=""):
    tk.Label(frame_options, text=label_text, font=font_label, fg="white", bg="#0d0d0d").pack(anchor="w")
    e = tk.Entry(frame_options, font=font_input, fg="red", bg="black", insertbackground="red", width=50)
    if default:
        e.insert(0, default)
    e.pack(pady=2)
    return e

entry_target = add_entry("Target URL o IP:")
entry_duration = add_entry("Durata (s):", "60")
entry_concurrency = add_entry("Concorrenza:", "2000")
# RIMOSSO il campo Payload Size

# Console frame
frame_dos = tk.Frame(root, bg="#0d0d0d")
frame_dos.pack(pady=10)

def create_fake_dos(title):
    box = scrolledtext.ScrolledText(frame_dos, height=10, width=40, bg="black", fg="green", font=("Consolas", 9),
                                    insertbackground="green", highlightbackground="red", highlightthickness=1)
    box.insert(tk.END, f"{title}\nIn attesa di avvio...\n")
    box.pack(side=tk.LEFT, padx=10)
    return box

output_box_main = create_fake_dos("DOS Console #1")
output_box_fake2 = create_fake_dos("DOS Console #2")
output_box_fake3 = create_fake_dos("DOS Console #3")

# Pulsanti
button_frame = tk.Frame(root, bg="#0d0d0d")
button_frame.pack(pady=20)

def hover(e, color): e.widget.config(bg=color)

btn_start = tk.Button(button_frame, text="START", command=start_test, font=font_label,
                      fg="white", bg="red", width=20, height=2)
btn_start.pack(side=tk.LEFT, padx=20)
btn_start.bind("<Enter>", lambda e: hover(e, "#cc0000"))
btn_start.bind("<Leave>", lambda e: hover(e, "red"))

btn_stop = tk.Button(button_frame, text="STOP", command=stop_test, font=font_label,
                     fg="white", bg="grey", width=20, height=2)
btn_stop.pack(side=tk.LEFT, padx=20)

root.mainloop()
