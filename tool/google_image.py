from google_images_download import google_images_download
import glob
import os

config = {
    "Records": [
    {
        "keywords":"ビニールハウス",
        "limit":2000, #ダウンロード数のリミット
        "no_numbering":True, #デフォルトはダウンロード順に画像にnoが振られる（重複排除に邪魔になる）
        "output_directory":"greenhouse_image_google", #ダウンロード先のフォルダ
        "format":"jpg", #対象データの形式を指定GIFとかが混ざるが不要
        "suffix_keywords":"倒壊,損壊,被害,大風,大雪,解体,災害", #keywords+でカンマで区切ったワードぶん検索する（例えば「ビニールハウス 倒壊」、「ビニールハウス 損壊」と順に検索する）
        "related_images":True, #大量ダウンロードする場合に設定
        #"print_urls":True, #ダウンロードurlを表示（テキスト出力にも反映）
        "socket_timeout":30, #ダウンロードのタイムアウト時間設定
        "save_source":"download_list_JPN", #テキストファイルにダウンロード結果をリストで出力（追記される）
        "image_directory":"images_JPN", #出力フォルダの指定先、複数キーワードで同じフォルダにしておくと重複は生じない（上書き保存される）
        "chromedriver":"/usr/local/Caskroom/chromedriver/79.0.3945.36/chromedriver",
    },
    {
        "keywords":"greenhouse damage wind damage",
        "limit":2000,
        "no_numbering":True,
        "output_directory":"greenhouse_image_google",
        "format":"jpg",
        "related_images":True,
        #"print_urls":True,
        "socket_timeout":30,
        "save_source":"download_list_ENG",
        "image_directory":"images_ENG",
        "chromedriver":"/usr/local/Caskroom/chromedriver/79.0.3945.36/chromedriver",
    }
    ]
}

response = google_images_download.googleimagesdownload()
for rc in config["Records"]:
        response.download(rc)
