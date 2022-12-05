from assembly_parser import assembly_parser
from instruction_table import instruction_table
from register_table import register_table
from pseudoinstruction_table import pseudoinstruction_table


def main():
    asm = open("test.asm")
    lines = asm.readlines()
    parser = assembly_parser(64, instruction_table, register_table, pseudoinstruction_table, 4)
    parser.first_pass(lines)
    parser.second_pass(lines)


if __name__ == '__main__':
    main()

