# 🌟 LiteUi - Lightweight UI for Python

LiteUi เป็นไลบรารี UI เบาๆ ที่ใช้ `pywebview` เพื่อสร้าง UI สำหรับ **Python** 🐍  
ใช้งานง่ายเหมือน **Roblox UI Library** 🎮 แต่สำหรับ **Python**  

> ✅ **รองรับ**: ปุ่ม, สไลเดอร์, ช่องกรอกข้อความ, Dropdown, และระบบแท็บ  
> 🎨 **รองรับธีม**: ปรับแต่งสี UI ได้ง่าย  

---

## 🚀 **ติดตั้ง**
ติดตั้ง LiteUi ผ่าน PyPI ได้ง่ายๆ  
```sh
pip install PyLiteUI
```

---

## 📌 **เริ่มต้นใช้งาน**
สร้าง UI ง่ายๆ ใน 3 บรรทัด  
```python
from LiteUi import LiteUi

ui = LiteUi("My First UI", 800, 600)
ui.create_window()
```

---

## 🎨 **ปรับแต่งธีม**
LiteUi รองรับ **Custom Theme** ให้คุณกำหนดสีเองได้!  
```python
custom_theme = {
    'background': '#1e1e1e',  # สีพื้นหลัง
    'text': '#ffffff',        # สีตัวหนังสือ
    'primary': '#ff4081',     # สีหลัก
    'secondary': '#03a9f4',   # สีรอง
    'accent': '#ffc107'       # สีเน้น
}

ui = LiteUi("Custom Theme Example", 800, 600, theme=custom_theme)
```

---

## 🛠 **องค์ประกอบ UI**
LiteUi มีองค์ประกอบหลักที่ช่วยให้คุณสร้าง UI ได้ง่าย 🔥  

### 🔱 **Button**
สร้างปุ่มง่ายๆ แล้วกำหนดฟังก์ชันให้มัน  
```python
def on_click(value):
    print("Button Pressed!")

ui.add_button("Click Me!", on_click, "Main")
```

### 🎚 **Slider**
เพิ่ม Slider เพื่อให้ผู้ใช้สามารถเลือกค่า  
```python
def slider_changed(value):
    print(f"Slider: {value}")

ui.add_slider(0, 100, 50, "Settings")
```

### 📝 **Textbox**
เพิ่มช่องให้ผู้ใช้กรอกข้อความ  
```python
def text_changed(value):
    print(f"User typed: {value}")

ui.add_textbox("Enter your name...", "General")
```

### 🗃 **Dropdown**
เพิ่ม Dropdown เลือกค่า  
```python
def dropdown_changed(value):
    print(f"Selected: {value}")

ui.add_dropdown(["Option 1", "Option 2", "Option 3"], "Settings")
```

---

## 🖥 **ตัวอย่างเต็ม**
```python
from LiteUi import LiteUi

def button_clicked(value):
    print("Button clicked!")

def slider_changed(value):
    print(f"Slider value: {value}")

def text_changed(value):
    print(f"Text entered: {value}")

def dropdown_changed(value):
    print(f"Selected option: {value}")

if __name__ == "__main__":
    custom_theme = {
        'background': '#f0f0f0',
        'text': '#333333',
        'primary': '#4CAF50',
        'secondary': '#2196F3',
        'accent': '#FF9800'
    }

    ui = LiteUi("Vinsenz example", 800, 600, theme=custom_theme)

    ui.create_tab("General")
    ui.create_tab("Settings")
    ui.create_tab("Advanced")

    ui.add_button("Click Me!", button_clicked, "General")
    ui.add_textbox("Enter your name...", "General")
    ui.add_slider(0, 100, 50, "Settings")
    ui.add_dropdown(["Option 1", "Option 2", "Option 3"], "Settings")
    ui.add_button("Advanced Action", button_clicked, "Advanced")
    ui.add_textbox("Advanced Configuration...", "Advanced")

    ui.create_window()
```

---

## ❓ **คำถามที่พบบ่อย**
### 🔹 รองรับ Windows, macOS, Linux ไหม?  
✅ รองรับทุก OS ที่มี **Python**  

### 🔹 จำเป็นต้องใช้ **PyQt** หรือ **Tkinter** ไหม?  
❌ ไม่ต้อง! LiteUi ใช้ **pywebview** เป็นพื้นฐาน  

### 🔹 สามารถใช้ LiteUi ทำแอป GUI ได้ไหม?  
✅ ได้แน่นอน!  

---

## 📜 **License**
LiteUi ใช้ **MIT License** ✅ คุณสามารถใช้ใน **โปรเจกต์ส่วนตัว & เชิงพาณิชย์** ได้  

---

## 📣 **ติดต่อ**
- 💬 **Feedback & Issues:** [GitHub](https://github.com/yourusername/LiteUi)  
- 👨‍💻 **Developer:** the_legoguys(Vinsenz Developer Team)  
- 📚 **License:** MIT  

---

**🔥 LiteUi - ทำให้ Python UI เป็นเรื่องง่าย! 🔥**

