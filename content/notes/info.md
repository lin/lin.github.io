---
math: true
---

<style>
strong {
  font-weight: bold;
  color: black;
  background-color: #fff200;
  padding: 0 4px;
}
</style>

## Information Theory

In **Reality**, High **Frequency** means high **Compresstion**, high **Certainty**.

Before **Action**, High **Uncertainty** means low **Probable**, high **Entropy**, high **Work** to identify.

After **Action**, High **Surprise** means low **Probable**, high **Information Gain**.

Low **Energy** means high **Probable**, high **Frequency**.

To change **Reality**, you need to spend energy, change low **Probable** to high **Probable**. One action agent provides **Surprise** to the other non-action agent.

Agent changes the local **Vocabulary** of the reality.

Energy is the money you pay to change env vocabulary to match your dictionary, shibun vs nyusu.

A stable state is a high probable situation.

You want your vocabulary to be more probable to let the env learn a new word with high probable.

## Abstration

if many **states** leads to few **attractors**, make these states form a **class**.

## Examples

$$
H = - p_i \log_2 p_i
$$

## Surprise

### Morse Code / Huffman Coding

High frequency means shorter encoding.

#### Frequency & Encoding

| Symbol | Probability | Code |
| ------ | ----------- | ---- |
| A      | 0.5         | 0    |
| B      | 0.25        | 10    |
| C      | 0.125       | 110    |
| D      | 0.125       | 111    |

#### Decoding

01001101110 gives you A B A C D A.




---


```python
import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(freq=node1.freq + node2.freq, left=node1, right=node2)
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_code_table(node, prefix='', code_table={}):
    if node.char is not None:
        code_table[node.char] = prefix
    else:
        build_code_table(node.left, prefix + '0', code_table)
        build_code_table(node.right, prefix + '1', code_table)
    return code_table

def encode(text, code_table):
    return ''.join(code_table[char] for char in text)

def decode(encoded, root):
    decoded = []
    node = root
    for bit in encoded:
        node = node.left if bit == '0' else node.right
        if node.char:
            decoded.append(node.char)
            node = root
    return ''.join(decoded)

# Example usage:
text = "ABACABAD"
freq = Counter(text)

# Step 1: Build tree and code table
root = build_huffman_tree(freq)
code_table = build_code_table(root)

# Step 2: Encode
encoded = encode(text, code_table)
decoded = decode(encoded, root)

print("Original text:", text)
print("Code table:", code_table)
print("Encoded:", encoded)
print("Decoded:", decoded)
```