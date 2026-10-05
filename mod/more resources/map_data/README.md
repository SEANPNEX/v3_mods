# More resource

Inspired by More Arable Land Mod. I am still a beginner in V3 moding. Please inform me if there is any bug.

[Steam Mod Link](https://steamcommunity.com/sharedfiles/filedetails/?id=2894989658&searchtext=more+arable)

This mod increases resource availability. By default:

- Arable land is **7 times** the original amount,
- All mines are **5 times** their original size,
- Logging and fishing resources are **10 times** the original,
- Gold mines are **3 times** the original.

I have added a Python script to make these modifications in the mod folder.
Adjust the `MULT` variables in the script, then run it with the game's `state_regions` folder, e.g.
`python create_more_resource.py "<Victoria 3>/game/map_data/state_regions"`.
The result is written to `map_data/state_regions/`. (Running it without an argument multiplies the files already in `state_regions/` in place.)

The included files are generated from Victoria 3 1.14.5. Re-run the script after a game update that changes the map.

受 “更多可耕地” 模组启发。作者仍为V3mod初学者。如有bug请留言。

[Steam 模组链接](https://steamcommunity.com/sharedfiles/filedetails/?id=2894989658&searchtext=more+arable)

这个模组增加了更多的资源。默认情况下：

- 可耕地数量是原来的 **7 倍**，
- 所有矿山资源是原来的 **5 倍**，
- 伐木场和渔业资源是原来的 **10 倍**，
- 金矿资源是原来的 **3 倍**。

我已经将一个用于这些修改的 Python 脚本添加到模组文件夹中。
修改脚本中的 `MULT` 变量后，以游戏的 `state_regions` 文件夹为参数运行，例如
`python create_more_resource.py "<Victoria 3>/game/map_data/state_regions"`，结果会写入 `map_data/state_regions/`。（不带参数运行时，会直接放大 `state_regions/` 中已有的文件。）

当前附带的文件基于 Victoria 3 1.14.5 生成。游戏更新地图后请重新运行脚本。