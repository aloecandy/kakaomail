# kakaomail

send simple text using kakao mail

## install

```shell
pip install kakaomail
```

## usage

```python
import kakaomail

logged_in=False

while logged_in==False:
    logged_in=kakaomail.login(input('id:'),input('pw:'))

kakaomail.send('recipient@domain','subject','text')
```
