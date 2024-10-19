# ZipFileCracker 功能架构

## 主要特性

- 基于命令行，argv输入

## 文件结构

通用文件：

- `__init__` 对模块做必要的准备，一些描述性字符串

特定文件：

- `zipCracker`
- core 核心处理模块
  - main 负责直接接受参数(下传到commands)
  - commands 负责参数解析与分层调用
- modules 所有子模块，扩展功能实现
  - all 一键化根据默认处理逻辑对压缩包进行自动化分析
  - info 检测并显示基本信息（压缩包版本、结构、文件列表）
  - crc 利用CRC32值爆破(1-6)[参考一](https://github.com/AabyssZG/CRC32-Tools),[参考二](https://github.com/theonlypwner/crc32)
  - headcrack 检测并修复伪加密(在实际过程直接使用分离的方法更为有效,例如[foremost](https://github.com/korczis/foremost))
  - passcrack 使用字典爆破压缩包(后续添加其他爆破方式)(zip,rar,7z) (拟使用GO完成爆破模块)
  - plain-text 明文攻击(参考[bkcrack](https://github.com/kimci86/bkcrack))

类似的项目[zipcracker](https://github.com/asaotomo/ZipCracker)

- util 底层功能模块
  - logger 记录操作日志，可以自行实现
  - 这里我记得高中的时候编了[一个](https://github.com/clonewith/translator-tools)简单的，实现了一些基本的命令行交互界面
  - docs 记录基本字符串（如版本、作者、许可证）
