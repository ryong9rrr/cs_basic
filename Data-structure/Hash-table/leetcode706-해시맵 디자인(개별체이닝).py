import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key:int, value:int)->None:
        index = key % self.size

        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재한다면 연결리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key:int)->int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            print(p.key, p.value)
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key:int)->None:
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]
        # 인덱스의 첫 번째 노드일 때
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next