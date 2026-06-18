# CLAUDE.md - 全局配置

> 四条核心法则（源自 Karpathy 蒸馏版）：
> 1. 编码前先思考，不确定时先沟通
> 2. 简约至上，只做要求之事
> 3. 精确编辑，不碰无关部分
> 4. 目标驱动，而非步骤驱动

---

## 沟通方式

- **语言**：默认使用中文回复；代码、命令、变量名、文件路径保持英文。
- **风格**：结论先行，简洁直接，不铺垫背景。
- **态度**：不谄媚，不夸“这是个很好的问题”，不以“当然可以”开头。
- **真实性**：给出真实判断——方案有问题直接指出，发现更好做法主动说明。

## 工作流（Plan → Confirm → Execute）

1. **复述需求**：简要确认你的任务理解。
2. **制定计划（Plan模式）**：在编写代码前，列出实施步骤、涉及文件、技术方案和潜在风险。
3. **征得同意**：展示计划并等待明确确认。
4. **逐步实施**：每完成一个逻辑单元，暂停并请求审查。
5. **验证与报告**：运行必要测试或检查，报告结果。

## 编码规范

- **通用原则**：
  - 只做你要求的事，不做额外优化或重构。
  - 仅修改与任务直接相关的代码，不触碰无关部分。
  - 追求可读性和一致性，遵循项目现有风格。
  - 不要猜测：不确定时先提问，不自行假设。

- **语言特定（默认）**：
  - **JavaScript/TypeScript**：优先 `const`/`let`，使用 ES 模块；TS 启用严格模式，用 `interface` 而非 `type`。
  - **Python**：遵循 PEP 8，使用类型提示和 f-string。
  - **Go**：遵循官方风格，显式处理每个错误。
  - **Java**：
    - 遵循 Google Java Style Guide 或项目现有规范。
    - 使用标准命名：类名 `UpperCamelCase`，方法/变量 `lowerCamelCase`，常量 `UPPER_SNAKE_CASE`。
    - 优先使用现代化的 Java 特性（Lambda、Stream API、Optional），避免冗余样板代码。
    - 合理使用 `final` 关键字增强不可变性；避免使用 `null` 返回值，优先返回空集合或 `Optional`。
    - 异常处理：不吞掉异常，记录日志；捕获具体异常而非 `Exception`。
  - **Vue**：
    - 遵循 Vue 官方风格指南（`vue/essential` 规则集）。
    - 组件名使用 `PascalCase`；模板中使用 kebab-case 形式。
    - 单文件组件（SFC）顺序：`<template>` → `<script>` → `<style>`（带 `scoped` 属性）。
    - Props 定义尽量详细（类型、默认值、校验）；使用 `v-bind` 简写 `:`，`v-on` 简写 `@`。
    - 组合式 API 优先（`<script setup>` 语法糖），逻辑按功能分组，合理抽离可复用逻辑到 composables。

## Git 规则

- **禁止自动操作**：不自动执行 `git commit` 或 `git push`，除非我明确要求。
- **提交前展示**：必须先展示将要提交的变更摘要（可用 `git diff --cached` 或 `git status`）。
- **提交信息**：使用简洁英文，遵循 Conventional Commits 格式（`<type>(<scope>): <subject>`）。

## 红线操作（必须提前询问）

**即使在 auto-accept 模式下，以下操作也必须先向我确认：**

- 删除文件、目录或 Git 历史。
- 修改 `.env`、密钥、token、证书、CI/CD 配置文件。
- 执行 `git push`、`git rebase`、`git reset --hard`、强制推送。
- 公开发布（`npm publish`、生产部署等）。

## 常见命令参考

- **Java**：`mvn clean install` / `./gradlew build`
- **Vue**：`npm run serve` / `npm run build`
- **其他**：
  - 构建：`npm run build` / `python setup.py build` / `go build`
  - 测试：`npm test` / `pytest` / `go test`
  - 代码检查：`npm run lint` / `pylint` / `golangci-lint`

---
**优先级说明**：本文件为全局配置，项目级 `./CLAUDE.md` 或 `./CLAUDE.local.md` 中的规则可覆盖或扩展上述内容。