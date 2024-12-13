import re
from dataclasses import dataclass

class NoCombinationFound(Exception):
    pass

@dataclass
class ClawMachine:
    Ax: int
    Ay: int
    Bx: int
    By: int
    Px: int
    Py: int

def calculate_pushings(claw_machine: ClawMachine) -> tuple[int]:
    """
    i = (PxBy-PyBx) / (AxBy-AyBx)
    j = (Px-Ax*i) / Bx
    """
    i = (claw_machine.Px*claw_machine.By-claw_machine.Py*claw_machine.Bx) / (claw_machine.Ax*claw_machine.By-claw_machine.Ay*claw_machine.Bx)
    j = (claw_machine.Px-claw_machine.Ax*i) / claw_machine.Bx
    if i.is_integer() and j.is_integer():
        return (int(i), int(j))
    raise NoCombinationFound

def parse_machines(list_of_machines: list[str], prize_offset: int = 0) -> list[ClawMachine]:
    pattern = r"(\d+)"
    claw_machines = []
    i = 0 
    while i < len(list_of_machines):
        if "Button A" in list_of_machines[i]:
            Ax, Ay = [int(x) for x in re.findall(pattern, list_of_machines[i])]
            Bx, By = [int(x) for x in re.findall(pattern, list_of_machines[i+1])]
            Px, Py = [int(x)+prize_offset for x in re.findall(pattern, list_of_machines[i+2])]
            claw_machines.append(ClawMachine(Ax, Ay, Bx, By, Px, Py))
            i += 4
        else:
            print("!!!!!")
    return claw_machines
    

with open("input") as f:
    machines = parse_machines(f.read().splitlines(), prize_offset=10000000000000)

tokens = 0 
for machine in machines:
    try:
        pushings = calculate_pushings(machine)
        tokens += (pushings[0] * 3) + pushings[1]
    except NoCombinationFound:
        pass
print(tokens)