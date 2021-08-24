from pywebio.input import input, NUMBER, input_group
from pywebio.output import put_text, put_buttons
from pywebio.platform.tornado import start_server
from pywebio.session import go_app, set_env, hold

#開発環境
#windows10
#python==3.6.5

#フレームワーク
#pyweblio==1.3.3

#エディター
#VisualStudioCode==1.58.2

#       cd Desktop\ワークスペース\python
#       python mathcalc.py runserver
#       http://localhost:8080

#初期ページ
def index():
    set_env(title="色々計算します")
    put_text("このサイトでは素数・最小公倍数・最大公約数の算出をします").style('color: Purple; font-size: 30px')
    put_buttons(['素数を算出'], [lambda: go_app('sosucalc', new_window=False)])
    put_buttons(['最大公約数を算出'], [lambda: go_app('yakusucalc', new_window=False)])
    put_buttons(['最小公倍数を算出'], [lambda: go_app('kobaicalc', new_window=False)])
    hold()

#素数算出ページ
def sosucalc():

    #入力値を格納
    usr_input = input("入力値までの素数を出します",type=NUMBER, placeholder='2以上の自然数を入力してください')
    
    while True:
        if usr_input is None:
            usr_input = input("入力値までの素数を出します",type=NUMBER, placeholder='2以上の自然数を入力してください')
        elif usr_input < 2:
            usr_input = input("入力値までの素数を出します",type=NUMBER, placeholder='2以上の自然数を入力してください')
        else:
            break

    sosu = []

    total = 0

    #素数の算出・出力
    for i in range(1,usr_input+1):
        cnt = 0
        for j in range(1,i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 2:
            sosu.append(i)
            total += 1

    put_text(f"{usr_input}までの素数は{sosu}の計{total}個です。")
    put_buttons(['やり直す'], [lambda: go_app('sosucalc', new_window=False)])
    put_buttons(['トップに戻る'], [lambda: go_app('index', new_window=False)])
    hold()


#最大公約数算出ページ
def yakusucalc():

    #入力値の格納
    yakusu = input_group("入力値1と入力値2の最大公約数を算出します。", [
    input("入力値1",type=NUMBER, placeholder='1以上の自然数を入力', name="usr_input1"), 
    input("入力値2",type=NUMBER, placeholder='1以上の自然数を入力', name="usr_input2")])

    yakusu_1 = yakusu["usr_input1"]
    yakusu_2 = yakusu["usr_input2"]
 
    while True:
        if yakusu_1 is None or yakusu_2 is None or yakusu_1 < 1 or yakusu_2 < 1:
            yakusu = input_group("入力値1と入力値2の最大公約数を算出します。", [
            input("入力値1",type=NUMBER, placeholder='1以上の自然数を入力', name="usr_input1"), 
            input("入力値2",type=NUMBER, placeholder='1以上の自然数を入力', name="usr_input2")])
            yakusu_1 = yakusu["usr_input1"]
            yakusu_2 = yakusu["usr_input2"]
        else:
            break

    #最大公約数の算出・出力
    tmp : int = 0
    x = yakusu_1 * yakusu_2

    if yakusu_1 < yakusu_2 :
        tmp = yakusu_1
        yakusu_1 = yakusu_2
        yakusu_2 = tmp

    r = yakusu_1 % yakusu_2

    while r!=0:
        yakusu_1 = yakusu_2
        yakusu_2 = r
        r = yakusu_1 % yakusu_2
    
    put_text(f"{yakusu['usr_input1']}と{yakusu['usr_input2']}の最大公約数は{int(yakusu_2)}です。")
    put_buttons(['やり直す'], [lambda: go_app('yakusucalc', new_window=False)])
    put_buttons(['トップに戻る'], [lambda: go_app('index', new_window=False)])
    hold()

#最小公倍数算出ページ
def kobaicalc():

    #入力値の格納
    kobai = input_group("入力値1と入力値2の最小公倍数を算出します。", [
    input("入力値1",type=NUMBER, placeholder='1以上の自然数を入力', name="usr_input1"), 
    input("入力値2",type=NUMBER, placeholder='1以上の自然数を入力', name="usr_input2")])

    kobai_1 = kobai["usr_input1"]
    kobai_2 = kobai["usr_input2"]

    while True:
        if kobai_1 is None or kobai_2 is None or kobai_1 < 1 or kobai_2 < 1:
            kobai = input_group("入力値1と入力値2の最大公約数を算出します。", [
            input("入力値1",type=NUMBER, placeholder='1以上の自然数を入力', name="usr_input1"), 
            input("入力値2",type=NUMBER, placeholder='1以上の自然数を入力', name="usr_input2")])
            kobai_1 = kobai["usr_input1"]
            kobai_2 = kobai["usr_input2"]
        else:
            break

    #最小公倍数の算出・出力
    tmp : int = 0
    x = kobai_1 * kobai_2

    if kobai_1 < kobai_2 :
        tmp = kobai_1
        kobai_1 = kobai_2
        kobai_2 = tmp

    r = kobai_1 % kobai_2

    while r!=0:
        kobai_1 = kobai_2
        kobai_2 = r
        r = kobai_1 % kobai_2

    put_text(f"{kobai['usr_input1']}と{kobai['usr_input2']}の最小公倍数は{int(x/kobai_2)}です。")
    put_buttons(['やり直す'], [lambda: go_app('kobaicalc', new_window=False)])
    put_buttons(['トップに戻る'], [lambda: go_app('index', new_window=False)])
    hold()
    
start_server([
index,
yakusucalc,
kobaicalc,
sosucalc],
port=8080)