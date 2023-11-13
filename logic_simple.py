class SimpleInstruction:
    def __init__(self):
        self.name = ""
        self.size = 0

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def set_name(self, name):
        self.name = name

    def set_size(self, size):
        self.size = size
        
def run_instructions_simple(instructions_array, cycles, longest_instruction_string):
    log = []
    number_of_instructions = len(instructions_array)
    
    spaces = ""   
    for i in range(longest_instruction_string):
        spaces += " "
    
    loops = 0
    
    while True:
        current_index = 0
        times_printed = 0
        iteration_string = ""
        
        for i in range(cycles):
            if(i < loops):
                iteration_string += "X" + spaces
            else:
                if(current_index < number_of_instructions):
                    if(times_printed < instructions_array[current_index].get_size()):
                        iteration_string += (instructions_array[current_index].get_name() + spaces)
                        times_printed += 1
                    else:
                        times_printed = 0
                        current_index += 1
                        if(current_index < number_of_instructions):
                            iteration_string += (instructions_array[current_index].get_name() + spaces)
                            times_printed += 1
                        else:
                            iteration_string += "X" + spaces
                else:
                    iteration_string += "X" + spaces
                    
        if(current_index < number_of_instructions):
            break
        
        loops += 1
        
        log.append(iteration_string)

    return log, loops