def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        skill_index=[0 for v in range(len(skill))]
        answer = answer + skilltree(i,skill,skill_index)
    return answer

def skilltree(skill_tree_list,skill,skill_index):
    for j in skill_tree_list:
        numnum = search(skill,j)
        if(numnum<28):
            if(numnum!=0):
                if(skill_index[numnum-1]==0):
                    return 0
                else:
                    skill_index[numnum] = 1
            else:
                skill_index[0]= 1
    return 1

def search(skill,letter):
    num = len(skill)
    for i in range(num):
        if(letter==skill[i]):
            return i
    return 28



