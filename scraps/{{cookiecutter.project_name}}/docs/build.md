# Building {{cookiecutter.project_name}}
To help deploy, a .deb builder/installer has been included

# Notes

### Webhook monitoring
```
[LOGGING]
    discord_webhook = #SECRET
    slack_webhook = #SECRET
```

Two tools have been included to help alert humans if there are `logger.error()` calls.  Both Slack and Discord are supported.

Just add a webhook into the `app.cfg` file in `scripts/` and logging will handle the rest

# How To Build
* Debian system (tested on Ubuntu 16)
* Python 3.x (developed for Python 3.5)
* pip packages
    * wheel
    * setuptools
    * virtualenv
    * [Plumbum](https://plumbum.readthedocs.io/en/latest/)
* dpkg
* [dh-virtualenv](http://dh-virtualenv.readthedocs.io/en/latest/index.html) v1.0

## Building the Package

1. `sudo apt-get install dpkg`
2. `sudo apt-get install dh-virtualenv`
3. `sudo apt-get install debhelper`
4. `sudo apt-get install python3-pip`
5. `sudo pip3 install wheel`
6. `sudo pip3 install setuptools`
7. `sudo dpkg-buildpackage -us -uc`

# How to Install

1. `sudo dpkg -i {{cookiecutter.deb_project_name}}_[version]_amd64.deb
2. `sudo systemctl status {{cookiecutter.endpoint_group}}.service` to  make sure deploy is correct

## Notes
Deploys a virgin virtualenv for code to run in.  Does not adjust production python on machine.

`source /opt/venvs/{{cookiecutter.deb_project_name}}/bin/activate`
`sudo /opt/venvs/{{cookiecutter.deb_project_name}}/bin/python` <-- for running python directly
