# Jupyter Notebook

shift+tab  shows options

1. run jupyter kernelspec list

2. cd /usr/local/share/jupyter/kernels/python3

3. open kernel.json file

4. change

{
 "argv": [
  "REPLACE-THIS-WITH-THE-CORRECT-EXECUTABLE-PATH",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "heterodimers",
 "language": "python"
}

to

{
 "argv": [
  "/Users/serdar/Documents/udel/python/nerResume/env/bin/python",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "Python 3",
 "language": "python"
}


to run the kernel location needs to be change

I had the same issue. After going through many (like way too many) solutions to this issue found elsewhere, I manage to figure out a solution that at least works in my case.

Step1: check the correct executable path of the anaconda environment.
Go on command line, activate the conda environment that is problematic, and check the correct executable path for the environment.

conda activate {envronment name};
then on python console, (>>>)import sys;sys.executable

For instance on Linux it will be /media/{username}/{path-to}/anaconda3/envs/{environment name}/bin/python


Step2: correct the executable path for jupyter sessions.
From command line, check the path where kernel.json of your problematic conda environment is located.

jupyter kernelspec list

For instance on Linux it will be: /home/{username}/.local/share/jupyter/kernels/{environment name}

Open the kernel.json located in that folder and replace the incorrect executable path, as shown below.

{
 "argv": [
  "REPLACE-THIS-WITH-THE-CORRECT-EXECUTABLE-PATH",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "heterodimers",
 "language": "python"
}
