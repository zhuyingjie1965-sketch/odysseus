# 更新日志 / Changelog

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)(SemVer):`主版本.次版本.修订号`。
- **主版本**:不兼容的重大改动
- **次版本**:向后兼容的新功能
- **修订号**:向后兼容的问题修复

---

## [0.1.0] - 2026-06-08

首个正式版本基线。在原 Odysseus 基础上完成了完整的中英文双语(i18n)支持。

### 新增 (Added)
- 前端 i18n 框架(`static/js/i18n.js`):`t('key')` 翻译函数、`data-i18n` 属性自动扫描、`localStorage` 语言持久化、EN/ZH 一键切换。
- 登录页自包含 i18n(内联迷你字典,无需 ES 模块)。
- 全部 UI 模块汉化:对话、会话、笔记、任务、记忆、相册、日历、文档、邮件、Cookbook、模型、预设、群组、文档库、RAG、语音、研究面板、主题面板。
- 中英文语言资源文件:`static/locales/en.json`、`static/locales/zh.json`(约 320 个键)。
- Python 后端错误消息翻译:`I18nMiddleware`(`core/middleware.py`)自动将 JSON 错误响应的 `detail` 字段译为中文;辅助模块 `src/i18n.py`;资源 `locales/py_en.json`、`locales/py_zh.json`。
- 前端全局 fetch 拦截器:为 `/api` 请求注入 `Accept-Language` 头,驱动后端 i18n。

### 说明
- 本版本作为后续改动、安装、升级的参考起点。
- 对应 git tag:`v0.1.0`(基线提交见本次合并)。

[0.1.0]: https://github.com/zhuyingjie1965-sketch/odysseus/releases/tag/v0.1.0
