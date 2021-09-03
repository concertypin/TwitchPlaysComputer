<h1 align="center">TwitchPlaysComputer 리포에요!👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.01-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/rophin/TwitchPlaysComputer/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT License" src="https://img.shields.io/badge/License-MIT License-yellow.svg" />
  </a>
</p>

## 설치
BOT_USERNAME, OAUTH_TOKEN, CHANNEL_NAME 환경 변수는 있어야 해요. 각각 봇의 트위치 ID, 봇의 토큰, 들어가 있을 채널명이에요.
```sh
pip install -r requirements.txt & npm run start
```

## 사용법

### 잠깐만요!
이 코드는 조금 무식하게 작성되었어요. 이 말을 달리 하면, 보안 장치를 만들어두지 않았다는 소리에요. 아무도 없는 한적한 곳에서의 테스트가 아니라면, 제발, 제발, <strong>제발</strong> 가상 머신 안에서만 실행해주세요.
```sh
npm run start
```
CHANNEL_NAME의 트위치 채팅방에서 # 글자(샵 띄어쓰기 글자에요!) 식으로 입력하면, 컴퓨터에서 글자를 입력하는 것처럼 됩니다. # d라고 입력하면 키보드 d 키가 눌린다는 거에요. <br>
끝내고 싶은데 끝낼 수 없다면, 스크롤 락을 켜 보세요. 일시 정지되요.
## 만든놈

* Github: [@rophin](https://github.com/rophin)

## 🤝 기여

기여와 이슈, 기능 건의는 언제나 받고 있어요!<br />[여기](https://github.com/rophin/TwitchPlaysComputer/issues)에서 이슈를 만들 수 있어요. 

## 📝 License

이 프로젝트는 [MIT License](https://github.com/rophin/TwitchPlaysComputer/blob/main/LICENSE)를 사용하고 있어요.
bot.js 파일의 상당수는 [여기](https://dev.twitch.tv/docs/irc)에서 가져왔답니다.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
