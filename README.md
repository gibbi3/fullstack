Files:

tournament.sql -- Database structure for Swiss-style tournament.
tournament.py -- Functions for maintaining results of the tournament.
tournament_test.py -- Tests the funcitoning of the program.

What does this program do?:

This program is designed so that users may input the wins and losses of a
Swiss-style tournament and receive the resulting standings and matchups.

How can it be implemented?

This program was designed to run on a virtual environment, namely vagrant.
Vagrant should first be installed, one may cd to the "vagrant" subfolder within
the greater "fullstack" directory. Running "vagrant up" in the terminal will
create the necessary environment for the use of this program. Once created,
the virtual machine may be connected to by entering the command "vagrant ssh".
One may then enter "cd /vagrant/tournament" to reach the appropriate directory.

The necessary schema may then be constructed here by entering the command:

"psql < tournament.sql"

The module "tournament_test.py" can then be executed using the "python" command,
running 10 tests to determine the functionality of the program and its
environment. This ensures the functions within "tournament.py" can be utilized
to maintain and monitor the outcomes of a Swiss-style tournament.
