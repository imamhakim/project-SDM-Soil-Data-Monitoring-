import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'Win64':
    base = "Win64GUI"
else:
    base = "Win32GUI"

executables = [cx_Freeze.Executable("SDM_APP.py",base=base,icon="logo.ico")]
addtional_mods = ['numpy.core._methods','numpy.lib.format','UserList','UserString']
cx_Freeze.setup(
    name="APP SDM",
    options={"build_exe":{"includes":addtional_mods,"packages":["Tkinter","matplotlib","serial","tkMessageBox","ttk","xlsxwriter"],
                          "include_files":["logo.ico","itk.gif","logo_aplikasi.gif","grafik.gif","arrow.gif","pimnas_logo.gif","excel.gif"]}},
    version = "0.01",
    description = "Soil Data Monitoring application",
    executables = executables
    )
