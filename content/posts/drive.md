---
title: "Motivation in Games"
date: 2025-09-11
isCJKLanguage: true
---

## 结构：起承转合

始终保持一种被优化的难度和刺激度

1. 家：玩家可以放松的没有压力，村庄，回血，商店
1. 器：在家的商店中，或任务中，或近距离的野外，给玩家新的武器、词汇、消化点
1. 野：玩家可以在野外尝试这个新的武器，但没有太大的失败惩罚
1. 牢：玩家必须要在资源有限的情况下，较长时间面临失败压力的情境下，进行清怪
1. 考：玩家的终极考试，类似于肉鸽一样的关底大怪挑战，需要反复尝试、背板、解谜

## 动力：武器、道具与代理

1. 剧情：求知欲的满足，新鲜感和进度感的来源
1. 打怪：生存危机，是核心的驱动力，消灭强敌的快感，挫败即燃料
1. 武器：是打怪的第一代理，获得并能够装配高级武器的快感，容易是诱饵
1. 道具：是打怪的第二代理，斯金纳盒，获得稀有道具的快感，超预期奖励
1. 素材：是打怪的二级代理，日常努力，刷素材的满足感，一分耕耘一分收获

## 题型：刷怪、背板与解谜

随着Bloom级别的提升而带来的题目类型变化，也伴随着难度的变化

1. 刷怪：电子奴役式的赛博打工，没有挑战，只要付出时间即可，RPG
1. 背板：需要熟练的掌握词汇，有大量的词汇训练积累和反应速度，ACT
1. 解谜：需要玩家尝试、整合和验证，需要玩家有耐心和思维强度，AVG

## Game Design

> Game design is basically motivation design.

There are two main ways to make something highly motivating:

1.	Accumulative, linked motivations
2.	Exceeding expected returnss.

In this article, we are focusing on structure of the motiviation design in games, not details. As in a well polished game, you can have minimal structure as in many indie roguelike games.

The common core drivers are:

1. Completions – Single-Playthrough Focus. In games designed to be experienced once, the primary drive is progressing through the main storyline. Every system—combat, exploration, puzzles—serves the overarching narrative arc and helps maintain a sense of forward momentum.

2. Loops – Replayable / Roguelike Mechanics. In games built for multiple playthroughs, the focus shifts to repeatable loops such as procedural generation, randomized encounters, or roguelike systems. These mechanics keep each run fresh and rewarding. Even in non-roguelike titles, certain elements can function as self-contained loops to encourage replayability.

3. Problem Sets – Layered Challenge Structures. Well-designed games feature multi-tiered challenges—maps, rooms, enemies, skills—creating a natural progression of difficulty and complexity. Bosses, while appearing as singular encounters, often act as milestone levels or mastery gatekeepers. In particularly challenging titles like Elden Ring, bosses effectively create miniature roguelike experiences within the broader game.

4. Currencies – Experience and Resource Rewards. Clearing each challenge tier grants rewards such as XP or coins. These rewards serve as tangible markers of progress, encourage continued engagement, and provide players with resource-management freedom.

5. Items – Expanding the Player’s Toolkit. Beyond XP and coins, stages and exploration yield items and abilities. These rewards introduce strategic choice and expand the player’s toolkit. XP or currency can then be spent to upgrade items, enhance skills, or unlock new abilities—creating a satisfying feedback loop between effort and growth.

6. Skills – Player Mastery and Frustration. Skills represent what players must master personally, much like real-life exams. The process of honing skills brings a sense of accomplishment, but it can also lead to frustration if the challenge curve is steep or unclear.

7. Characters – Living Items and Skill Containers. In some games—Pokémon, for example—characters themselves function as a special category of item or skill container. They blend the mechanics of inventory and progression, acting simultaneously as tools, companions, and progression markers.

## Pokémon

<img src='../img/game/pokemon.svg' height='600'>

In the image above and the following images:

* **Arrow:** Indicates that one element benefits from another — either by producing more or by operating more efficiently.
* **Rectangle:** Represents collectable or completable items. Completing these tasks is generally desirable. Rare items encountered unexpectedly can act as “surprises,” triggering dopamine. Most items help reduce the difficulty of solving problems and are often obtained after completing a task.
* **Circle:** Denotes repeatable problem sets. These sets may exist at different levels, such as map-level, room-level, enemy-level, or skill-level (图、室、敌、技).
* **Diamond:** Signifies accumulable currency. This currency can be exchanged for useful items, improve efficiency, satisfy curiosity, or purchase rare/high-value goods.
* **Colored shapes:** These represent items or activities that are inherently desirable on their own. When linked to colored shapes, the transparent shapes become desirable as proxies, gaining value through association. The darker the color, more motivated the mechanic, but not add up.

Using Pokémon Red and Green as an example:

The main walkthrough path is largely linear, and unlike roguelike games, relatively few players replay it multiple times. This path represents the core progression that players focus on, since “beating the game” is widely seen as an achievement. Along the way, completing gym challenges and collecting badges provides additional milestones and a sense of accomplishment.

Defeating enemies rewards players with coins and experience points. On their own, these forms of “virtual currency” are not intrinsically desirable — they act as proxies for something more valuable. Coins can be exchanged for items that make problem-solving easier, similar to using a cheat sheet to look up answers or cheating to get a certificate.

If the items themselves are visually appealing, like Pokémon, they become inherently desirable. However, in most cases items are functional, like medicine pills — useful but not directly enticing, unlike a beautifully presented meal at a restaurant.

Pokémon characters stand out because they’re cute and engaging. The act of catching them is rewarding in itself, and once players realize that these creatures also help them solve the challenges they care about, their desirability increases further — much like the way an Apple MacBook Air is both aesthetically appealing and functionally powerful.

## Super Mario Bros.

<img src='../img/game/mario.svg' height='300'>

Pokémon is a classic RPG, whereas **Mario** is an action game.

1. In **Mario**, you can’t use coins or experience points to buy upgrades or improve your abilities for future challenges. The only RPG-like element is starting a new level as Super Mario with an extra life — but even that feels more like part of the challenge than an upgrade or “cheat.”
2. Coins are not useless, though. Collecting 100 coins grants an extra life, which gives you more chances to progress along the path.
3. Another appeal of coins is the competitive aspect — players like to compare who can achieve the highest score in a single run.
4. Unlike **Pokémon**, the original *Super Mario Bros.* is often replayed many times because it’s difficult to progress far in a single attempt and you usually have to start over. In this sense, it’s somewhat “roguelike,” although the levels themselves don’t change much between runs.
5. Also unlike **Pokémon**, your skills in **Mario** improve rapidly through practice. In **Pokémon**, improvement comes mainly from leveling up your creatures and acquiring better abilities, with relatively few mechanics for players to master. This makes **Mario** feel more like a pure action (ACG) game.

## Duolingo

<img src='../img/game/duolingo.svg' height='500'>

Duolingo incorporates game elements that seem inspired by **Candy Crush**, which was a huge success around the time Duolingo launched. Many of the mechanics found in tile-matching mobile games are echoed in Duolingo’s design.

1. In most games, the “lexemes” or tasks players master are not directly useful in the real world. In a gamified education app, however, mastering these elements is the core motivation — learning itself is the reward.
2. Duolingo lets users buy hearts to continue, similar to purchasing extra chances in a mobile game. In a testing context this would feel like cheating on an exam, but because Duolingo is a learning app rather than a testing app, mistakes shouldn’t be overly punishing. By using hearts or energy, Duolingo creates a monetization pathway for serious users, but this isn’t “designed cheating” in the RPG sense — it’s a way to balance learning with engagement.
3. Duolingo’s main motivational force is people’s desire to master a new skill. Its XP system, leaderboards, and daily quests provide some external motivation, but these features aren’t as strong or as compelling as the intrinsic goal of learning itself. As seen in many console games, leaderboards and streak systems alone rarely drive long-term engagement unless paired with strong core gameplay or meaningful progress.

## Slime Rancher

<img src='../img/game/slime.svg' height='500'>

1. In **Slime Rancher**, collecting and raising slimes, harvesting the “plorts” (or other resources) they produce, and selling those resources form the core gameplay loop — much like defeating enemies or using skills in a traditional RPG to gain rewards.
2. The plorts or resources produced by slimes act as the equivalent of **gold coins or rewards**, which players can then use to purchase upgrades or expand their ranch.
3. Upgrading and expanding the ranch is structured as a series of small, discrete stages — similar to clearing levels or unlocking new areas in a game. Each new section offers new types of slimes, resources, and challenges, creating a sense of steady progression.
4. Completing major upgrades and unlocking all areas typically signals that you’ve reached the main content of the game, much like beating the “main quest” in an RPG or clearing the gyms in Pokémon.

In other words, **Slime Rancher** uses the *collect–raise–harvest–upgrade* loop as its core experience. The resources act as renewable currency, the ranch serves as a customizable hub, and progression comes from unlocking new areas and slimes. This design combines the satisfaction of farming and resource management (like *Stardew Valley*) with the collectible creature aspect of Pokémon, all wrapped in a first-person exploration and action format.