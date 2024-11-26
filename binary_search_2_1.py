from bisect import bisect_left, bisect_right


def count_by_value(a, left_value, right_value):
    left_idx = bisect_left(a, left_value)
    right_idx = bisect_right(a, right_value)
    return right_idx - left_idx


array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

n = int(input())
words = input().strip().split()
query = input().strip()

for word in words:
    array[len(word)].append(word)
    reversed_array[len(word)].append(word[::-1])

for i in range(10001):
    array[i].sort()
    reversed_array[i].sort()

if query[0] != '?':
    result = count_by_value(array[len(query)],
                            query.replace('?', 'a'), query.replace('?', 'z'))
else:
    result = count_by_value(reversed_array[len(query)],
                            query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
print(result)

# Ø친구들로부터 천재 프로그래머로 불리는 "프로도"는 음악을 하는 친구로부터 자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니 프로그램으로 개발해 달라는 제안을 받았습니다.

# Ø그 제안 사항 중, 키워드는 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻합니다. 와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다. 예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.

# Ø가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드 query가 주어질 때, 키워드에 매치된 단어가 몇 개인지 찾아주세요.

# Ø가사 단어 제한사항
# -words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
# -각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# -전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
# -가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
# -각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.

# Ø검색 키워드 제한사항
# -검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# -검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
# -검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
#   + 예를 들어 "??odo", "fro??", "?????"는 가능한 키워드입니다.
#   + 반면에 "frodo"('?'가 없음), "fr?do"('?'가 중간에 있음), "?ro??"('?'가 양쪽에 있음)는 불가능한 키워드입니다.

# Ø예시
# Words
# [frodo front frost frozen frame kakao]

# -키워드 fro??는 frodo, front, frost에 매치되므로 3입니다.
# -키워드 ????o는 frodo, kakao에 매치되므로 2입니다.
# -키워드 fr???는 frodo, front, frost, frame에 매치되므로 4입니다.
# -키워드 fro???는 frozen에 매치되므로 1입니다.
# -키워드 pro?는 매치되는 가사 단어가 없으므로 0 입니다.
# Ø입력
# -첫 줄에는 가사 단어 (words)의 수가 입력됩니다.
# -둘째 줄에는 가사가 입력됩니다.
# -셋째 줄에는 키워드가 입력됩니다.

# Ø출력
# -키워드에 매치된 단어의 수

# Ø입력 예시
# 6

# frodo front frost frozen frame kakao

# ????o


# Ø출력 예시
# 2