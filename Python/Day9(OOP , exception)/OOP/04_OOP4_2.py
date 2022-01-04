# 1. 클래스 선언
# 클래스 이름 : 식별자 규칙에 정의, 대문자로 시작(구분하기 위해서 대문자로 시작)
# 클래스 선언 시 필드 추가
# 클래스 동작 선언!!

class Car :
    color = ''
    speed = 0

    def speedUp(self):
        self.speed+= 10


    def speedDown(self):
        pass

# self : 실제로 존재하는 인스턴스가 사용하는 것 (자신의 것)
#        기존의 함수와 구분

# 2. 객체(인스턴스) 생성
myCar = Car()
yourCar = Car()

# 3. 객체(인스턴스) 사용
# 필드가 없는데 instance를 생성한 후에 필드를 추가하는 과정
print(myCar.color)
myCar.color = 'black'
print(myCar.color)

# 메서도 호출 : 인스턴스.메서드() => myCar.speedUp()
print(myCar.speed)
myCar.speedUp()
print(myCar.speed)
myCar.speedUp()
print(myCar.speed)





