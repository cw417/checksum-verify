import tkinter as tk
from tkinter import messagebox as mb
import subprocess

class ChecksumVerify(tk.Frame):
  def __init__(self, master=None, *args, **kwargs):
      super().__init__(master, **kwargs)
      self.init_window()

  def init_window(self):
      self.master.title("Checksum Verifier")

      # Settings for field size
      label_width = 20
      entry_width = 60
      button_width = label_width
      
      # Labels
      file_label = tk.Label(self, width=label_width, text="File path:")
      md5_label = tk.Label(self, width=label_width, text="MD5 hash:")
      sha1_label = tk.Label(self, width=label_width, text="SHA1 hash:")

      file_label.grid(row=0, column=0, sticky='w')
      md5_label.grid(row=1, column=0, sticky='w')
      sha1_label.grid(row=2, column=0, sticky='w')

      # Entry fields
      self.file_entry = tk.Entry(self, width=entry_width)
      self.md5_entry = tk.Entry(self, width=entry_width)
      self.sha1_entry = tk.Entry(self, width=entry_width)

      self.file_entry.grid(row=0, column=1)
      self.md5_entry.grid(row=1, column=1)
      self.sha1_entry.grid(row=2, column=1)

      # Buttons
      compare_button = tk.Button(self, width=button_width, text="Compare", command=lambda: [check_md5(), check_sha1()])
      compare_button.grid(row=3, column=0)

      # Functions
      def check_md5():
        # Generates MD5 hash and compares against given MD5 hash
        file_to_check = self.file_entry.get()
        md5_hash = self.md5_entry.get()
        output = subprocess.Popen(['fciv.exe','-md5', file_to_check], stdout=subprocess.PIPE).communicate()[0].split()
        output_sum = output[9].decode('utf-8')
        if output_sum == md5_hash:
          mb.showinfo("Results", "The MD5 checksums match!")
        else:
          mb.showinfo("Results", "WARNING: the MD5 checksums do NOT match.")

      def check_sha1():
        # Generates SHA1 hash and compares against given SHA1 hash
        file_to_check = self.file_entry.get()
        sha1_hash = self.sha1_entry.get()
        output = subprocess.Popen(['fciv.exe','-sha1', file_to_check], stdout=subprocess.PIPE).communicate()[0].split()
        output_sum = output[9].decode('utf-8')
        if output_sum == sha1_hash:
          mb.showinfo("Results", "The SHA1 checksums match!")
        else:
          mb.showinfo("Results", "WARNING: the SHA1 checksums do NOT match.")

root = tk.Tk()
app = ChecksumVerify(root)
app.pack(fill=tk.BOTH, expand=1)
root.mainloop()