import grpc
import chat_pb2
import chat_pb2_grpc
import proxy_pb2_grpc
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
import hashlib
import random

def rgb_to_hsl(r, g, b):
    """Convert RGB values (0-255) to HSL (0-1, 0-1, 0-1)"""
    r, g, b = r/255.0, g/255.0, b/255.0
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    h, s, l = 0, 0, (max_val + min_val)/2
    
    if max_val != min_val:
        d = max_val - min_val
        s = d/(2 - max_val - min_val) if l > 0.5 else d/(max_val + min_val)
        if max_val == r:
            h = (g - b)/d + (6 if g < b else 0)
        elif max_val == g:
            h = (b - r)/d + 2
        else:
            h = (r - g)/d + 4
        h /= 6
    return h, s, l

def hsl_to_rgb(h, s, l):
    """Convert HSL values (0-1, 0-1, 0-1) to RGB (0-255)"""
    def hue_to_rgb(p, q, t):
        t += 1 if t < 0 else (-1 if t > 1 else 0)
        if t < 1/6: return p + (q - p) * 6 * t
        if t < 1/2: return q
        if t < 2/3: return p + (q - p) * (2/3 - t) * 6
        return p
    
    if s == 0:
        r = g = b = l
    else:
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)
    
    return int(round(r * 255)), int(round(g * 255)), int(round(b * 255))

class ChatApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chat Application")
        self.root.geometry("300x300")

        # Username section
        tk.Label(self.root, text="Enter your name:").pack(pady=5)
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.generate_button = tk.Button(self.root, text="Generate Name", command=self.generate_name)
        self.generate_button.pack(pady=5)

        # Proxy server section
        tk.Label(self.root, text="Proxy Server (optional):").pack(pady=5)
        self.proxy_frame = tk.Frame(self.root)
        self.proxy_frame.pack(pady=5)
        
        self.proxy_entry = tk.Entry(self.proxy_frame, width=20)
        self.proxy_entry.pack(side=tk.LEFT, padx=2)
        self.proxy_entry.insert(0, "localhost")
        
        tk.Label(self.proxy_frame, text=":").pack(side=tk.LEFT)
        
        self.port_entry = tk.Entry(self.proxy_frame, width=6)
        self.port_entry.pack(side=tk.LEFT, padx=2)
        self.port_entry.insert(0, "50052")

        self.submit_button = tk.Button(self.root, text="Join Chat", command=self.submit_name)
        self.submit_button.pack(pady=10)

        self.root.mainloop()

    def generate_name(self):
        adjectives = ["Cool", "Funny", "Fast", "Happy", "Crazy", "Wild", "Silly", "Epic", "Awesome", "Mighty"]
        nouns = ["Tiger", "Panda", "Eagle", "Ninja", "Wizard", "Knight", "Pirate", "Robot", "Vampire", "Zombie"]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{random.choice(adjectives)}{random.choice(nouns)}{random.randint(100, 999)}")

    def submit_name(self):
        name = self.entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter a name")
            return

        proxy_address = self.proxy_entry.get().strip()
        port = self.port_entry.get().strip()
        
        # Validate port
        try:
            port = int(port)
            if not (1 <= port <= 65535):
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Port", "Please enter a valid port number (1-65535)")
            return
            
        # If proxy address is empty, use localhost
        if not proxy_address:
            proxy_address = "localhost"
            
        server_address = f"{proxy_address}:{port}"
        
        # Test connection before proceeding
        try:
            channel = grpc.insecure_channel(server_address)
            grpc.channel_ready_future(channel).result(timeout=5)  # 5 second timeout
            self.root.destroy()
            ChatClientGUI(name, server_address)
        except grpc.FutureTimeoutError:
            messagebox.showerror("Connection Failed", 
                               f"Could not connect to server at {server_address}\n"
                               "Please check the address and try again.")
        except Exception as e:
            messagebox.showerror("Connection Error", 
                               f"An error occurred while connecting:\n{str(e)}")

class ChatClientGUI:
    def __init__(self, name, proxy_address):
        self.name = name
        try:
            self.channel = grpc.insecure_channel(proxy_address)
            grpc.channel_ready_future(self.channel).result(timeout=5)  # Verify connection
            self.stub = proxy_pb2_grpc.ProxyServiceStub(self.channel)
            
            self.root = tk.Tk()
            self.root.title(f"Chat - {self.name}")
            self.root.geometry("400x500")

            self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state=tk.DISABLED)
            self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            self.entry = tk.Entry(self.root)
            self.entry.pack(padx=10, pady=5, fill=tk.X)
            self.entry.bind("<Return>", self.send_message)

            self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
            self.send_button.pack(pady=5)

            self.join_chat()
            threading.Thread(target=self.receive_messages, daemon=True).start()

            self.root.protocol("WM_DELETE_WINDOW", self.on_close)
            self.root.mainloop()
            
        except grpc.FutureTimeoutError:
            messagebox.showerror("Connection Failed", 
                               f"Lost connection to server at {proxy_address}")
            self.root.destroy() if hasattr(self, 'root') else None
            ChatApp()  # Return to login screen
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.root.destroy() if hasattr(self, 'root') else None
            ChatApp()  # Return to login screen

    def join_chat(self):
        response = self.stub.Join(chat_pb2.JoinRequest(name=self.name))
        self.append_message("System", response.welcome_message)

    def send_message(self, event=None):
        msg = self.entry.get().strip()
        if msg:
            try:
                self.stub.SendMessage(chat_pb2.Message(sender=self.name, content=msg))
                self.entry.delete(0, tk.END)
            except grpc.RpcError as e:
                messagebox.showerror("Send Error", f"Failed to send message: {e.details()}")
                self.root.destroy()
                ChatApp()  # Return to login screen

    def receive_messages(self):
        try:
            for message in self.stub.ReceiveMessages(chat_pb2.Empty()):
                self.append_message(message.sender, message.content)
        except grpc.RpcError as e:
            messagebox.showerror("Connection Error", f"Lost connection to server: {e.details()}")
            self.root.destroy()
            ChatApp()  # Return to login screen

    def append_message(self, sender, content):
        color = self.get_username_color(sender)
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, f"{sender}: ", color)
        self.text_area.insert(tk.END, f"{content}\n", "black")
        self.text_area.tag_config(color, foreground=color)
        self.text_area.config(state=tk.DISABLED)
        self.text_area.yview(tk.END)

    def get_username_color(self, username, dark_mode=False):
        """
        Generate a color for a username that has good contrast against dark or light backgrounds.
        
        Args:
            username (str): The username to generate a color for
            dark_mode (bool): Whether the background is dark (True) or light (False)
        
        Returns:
            str: Hex color code in format "#RRGGBB"
        """
        # Generate hash from username
        hash_val = hashlib.md5(username.encode()).hexdigest()
        
        # Extract RGB components
        r, g, b = int(hash_val[0:2], 16), int(hash_val[2:4], 16), int(hash_val[4:6], 16)
        
        if dark_mode:
            # For dark backgrounds, we want brighter colors (minimum brightness)
            # Convert to HSL and adjust lightness if needed
            h, s, l = rgb_to_hsl(r, g, b)
            if l < 0.65:  # If too dark for dark background
                l = 0.65
            r, g, b = hsl_to_rgb(h, s, l)
        else:
            # For light backgrounds, we want darker colors
            h, s, l = rgb_to_hsl(r, g, b)
            if l > 0.35:  # If too light for light background
                l = 0.35
            r, g, b = hsl_to_rgb(h, s, l)
        
        # Convert back to hex
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def on_close(self):
        self.root.quit()
        self.root.destroy()

if __name__ == '__main__':
    ChatApp()