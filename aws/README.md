## AWS command Line
본 문서는 hands-on에 가까운 문서이며 IaC(Infrastructure as code)에 따라서 테스트한 내용 입니다.

---
### reference link
- [AWS CLI install](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-install-macos.html#awscli-install-osx-path)
- [AWS CLI configure](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration)
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/index.html#cli-aws-ec2)

---
### AWS CLI install
AWS CLi install (python3.7 설치 완료한 상태)
* 환경변수 등록은 아래에 내용 추가 하였습니다. (mac 기준)
- [get-pip.py](get-pip.py)
```
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
pip3 install awscli --upgrade --user
aws --version
```
![aws-version](images/aws-version.png)
* bash 사용시
```
echo 'export PATH="/Users/$(whoami)/Library/Python/3.7/bin:$PATH"' >> .bashrc
```
* zsh 사용시
```
echo 'export PATH="/Users/$(whoami)/Library/Python/3.7/bin:$PATH"' >> .zshrc
```

---

## Overview

* 18.11.28 ~
    * [AWS CLI command IaC EC2 infra setup (11.28-30)](https://github.com/Moon-Tae-Kwon/devops/tree/master/aws/ec2/README.md)