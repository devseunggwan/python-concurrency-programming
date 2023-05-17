"""
https://www.inflearn.com/course/lecture?courseSlug=%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8F%99%EC%8B%9C%EC%84%B1-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D&unitId=87547
"""

import time

def delivery(name, mealtime):
    print(f"{name}에게 배달 완료")
    time.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime} 시간 소요")
    print(f"{name} 그릇 수거 완료")
    
def main():
    delivery("A", 5)
    delivery("B", 3)
    delivery("C", 4)