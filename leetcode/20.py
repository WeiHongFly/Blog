# 判断括号是否有效
class Solution(object):
    def check(self,s,_stack):
        #检查目前能否匹配
        if (s=="(" and _stack[-1]==")") or (s=="{" and _stack[-1]=="}") or (s=="[" and _stack[-1]=="]"):
            _stack.pop()
            return True
        else:
            return False
        
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #判断是否为空字符串
        if not s:
            return True
        else:
            s_list=[i for i in s]
            s_list.reverse()
        _stack=[]
        for i in s_list:
            if i in [")","}","]"]:
                _stack.append(i)
            else:
                if _stack:
                    res=self.check(i,_stack)
                    if not res:
                        return False
                else:
                    return False
                    
        if _stack:
            return False
        else:
            return True