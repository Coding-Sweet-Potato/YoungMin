# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true

def designerPdfViewer(h, word):
    length = len(word)
    maximum = 0
    for i in word:
        idx = ord(i)-97
        if maximum < h[idx]:
            maximum = h[idx]
    return length * maximum
