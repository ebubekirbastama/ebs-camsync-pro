import os
import sys
import subprocess

# =========================
# OTOMATİK BAĞIMLILIK KURULUMU
# =========================

REQUIRED_PACKAGES = {
    "customtkinter": "customtkinter",
    "win10toast": "win10toast",
    "pystray": "pystray",
    "PIL": "Pillow"
}

def install_missing_packages():
    for import_name, pip_name in REQUIRED_PACKAGES.items():
        try:
            __import__(import_name)
        except ImportError:
            print(f"[i] Eksik paket yükleniyor: {pip_name}")
            subprocess.check_call([
                sys.executable,
                "-m",
                "pip",
                "install",
                pip_name
            ])

install_missing_packages()

import socket
import time
import ctypes
import threading
import customtkinter as ctk

from win10toast import ToastNotifier
from PIL import Image, ImageDraw
import pystray


PORT = 9999
SAVE_DIR = "Gelen_Resimler"
RULE_NAME = "EBS_Kamera_Sync_Rule"

os.makedirs(SAVE_DIR, exist_ok=True)
toaster = ToastNotifier()

DARK_METAL = "#1A1E29"
CARD_BG = "#242A38"
NEON_BLUE = "#0096FF"
SUCCESS_GREEN = "#00DCB4"
TEXT_MUTED = "#828C9B"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            " ".join(sys.argv),
            None,
            1
        )
        sys.exit(0)


def hide_console():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)


def check_and_open_firewall(log_callback):
    log_callback("[i] Windows Güvenlik Duvarı kontrol ediliyor...\n")
    try:
        check_cmd = f'netsh advfirewall firewall show rule name="{RULE_NAME}"'
        result = subprocess.run(
            check_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True
        )

        if (
            "no rules match" in result.stdout.lower()
            or "eşleşen kural yok" in result.stdout.lower()
            or result.returncode != 0
        ):
            log_callback(f"[+] {PORT} portu için kural ekleniyor...\n")
            add_cmd = f'netsh advfirewall firewall add rule name="{RULE_NAME}" dir=in action=allow protocol=TCP localport={PORT}'
            subprocess.run(add_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            log_callback("[✓] Güvenlik duvarı izni otomatik açıldı!\n")
        else:
            log_callback("[✓] Güvenlik duvarı izni zaten mevcut.\n")

    except Exception as e:
        log_callback(f"[X] Güvenlik duvarı ayarlanırken hata: {e}\n")


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def safe_filename(name):
    bad_chars = '<>:"/\\|?*'
    for ch in bad_chars:
        name = name.replace(ch, "_")
    return name


def create_tray_image():
    image = Image.new("RGB", (64, 64), "#1A1E29")
    draw = ImageDraw.Draw(image)
    draw.ellipse((10, 10, 54, 54), fill="#0096FF")
    draw.text((22, 22), "E", fill="white")
    return image


class EbsSyncGui(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")

        self.title("EBS Ultra Sync - PC Server Panel")
        self.geometry("750x620")
        self.minsize(700, 550)
        self.configure(fg_color=DARK_METAL)

        self.local_ip = get_local_ip()
        self.server_running = False
        self.tray_icon = None

        self.protocol("WM_DELETE_WINDOW", self.minimize_to_tray)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.create_widgets()

        threading.Thread(target=self.init_backend_services, daemon=True).start()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="EBS ULTRA SYNC",
            font=ctk.CTkFont(family="Arial", size=26, weight="bold"),
            text_color=NEON_BLUE
        )
        self.title_label.grid(row=0, column=0, padx=25, pady=(20, 2), sticky="w")

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Mobil Cihaz Fotoğraf Otomasyon Yönetim Paneli",
            font=ctk.CTkFont(size=13),
            text_color=TEXT_MUTED
        )
        self.subtitle_label.grid(row=1, column=0, padx=25, pady=(0, 15), sticky="w")

        self.card_frame = ctk.CTkFrame(
            self,
            fg_color=CARD_BG,
            corner_radius=15,
            border_width=1,
            border_color="#373D4B"
        )
        self.card_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.card_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.create_info_box(self.card_frame, "BİLGİSAYAR IP", self.local_ip, 0)
        self.create_info_box(self.card_frame, "DİNLENEN PORT", str(PORT), 1)

        self.status_frame = ctk.CTkFrame(self.card_frame, fg_color="transparent")
        self.status_frame.grid(row=0, column=2, padx=15, pady=15, sticky="nsew")

        self.status_title = ctk.CTkLabel(
            self.status_frame,
            text="SUNUCU DURUMU",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=TEXT_MUTED
        )
        self.status_title.pack(anchor="center", pady=(5, 0))

        self.status_badge = ctk.CTkLabel(
            self.status_frame,
            text="BAŞLATILIYOR",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#FFA500",
            fg_color="#3D2B00",
            corner_radius=8,
            width=130,
            height=32
        )
        self.status_badge.pack(anchor="center", pady=5)

        self.log_header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.log_header_frame.grid(row=3, column=0, padx=20, pady=(15, 0), sticky="ew")
        self.log_header_frame.grid_columnconfigure(0, weight=1)

        self.log_label = ctk.CTkLabel(
            self.log_header_frame,
            text="Canlı Aktivite Günlüğü",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=TEXT_MUTED
        )
        self.log_label.grid(row=0, column=0, sticky="w", padx=5)

        self.minimize_button = ctk.CTkButton(
            self.log_header_frame,
            text="Aşağı At",
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="#2D3343",
            hover_color=SUCCESS_GREEN,
            text_color="white",
            corner_radius=8,
            width=100,
            height=28,
            command=self.minimize_to_tray
        )
        self.minimize_button.grid(row=0, column=1, sticky="e", padx=5)

        self.clear_button = ctk.CTkButton(
            self.log_header_frame,
            text="Günlüğü Temizle",
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="#2D3343",
            hover_color=NEON_BLUE,
            text_color="white",
            corner_radius=8,
            width=120,
            height=28,
            command=self.clear_logs
        )
        self.clear_button.grid(row=0, column=2, sticky="e", padx=5)

        self.log_view = ctk.CTkTextbox(
            self,
            fg_color="#131722",
            border_width=1,
            border_color="#2D3343",
            font=ctk.CTkFont(family="Consolas", size=12),
            text_color="#E0E6ED",
            corner_radius=10
        )
        self.log_view.grid(row=4, column=0, padx=20, pady=(5, 15), sticky="nsew")

        self.progress_bar = ctk.CTkProgressBar(
            self,
            progress_color=NEON_BLUE,
            fg_color="#131722",
            height=10
        )
        self.progress_bar.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")
        self.progress_bar.set(0)

        self.footer_label = ctk.CTkLabel(
            self,
            text=f"Kayıt Klasörü: {os.path.abspath(SAVE_DIR)}",
            font=ctk.CTkFont(size=12),
            text_color=TEXT_MUTED
        )
        self.footer_label.grid(row=6, column=0, padx=25, pady=(0, 15), sticky="w")

    def create_info_box(self, parent, title, value, col):
        frame = ctk.CTkFrame(parent, fg_color="#1A1E29", corner_radius=10)
        frame.grid(row=0, column=col, padx=15, pady=15, sticky="nsew")

        lbl_title = ctk.CTkLabel(
            frame,
            text=title,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=TEXT_MUTED
        )
        lbl_title.pack(anchor="w", padx=15, pady=(8, 0))

        lbl_val = ctk.CTkLabel(
            frame,
            text=value,
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            text_color="white"
        )
        lbl_val.pack(anchor="w", padx=15, pady=(2, 8))

    def minimize_to_tray(self):
        self.withdraw()

        if self.tray_icon is None:
            menu = pystray.Menu(
                pystray.MenuItem("Paneli Aç", self.show_from_tray),
                pystray.MenuItem("Çıkış", self.exit_app)
            )

            self.tray_icon = pystray.Icon(
                "EBS Ultra Sync",
                create_tray_image(),
                "EBS Ultra Sync çalışıyor",
                menu
            )

            threading.Thread(target=self.tray_icon.run, daemon=True).start()

        try:
            toaster.show_toast(
                "EBS Ultra Sync",
                "Program sağ altta çalışmaya devam ediyor.",
                duration=3,
                threaded=True
            )
        except:
            pass

    def show_from_tray(self, icon=None, item=None):
        self.after(0, self.deiconify)
        self.after(0, self.lift)
        self.after(0, self.focus_force)

    def exit_app(self, icon=None, item=None):
        if self.tray_icon:
            self.tray_icon.stop()
        self.after(0, self.destroy)

    def write_log(self, text):
        self.after(0, lambda: self._write_log_safe(text))

    def _write_log_safe(self, text):
        self.log_view.insert("end", text)
        self.log_view.see("end")

    def clear_logs(self):
        self.log_view.delete("1.0", "end")
        self.write_log("[i] Günlük geçmişi temizlendi.\n")
        self.write_log("-" * 65 + "\n")

    def init_backend_services(self):
        check_and_open_firewall(self.write_log)
        threading.Thread(target=self.start_socket_server, daemon=True).start()

    def start_socket_server(self):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(("0.0.0.0", PORT))
            server.listen(20)

            self.server_running = True

            self.after(0, lambda: self.status_badge.configure(
                text="AKTİF / BEKLENİYOR",
                text_color=SUCCESS_GREEN,
                fg_color="#003D30"
            ))

            self.write_log(f"[✓] TCP Sunucu aktif edildi. Port: {PORT}\n")
            self.write_log("[i] Telefonda APK'yı açıp bu PC'nin IP adresini girerek fotoğrafları yollayabilirsiniz.\n")
            self.write_log("-" * 65 + "\n")

            try:
                toaster.show_toast(
                    "EBS Ultra Sync",
                    "Alıcı Panel Aktif!\nBağlantı bekleniyor...",
                    duration=4,
                    threaded=True
                )
            except:
                pass

            while True:
                conn, addr = server.accept()
                self.write_log(f"[+] Telefon Bağlandı -> {addr[0]}:{addr[1]}\n")
                threading.Thread(target=self.handle_client, args=(conn,), daemon=True).start()

        except Exception as e:
            self.after(0, lambda: self.status_badge.configure(
                text="HATA OLUŞTU",
                text_color="#FF4D4D",
                fg_color="#3D0000"
            ))
            self.write_log(f"[X] Sunucu başlatılamadı: {e}\n")

    def handle_client(self, conn):
        conn.settimeout(15.0)

        try:
            header_data = b""

            while b"\n" not in header_data:
                chunk = conn.recv(1)
                if not chunk:
                    break
                header_data += chunk

            if not header_data:
                return

            header_str = header_data.decode("utf-8").strip()

            if "|" not in header_str:
                self.write_log("[-] Geçersiz başlık formatı alındı.\n")
                return

            file_name_raw, file_size_str = header_str.split("|")
            file_name = safe_filename(file_name_raw)
            file_size = int(file_size_str)

            self.write_log(f"[i] Dosya Alınıyor: {file_name} ({file_size} Byte)\n")

            conn.sendall(b"OK")

            save_path = os.path.join(SAVE_DIR, file_name)

            if os.path.exists(save_path):
                base, ext = os.path.splitext(file_name)
                save_path = os.path.join(SAVE_DIR, f"{base}_{int(time.time())}{ext}")

            received = 0

            with open(save_path, "wb") as f:
                while received < file_size:
                    chunk = conn.recv(min(16384, file_size - received))
                    if not chunk:
                        break

                    f.write(chunk)
                    received += len(chunk)

                    percent = received / file_size
                    self.after(0, lambda p=percent: self.progress_bar.set(p))

            if received == file_size:
                self.write_log(f"[✓] Kaydedildi: {os.path.basename(save_path)}\n")

                try:
                    toaster.show_toast(
                        "EBS Ultra Sync",
                        f"Yeni Fotoğraf Geldi:\n{file_name}",
                        duration=3,
                        threaded=True
                    )
                except:
                    pass
            else:
                self.write_log(f"[X] Eksik veri alındı! {received}/{file_size}\n")

            self.write_log("-" * 65 + "\n")
            self.after(0, lambda: self.progress_bar.set(0))

        except Exception as e:
            self.write_log(f"[X] Akış hatası: {e}\n")

        finally:
            try:
                conn.close()
            except:
                pass


if __name__ == "__main__":
    run_as_admin()
    hide_console()
    app = EbsSyncGui()
    app.mainloop()
