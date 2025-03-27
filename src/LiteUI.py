import webview
import json

class LiteUi:
    def __init__(self, title="My App", width=800, height=600, theme=None):
        self.title = title
        self.width = width
        self.height = height
        self.elements = []
        self.callbacks = {}
        self.tabs = {}
        self.current_tab = None
        self.theme = theme or {
            'background': '#ffffff',
            'text': '#000000',
            'primary': '#007bff',
            'secondary': '#6c757d',
            'accent': '#28a745'
        }
        
    def create_tab(self, tab_name):
        if tab_name not in self.tabs:
            self.tabs[tab_name] = []
            if self.current_tab is None:
                self.current_tab = tab_name
        return tab_name
        
    def set_current_tab(self, tab_name):
        if tab_name in self.tabs:
            self.current_tab = tab_name
            
    def add_element_to_tab(self, tab_name, element):
        if tab_name in self.tabs:
            self.tabs[tab_name].append(element)
            
    def create_window(self):
        html = self._generate_html()
        self.window = webview.create_window(self.title, html=html, width=self.width, height=self.height)
        self.window.expose(self.handle_event)
        webview.start()

    def add_button(self, text, callback, tab_name=None):
        element_id = f"button_{len(self.elements)}"
        element = {
            'type': 'button',
            'id': element_id,
            'text': text
        }
        self.elements.append(element)
        self.callbacks[element_id] = callback
        if tab_name:
            self.add_element_to_tab(tab_name, element)
        return element_id

    def add_slider(self, min_value=0, max_value=100, default=50, tab_name=None):
        element_id = f"slider_{len(self.elements)}"
        element = {
            'type': 'slider',
            'id': element_id,
            'min': min_value,
            'max': max_value,
            'value': default
        }
        self.elements.append(element)
        if tab_name:
            self.add_element_to_tab(tab_name, element)
        return element_id

    def add_textbox(self, placeholder="Enter text...", tab_name=None):
        element_id = f"textbox_{len(self.elements)}"
        element = {
            'type': 'textbox',
            'id': element_id,
            'placeholder': placeholder
        }
        self.elements.append(element)
        if tab_name:
            self.add_element_to_tab(tab_name, element)
        return element_id

    def add_dropdown(self, options, tab_name=None):
        element_id = f"dropdown_{len(self.elements)}"
        element = {
            'type': 'dropdown',
            'id': element_id,
            'options': options
        }
        self.elements.append(element)
        if tab_name:
            self.add_element_to_tab(tab_name, element)
        return element_id

    def handle_event(self, element_id, value):
        if element_id in self.callbacks:
            self.callbacks[element_id](value)

    def _generate_html(self):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    transition: all 0.3s ease;
                }}
                
                body {{ 
                    font-family: 'Segoe UI', Arial, sans-serif;
                    padding: 20px;
                    background-color: {self.theme['background']};
                    color: {self.theme['text']};
                    line-height: 1.6;
                }}
                
                .ui-element {{ 
                    margin: 15px 0;
                    opacity: 0;
                    animation: fadeIn 0.5s forwards;
                }}
                
                @keyframes fadeIn {{
                    from {{ opacity: 0; transform: translateY(10px); }}
                    to {{ opacity: 1; transform: translateY(0); }}
                }}
                
                .tab-nav {{ 
                    display: flex;
                    margin-bottom: 25px;
                    border-bottom: 2px solid {self.theme['secondary']}40;
                    padding: 0 10px;
                    gap: 10px;
                }}
                
                .tab-button {{
                    padding: 12px 24px;
                    border: none;
                    background-color: transparent;
                    color: {self.theme['text']};
                    cursor: pointer;
                    font-weight: 500;
                    position: relative;
                    overflow: hidden;
                }}
                
                .tab-button:before {{
                    content: '';
                    position: absolute;
                    bottom: 0;
                    left: 50%;
                    transform: translateX(-50%);
                    width: 0;
                    height: 3px;
                    background-color: {self.theme['primary']};
                    transition: width 0.3s ease;
                }}
                
                .tab-button:hover:before {{
                    width: 100%;
                }}
                
                .tab-button.active {{
                    color: {self.theme['primary']};
                }}
                
                .tab-button.active:before {{
                    width: 100%;
                }}
                
                .tab-content {{
                    display: none;
                    padding: 25px;
                    border-radius: 8px;
                    background-color: {self.theme['background']}80;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    opacity: 0;
                    transform: translateY(10px);
                }}
                
                .tab-content.active {{
                    display: block;
                    animation: slideIn 0.3s forwards;
                }}
                
                @keyframes slideIn {{
                    to {{
                        opacity: 1;
                        transform: translateY(0);
                    }}
                }}
                
                button {{ 
                    padding: 10px 20px;
                    cursor: pointer;
                    background-color: {self.theme['primary']};
                    color: white;
                    border: none;
                    border-radius: 6px;
                    font-weight: 500;
                    box-shadow: 0 2px 4px {self.theme['primary']}40;
                }}
                
                button:hover {{
                    transform: translateY(-2px);
                    box-shadow: 0 4px 8px {self.theme['primary']}60;
                }}
                
                button:active {{
                    transform: translateY(0);
                }}
                
                select {{ 
                    padding: 10px;
                    width: 200px;
                    border: 2px solid {self.theme['secondary']}40;
                    border-radius: 6px;
                    background-color: {self.theme['background']};
                    color: {self.theme['text']};
                    cursor: pointer;
                }}
                
                select:focus {{
                    border-color: {self.theme['primary']};
                    outline: none;
                }}
                
                input[type="text"] {{ 
                    padding: 10px;
                    width: 200px;
                    border: 2px solid {self.theme['secondary']}40;
                    border-radius: 6px;
                    background-color: {self.theme['background']};
                    color: {self.theme['text']};
                }}
                
                input[type="text"]:focus {{
                    border-color: {self.theme['primary']};
                    outline: none;
                    box-shadow: 0 0 0 3px {self.theme['primary']}20;
                }}
                
                input[type="range"] {{ 
                    width: 200px;
                    height: 6px;
                    -webkit-appearance: none;
                    background: {self.theme['secondary']}40;
                    border-radius: 3px;
                    outline: none;
                }}
                
                input[type="range"]::-webkit-slider-thumb {{
                    -webkit-appearance: none;
                    width: 18px;
                    height: 18px;
                    background: {self.theme['accent']};
                    border-radius: 50%;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                    transition: all 0.2s ease;
                }}
                
                input[type="range"]::-webkit-slider-thumb:hover {{
                    transform: scale(1.1);
                }}
            </style>
            <script>
                function switchTab(tabName) {{
                    var tabs = document.querySelectorAll('.tab-content');
                    var buttons = document.querySelectorAll('.tab-button');
                    
                    tabs.forEach(tab => {{
                        tab.classList.remove('active');
                    }});
                    
                    buttons.forEach(button => {{
                        button.classList.remove('active');
                    }});
                    
                    document.getElementById('tab-' + tabName).classList.add('active');
                    document.getElementById('btn-' + tabName).classList.add('active');
                    pywebview.api.handle_event('tab_switch', tabName);
                }}

                // Add stagger effect to elements
                document.addEventListener('DOMContentLoaded', function() {{
                    const elements = document.querySelectorAll('.ui-element');
                    elements.forEach((el, index) => {{
                        el.style.animationDelay = `${{index * 0.1}}s`;
                    }});
                }});
            </script>
        </head>
        <body>
            <div class="tab-nav">
        """
        
        # Generate tab buttons
        for tab_name in self.tabs.keys():
            is_active = 'active' if tab_name == self.current_tab else ''
            html += f'''
                <button id="btn-{tab_name}" class="tab-button {is_active}" 
                    onclick="switchTab('{tab_name}')">{tab_name}</button>
            '''
            
        html += '</div>'
        
        # Generate tab contents
        for tab_name, tab_elements in self.tabs.items():
            is_active = 'active' if tab_name == self.current_tab else ''
            html += f'<div id="tab-{tab_name}" class="tab-content {is_active}">'
            
            for element in tab_elements:
                html += self._generate_element_html(element)
                
            html += '</div>'
        
        html += """
        </body>
        </html>
        """
        return html

    def _generate_element_html(self, element):
        html = f'<div class="ui-element">'
        
        if element['type'] == 'button':
            html += f'<button onclick="pywebview.api.handle_event(\'{element["id"]}\', \'click\')">{element["text"]}</button>'
        
        elif element['type'] == 'slider':
            html += f'''
            <input type="range" id="{element["id"]}" min="{element["min"]}" max="{element["max"]}" 
            value="{element["value"]}" oninput="pywebview.api.handle_event('{element["id"]}', this.value)">
            '''
        
        elif element['type'] == 'textbox':
            html += f'''
            <input type="text" id="{element["id"]}" placeholder="{element["placeholder"]}"
            onchange="pywebview.api.handle_event('{element["id"]}', this.value)">
            '''
        
        elif element['type'] == 'dropdown':
            html += f'<select onchange="pywebview.api.handle_event(\'{element["id"]}\', this.value)">'
            for option in element['options']:
                html += f'<option value="{option}">{option}</option>'
            html += '</select>'
        
        html += '</div>'
        return html

__all__ = ['UILibrary']
