class Transition:
    def __init__(self, write, turn, next_state):
        self.write = write
        self.turn = turn
        self.next_state = next_state
        

class State:
    def __init__(self, read_zero, read_one):
        self.read = {}
        self.read_zero = read_zero
        self.read_one = read_one
        

def apply_turn(orientation, turn):
    
    turn_to_angle = {
    'L': 90,  # 'L' corresponds to 90 degrees
    'R': -90, # 'R' corresponds to -90 degrees
    'N': 0,   # 'N' corresponds to 0 degrees
    'U': 180  # 'U' corresponds to 180 degrees
    }
    
    orientation = (orientation + turn_to_angle[turn])
    orientation %= 360  # Modulo 360 to ensure the angle is within 0 to 359 degrees
    angle_to_direction = {
        0: [-1, 0],    # 0 degrees: [0, 1]
        90: [0, 1],    # 90 degrees: [1, 0]
        180: [1, 0],  # 180 degrees: [0, -1]
        270: [0, -1]   # 270 degrees: [-1, 0]
    }

    return angle_to_direction[orientation], orientation


class turmite:
    def __init__(self, x, y):
        
        self.turmite = {}
        self.current_state = "A"
        self.coordinates = [x, y]
        self.orientation = 90
        self.direction = [1, 0]
        
    def crawl(self, grid, gh, gw):
        while self.current_state != "HALT":
            head = self.turmite[self.current_state]
            
            
            if grid[self.coordinates[0] % gh][self.coordinates[1] % gw] == 0:
                transition = head.read_zero
            else:
                transition = head.read_one
            
                        
            
            
            grid[self.coordinates[0] % gh][self.coordinates[1] % gw] = transition.write
            
            yield transition.write, self.coordinates
            
            if transition.turn == 'N':
                self.coordinates[0] += self.direction[0]
                self.coordinates[1] += self.direction[1]
            else:
                self.direction, self.orientation = apply_turn(self.orientation, transition.turn)
                
            print(f"Writing: {transition.write}")
            print(f"Turn: {transition.turn}")
            print(f"Transition to {transition.next_state}")
            
            self.current_state = transition.next_state
            
            
            
            


def run_turmite(grid, x, y, gh, gw):
    t = turmite(x,y)

    t.turmite["A"] = State(read_zero=Transition(write=1,turn='R', next_state="K"), read_one=Transition(write=1,turn='L', next_state="F"))
    t.turmite["F"] = State(read_zero=Transition(write=0,turn='N', next_state="X"), read_one=Transition(write=1,turn='N', next_state="K"))
    t.turmite["B"] = State(read_zero=Transition(write=0,turn='N', next_state="F"), read_one=Transition(write=0,turn='N', next_state="A"))
    t.turmite["K"] = State(read_zero=Transition(write=1,turn='N', next_state="X"), read_one=Transition(write=0,turn='L', next_state="X"))
    t.turmite["X"] = State(read_zero=Transition(write=1,turn='R', next_state="F"), read_one=Transition(write=1,turn='R', next_state="Z"))
    t.turmite["Z"] = State(read_zero=Transition(write=0,turn='N', next_state="X"), read_one=Transition(write=0,turn='L', next_state="D"))
    t.turmite["D"] = State(read_zero=Transition(write=1,turn='U', next_state="B"), read_one=Transition(write=0,turn='R', next_state="HALT")) 

    return t.crawl(grid, gh, gw)


           
            
             