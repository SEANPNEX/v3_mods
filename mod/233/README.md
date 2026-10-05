233自用整合

原mod: https://steamcommunity.com/sharedfiles/filedetails/?id=2882874184

在原mod基础上增加了每周建造上限，整合了[no local price](https://steamcommunity.com/sharedfiles/filedetails/?id=3280497939)

在修改意识形态选项中新增了两种锡克教意识形态，如果有整合其他意识形态的需求，请给我留言

## 1.14 兼容性更新 / Victoria 3 1.14 update

- 每周建造上限和 no local price 改为 `common/static_modifiers/zz_233_base_values.txt` 中的 `INJECT:base_values`，不再整份覆盖原版静态修正（旧的 `za_static_modifiers.txt` 和 `mcmarketacces_modifiers.txt` 是 1.5/1.8 版原版文件的副本，会覆盖新版内容）。
  Weekly construction cap and no-local-price now use `INJECT:base_values` instead of overriding the whole vanilla static modifier file.
- 战区选择改为 1.13 之后的 36 个新战略区域（旧区域已被原版合并）。
  The leader region picker now uses the 36 strategic regions introduced in 1.13.
- 修正已被移除或改名的修正、触发器、建筑、文化和意识形态（无神论者 → 实证主义者，`ideology_positivist`）。
  Renamed or removed modifiers, triggers, buildings, cultures and ideologies were updated (Atheist leaders now use `ideology_positivist`).
