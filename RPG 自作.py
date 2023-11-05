def gameprogram(savedata):
    #ここからゲームプログラム
    print("ゲームをはじめます！")
    #load savedata
    print("セーブデータをロードしています！")
    if savedata!="":
            print("error--セーブデータがありません。はじめから始めるを選択してください！")
            openanswer="-2"
    if openanswer!="-2":
        #ランクの設定
        rank=savedata[0]
        #セクションの設定
        section=savedata[1]
        #経験値の設定
        xp=savedata[4]
        #トロフィーの達成状況
        torofy=string(savedata[5])
        print("使い方；")
        print("１，yes")
        print("０，no")
        print("２、推理力の確認")
        print("３，達成したトロフィーの確認")
        print("４，セクションをやり直す")

def check(q):
    while not(each_times_answer=="1" or each_times_answer=="0"):
        each_times_answer=input("q")
        if each_times_answer=="1":
            return(1)
        if each_times_answer=="0":
            return(0)
        if each_times_answer=="2":
            print("推理力は"+string(xp))
        if each_times_answer=="3":
            print("以下が取得したトロフィです。")
            #トロフィの読み込み

openanswer="1"
while openanswer=="1" or openanswer=="2":
    openanswer=input("続きからはじめるなら１、はじめから始めるなら２を選択！")
    if openanswer=="1":
    #続きからはじめる
        while openanswer!="-1":
            print("続きからはじめる")
            print("質問にyesの場合は１、質問にnoの場合は０を入力してね！")
            #フォルダの内部を参照
            savedata=[1,2]
            gameprogram(savedata)
            if openanswer!="-2":
                break
            openanswer=input("終了しますか？")
            if openanswer=="1":
                openanswer=input("セーブしますか？")
                if openanswer=="0":
                    print("終わります。")
                    openanswer="-1"
                if openanswer=="1":
                    #ゲームデーターのセーブ
                    print("セーブします。")
                    print("終了します。")
                    openanswer="-1"
    if openanswer=="2":
    #はじめから始める
        print("はじめから始める")
        #既存ファイルの確認
        openanswer=input("前回のセーブデータを消去しますか？（消去しないと新しく始められません！）")
        if openanswer=="1":
            #ファイルの消去と作成
            print("消去します。")
        if openanswer=="0":
            openanswer="1"