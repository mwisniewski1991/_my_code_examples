# Linux Commands

- ssh
    - ssh username@server

- ls    :list
    - ls -l     :nice looking list
    - ls -al    :show hidden stuffs

- pwd   :current workind directory
- cd    :change directory
    - cd /  :go to root of file system
    - cd dir    :go to dir
    - cd ..     :go back
    - cd        :go back to root

- touch :create file 
    - touch filename.txt    :create file
    - touch file1 file2 file3       :create multiple files
    - touch file{1..10}     :create 10 files
    - touch -d tomorrow     :create file tomorrow 

- echo  :write text to file
    - echo "Text in file" > newfile.txt

- nano  :file editor
    - nano filename.txt
    - to save file
        - CTRL + X
        - y
        - enter

- vim   :file editor
    - vim filename.txt
    - to save file
        - ESC
        - :wq   :write quit

- cat   :check file body
    - cat filename.txt

- less  :check file in read mode
    - less filename.txt

- wc    :word counter  

- shred :change file with ranodm letters and numbers
    - shred filename.txt

- mkdir :new dir
    - mkdir mynewdir 
    
- cp    :copy file
    - cp filename.txt ./target_directory.filename.txt

- mv    :move file
    - mv filename.txt ./target_directory.filename.txt

- rm    :remove file
    - rm filename.txt
    
- rmdir :remove directory
    - rmdir my_directory
    - rm -r my_directory    :if dir is not empty  -r recursice
    - rm -rf my_directory   :if dir is not empty  -r recursice -f force

- ln    :create link to file
    - ln -s filename.txt linktofile.txt

- clear :clear terminal
    - clear

- cltr + l  ::clear terminal

- whoami    :show user name
    - whoami

- sudo  :run commadn as admin

- useradd   :create new user
    - sudo useradd nick
        - then set password for user

- su    :switch user
    - su nick   :switch to other user
    - exit      :exit from user

- passwd    :change password
    - sudo passwd
    - sudo passwd nick  :change other user password

- apt update    :update applications
    - sudo apt update

- finger    :inspect users
    - finger nick 

- man   :check docs for command
    - man finger
    - man cat
    - man man

- --help    :show shortes manual
    - finger --help
    - wc --help

- whatis    :short version of man
    - whatis finger

- whereis   :place of libs
    - whereis finger

- wget  :download from net
    - wget  link_to_source

- curl  :download form net
    - curl link_to_source
    - curl link_to_source > filename    :put data into file

- zip   :compress file 
    - zip zipped_file.zip file_to_zip.txt

- unzip :unzip files
    - unzip zipped_file.zip
        - then choose option if file will be replaced
            - y
            - n
            - a
            - N
            - r

- less  :open file like cat but allows to page down/ip
    - less filename.txt

- head  :show beggining of file
    head filename.txt

- tail  :show end of file
    - tail filename.txt

- cmp   :compare two files
    - cmp fist_file.txt second_file.txt

- diff  :show diffrence between two files
    - diff fist_file.txt second_file.txt

- sort  :sort stuffs
    - cat filename.txt | sort 

- find  :find things
    - sudo find / -name filename.txt                :find file name in all dirs
    - sudo find /my_directory -name filename.txt    :find file name in specific dir
    - sudo find . -type ".*"    :find hidden stuff
    - find . -type f -empty                         :find empty dirctories
    - find / -perm /a-x                             :find executable files
    
- chmod :change attributes
    - chmod +x executthis.sh    :make file executable

- chown :change ownership
    - chown nick filename.txt   :user nick now owns filename.txt.

- ifconfig  :ip details
    - ifconfig

- ip address :ip details
    - ip address

- grep  :find sth in files
    - grep A filename.txt   :find letter 'A' in file,
    - ip address | grep eth0   :show only part of ip address details
    - ip address | grep eth0 | grep net    :show only net part
    - ip address | grep eth0 | grep net | awk '{print $s}'
 
DNS server
- cat /etc/resolv.conf
- resolvectl status

- ping  :check network connectivity 
    - ping websitename.com
    - ping -c 5 websitename.com     :-c numbers of responses
    - ping -c 5 -s 500 websitename.com  :-s size of packets

- traceroute    :check route from computer to website
    - traceroute websitename.com

- netstat   :open ports
    - netstat  
    - netstat -tulpn

- ss    :open ports, same as netstat
    - ss
    - ss -tulpn

- ufw 

- uname :name of your system
    - uname
    - uname -a  :more details

- neofetch  :version of system
    - neofetch

- cal   :show callendar
    - cal

- echo "4+5+6+7" | bc   :math in terminal

- free  :how many memory is used
    - free

- df    :disk space
    - df 
    - df -H     :other than bytes

- ps    :system processes
    - ps
    - ps -aux 

- top   :process consumed memory
    - top
    - htop  :preetier way

- kill  :stop process with id
    - ps -aus | grep my_process :find process if
    - kill -9 my_process_id     :stop process

- pkill :stop process without id
    - pkill -f my_process

- systemctl :start stop systems
    - sudo systemctl stop apache2
    - sudo systemctl status apache2
    - sudo systemctl start apache2

- history   :history of your commands
    - history
     
- reboot  
    - sudo reboot

- shutdown 
    - sudo shutdown         :shutdown in one minute
    - sudo shutdown -h now  :shutdown right now



- gzip  :zip files
    - gzip filename.txt

- gunzip    :unzip files
    - gunzip filename.txt


- ps auxf :check running programs
    - ps auxf