Bellagora

SUMMARY:

  This is a Flask application which manages an item catalog. Users can sign in
  with Google and Facebook, and the alteration of items within the catalog are
  limited to the user responsible for their creation. The database is managed
  via SQLAlchemy, and some files are included to get it up and running.

CONTENTS:

Directories:

  /js - This directory contains the scripts necessary for bootstrap elements to
        function properly. JQuery is linked via a web URL, as the most recent
        version is incompatible with some bootstrap elements.

  /static - This directory is home to CSS files and images, which are contained
            in the subfolder "/staic/img".

  /templates - This directory, as the name suggests, is where the HTML templates
               rendered by the Flask application are stored.

Files:

  bellagora.py - This file contains the actual Flask application, and is the
                 file which is actually executed in order for the site to run.

  client_secrets.json &
  fb_client_secrets.json - These files contain the client secrets necessary in
                           order to facilitate Google and Facebook logins
                           respectively.

  config.json - This file is used by Bootstrap, storing its configuration.

  database_setup.py - This file, when run, creates the tables used in the
                      database schema implemented within the project.

  stock.db - This is the actual database used by the project, and is created by
             testdb.py.

  testdb.py - This file's use is optional if a user wishes to set up their
              database manually per the command line. It creates an initial
              user, two categories, and a few items within said categories. To
              be used effectively, the email must be set to that which would
              match the Google and/or Facebook account the user would sign in
              with. Users are created based on their email addresses.

USING THE APPLICATION:

  First of all, a Vagrant/Virtualbox environment must be created and run. The
  directory, once cloned, can facilitate this if both Vagrant and Virtualbox
  are installed on the users computer. In the "vagrant" directory, the
  command "vagrant up" may be run in the command line in order to create the
  virtual machine. After its creation, one may then enter "vagrant ssh" to
  run the machine. Once running, enter "cd /vagrant/catalog" in order to access
  the files necessary to implement the application.

  Enter the command "python database_setup.py" to create the database the
  application will work with. If desired, one may then edit the contents of
  "testdb.py" to generate some initial entries into the database. It is
  necessary to enter one's appropriate email in the "User1" entry in order to
  edit entries once up and running. Users are created by email, and this should
  match that of the user's Google and/or Facebook accounts. Alternatively, the
  user may create initial entries in the Python console using SQLAlchemy.

  It is then necessary to register w/ Google and Facebook in order to obtain
  client secrets and app ids for the user's instance of the application.
  The corresponding values within the script at the lower end of the
  "login.html" template will have to be changed to match those provided by
  Google and Facebook, and the .json files containing the client secrets must
  be replaced by those offered by both Google and Facebook. Simply download, and
  replace the files within the "catalog" directory, making sure to name them the
  same as they are shown in the directory.

  The site should now be ready for use. Enter "python bellagora.py" in the
  command line. The site will be hosted locally on port 5000 of the user's
  machine, or whichever port the user might select (the port may be changed at
  the tail-end of bellagora.py).

  The database and most of its entries can now be instantiated through the site
  itself. It is important to note that the initiating user will be the only one
  able to add or delete categories. This can be altered, however, by equating
  the "admin" variable near the top of bellagora.py to the ID of the desired
  user. By default, it will be 1.
