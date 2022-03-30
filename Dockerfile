#the base image
FROM daisukekobayashi/darknet

#updates 
RUN apt update
#updates 
RUN apt update

#install tzdata
RUN apt install tzdata
RUN export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true
COPY ./preseed.txt /usr/share/preseed.txt
RUN debconf-set-selections /usr/share/preseed.txt
RUN dpkg-reconfigure -f noninteractive tzdata

#installing build tools
RUN apt install -y build-essential 
RUN apt install -y checkinstall
RUN apt install -y libreadline-gplv2-dev 
RUN apt install -y libncursesw5-dev 
RUN apt install -y libssl-dev 
RUN apt install -y libsqlite3-dev 
RUN apt install -y tk-dev 
RUN apt install -y libgdbm-dev 
RUN apt install -y libc6-dev 
RUN apt install -y libbz2-dev

#install other tools
RUN apt install -y wget
RUN apt install -y curl
RUN apt install -y bash
RUN apt install -y iputils-ping
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y gettext

#to install python3.6 from source
#RUN wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz
#RUN tar xvf Python-3.6.0.tar.xz
#WORKDIR Python-3.6.0/
#RUN echo $pwd
#RUN ./configure
#RUN apt install -y zlib1g-dev 
#RUN make altinstall
#WORKDIR ..
#RUN rm Python-3.6.0.tar.xz

#install all the packages
RUN pip3 install --upgrade --no-input pip
RUN pip3 install --no-input tensorflow-gpu
RUN pip3 install --no-input opencv-python
RUN pip3 install urlparse3
RUN pip3 install --upgrade onvif2_zeep
RUN pip3 install PyQt5
RUN pip3 install jsonpickle
RUN pip3 install wsdiscovery
RUN pip3 install watchdog
RUN pip3 install kafka-python
RUN pip3 install scikit-learn
RUN pip3 install grpcio
RUN pip3 install grpcio-tools
RUN pip3 install Shapely


#install pycharm
RUN mkdir /opt/pycharm
WORKDIR /opt/pycharm
ARG pycharm_source=https://download.jetbrains.com/python/pycharm-community-2021.3.1.tar.gz
RUN curl -fsSL $pycharm_source -o /opt/pycharm/installer.tgz 
RUN tar --strip-components=1 -xzf installer.tgz 
RUN rm installer.tgz 
WORKDIR /

#create code directory
RUN mkdir PythonProjects
WORKDIR PythonProjects

#command to run after 
CMD bash


