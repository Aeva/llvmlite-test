
# llvmlite setup
You can install llvmlite via pip, in theory, but it looks to require building llvm.
On the other hand, you can get a nice binary distribution via conda, at the cost of
having to install conda.

I went with
[Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html )
and that seems to work well enough.

With that installed, you can open the conda environment via the start menu and do:
`conda install llvmlite`

# pyinstaller
Pyinstaller seems to work without a fuss, and when I ran the resulting exe in a sandbox,
it Just Worked!  So no need for the end user to install a compiler etc! :D

Downside: windows defender thinks the exe is a virus >:|
