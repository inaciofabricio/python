import cx_Freeze

executables = [cx_Freeze.Executable("primeiro jogo.py")]

cx_Freeze.setup(
    name = "A bit Racey",
    options = {"build_exe": {"packages":["pygame"],
                             "include_files": ["carro.png"]}},
    executables = executables
    )