from typing import Optional
import re
from sys import argv
import requests

def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    # Transform: "abba" -> "^#a#b#b#a#$"
    t = "^#" + "#".join(s) + "#$"
    p = [0] * len(t)

    center = right = 0

    for i in range(1, len(t) - 1):
        mirror = 2 * center - i

        if i < right:
            p[i] = min(right - i, p[mirror])

        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

    max_len = max(p)
    center_index = p.index(max_len)

    start = (center_index - max_len) // 2
    return s[start:start + max_len]


def palindromes_at_least(seq, min_len: int):
    result = []

    def expand(left: int, right: int):
        while left >= 0 and right < len(seq) and seq[left] == seq[right]:
            length = right - left + 1
            if length >= min_len:
                result.append(seq[left:right + 1])
            left -= 1
            right += 1

    for center in range(len(seq)):
        expand(center, center)       # odd length
        expand(center, center + 1)   # even length

    return result


def keep_alnum(v: Optional[str]) -> Optional[str]:
    if v is None:
        return None
    return re.sub("[^a-zA-Z0-9]", "", v).lower()


def extract_sentences(url: str) -> list[str]:
    text = requests.get(url, timeout=30).text
    
    # Remove Gutenberg header/footer
    start = text.find("*** START OF THE PROJECT GUTENBERG EBOOK")
    end = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")
    
    text = text[start:end]
    
    # Remove the START line itself
    text = text.split("\n", 1)[1]
    
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    
    # Simple sentence split
    sentences = re.split(r"(?<=[.!?])\s+", text)
    
    # Optional: remove very short fragments
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
    
    print(len(sentences))
    return sentences

def extract_palindromes(lines: list[str], min_len: int) -> dict[int, list[str]]:
    out_dict = {}
    for i, line in enumerate(lines):
        palindromes = palindromes_at_least(keep_alnum(line), min_len)
        if palindromes:
            out_dict[i] = palindromes
    return out_dict

def collapse_with_positions(text: str) -> tuple[str, list[int]]:
    chars = []
    positions = []

    for i, ch in enumerate(text):
        if ch.isalnum():
            chars.append(ch.lower())
            positions.append(i)

    return "".join(chars), positions


def find_original_span(text: str, palindrome: str) -> str | None:
    collapsed, positions = collapse_with_positions(text)
    target = "".join(ch.lower() for ch in palindrome if ch.isalnum())

    start = collapsed.find(target)
    if start == -1:
        return None

    end = start + len(target) - 1

    original_start = positions[start]
    original_end = positions[end]

    return text[original_start:original_end + 1]

def show_details(i_extracted_palindromes: dict[int, list[str]], i_sentences: list[str]):
    for line_no, ps in i_extracted_palindromes.items():
        print(i_sentences[line_no])
        for p in ps:
            orig_text = find_original_span(i_sentences[line_no], p)
            print("    " + (orig_text or ""))

def show_palindromes_in_sentence(i_sentence: str, min_len: int):
    ps = palindromes_at_least(keep_alnum(i_sentence), min_len)
    if ps:
        print(i_sentence)
        for p in ps:
            orig_text = find_original_span(i_sentence, p)
            print("    " + (orig_text or ""))

if __name__ == "__main__":
    sentence = argv[1] if len(argv) > 1 else "Madam, in Eden, I'm Adam."
    min_len = int(argv[2]) if len(argv) > 2 else 3
    show_palindromes_in_sentence(sentence, min_len)
