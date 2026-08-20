<p align="right"><strong>中文</strong> · <a href="README.en.md">English</a></p>

# Co-Research Lab

> 面向人与 AI 协作科研的 GitHub-first 工作空间模板。

<p align="center">
  <img src="assets/research-workflow-hero.png" alt="人在私有研究工作区内与 AI 协作，并将审核后的成果发布到公开仓库" width="100%">
</p>

Co-Research Lab 用一套轻量目录和工作约定，统一组织代码、实验、发现、报告与研究上下文。它不提供固定平台或重型框架，而是让项目在实际使用中逐步增加自己的 context、skills 和 harness。

## 它解决什么问题

- AI 不应每次进入项目都扫描整个仓库。
- 实验输出不应只留在终端、聊天或临时运行目录里。
- 发现、失败和决策需要能追溯到具体证据。
- 面向汇报、投稿和发布的材料应从研究第一天持续积累。
- 私有科研记忆与最终公开内容必须有不可误解的边界。

## 两条核心流程

AI 默认只加载最小上下文：

```text
AGENTS.md
  → research/NOW.md
  → research/INDEX.md
  → .agents/context/project.md
  → 按任务读取对应 context / skill / record
```

研究产物沿证据链逐级提炼：

```text
storage/runs/... → experiment E### → finding F### → report R###
                                                   → paper claim
                                                   → reviewed open/ release
```

<p align="center">
  <img src="assets/workspace-flow.svg" alt="Co-Research Lab 上下文加载、证据提炼与公开发布流程" width="100%">
</p>

## 目录结构

```text
.
├── README.md / README.en.md
├── AGENTS.md                    # AI 的项目入口与工作协议
├── open/                        # 唯一允许导出到公开仓库的内容
│   ├── src/
│   ├── configs/
│   ├── scripts/
│   ├── tests/
│   └── assets/
├── research/                    # 私有、进入 Git 的科研记忆
│   ├── NOW.md                   # 当前目标、状态和下一步
│   ├── INDEX.md                 # 持久记录导航
│   ├── LOG.md                   # 追加式决策日志
│   ├── experiments/             # E###：做了什么、如何复现
│   ├── findings/                # F###：证据支持什么结论
│   ├── reports/                 # R###：面向决策或投稿的综合材料
│   ├── literature/
│   └── paper/
├── .agents/                     # AI-native 工作层
│   ├── context/                 # 稳定项目约定
│   ├── skills/                  # 按需加载的任务流程
│   └── harness/                 # 可确定性验证的轻量工具
├── storage/                     # 数据、模型和 runs；默认不进 Git
└── _trash/                      # 可丢弃内容；默认不进 Git
```

## 开始使用

1. 由此模板创建一个 **private** 工作仓库。
2. 填写 [`.agents/context/project.md`](.agents/context/project.md)，确定研究问题、评估契约和技术约定。
3. 在 [`research/NOW.md`](research/NOW.md) 写下当前目标、成功标准和下一步。
4. 让人或 AI 按 [`AGENTS.md`](AGENTS.md) 工作，不默认扫描全仓库。
5. 运行结构检查：

```bash
python3 .agents/harness/check_workspace.py
```

## 记录如何晋级

- **Experiment** 记录问题、协议、命令、环境、结果与失败。
- **Finding** 把一个有边界的结论连接到实验或文献证据，并保留反证与局限。
- **Report** 为里程碑、决策、协作汇报或投稿组织多个 finding。
- **Paper claim** 只有在证据和限制明确后才进入论文叙事。
- **Open release** 只接收经过人工审核、可公开且可复现的内容。

示例目录使用 `_template/`，不会占用真实的 `E###`、`F###` 或 `R###` 编号。

## 私有与公开边界

工作仓库从创建开始就应保持 private：

- `research/` 进入 private Git 历史，用于追踪研究过程。
- `storage/` 和 `_trash/` 默认不进入 Git。
- `open/` 是唯一公共发布源，但完成任务不会自动发布。
- 发布时把 `open/` 的**内容**复制到一个全新的 public repo；不要把工作仓库直接改为 public。

删除 Git 中的私有文件并不等于清除历史，因此这条边界必须从第一天执行。

## 扩展方式

- 新的稳定项目知识放入 `.agents/context/`。
- 新的可复用任务流程放入 `.agents/skills/<name>/SKILL.md`。
- 能明确判定通过或失败的检查放入 `.agents/harness/`。
- 科研证据始终写入 `research/`，不要把 `.agents/` 变成第二本研究笔记。

模板自带 `run-experiment`、`analyze-experiment`、`review-literature` 和 `prepare-release` 四个最小 skill，可按领域逐步替换或扩展。
