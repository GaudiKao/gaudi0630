def get_bmi(height, weight):
    return weight / (height  / 100) **2
    
def get_status(bmi):
    if bmi < 18.5:
        return '體重過輕'
    elif 18.5 <= bmi < 24:
        return '正常範圍'
    elif 24 <= bmi < 27:
        return '體重過重'
    elif 27 <= bmi < 30:
        return '輕度肥胖'
    elif 30 <= bmi < 35:
        return '中度肥胖'
    else:
        return '重度肥胖'


def main():
    try:
        height = float(input('請輸入身高120-250cm):'))
        if not (120 <= height <= 250):
            print('身高範圍輸入錯誤')
            return

        weight = float(input('請輸入體重30-200kg):'))
        if not (30 <= weight <=200):
            print('體重範圍輸入錯誤')
            return

        bmi = get_bmi(height, weight)
        status = get_status(bmi)
        print(f'您的BMI為:{bmi:.2f}')
        print(f'體重狀態為:{status}')

    except Exception as e:
        print(f'輸入格式錯誤:{e}')
    finally:
        print('應用程式結束')


if __name__ == "__main__":
    main()