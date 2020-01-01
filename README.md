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
   - APIの内容  
     API化されているのでJSONのようなフォーマットでリクエストすればいい  
     【引数の参考先】  
     https://boomin.yokohama/archives/1328  
     https://github.com/hardikvasa/google-images-download
