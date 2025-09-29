"""
ch = 'R'
print(f"{ord(ch)}")
อันนี้จะได้เท่ากับ เลข ASCII คือ 82

print(chr(82))
อันนี้จะรันออกมาได้ ตัว R

for i in range(1, 4):  # rows
    for j in range(1, 4):  # columns
        print(f"{i} x {j} = {i*j}", end="\t")
    print()
ยืมโค้ดจารย์สอนแลปมาใช้
"""

for i in range(1, 7):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()