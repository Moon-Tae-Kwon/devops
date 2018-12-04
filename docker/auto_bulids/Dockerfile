# FROM - 어떠한 이미지를 기반으로 설치 할지 설정
# ubuntu 최신 버전 사용
FROM ubuntu:latest
MAINTAINER Moontaekwon <m.taekwon.se@gmail.com>

# RUN - 쉘스크립트 또는 명령어 실행
# apt-get 를 이용한 업데이트 작업 및 apache2 install
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install apache2

# index.html 파일 내용 변경
RUN mv /var/www/html/index.html /var/www/html/index.html_old
RUN touch /var/www/html/index.html && echo "Moon dockerfile test" >> /var/www/html/index.html
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
# EXPOSE - 호스트와 연결할 포트 번호
EXPOSE 80

# CMD - container 실행시 실행할 실행 파일 및 스크립트
# apache2 start
CMD ["/usr/sbin/apache2ctl","-DFOREGROUND"]
