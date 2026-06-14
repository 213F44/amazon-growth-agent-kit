# Skill Cards

## 1. ads_diagnosis_skill

**Input:** 广告活动、花费、销售额、点击、展示、订单、CPC。  
**Output:** 指标摘要、问题标签、优化建议、warning。  
**Business Value:** 快速定位高 ACOS、高花费无订单、低 CTR、低 CVR 和可放量活动。  
**Interview Talking Point:** “广告诊断不是让模型自由发挥，而是先用可解释规则把异常点结构化，再交给 Agent 生成行动方案。”

## 2. search_term_mining_skill

**Input:** 搜索词、匹配类型、花费、销售额、订单、点击。  
**Output:** 否词候选、扩词候选、观察词。  
**Business Value:** 把人工每天看搜索词报表的动作变成固定分类规则。  
**Interview Talking Point:** “这一步可以作为广告 Agent 的训练样本标注逻辑，也可以作为自动化投放前的人工确认节点。”

## 3. listing_optimization_skill

**Input:** 标题、五点、关键词、评分、搜索词机会、评论洞察。  
**Output:** 已覆盖关键词、缺失关键词、Listing 风险和优化建议。  
**Business Value:** 判断广告流量是否能被详情页承接，避免只优化投放不优化转化。  
**Interview Talking Point:** “广告数据和 Listing 不是割裂的。高点击低转化词会回流到 Listing 承接检查。”

## 4. review_insight_skill

**Input:** 评论文本、评分、日期。  
**Output:** 高频卖点、痛点、素材角度、FAQ 思路。  
**Business Value:** 把用户真实语言沉淀为 Listing 文案和素材 brief 的输入。  
**Interview Talking Point:** “评论是低成本用户研究。正评提炼卖点，差评提炼风险和内容补救点。”

## 5. creative_brief_skill

**Input:** Listing 风险、评论卖点、评论痛点、目标站点。  
**Output:** 主图 brief、场景图 brief、短视频脚本、AI prompt 草案。  
**Business Value:** 把运营洞察转成 AI 内容生产任务，连接增长和素材。  
**Interview Talking Point:** “AI 工具不是独立玩图，而是服务点击率、转化率和用户信任。”

## 6. weekly_growth_report_skill

**Input:** 前五个 Skill 的结构化结果。  
**Output:** 周报、今天做、本周做、继续观察三类行动清单。  
**Business Value:** 把 Agent 分析结果变成业务负责人可以执行的清单。  
**Interview Talking Point:** “Agent 的最终交付不是一堆分析，而是优先级明确、可以执行、可复盘的运营动作。”
