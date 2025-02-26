import sys
sys.setrecursionlimit(100000000)

N = int(input())
left = [0] * 100
right = [0] * 100
for i in range(N):
    node, leftNode, rightNode = input().split()
    node = ord(node)
    leftNode = ord(leftNode) if leftNode != '.' else 0
    rightNode = ord(rightNode) if rightNode != '.' else 0

    left[node] = leftNode
    right[node] = rightNode

preOrderResult = []
inOrderResult = []
postOrderResult = []

def preOrder(cur):

    preOrderResult.append(cur)
    if left[cur]:
        preOrder(left[cur])
    if right[cur]:
        preOrder(right[cur])


def inOrder(cur):

    if left[cur]:
        inOrder(left[cur])
    inOrderResult.append(cur)
    if right[cur]:
        inOrder(right[cur])

def postOrder(cur):

    if left[cur]:
        postOrder(left[cur])
    if right[cur]:
        postOrder(right[cur])
    postOrderResult.append(cur)

preOrder(ord('A'))
inOrder(ord('A'))
postOrder(ord('A'))


print("".join(map(chr,preOrderResult)))
print("".join(map(chr,inOrderResult)))
print("".join(map(chr,postOrderResult)))