###  ■NTT東日本の個人作業用のリポジトリー
####  ■Google画像検索から画像を収集する仕組みを構築
 - venv配下に環境作成  
   python3 -m venv ntteast-greenhouse
 - 必要なライブラリ
   - pip install google-images-download
   - pipのバージョンが古いらしいのでアップデートしておく  
      - pip install --upgrade pip
   - Selenium WebDriver（自動でブラウザを動かすAPI）のchromedriverをインストールする
      - brew install chromedriver  
     下記のエラーが出る。どうやらbrewのcaskというMacのdmgファイルでインストールするものをしなくてよくなるもの。
     ```
     Error: No available formula with the name "chromedriver" 
     It was migrated from homebrew/core to homebrew/cask.
     You can access it again by running:
        brew tap homebrew/cask
     And then you can install it by running:
        brew cask install chromedriver
     ```
   - brewをupdateしchromedriverをインストールする
      - brew tap homebrew/cask  
      - brew cask install chromedriver  
   - インストール確認
      - brew cask list
   - エラー内容
     - import sslでエラーが発生  
     pyenvを削除（元々削除したかった）。pythonの入れ直し。env環境の再作成をすると解消。
   - APIの内容  
     API化されているのでJSONのようなフォーマットでリクエストすればいい  
     【引数の参考先】  
     https://boomin.yokohama/archives/1328  
     https://github.com/hardikvasa/google-images-download
   - その後エラー
     - chromeとのバージョン違いで落ちる  
     Looks like we cannot locate the path the 'chromedriver' (use the '--chromedriver' argument to specify the path to the executable.) or google chrome browser is not installed on your machine (exception: Message: session not created: This version of ChromeDriver only supports Chrome version 83
     - Googleのupdateにより本家が機能しなくなった  
     ある方が修正してくれいているので「google_images_download.py」を入れ替える
     https://github.com/voins/google-images-download/tree/2cd68173c961324a2c41c61e8b6f40a49663ce60
       - 入れ替えただけではダメ
         - 400枚までになっている
         - keywordsが効いていない  
       - chromdriverをpythonと同一フォルダに置き下記のように直接実行するとpythonと同一フォルダに検索キーワードフォルダが作成されて格納される。
       python google_images_download.py -ri -cd "chromedriver" -l 1000  -k "ナンバープレート"  
       ※何をやっても400枚までになる
       - オプションは下記
       https://qiita.com/tomokin966/items/fdf14f4bfaa8bf97eed6
     - 派生してBingを作成してくれている人もいる  
     https://github.com/ultralytics/google-images-download
     ```
     こんなコマンドで実行する
     python bing_scraper.py --search '車両ナンバー' --limit 10000 --f png --type 'photo' -nn -ri -st 30 --download --chromedriver /usr/local/Caskroom/chromedriver/83.0.4103.39/chromedriver
     ```
  - 別ツール
    - Google, Bing, Baidu. 谷歌、百度からのダウンロード  
    https://github.com/sczhengyabin/Image-Downloader

