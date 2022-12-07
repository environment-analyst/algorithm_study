#!/usr/bin/env python
# coding: utf-8

# In[24]:


#하노이탑
# 유명한 재귀함수 문제
# n: 옮기녀는 원반의 개수
# from_pol: 옮길 원반이 현재 있는 출발점 기둥 
# to_pol : 옮긴 원반이 있는 도착점 기둥
# aux_pol : 원반이 거쳐가는 보조 기둥


def hanoi(n, from_pol, aux_pol, to_pol):
    if n == 1:
        print(from_pol," ",to_pol)
        
        return
    
    # 원반 N -1개를 aux_pol로 이동(to_pol를 보조 기둥으로)
    hanoi(n-1, from_pol, to_pol, aux_pol)
    
    # 가장 큰 원반을 목적지로 이동
    print(from_pol," ",to_pol)
    
    #aux_pol에 있는 원반 n -1개를 목적지로 이동(from_pol를 보조 기둥으로)
    hanoi(n-1,aux_pol, from_pol, to_pol)
    
    # 함수에서는 저장되어 있는 값보다 주어진 위치가 더 중요한 것 같다...
    
    
    


# In[25]:


n = int(input())

print(2**n-1) # 굳이 함수로 구할 필요 없음
hanoi(n,1,2,3) # n만 값을 받아오면 되고 나머지 값은 미리 입력


# In[ ]:




