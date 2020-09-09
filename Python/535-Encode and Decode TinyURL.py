# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 535-Encode and Decode TinyURL.py
@time: 2020/9/9 9:46
@desc:
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL
such as https://leetcode.com/problems/design-tinyurl
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Accepted
"""

import random
class Codec:
    codeDic = {}
    i = 0
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        while self.i in self.codeDic:
            self.i = random.randint(0, 10000)
        self.codeDic[self.i] = longUrl
        return "http://tinyurl.com/" + str(self.i)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.codeDic.get(int(shortUrl.replace("http://tinyurl.com/", "")))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


if __name__ == '__main__':
    # print(int("http://tinyurl.com/2836".replace("http://tinyurl.com/", "")))
    s = Codec()
    short = s.encode("https://leetcode.com/problems/design-tinyurl")
    print(short)
    print(s.codeDic)
    print(s.decode(short))