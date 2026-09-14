import unittest

import calc

# * unit test -> 함수/메서드 하나하나가 의도대로 동작하는지 자동으로 검증하는 것
# * 시작은 항상 클래스로 시작 -> unittest.TestCase를 상속해야 "테스트 클래스"로 인식됨


class TestCalc(unittest.TestCase):
    def test_add(self):  # * 메서드 이름이 test로 시작해야 자동으로 테스트로 인식/실행됨
        result = calc.add(1, 2)
        self.assertEqual(result, 3)  # * assertEqual(실제값, 기대값) -> 둘이 다르면 테스트 실패 처리

    def test_add2(self):
        result = calc.add(0, -1)
        self.assertEqual(result, -1)


if __name__ == "__main__":  # ! 이 파일을 직접 실행했을 때만 참 (import해서 쓸 땐 실행 안 됨)
    unittest.main()  # * 이 파일 안의 test로 시작하는 메서드들을 전부 찾아서 자동 실행
