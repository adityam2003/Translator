import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        self.translator = Translator()

        self.create_widgets()

    def create_widgets(self):
        # Source text
        self.src_text_label = tk.Label(self.root, text="Source Text")
        self.src_text_label.grid(row=0, column=0, padx=10, pady=10)
        self.src_text = tk.Text(self.root, height=10, width=50)
        self.src_text.grid(row=1, column=0, padx=10, pady=10)

        # Target text
        self.trg_text_label = tk.Label(self.root, text="Translated Text")
        self.trg_text_label.grid(row=0, column=1, padx=10, pady=10)
        self.trg_text = tk.Text(self.root, height=10, width=50)
        self.trg_text.grid(row=1, column=1, padx=10, pady=10)

        # Source language
        self.src_lang_label = tk.Label(self.root, text="Source Language")
        self.src_lang_label.grid(row=2, column=0, padx=10, pady=10)
        self.src_lang = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.src_lang.grid(row=3, column=0, padx=10, pady=10)
        self.src_lang.current(21)  # Default to English

        # Target language
        self.trg_lang_label = tk.Label(self.root, text="Target Language")
        self.trg_lang_label.grid(row=2, column=1, padx=10, pady=10)
        self.trg_lang = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.trg_lang.grid(row=3, column=1, padx=10, pady=10)
        self.trg_lang.current(22)  # Default to French

        # Translate button
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate)
        self.translate_button.grid(row=4, column=0, columnspan=2, pady=10)

    def translate(self):
        src_text = self.src_text.get("1.0", tk.END).strip()
        src_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(self.src_lang.get())]
        trg_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(self.trg_lang.get())]

        if src_text:
            translated = self.translator.translate(src_text, src=src_lang_code, dest=trg_lang_code)
            self.trg_text.delete("1.0", tk.END)
            self.trg_text.insert(tk.END, translated.text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
