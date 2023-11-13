from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QScrollArea, QRadioButton
from logic_simple import SimpleInstruction, run_instructions_simple
from logic_no_overlap import NoOverlapInstruction, run_instructions_no_overlap

class ManualInputView(QWidget):
    def __init__(self, show_main_menu_callback):
        super().__init__()
        
        self.show_main_menu_callback = show_main_menu_callback
        self.state = 0
        self.simple_logic_array = []
        self.no_overlap_logic_array = []
        self.longest_input_string = 0
        self.instruction_inputs = {}
        
        self.manual_input_layout = QVBoxLayout()
        self.manual_input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.manual_input_layout_label = QLabel("<h2>Dados das Instrucoes</h2>")
        self.manual_input_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.manual_input_layout.addWidget(self.manual_input_layout_label)
        
        self.number_of_instructions_layout = QHBoxLayout()
        self.number_of_instructions_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.number_of_instructions_layout_label = QLabel("<h3>Quantidade de instrucoes</h3>")
        self.number_of_instructions_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_of_instructions_layout.addWidget(self.number_of_instructions_layout_label)
        
        self.number_of_instructions_layout_input = QLineEdit()
        self.number_of_instructions_layout_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_of_instructions_layout_input.setPlaceholderText("Insira a quantidade de instrucoes")
        self.number_of_instructions_layout.addWidget(self.number_of_instructions_layout_input)
        
        self.manual_input_layout.addLayout(self.number_of_instructions_layout)
        
        
        self.instructions_layout = QVBoxLayout()
        self.instructions_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.instructions_layout_label = QLabel("<h2>Instrucoes</h2>")
        self.instructions_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.instructions_layout.addWidget(self.instructions_layout_label)
        self.manual_input_layout.addLayout(self.instructions_layout)
        
        # rules_layout items start invisible
        for i in range(self.instructions_layout.count()):
            item = self.instructions_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
        
        
        self.time_limit_layout = QHBoxLayout()
        self.time_limit_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)        
        
        self.time_limit_layout_label = QLabel("<h3>Quantidade de tempo</h3>")
        self.time_limit_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_limit_layout.addWidget(self.time_limit_layout_label)
        
        self.time_limit_layout_input = QLineEdit()
        self.time_limit_layout_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_limit_layout_input.setPlaceholderText("Insira a quantidade de tempo")
        self.time_limit_layout.addWidget(self.time_limit_layout_input)
        
        self.manual_input_layout.addLayout(self.time_limit_layout)
        
        # alphabet_layout items start invisible
        for i in range(self.time_limit_layout.count()):
            item = self.time_limit_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
                
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
        
        
        self.manual_input_layout.addLayout(self.output_layout)
        
        # output_layout items start invisible
        for i in range(self.output_layout.count()):
            item = self.output_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
        ## Footer
        self.continue_button_layout = QHBoxLayout()
        self.continue_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_script_validate_input = (QPushButton("Continuar"))
        self.button_script_validate_input.clicked.connect(self.validate_input)
        self.continue_button_layout.addWidget(self.button_script_validate_input)
        self.manual_input_layout.addLayout(self.continue_button_layout)
        
        self.simple_or_complex_radio_layout = QHBoxLayout()
        self.simple_or_complex_radio_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.simple_or_complex_radio = QRadioButton("Permitir Overlap?")
        self.simple_or_complex_radio.setChecked(True)
        self.simple_or_complex_radio.setVisible(False)
        self.simple_or_complex_radio_layout.addWidget(self.simple_or_complex_radio)
        self.manual_input_layout.addLayout(self.simple_or_complex_radio_layout)
        
        self.choices_bottom = QHBoxLayout()
        self.choices_bottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_script_show_options_menu = (QPushButton("Resetar"))
        self.button_script_show_options_menu.clicked.connect(self.reset)
        self.choices_bottom.addWidget(self.button_script_show_options_menu)
        self.manual_input_layout.addLayout(self.choices_bottom)
        
        self.back_button_layout = QHBoxLayout()
        self.back_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.manual_input_layout_back_button = (QPushButton("Voltar"))
        self.manual_input_layout_back_button.clicked.connect(self.show_main_menu_callback)
        self.back_button_layout.addWidget(self.manual_input_layout_back_button)
        self.manual_input_layout.addLayout(self.back_button_layout)
        
        
        self.scroll_container_layout = QVBoxLayout()
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        scroll_content.setLayout(self.manual_input_layout)
        
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
        
    def validate_value(self, value, instruction_number):
        if not self.is_integer(value):
            QMessageBox.warning(self, "Valor invalido!", f"Por favor, insira um valor numerico para a instrucao {str(instruction_number+1)}.")
            return False 
        elif not self.is_integer_float(value):
            QMessageBox.warning(self, "Valor invalido!", f"Por favor, insira um valor inteiro para a instrucao {str(instruction_number+1)}.")
            return False
        else:
            return True
    
    def validate_input(self):
        match self.state:
            case 0: 
                user_input = self.number_of_instructions_layout_input.text()
                
                if not self.is_integer(user_input):
                    QMessageBox.warning(self, "Valor invalido!", f"Por favor, insira um valor numerico.")
                    return
                elif not self.is_integer_float(user_input):
                    QMessageBox.warning(self, "Valor invalido!", f"Por favor, insira um valor inteiro.")
                    return
                else:
                    user_input = int(user_input)
                    
                self.number_of_instructions_layout_input.setDisabled(True)
                self.simple_logic_array = [SimpleInstruction() for _ in range(user_input)]
                self.no_overlap_logic_array = [NoOverlapInstruction() for _ in range(user_input)]
                self.state = 1
                
                for i in range(self.instructions_layout.count()):
                    item = self.instructions_layout.itemAt(i)

                    if isinstance(item.widget(), QWidget):
                        item.widget().setVisible(True)

                for i in range(user_input):
                    instruction_layout = QHBoxLayout()
                    instruction_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                    instruction_layout_label = QLabel("<h3>Instrucao " + str(i+1) + " - </h3>")
                    instruction_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    instruction_layout.addWidget(instruction_layout_label)
                    
                    instruction_layout_name_label = QLabel("Nome - ")
                    instruction_layout_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    instruction_layout.addWidget(instruction_layout_name_label)

                    instruction_layout_name_input = QLineEdit()
                    instruction_layout_name_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    instruction_layout_name_input.setPlaceholderText(f"Insira o nome da instrucao {str(i+1)}")
                    instruction_layout.addWidget(instruction_layout_name_input)
                    
                    instruction_layout_time_label = QLabel("Unidades de Tempo - ")
                    instruction_layout_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    instruction_layout.addWidget(instruction_layout_time_label)

                    instruction_layout_time_input = QLineEdit()
                    instruction_layout_time_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    instruction_layout_time_input.setPlaceholderText(f"Insira o tempo necessario para executar a instrucao {str(i+1)}")
                    instruction_layout.addWidget(instruction_layout_time_input)

                    self.instructions_layout.addLayout(instruction_layout)
                    
                    self.instruction_inputs[i] = (instruction_layout_name_input, instruction_layout_time_input)
                    
            case 1:
                valid_input = True
                self.longest_input_string = 0
                current_index = 0
                
                for i, (instruction_layout_name_input, instruction_layout_time_input) in self.instruction_inputs.items():
                    instruction_name = instruction_layout_name_input.text()
                    instruction_time = instruction_layout_time_input.text()
                    
                    if(not instruction_name):
                        QMessageBox.warning(self, "Campo Vazio", f"Campo vazio detectado para a instrucao {str(i+1)}.")
                        valid_input = False
                        break
                    
                    if (not self.validate_value(instruction_time, i)):
                        valid_input = False
                        break
                    else:
                        instruction_time = int(instruction_time)
                        
                    if(len(instruction_name) > self.longest_input_string):
                        self.longest_input_string = len(instruction_name)
                    
                    self.simple_logic_array[i].set_name(instruction_name)
                    self.simple_logic_array[i].set_size(instruction_time)
                    
                    self.no_overlap_logic_array[i].set_name(instruction_name)
                    tempSize = instruction_time
                    self.no_overlap_logic_array[i].set_size(tempSize)
                    self.no_overlap_logic_array[i].set_starting_index(current_index)
                    current_index += (tempSize - 1)
                    self.no_overlap_logic_array[i].set_ending_index(current_index)
                    current_index += 1
                
                if valid_input:
                    self.state = 2
                    
                    for i, (instruction_layout_name_input, instruction_layout_time_input) in self.instruction_inputs.items():
                        instruction_layout_name_input.setDisabled(True)
                        instruction_layout_time_input.setDisabled(True)
                        
                    for i in range(self.time_limit_layout.count()):
                        item = self.time_limit_layout.itemAt(i)

                        if isinstance(item.widget(), QWidget):
                            item.widget().setVisible(True)
                            
                    self.button_script_validate_input.setText("Gerar pipeline")
                    self.simple_or_complex_radio.setVisible(True)
                            
                else:
                    self.simple_logic_array = []
                    self.no_overlap_logic_array = []
                    self.simple_logic_array = [SimpleInstruction() for _ in range(user_input)]
                    self.no_overlap_logic_array = [NoOverlapInstruction() for _ in range(user_input)]
                            
            case 2:
                user_input = self.time_limit_layout_input.text()
                
                if not self.is_integer(user_input):
                    QMessageBox.warning(self, "Valor invalido!", f"Por favor, insira um valor numerico.")
                    return
                elif not self.is_integer_float(user_input):
                    QMessageBox.warning(self, "Valor invalido!", f"Por favor, insira um valor inteiro.")
                    return
                else:
                    user_input = int(user_input)
                
                if(self.simple_or_complex_radio.isChecked() == True):
                    result, loops = run_instructions_simple(self.simple_logic_array, user_input, self.longest_input_string)
                else:
                    result, loops = run_instructions_no_overlap(self.no_overlap_logic_array, user_input, self.longest_input_string)
                
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
        self.instruction_inputs.clear()
        
        self.number_of_instructions_layout_input.setText("")
        self.time_limit_layout_input.setText("")
        self.output_contents_layout_label.setText("")
        
        self.number_of_instructions_layout_input.setDisabled(False)
        self.time_limit_layout_input.setDisabled(False)
                
        while self.instructions_layout.count():
            layout_item = self.instructions_layout.takeAt(0)
            if layout_item:
                item_layout = layout_item.layout()
                if item_layout:
                    while item_layout.count():
                        item = item_layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()
                        else:
                            pass
                    item_layout.deleteLater()
                else:
                    widget = layout_item.widget()
                    if widget:
                        widget.deleteLater()
                                        
        self.instructions_layout_label = QLabel("<h2>Instrucoes</h2>")
        self.instructions_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.instructions_layout.addWidget(self.instructions_layout_label)
        self.manual_input_layout.addLayout(self.instructions_layout)
        
        for i in range(self.instructions_layout.count()):
            item = self.instructions_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
        for i in range(self.time_limit_layout.count()):
            item = self.time_limit_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
        for i in range(self.output_layout.count()):
            item = self.output_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
                
        self.button_script_validate_input.setText("Continuar")
        self.simple_or_complex_radio.setVisible(False)