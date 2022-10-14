
To use this playbook you need to have ansible installed on your host
add your public key to the server and change host file, 
by replace suggested ip to public ip of your server
and run 
$ ansible-galaxy collection install community.docker
$ ansible-playbook -i hosts DockerPlay.yml 
