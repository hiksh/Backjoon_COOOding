def triangle_area(d1, d2, d3):
    u = d1[0]*d2[1]+d2[0]*d3[1]+d3[0]*d1[1]
    d = d1[1]*d2[0]+d2[1]*d3[0]+d3[1]*d1[0]
    return (u - d) / 2

N = int(input())
diagram = []
for i in range(N):
    dx,dy = map(int, input().split())
    diagram.append([dx,dy])

area = 0
# 점 세개 삼각형 만들어 계산하고 점 하나 제거
while len(diagram) > 2:
    area += triangle_area(diagram[0], diagram[1], diagram[2])
    del diagram[1]

print(abs(round(area, 1)))