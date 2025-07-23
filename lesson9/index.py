import tools
#from tools import play_game,Empty(class)
#可用from ... import ...讀取指定的function和class


def main():
    try:
        play_count = 0
        while(True):
            play_count += 1
            tools.play_game() #要記得是執行tools裡的play_game
            is_continue = input("您還要繼續嗎(y,n)?")
            if is_continue == "n":
                break
            
        print(f"{tools.use_name}共玩了{play_count}次") #把tools的常數帶進來
        print("遊戲結束")
    except ValueError:
        print("格式錯誤")
        print("應用程式中斷")        
    except Exception as e:
        print(e)
        print("應用程式中斷")
    

if __name__ == "__main__":
    main()