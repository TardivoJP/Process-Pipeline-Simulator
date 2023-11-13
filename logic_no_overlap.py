class NoOverlapInstruction:
    def __init__(self):
        self.name = ""
        self.size = 0
        self.starting_index = 0
        self.ending_index = 0

    def increment_indexes(self):
        self.starting_index += self.size
        self.ending_index += self.size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_starting_index(self):
        return self.starting_index

    def get_ending_index(self):
        return self.ending_index

    def set_name(self, name):
        self.name = name

    def set_size(self, size):
        self.size = size

    def set_starting_index(self, starting_index):
        self.starting_index = starting_index

    def set_ending_index(self, ending_index):
        self.ending_index = ending_index

def run_instructions_no_overlap(instructions_array, cycles, longest_instruction_string):
    log = []
    number_of_instructions = len(instructions_array)
    
    spaces = ""   
    for i in range(longest_instruction_string):
        spaces += " "
        
    loops = 0
    
    while True:
        current_index = 0
        iteration_string = ""
        
        for i in range(cycles):
            if(current_index < number_of_instructions):
                if (instructions_array[current_index].get_starting_index() > cycles):
                    break
                
                if(i < instructions_array[current_index].get_starting_index()):
                    iteration_string += "X" + spaces
                else:
                    if(i <= instructions_array[current_index].get_ending_index()):
                        iteration_string += (instructions_array[current_index].get_name() + spaces)
                    else:
                        instructions_array[current_index].increment_indexes()
                        current_index += 1
                        
                        if(current_index < number_of_instructions):
                            if(instructions_array[current_index].get_starting_index() > cycles):
                                break
                            
                            if(i < instructions_array[current_index].get_starting_index()):
                                iteration_string += "X" + spaces
                            else:
                                iteration_string += (instructions_array[current_index].get_name() + spaces)
                        else:
                            iteration_string += "X" + spaces
            else:
                iteration_string += "X" + spaces
        
        if(current_index < number_of_instructions):
            break
        
        loops += 1
        
        log.append(iteration_string)
    
    return log, loops