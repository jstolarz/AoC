# flake8: noqa: E501
class Computer:
    def __init__(self, register_a, register_b, register_c, program):
        self.register_a = register_a
        self.register_b = register_b
        self.register_c = register_c
        self.program = program

        self.output = []
        self.pointer = 0

    def _get_combo_operand_value(self):
        operand = self.program[self.pointer]
        if operand < 4:
            return operand
        if operand == 4:
            return self.register_a
        if operand == 5:
            return self.register_b
        if operand == 6:
            return self.register_c

    def _get_literal_operand_value(self):
        return self.program[self.pointer]

    def adv(self):
        self.pointer += 1
        operand = self._get_combo_operand_value()
        self.register_a = self.register_a // (2**operand)
        self.pointer += 1

    def bxl(self):
        self.pointer += 1
        operand = self._get_literal_operand_value()
        self.register_b = self.register_b ^ operand
        self.pointer += 1

    def bst(self):
        self.pointer += 1
        operand = self._get_combo_operand_value()
        self.register_b = operand % 8
        self.pointer += 1

    def jnz(self):
        if self.register_a == 0:
            self.pointer += 2
            return
        self.pointer += 1
        operand = self._get_literal_operand_value()
        self.pointer = operand

    def bxc(self):
        self.register_b = self.register_b ^ self.register_c
        self.pointer += 2

    def out(self):
        self.pointer += 1
        operand = self._get_combo_operand_value()
        self.output.append(operand % 8)
        self.pointer += 1

    def bdv(self):
        self.pointer += 1
        operand = self._get_combo_operand_value()
        self.register_b = self.register_a // (2**operand)
        self.pointer += 1

    def cdv(self):
        self.pointer += 1
        operand = self._get_combo_operand_value()
        self.register_c = self.register_a // (2**operand)
        self.pointer += 1

    def run(self):
        opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        while self.pointer < len(self.program):
            opcodes[self.program[self.pointer]]()
        return self.output


with open("input") as f:
    lines = f.read().splitlines()
    ra = int(lines[0].split(":")[1])
    rb = int(lines[1].split(":")[1])
    rc = int(lines[2].split(":")[1])
    program = [int(x) for x in lines[4].split(":")[1].split(",")]


ra = 202975183644 * (10**3)

while True:
    computer = Computer(ra, rb, rc, program)
    result = computer.run()
    if result[-14:] == program[-14:]:
        print(ra // (10**2), result)
    if result == program:
        print("!!!!!!!!!!!!!!!!!!", ra)
        break
    ra += 1
    if ra > 205973735000000:
        break
