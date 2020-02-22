import unittest

class Solution(unittest.TestCase):
    def simplifyPath(self, path: str) -> str:
        """
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.



Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:

Input: "/a/./b/../../c/"
Output: "/c"

Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"

Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"

---
Basic idea: add one more tailing `/`, then use a stack to store and `dir/` and deal with `.` or `..`, finally return `'/' + ret`. This way can only deal with `{dir}/` pattern
        """
        if not path:
            return path

        # add one more '/' incase no tailing `/`
        path += '/'
        stack = []
        dirName = ""
        for c in path:
            if c == '/':
                if not dirName or dirName == '.':
                    # means `//` or `/./`
                    # do nothing
                    pass
                elif dirName == '..':
                    # pop `dir/`
                    if stack:
                        stack.pop()
                else:
                    stack.append(dirName + '/')
                # reset dirName folder name
                dirName = ""
            else:
                dirName += c

        ret = ""
        while stack:
            d = stack.pop()
            if not ret:
                d = d[:-1]
            ret = d + ret

        return '/' + ret

    def testSimplifyPath(self):
        self.assertEqual(self.simplifyPath("/home/"), "/home")
        self.assertEqual(self.simplifyPath("/../"), "/")
        self.assertEqual(self.simplifyPath("/..."), "/...")
        self.assertEqual(self.simplifyPath("/home//foo/"), "/home/foo")
        self.assertEqual(self.simplifyPath("/a/./b/../../c/"), "/c")
        self.assertEqual(self.simplifyPath("/a/../../b/../c//.//"), "/c")
        self.assertEqual(self.simplifyPath("/a//b////c/d//././/.."), "/a/b/c")
