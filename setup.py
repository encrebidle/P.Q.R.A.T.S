from cx_Freeze import setup, Executable

base = None    

executables = [Executable("passportphoto_psycho.py", base=base)]

packages = ["idna","cv2","numpy","pandas"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<passport_psycho>",
    options = options,
    version = "<1.3>",
    description = '<any description>',
    executables = executables
)
