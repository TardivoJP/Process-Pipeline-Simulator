from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QScrollArea, QRadioButton, QTextEdit
from logic_simple import SimpleInstruction, run_instructions_simple
from logic_no_overlap import NoOverlapInstruction, run_instructions_no_overlap

class FileInputView(QWidget):
    def __init__(self, show_main_menu_callback):
        super().__init__()
        
        self.show_main_menu_callback = show_main_menu_callback
        self.simple_logic_array = []
        self.no_overlap_logic_array = []
        self.longest_input_string = 0
        self.time_limit = 0
        
        self.file_input_layout = QVBoxLayout()
        self.file_input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        self.file_input_layout_label = QLabel("<h2>Dados das Instrucoes</h2>")
        self.file_input_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_input_layout.addWidget(self.file_input_layout_label)
        
        self.text_input = QTextEdit()
        self.text_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_input.setPlaceholderText("Cole aqui os dados das instrucoes")
        self.file_input_layout.addWidget(self.text_input)
        
                
        self.output_layout = QVBoxLayout()
        self.output_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.output_layout_label = QLabel("<h2>Pipeline de Instrucoes Gerado</h2>")
        self.output_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_layout.addWidget(self.output_layout_label)
        
        self.output_contents_layout = QHBoxLayout()
        self.output_contents_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.output_contents_layout_label = QLabel("")
        self.output_contents_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_contents_layout.addWidget(self.output_contents_layout_label)

        self.output_layout.addLayout(self.output_contents_layout)
        
        
        self.file_input_layout.addLayout(self.output_layout)
        
        # output_layout items start invisible
        for i in range(self.output_layout.count()):
            item = self.output_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
        ## Footer
        self.continue_button_layout = QHBoxLayout()
        self.continue_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_script_validate_input = (QPushButton("Gerar pipeline"))
        self.button_script_validate_input.clicked.connect(self.validate_input)
        self.continue_button_layout.addWidget(self.button_script_validate_input)
        self.file_input_layout.addLayout(self.continue_button_layout)
        
        self.simple_or_complex_radio_layout = QHBoxLayout()
        self.simple_or_complex_radio_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.simple_or_complex_radio = QRadioButton("Permitir Overlap?")
        self.simple_or_complex_radio.setChecked(True)
        self.simple_or_complex_radio_layout.addWidget(self.simple_or_complex_radio)
        self.file_input_layout.addLayout(self.simple_or_complex_radio_layout)
        
        self.choices_bottom = QHBoxLayout()
        self.choices_bottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_script_show_options_menu = (QPushButton("Resetar"))
        self.button_script_show_options_menu.clicked.connect(self.reset)
        self.choices_bottom.addWidget(self.button_script_show_options_menu)
        self.file_input_layout.addLayout(self.choices_bottom)
        
        self.back_button_layout = QHBoxLayout()
        self.back_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_input_layout_back_button = (QPushButton("Voltar"))
        self.file_input_layout_back_button.clicked.connect(self.show_main_menu_callback)
        self.back_button_layout.addWidget(self.file_input_layout_back_button)
        self.file_input_layout.addLayout(self.back_button_layout)
        
        
        self.scroll_container_layout = QVBoxLayout()
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        scroll_content.setLayout(self.file_input_layout)
        
        scroll_area.setWidget(scroll_content)
        
        self.scroll_container_layout.addWidget(scroll_area)
        
        
        self.setLayout(self.scroll_container_layout)
        
    def is_integer(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False 
        
    def is_integer_float(self, value):
        try:
            float_value = float(value)
            int_value = int(float_value)
            return float_value == int_value
        except (ValueError, TypeError):
            return False
        
    def validate_value(self, value, instruction):
        if not self.is_integer(value):
            QMessageBox.warning(self, "Valor invalido!", f"Por favor, insira um valor numerico para a instrucao '{instruction}'.")
            return False 
        elif not self.is_integer_float(value):
            QMessageBox.warning(self, "Valor invalido!", f"Por favor, insira um valor inteiro para a instrucao '{instruction}'.")
            return False
        else:
            return True
    
    def validate_input(self):
        raw_text_input = self.text_input.toPlainText()
        lines = raw_text_input.split('\n')
        current_index = 0
        self.longest_input_string = 0
        self.time_limit = 0
        self.simple_logic_array = []
        self.no_overlap_logic_array = []
        
        for line in lines:
            parts = line.split(',')
            if len(parts) == 2:
                instruction, value = parts
                
                if(not instruction):
                    QMessageBox.warning(self, "Campo Vazio", f"Campo vazio detectado para uma instrucao.")
                    return
                
                if(not self.validate_value(value, instruction)):
                    return
                else:
                    simple_instruction = SimpleInstruction()
                    no_overlap_instruction = NoOverlapInstruction()
                    
                    if(len(instruction) > self.longest_input_string):
                        self.longest_input_string = len(instruction)
                    
                    simple_instruction.set_name(instruction)
                    simple_instruction.set_size(int(value))
                    
                    no_overlap_instruction.set_name(instruction)
                    tempSize = int(value)
                    no_overlap_instruction.set_size(tempSize)
                    no_overlap_instruction.set_starting_index(current_index)
                    current_index += (tempSize - 1)
                    no_overlap_instruction.set_ending_index(current_index)
                    current_index += 1
                    
                    self.simple_logic_array.append(simple_instruction)
                    self.no_overlap_logic_array.append(no_overlap_instruction)
            else:
                if not self.is_integer(line):
                    QMessageBox.warning(self, "Valor invalido!", f"Por favor, insira um valor numerico para a quantidade de tempo.")
                    return
                elif not self.is_integer_float(line):
                    QMessageBox.warning(self, "Valor invalido!", f"Por favor, insira um valor inteiro para a quantidade de tempo.")
                    return
                else:
                    self.time_limit = int(line)
                    
        if(self.simple_or_complex_radio.isChecked() == True):
            result, loops = run_instructions_simple(self.simple_logic_array, self.time_limit, self.longest_input_string)
        else:
            result, loops = run_instructions_no_overlap(self.no_overlap_logic_array, self.time_limit, self.longest_input_string)
        
        result.append(f"=====================================================")    
        result.append(f"Total de instrucoes - {loops}")
        
        for i in range(self.output_layout.count()):
            item = self.output_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(True)
                
        self.output_contents_layout_label.setText('\n'.join(result))
                           
    def reset(self):
        self.state = 0
        self.simple_logic_array = []
        self.no_overlap_logic_array = []
        self.longest_input_string = 0
        
        self.text_input.setText("")
        self.output_contents_layout_label.setText("")
                
        for i in range(self.output_layout.count()):
            item = self.output_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)