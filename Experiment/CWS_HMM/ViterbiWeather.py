# https://blog.csdn.net/Luzichang/article/details/91365752

import math
# 状态的样本空间
states = ('晴', '阴','雨')
# 观测的样本空间
observations = ( '读书', '打球','访友','读书')
#observations = ( '读书', '读书','读书','读书')
#observations = ( '打球', '打球','打球','打球')
#observations = ( '访友', '访友','访友','访友')
#observations = ( '访友', '访友','读书','访友', '访友','访友','读书')
# 起始个状态概率
start_probability = {'晴':0.5, '阴':0.3,'雨':0.2}
# 状态转移概率
transition_probability = {
  '晴': {'晴':0.7, '阴':0.2,'雨':0.1},
  '阴': {'晴':0.3, '阴':0.5,'雨':0.2},
  '雨': {'晴':0.3, '阴':0.4,'雨':0.3},
}
# 状态->观测的发散概率
emission_probability = {
  '晴': { '读书': 0.3,'打球': 0.4, '访友': 0.3},
  '阴': { '读书': 0.3,'打球': 0.2, '访友': 0.5},
  '雨': { '读书': 0.8,'打球': 0.1, '访友': 0.1},
}
# 计算以E为底的幂
def E(x):
  #return math.pow(math.e,x)
  return x
 
 
def display_result(observations,result_m):#较为友好清晰的显示结果
  # 从结果中找出最佳路径
  #print(result_m)
  infered_states = []
  final = len(result_m) - 1
  (p, pre_state), final_state = max(zip(result_m[final].values(), result_m[final].keys()))
  infered_states.insert(0, final_state)
  infered_states.insert(0, pre_state)
  for t in range(final - 1, 0, -1):
    _, pre_state = result_m[t][pre_state]
    infered_states.insert(0, pre_state)
  print(format("Viterbi Result", "=^80s"))
  head = format("观测序列", " ^7s")
  head += format("推断状态", " ^16s")
  for s in states:
    head += format(s, " ^15s")
  print(head)
  print(format("", "-^80s"))
 
  for obs,result,infered_state in zip(observations,result_m,infered_states):
    item = format(obs," ^10s")
    item += format(infered_state," ^18s")
    for s in states:
      item += format(result[s][0]," >12.8f")
      if infered_state == s:
        item += "(*)"
      else:
        item +="   "
 
    print(item)
  print(format("", "=^80s"))
 
 
 
def viterbi(obs, states, start_p, trans_p, emit_p):
 
  result_m = [{}] # 存放结果,每一个元素是一个字典，每一个字典的形式是 state:(p,pre_state)
                  # 其中state,p分别是当前状态下的概率值，pre_state表示该值由上一次的那个状态计算得到
  for s in states:  # 对于每一个状态
    result_m[0][s] = (E(start_p[s]*emit_p[s][obs[0]]),None) # 把第一个观测节点对应的各状态值计算出来
    #print('11',result_m[0][s])
  for t in range(1,len(obs)):
    result_m.append({})  # 准备t时刻的结果存放字典，形式同上
 
    for s in states: # 对于每一个t时刻状态s,获取t-1时刻每个状态s0的p,结合由s0转化为s的转移概率和s状态至obs的发散概率
                     # 计算t时刻s状态的最大概率，并记录该概率的来源状态s0
                     # max()内部比较的是一个tuple:(p,s0),max比较tuple内的第一个元素值
      result_m[t][s] = max([(E(result_m[t-1][s0][0]*trans_p[s0][s]*emit_p[s][obs[t]]),s0) for s0 in states])
      #print(result_m[t][s])
  return result_m    # 所有结果（包括最佳路径）都在这里，但直观的最佳路径还需要依此结果单独生成，在显示的时候生成
 
 
if __name__ == "__main__":
    result_m = viterbi( observations,
                        states,
                        start_probability,
                        transition_probability,
                        emission_probability)
    display_result(observations,result_m)