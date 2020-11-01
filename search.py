### csvを読み込むためにインポート
import csv
# 検索ソース
sources=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    input_word =input("鬼滅の登場人物の名前を入力してください >>> ")
    result = 0
    ### 課題1
    for word in sources:
        if word == input_word:
            print("{}が見つかりました".format(input_word))
            result = True
            break
        else:
            pass
    if result == True:
        pass
    else:
        ### 課題2
        print("{}が見つかりませんでした".format(input_word))
        ### 課題３
        print("{}をリストに追加します".format(input_word))
        sources.append(input_word)
        ### 課題3出力結果確認
        #print(sources)

### 課題4
def csvAddList():
    with open("data.csv") as f:
        for row in csv.reader(f):
            sources.extend(row)
    ### 課題4出力結果確認
    #print(sources)

if __name__ == "__main__":
    ### csvファイルを読み込み後、検索ソースを実行するように順番を修正
    csvAddList()
    search()
