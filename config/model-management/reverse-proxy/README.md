#### Reverse proxy (Nginx) Installation
---

1. This reverse proxy was configured, in the first moment, to serve the MLFlow. Based on that is recommended to follow the instructions of the local project at https://gitlab.com/demeterproject/wp2/dataanalytics/model-management. 


2. Install Docker, docker-compose and Git.
   

3. Clone the project using the following command: git clone git@gitlab.cc-asp.fraunhofer.de:jaresalv/demeter-webserver-config.git

4. Copy all the files under the 'etc/nginx', of this repository, to the '/etc/nginx', of the target server where the reverse-proxy should be installed.

5. Navigate to the 'reverse-proxy' folder, of this repository.

6. Execute the following command: docker-compose up -d

7. Test the solution through the following URL in your browser: https://demeter.fit.fraunhofer.de/


Ps.: As the HTTPS is enabled using a self-signed certificate (temporarily), you could be asked to accept the certificate. Plus, as the Authentication and Authorization are enabled too, you will probably be asked for a username and password.