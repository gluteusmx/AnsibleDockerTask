
To use this playbook you need to have ansible installed on your host<br /> 
add your public key to the server<br /> 
change host file, by replace suggested ip to public ip of your server <br /> 
and run: <br /> 
$ ansible-galaxy collection install community.docker <br /> 
$ ansible-playbook -i hosts DockerPlay.yml <br /> 
