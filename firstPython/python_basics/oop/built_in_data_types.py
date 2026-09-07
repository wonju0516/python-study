# built in data types
# * List(리스트) -> mutable(변경 가능)

my_list = [1, 2, 3]
my_list.append(4)  # * 맨 뒤에 추가
print(my_list)
my_list[1] = 0  # * 인덱스로 값 변경 가능
print(my_list)

# * Dictionary(딕셔너리) -> mutable(변경 가능)
my_dictionary = {"country": "south korea", "city": "seoul"}
print(my_dictionary)

my_dictionary["country"] = "USA"
# * 딕셔너리[키] = 값 -> 그 키가 이미 있으면 "값 변경", 없으면 "새로 추가" (문법은 똑같음)
# * 여기선 "country"가 이미 있던 키라서 값만 바뀜 -> 다른 키(city)는 안 건드림
print(my_dictionary)


# * Set(세트)
## * 리스트에 있는 데이터를 중복 없는(unique) 값으로 바꾸고 싶을 때 사용
## * unchangeable(원소 자체를 바꿀 순 없음) but 추가/제거는 가능 -> add()/remove()
## * 인덱스로 접근 불가(cannot subscript), 원소는 항상 유일함(unique)

my_set1 = set((1, 2, 3))
# * set(이터러블) -> 괄호 두 개: 바깥은 함수 호출, 안쪽 (1,2,3)은 인자로 넘긴 튜플

print(my_set1)

# ! print(my_set1[1]) # Error!! Set is not subscribable(인덱스로 접근 불가)

l = [1, 2, 3, 4, 5, 1, 2, 3, 4]
print(set(l))  # * 리스트를 set으로 변환 -> 중복 제거됨
print(list(set(l)))  # * 다시 리스트로 변환 (순서는 보장 안 됨)

my_set2 = {1, 2, 3}  # * set 리터럴 -> {}는 원소만 있으면 set, key:value가 있으면 dict
print(my_set2)

my_set2.add(4)  # * 원소 추가
print(my_set2)

my_set2.remove(4)  # * 원소 제거
print(my_set2)

# * Tuples(튜플)
## * 인덱스로 접근 가능(리스트처럼)
## * immutable(한 번 만들면 값을 바꿀 수 없음)
## * 생성 속도가 리스트보다 빠름
my_tuples = (1, 2, 3)
# * list([])/dict({})처럼 tuple도 자체 리터럴(())이 있어서 tuple() 함수 호출 없이 바로 생성
print(my_tuples[1])
