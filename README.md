# Amazon Growth Agent Kit

面向“亚马逊跨境电商运营（转 AI 产品）”岗位的 Agent + Skill 作品集 Demo。

这个项目模拟一条完整的 Amazon 增长分析链路：

`广告报表 -> 广告诊断 -> 搜索词挖掘 -> Listing 承接检查 -> 评论洞察 -> AI 素材 brief -> 周度行动清单`

> 数据说明：`data/` 中的广告、搜索词、Listing 和评论数据均为脱敏模拟数据，只用于展示业务拆解和 Agent 化能力，不代表真实店铺业绩。

## 为什么契合岗位

- 对齐“亚马逊运营与广告投放”：用 ACOS、CTR、CVR、CPC、搜索词表现做规则诊断。
- 对齐“广告 Agent 模型训练/调优/落地”：把运营动作拆成独立 Skill，再由 Agent 编排。
- 对齐“电商 AI 产品规划”：每个 Skill 都有明确输入、输出、业务价值和可迭代方向。
- 对齐“AI 工具/设计审美”：从评论和 Listing 洞察生成主图、场景图、短视频 brief 和 prompt 草案。

## 快速运行

```bash
cd amazon_growth_agent_kit
python agent.py
```

运行后会生成：

```text
outputs/growth_report.md
```

运行测试：

```bash
cd amazon_growth_agent_kit
python -m unittest discover -v
```

## 项目结构

```text
amazon_growth_agent_kit/
  agent.py
  data/
    ads_report.csv
    search_terms.csv
    listing.json
    reviews.csv
  skills/
    ads_diagnosis.py
    search_term_mining.py
    listing_optimization.py
    review_insight.py
    creative_brief.py
    weekly_growth_report.py
  outputs/
    growth_report.md
  tests/
    test_ads_diagnosis.py
    test_search_term_mining.py
    test_content_skills.py
    test_report_generation.py
  SKILL_CARDS.md
```

## 六个 Skill

1. `ads_diagnosis_skill`：诊断 ACOS、CTR、CVR、CPC、花费浪费和可放量活动。
2. `search_term_mining_skill`：识别否词候选、扩词候选和需要观察的高点击低转化词。
3. `listing_optimization_skill`：检查 Listing 是否承接广告流量，输出关键词覆盖和转化风险。
4. `review_insight_skill`：从评论中提取卖点、痛点、素材角度和 FAQ 思路。
5. `creative_brief_skill`：把运营洞察转成主图、场景图、短视频和 AI prompt brief。
6. `weekly_growth_report_skill`：把所有 Skill 输出整理成周度增长报告和行动清单。

## 面试讲法

可以这样解释这个项目：

“我把 Amazon 广告优化拆成了可复用 Skill。广告诊断 Skill 负责判断指标异常，搜索词 Skill 负责否词和扩词，Listing Skill 判断广告流量能不能被详情页承接，评论 Skill 提炼用户语言，Creative Skill 把这些洞察转成 AI 素材生产 brief。Agent 不做复杂判断，只负责读取数据、编排 Skill、输出报告。后续如果接入 OpenClaw，可以把每个 Skill 改成独立工具，再加真实报表读取、权限控制和人工确认节点。”

## 后续可扩展

- 接入真实 Amazon Ads API 或第三方报表。
- 增加 OpenClaw Skill manifest。
- 增加 Web 上传页面和报告预览。
- 接入 LLM API，把规则结果转成更自然的运营复盘。
- 接入 Gemini、Lovart、Liblib、即梦、可灵等 AI 素材工具链。
