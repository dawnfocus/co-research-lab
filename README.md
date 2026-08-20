# Co-Research Lab

一个用于生成 **GitHub-first 人–AI 协作科研工作空间** 的轻量模板仓库。

本仓库本身用于维护框架；真正部署给研究项目的内容位于 [`template/`](template/)。二者的 `AGENTS.md` 职责不同：

- 根目录 `AGENTS.md`：说明怎样维护模板框架。
- `template/AGENTS.md`：说明 AI 进入一个具体研究项目后怎样读取、工作和回写。

## 设计目标

1. 让代码、实验、发现、报告与研究上下文形成可追踪的证据链。
2. 使用渐进披露，避免 AI 每次进入项目都扫描整个仓库。
3. 从研究第一天起，为汇报、投稿和公开发布积累可复用材料。
4. 将项目约定、可复用 skill 与自动检查分离，便于持续演化。
5. 明确区分私有研究记忆与最终公开产物。

## 默认发布模型

部署后的工作仓库应保持 **private**。`research/` 会被 Git 跟踪，但不应进入公开历史；需要发布时，只把 `open/` 导出到独立公开仓库或发布制品。

不要先把 `research/` 提交到同一仓库，再尝试通过删除文件将仓库公开。Git 历史仍可能包含已删除内容。

## 创建项目

```bash
./scripts/create-project.sh ../my-research-project
cd ../my-research-project
git init
python3 .agents/harness/check_workspace.py
```

脚本只复制模板，不替换已有目录，不安装依赖，也不替用户决定许可证、研究领域或技术栈。

## 框架结构

```text
.
├── AGENTS.md                 # 框架维护规则
├── README.md
├── scripts/
│   └── create-project.sh     # 最小部署入口
└── template/                 # 部署后项目的完整骨架
    ├── AGENTS.md             # 具体研究项目的 AI 入口
    ├── open/                 # 可公开产物
    ├── research/             # 私有、可版本化的研究记忆
    ├── .agents/              # context、skills 与 harness
    ├── storage/              # 大文件和运行产物，默认忽略
    └── _trash/               # 临时丢弃区，默认忽略
```

## 核心证据链

```text
storage/runs/...  ->  research/experiments/E...  ->  research/findings/F...
                                                       |
                                                       v
                         research/paper/...  <-  research/reports/R...
                                                       |
                                                       v
                                                    open/...
```

`storage/` 中的原始产物可以很大且不进 Git；进入结论的关键信息必须被提炼进可版本化的实验、发现或报告记录。

## 当前边界

这个仓库只提供目录、约定、记录模板和一个无依赖检查器。它不包含实验调度平台、数据库、模型 API、云存储封装或论文生成流水线；这些能力应按项目需要作为 skill 或 harness 增量加入。
