# 长信科技PPT规范

面向长信科技工作场景的共享 Agent Skill。用于工作汇报、技术改善、学习小结及阶段总结，强调统一品牌蓝、横向表格、少字多图和有依据的结果。

**技能标识：`changxin-ppt-standard` · 版本：1.0.0**

本项目由个人整理分享，不是长信科技正式发布的制度或官方品牌手册。名称用于说明适用场景，不表示公司授权、认证或背书。

## 它会帮助你做什么

- 沿用已认可模板，统一标题、Logo位置、页脚、字体与表格。
- 蓝底文字用白色，正文行统一白底，按内容量分配列宽。
- 用图片和图表呈现工作，减少泛泛的描述和无意义的小字。
- 做清楚SOP新旧对比、改善措施与结果、成果总结及工作计划。
- 核对统计口径，区分已完成工作、参与、学习、计划与已验证效果。
- 在需要时规划翻页笔可操作的图片放大/缩回顺序。

本技能是制作规范，不是PPT生成软件。需要使用支持技能的AI，以及当前环境可用的PPT制作工具。它不包含公司模板、Logo、内部汇报、生产照片、客户名称或真实生产数据。

## 第一次安装

### 在 Codex 中用自然语言安装

将本仓库链接 https://github.com/xmxiaomeng/changxin-ppt-standard 发给支持技能安装的 Codex，并说：

> 请使用 skill-installer 安装 https://github.com/xmxiaomeng/changxin-ppt-standard 中 `skills/changxin-ppt-standard` 目录里的技能。

安装后，在下一轮对话查看技能是否出现。如果未发现，重新打开会话或重启客户端。

### 手动安装

1. 从 GitHub 的 **Code → Download ZIP** 下载仓库，解压。
2. 复制里面的 `skills/changxin-ppt-standard` 文件夹到本机技能目录，保留完整目录结构。
3. 当前 Codex 官方文档列出的用户目录是 `~/.agents/skills/`，Windows 对应用户目录下的 `.agents\skills\`。部分桌面安装器使用 `$CODEX_HOME/skills`，以本机安装器返回的位置为准；不要同时复制两份同名技能。
4. 确认技能列表出现“长信科技PPT规范”。不要将整个仓库根目录误当成技能目录。

其他支持 Agent Skills 的客户端可以使用同一个技能文件夹，安装位置和调用方式以该客户端为准。只复制技能名称到尚未安装的AI，不会自动加载仓库内容。

## 安装后怎么用

最简单的说法：

> 使用长信科技PPT规范，帮我做一份工作汇报。下面是我的资料和模板。

精确调用：

```text
使用 $changxin-ppt-standard，根据附件制作一份8分钟左右的阶段工作汇报。
沿用我提供的模板，重点展示已完成工作和结果，图表为主。
```

修改现有PPT：

```text
使用 $changxin-ppt-standard，检查这份PPT的逻辑、表格和字体配色。
保留已认可的结构，仅优化明确存在的问题，另存一份新版本。
```

只整理大纲：

```text
使用 $changxin-ppt-standard，先根据资料列出大纲和每页要展示的证据。
这一步先不生成PPT。
```

建议随任务提供：汇报对象、报告期、时长、最新模板、真实工作材料，以及希望重点讲什么。没有模板也可制作通用蓝色风格稿，但不会伪造官方Logo或版式。

## 主题色说明

本规范采用的默认工作配色：**HEX `#0154A6` / RGB `(1, 84, 166)`**。用户提供的现行公司品牌标准优先。

不要将其与 HEX `#184166` 混淆，后者对应 RGB `(24, 65, 102)`，是另一种更暗的蓝色。本项目没有认证任何色号为公司的官方VI值。

## 文件结构

```text
skills/changxin-ppt-standard/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── visual-standard.md
    ├── content-patterns.md
    └── delivery-checklist.md
```

维护者可运行 `python tests/validate_package.py` 检查文件结构、引用、编码和版本一致性。内容与适用边界仍需人工审阅。更新使用正常语义版本号，例如 `1.0.1`。

## 分享范围

仓库只分享编写者整理的通用方法与规则。不包含任何公司的模板资产或商标授权；用户生成的PPT、原图、客户资料和生产数据不因使用本技能而自动获得公开许可。请勿把这些资料提交到公开Issue或Pull Request。

规则与代码采用 [MIT License](LICENSE)。公司名称及商标的权利不包含在此许可中。

官方技能说明：[Build skills](https://developers.openai.com/codex/skills)。
