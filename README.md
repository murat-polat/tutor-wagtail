# tutor-wagtail
Wagtail Plugin for Tutor Open edX



## Installation:

`python3 -m venv ~/tutor  `

`source ~/tutor/bin/activate  `

If you using Tutor in Production modus and on k8s, you have to add Wagtail subdomain to your " /etc/hosts "  file.

Cloning and installing plugin:


`git clone https://github.com/murat-polat/tutor-wagtail   `

`cd tutor-wagtail  `

`pip3 install -e tutor-wagtail    `

`tutor plugins list  `

You should see  Wagtail plugin in your plugins list. (If it's not, please reboot your server  check it again.)

`wagtail==0.1.0   `  

`tutor plugins enable wagtail `

Than grep all codes below and paste to terminal, enter

`tutor config save --set WAGTAIL_HOST=wagtail.{{LMS_HOST}} \ `

`tutor config save --set WAGTAIL_MYSQL_DATABASE=wagtail \`

`tutor config save --set WAGTAIL_MYSQL_HOST=mysql \`

`tutor config save --set WAGTAIL_MYSQL_PASSWORD=wagtail \`

`tutor config save --set WAGTAIL_MYSQL_PORT=3306 \ `

`tutor config save --set WAGTAIL_MYSQL_USERNAME=wagtail \`

`tutor config save --set WAGTAIL_DOCKER_IMAGE=muratp/wagtail \`

Building new Docker services for Tutor:

`tutor images build wagtail  `

`tutor images build openedx      `  optional

`tutor local quickstart  `

For Kubernetes deployment run:

`tutor k8s quickstart`        http://wagtail.yourdomain/


![](src/wagtail.png)


### Login to admin site:

Create superuser:

`tutor local run wagtail python3 manage.py createsuperuser  `

login your admin site:

http://wagtail.your_domain/admin


![](src/wagtailAdmin.png)