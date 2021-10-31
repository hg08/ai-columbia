参考文献：

1. Artificial Intelligence: A Modern Approach, 3rd Edition Russell & Norvig, Chapter 5.1-5.5

Please note: This book is strongly suggested but is not mandatory to complete the course.

2. Checkers, Solved! http://spectrum.ieee.org/computing/software/checkers-solved
3. Google's AlphaGo Beat a Go World Champion: https://www.theatlantic.com/technology/archive/2016/03/the-invisible-opponent/475611/
4. Poker is solved too!  WIRED: Inside Libratus, the Poker AI That Out-Bluffed the Best Humans: http://www.wired.com/2017/02/libratus/







第二篇文章(含概念的中文翻译)　来自　IEEE SPECTRUM　(2007, 6,2)

- Article 
- [Computing](https://spectrum.ieee.org/computing)
- [Software](https://spectrum.ieee.org/computing/software)

2 Jul 2007 | 14:42 GMT

# Checkers, Solved!

## Make no mistakes and it's a draw, says computer scientist　无错误，打成平局



By Suhas Sreedhar

Advertisement

19 July 2007—You might have to find a new game to play on your computer or cellphone soon, because checkers will only frustrate you. Even if you play it perfectly—without any mistakes, choosing the best strategy in each situation—you’ll have absolutely no chance of winning. One of the most popular board games in history, checkers has been definitively proved to end in a draw when played perfectly by both sides, according to Jonathan Schaeffer, professor of computer science, and his colleagues at the University of Alberta, Edmonton, Canada. They published their proof today on the Web site of the journal *Science*.

It took Schaeffer nearly 16 years to complete his checkers odyssey(历程). He began by inventing [Chinook](http://www.cs.ualberta.ca/~chinook), the world’s first computer program to win a world championship against a human in checkers, or any other game, for that matter. The program, created in 1989, draws from a library of stored opening moves that had been played by grandmasters, an endgame database that traces backward from the final results of games (wins, losses, or draws), and a deep-search algorithm that makes decisions during play based on evaluating all possible outcomes a certain number of moves ahead.

![Chinook, a checkers playing computer program](https://spectrum.ieee.org/img/check01-1404744072573.jpg)Photo: Jonathan Schaeffer**Man vs. Machine:** Chinook, a checkers playing computer program, played champion Marion Tinsley [right] at the first Man v. Machine World Championship match in 1992, in London. Tinsley, beat the program then, but had to withdraw from a rematch in 1994. Chinook played a key role in proving that checkers, when played perfectly by both sides always ends in a draw.

In 1990, Chinook won the right to compete in the World Championship by coming in second place at the United States National Open Checkers Championship to Marion Tinsley, considered to be the greatest checkers player who ever lived. Chinook was all set to face Tinsley in the World Championship, but the American Checker Federation (ACF) and the English Draughts Association (EDA) had not sanctioned the match. Tinsley, wanting to face the program, resigned his title in protest. The ACF and EDA soon created the Man vs. Machine World Championship to accommodate the match. Chinook lost to Tinsley, with two wins to Tinsley’s four. In 1994, Chinook was retooled with more information, including previous strategies used by Tinsley, and faced off against the grandmaster in a rematch. All six games played resulted in draws. Tinsley, who was suffering from pancreatic cancer, withdrew from the tournament and died seven months later. Chinook was declared the Man vs. Machine World Champion and went on to defend its title against grandmaster Don Lafferty by winning one match, losing one, and then drawing 18. After that defense, Schaeffer retired Chinook from playing and put it to use in helping to solve checkers.

Solving checkers, a game played on a board with 64 squares using 12 black and 12 white or red pieces, was a daunting(令人生畏的) task. There are 500 billion billion ($5 x 10^20$) possible situations that could arise while playing. Strongly solving the game or computing all of these possible positions would have taken decades, says Schaeffer. Instead, he implemented a two-pronged search technique(二叉搜索技术) that concluded with the game being a draw by examining only a fraction of all the possible game scenarios.

First, he constructed databases of endgames(游戏终点), building backward from all the possible wins, losses, or draws that checkers could conclude with. A so-called backward-searching algorithm(反向搜索算法) built the path of situations that would have led to these endgames all the way to the point where there were 10 game pieces on the board. The result is a database of 39 trillion positions compressed using a homebrew(自制的) algorithm into an average of 237 gigabytes for an average of 154 positions per byte of data.

When Schaeffer first developed these databases, it took him seven years—from 1989 to 1996—to build backward from the endgame to the point where there were eight pieces on the board. Deeming that there wasn’t enough horsepower or RAM available to compute any further, in 1997 he suspended the project. When he resumed the project in 2001, computing power had so improved that the endgame databases that had taken years to compute were redone in the course of a month. From there the eight-piece scenarios were extended back to 10-piece scenarios.

The next step was to use a forward-search technique(正向搜索技术), such as the ones chess software typically rely on to figure out how to get to those 10-piece situations from the beginning of the game, when all 24 pieces are on the board.

This forward search, however, was not performed in the way Chinook or IBM’s Deep Blue—the chess-playing computer that defeated world champion Garry Kasparov 10 years ago—would have done it. Those programs used deep-search algorithms to make their next moves by analyzing all possible situations that are one-move deep, then all possible situations that are two-moves deep, and so on.

Instead, Schaeffer and his colleagues used a technique called ”best first” to prioritize searching various positions and lines of play. At a given position in the game there are several possible moves that can be made. Instead of exploring all of these moves to their final outcomes using deep search, Schaeffer's team used Chinook to provide a measure of what the strongest line of play would be—what would most likely result in a win in the fewest moves. This line of play was evaluated first. If it did result in a win, then there was no need to search any other parallel lines of play, because the entire line was already known to result in a strong win. A win in such an instance is not a characteristic of perfect play by both sides; perfect play means that each side will try to win in as few moves as possible, or delay losing in as many moves as possible. Since a win was achieved so quickly, it means the losing side made a mistake and did not play perfectly. Entire lines of play branching from various positions were eliminated this way, vastly reducing the number of lines that had to be deeply explored. By applying such a technique, Schaeffer’s team was able to solve checkers using the least amount of effort. Of the 5 x 1020 possible positions, Schaeffer needed to evaluate only 1014 to prove that checkers, played perfectly, results in a draw.

Players had suspected for a while that checkers would result in a draw, says Schaeffer. Human players draw so frequently when playing that since 1934 championship tournaments require the first three half-moves (black-white-black) to be done randomly from a list of accepted openings in order to reduce the number of draws. Schaeffer’s proof solved checkers for 19 different openings, all of which end in draws. There are 300 total tournament openings, but many of these were determined to either be mirrors of other positions or altogether irrelevant to the proof because they lead to positions common to other openings.

Solving checkers has taken a big monkey off Schaefer’s back. The fact that the game wasn’t solved for every possible position and then tucked away in a database doesn’t seem to bother him. ”Well, the checkers players would love it, because [then] you’ve got this oracle that can tell them everything—answer every single unanswered question in the game of checkers,” he says. ”But first of all, I don’t have the patience to do it. And second of all, I don’t have the technology to do it.” Even with the best data-compression techniques, Schaeffer says, the amount of storage required to solve all possible positions of checkers would exceed even the capacity of the world’s biggest supercomputers with tens of petabytes (1015) of storage by an order of magnitude. That puts it—at the earliest—at least a decade away.

But there is little motivation for Schaeffer to pursue such a quest. He has solved checkers and has painstakingly verified that none of the data were corrupt or inaccurate. Vasik Rajlich, an international chess master [profiled in ”[Dream Jobs](https://spectrum.ieee.org/feb07/4899),” IEEE Spectrum, February 2007 described the accomplishment as the latest in a line of games that have been solved computationally. ”Every now and then some game is solved,” he says. ”And now we can ’check this box’ for a rather major game.” So far researchers have solved Connect Four, Qubic, Go-Moku, Nine Men’s Morris, and Awari.

As for the question of solving a game like chess, which people suspect will also result in a draw, the amount of data is even more monstrous. The number of positions in checkers is thought to be roughly the square root of the number of positions in chess. That’s somewhere in the order of 1040 to 1050 positions. Schaeffer says that even with the two-pronged technique he used in solving checkers, a breakthrough such as quantum computing would be needed to even attempt to solve chess. But he isn’t quick to rule out the possibility. ”The one thing I’ve learned in all of this is to never underestimate the advances in technology,” he says.





第三篇文章()

[TECHNOLOGY](https://www.theatlantic.com/technology/)

# How Google's AlphaGo Beat a Go World Champion

Inside a man-versus-machine showdown

[CHRISTOPHER MOYER](https://www.theatlantic.com/author/christopher-moyer/)

MAR 28, 2016

![img](https://cdn.theatlantic.com/assets/media/img/mt/2016/03/AP_609857013769/lead_720_405.jpg?mod=1522795858)

The South Korean professional Go player Lee Sedol reviews the match after finishing against Google's artificial-intelligence program, AlphaGo.LEE JIN-MAN / AP

On March 19, 2016, the strongest Go player in the world, Lee Sedol, sits down for a game against Google DeepMind’s artificial-intelligence program, AlphaGo. They’re at the Four Seasons Hotel in Seoul’s Gwanghwamun district, and it’s a big deal: Most major South Korean television networks are carrying the game. In China, 60 million people are tuning in. For the English-speaking world, the American Go Association and DeepMind are running an English-language livestream on YouTube, and 100,000 people are watching. A few hundred members of the press are in adjacent rooms, watching the game alongside expert commentators.

Sign up for The Atlantic Politics & Policy Daily.Know what mattered that day, find out what our editors are reading, and more.Email Address (required)Sign UpThanks for signing up!

The game room itself is spare: a table, two black leather chairs, some cameras. Three officials presiding over the match sit in the back. Across from Lee sits Aja Huang, one of AlphaGo’s lead programmers; and beside him is a computer monitor that displays AlphaGo’s move choices. Huang’s job is to physically place AlphaGo’s pieces on the board. AlphaGo itself is not any one machine—it’s a piece of distributed software supported by a team of more than 100 scientists.

Tonight, Lee Sedol is supported by one 33-year-old human brain and approximately 12 ounces of coffee.

Most people are betting on Lee to win.



At its core, the game of Go, which originated in China more than 2,500 years ago, is an abstract war simulation. Players start with a completely blank board and place black and white stones, one at a time, to surround territory. Once placed, stones do not move, and they’re removed only if they’re “killed”—that is, surrounded completely by the opponent’s stones. And so the game goes—black stone, white stone, black stone, white stone—until the board is covered in an intricate tapestry of black and white.

The rules of Go are simple and take only a few minutes to learn, but the possibilities are seemingly endless. The number of potential legal board positions is:

> 208,168,199,381,979,984,699,478,633,344,862,770,286,522,
>
> 453,884,530,548,425,639,456,820,927,419,612,738,015,378,
>
> 525,648,451,698,519,643,907,259,916,015,628,128,546,089,
>
> 888,314,427, 129,715,319,317,557,736,620,397,247,064,840,
>
> 935.

That number—which is greater than the number of atoms in the universe—was only [determined in early 2016](http://tromp.github.io/go/legal.html). Because there are so many directions any given game can move in, Go is a notoriously difficult game for computers to play. It has often been called the “Holy Grail” of artificial intelligence.

In February 2016, DeepMind researchers published a [paper ](http://www.nature.com/articles/nature16961.epdf?referrer_access_token=S7uXxNIroKd-0ITVLIW9mdRgN0jAjWel9jnR3ZoTv0OivKk3lXs6SxMz535byYwHnl5-dYSTNp9HCujoL8AwwR39NrI-N0UvQYqpO-G6W-1I6_OXAuVukQ08lbvopRKY2yVJlWWUJvj6gL5qyO8kI3FwsIuw4iSKC-s4RoTnZdVG8WevGFeuMdJ2Zl9cZF7yixAslaF4yKEx3rom3ZszmZBsyuq-9RAnx1XZac4keCI%3D&tracking_referrer=www.nature.com)in *Nature* that announced that they’d done something remarkable: Not only could their AI beat every other Go-playing program in the world, but it had beaten a professional named Fan Hui, the current European champion. AlphaGo didn’t just beat Fan Hui—it beat him soundly in every match of a five-game series.

The news rippled through the Go world. It was widely believed that an AI strong enough to beat a professional player was still at least a decade away, and that milestone had been quietly crushed. The next logical step was to discover what AlphaGo’s upper limit might be, and Lee was the logical choice for humanity’s champion.

\* * *

It’s curious that when someone is really good at something, we call them a “machine.” *Lee Sedol is a Go-playing machine*, enlisted to beat, well, a Go-playing machine*.*

Lee is not a machine, of course. He is a particularly young-looking 33-year-old. He is a man who gets up and eats breakfast, takes naps, feels embarrassed, gets nervous. Within the Go world, however, nobody is scarier(更加可怕) than Lee, who plays with an unnerving confidence. He creates situations that should end in disaster and then—effortlessly to the observer—turns them on their heads, like a magic trick, steamrolling his opponents.

In the weeks leading up to Game 1, the DeepMind team expressed humble optimism about AlphaGo’s chances of winning. Lee is more brazen; at a press conference with Demis Hassabis, DeepMind’s  founder, he claimed that for him, the challenge isn’t whether he’ll beat AlphaGo, but whether he’ll beat it 5-0 or 4-1.

Lee is not being arrogant. He’s making an objective evaluation based on AlphaGo’s play against Fan Hui, which he had seen. And Fan Hui and Lee Sedol are not exactly comparable in strength. In the Go world, Lee is Michael Jordan, Tiger Woods, Roger Federer. He is one of those rare virtuosos who defines his era, who sets the pace for the rest of the world. He is orders of magnitude more talented than Fan Hui, who is no slouch. And Fan Hui has actually beaten AlphaGo outside of the formal five-game match DeepMind publicized. With much stricter time settings, he won two out of five matches, giving AlphaGo a much harder time.

Other Korean professionals joke that they’re envious of Lee, that they feel the DeepMind Challenge Match is the easiest million dollars a top-level player could ever make.

\* * *

Minutes into Game 1, all expectations change. It’s immediately clear that Lee Sedol is not playing the same AlphaGo that Fan Hui did back in London. That version of AlphaGo played steadily but also passively, peacefully. The AlphaGo playing in Seoul is happy to engage in aggressive fighting with Lee. Lee has played an unconventional opening, trying to throw AlphaGo off, but it is not working.

AlphaGo has had nearly five months to improve—and it is always improving, playing itself millions of times, incrementally revising its algorithms based on which sequences of play result in a higher win percentage. As you are reading this, AlphaGo is improving. It does not take breaks. It does not have days when it just doesn’t feel like practicing, days when it can’t kick its electronic brain into focus. Day in and day out, AlphaGo has been rocketing towards superiority, and the results are staggering.

Lee goes on to lose Game 1, resigning after 186 moves. The turning point in the mental game seems to have come at White’s move 102. It’s a sharp, unexpected invasion, an aggressive move that invites complicating fighting positions. It is, in truth, exactly the kind of move Lee is known for. In this moment, [a full range of reactions](https://www.youtube.com/watch?v=1bc-8iomgB4&t=150m0s) washes over Lee: shock, surprise, acceptance, and finally grim resolution. His jaw drops, and after several seconds, he sits back in his chair and smiles, perhaps amused but certainly taken aback. Then his expression grows serious, and his hand rubs the back of his neck, a tic he exhibits when he’s thinking hard or feeling nervous.

The moment he throws in the towel, he begins revising moves, pushing stones around the board to play out alternate variations, experimenting with the roads untraveled. We can see him work through it, trying to pinpoint exactly how he has lost.

He has taken the machine’s measure. Going into Game 2, he understands the magnitude of what he’s up against. The following evening will be the real first test. But in the press conference following Game 1, he downgrades his perceived chances of winning to 50 percent.

\* * *

In Game 2, Lee exhibits a different style, attempting to play more cautiously. He waits for any opening he can exploit, but AlphaGo continues to surprise. At move 37, AlphaGo plays an unexpected move, what’s called a “shoulder hit” on the upper right side of the board. This move in this position is unseen in professional games, but its cleverness is immediately apparent. Fan Hui would later say, “I’ve never seen a human play this move. So beautiful.”

And Lee? He gets up and *walks out of the room.* For a moment it’s unclear what’s happening, but then he re-enters the game room, newly composed, sits down, and plays his response. What follows is a much closer game than Game 1, but the outcome remains the same. Lee Sedol resigns after 211 moves.

That night, Lee and a group of his colleagues stay up until 6:00 a.m. brainstorming possible strategies. They look for a silver bullet, an Achilles heel, any way to secure a win. He’ll now need three wins in a row to win the series.

\* * *

Game 3 ends in another loss—after four hours of grueling play, Sedol resigns. He’s playing some of the finest Go of his career, but he simply can’t chip away at the AI’s armor. It’s clear that AlphaGo’s strength surpasses even what was on display in Games 1 and 2. Later, David Ormerod, an American commentator, will write that watching AlphaGo’s Game 3 win made him feel “[physically unwell](https://gogameguru.com/alphago-shows-true-strength-3rd-victory-lee-sedol/).”

At the post-game conference, Lee looks 10 years older. Amidst a barrage of camera flash bulbs he apologizes to the entire world at once. “I apologize for being unable to satisfy a lot of people’s expectations,” he says. “I kind of felt powerless.” Even the DeepMind researchers, who have a deep admiration for Lee, seem more somber than jubilant at their own victory. There is a sense that something has changed. Gu Li, one of Lee’s long-term friends and rivals, comments on Chinese TV that Lee is fighting “a very lonely battle against an invisible opponent.”

\* * *

Lee has already lost the series, but going into Game 4 his new goal is to win at least once.

Lee, playing white against AlphaGo’s black, tries yet another new style—a riskier strategy called *amashi*. This time the pressure is off, and we see some of the Lee Sedol magic bubble to the surface. Until now, AlphaGo has won by allowing Lee to take small profits in exchange for its own incremental advantages, and its superior calculation abilities have enabled it to come out on top each time. Now, Lee forces AlphaGo into an all-or-nothing fight. He will lose big or win big.

Then comes Lee’s move 78,  which will come to be called his “Hand of God” move. It’s a brilliant tactical play that AlphaGo does not account for. Over the course of the next several moves, the sequence becomes disastrous for AlphaGo, which apparently “realizes”—as much as it can have a realization—that it has been outsmarted. Its strategy begins to crumble.

In the end, finding no moves that improve its chances of winning, it begins playing nonsense moves, moves that actually reduce its own points. Finally, it resigns.

[After the match](https://www.youtube.com/watch?v=C2txn4igy-M), hundreds chant Sedol’s name as he approaches the stage. The jubilant grandmaster thanks everyone involved, saying that the warmth he feels in this moment makes losing the three preceding matches worth it.

There is one more surprise in store for the evening, however. At the press conference, Lee points out that in both this game and in Game 2 (the closest of his losses), AlphaGo has played black. Lee  requests to play black himself in the final game, removing the one advantage he may have. It feels as if, having climbed Everest after three failed attempts, Lee has asked to try it yet again, only blindfolded.

In Game 5, Lee employs a strategy similar to Game 4. For a time, the game is close, but AlphaGo proves once more that it finds small ways to cement any advantages it has, and once it pulls ahead, it’s very good at protecting its lead. Lee is forced to resign one last time, ending the series at four losses and one win. This time, there is no Hand of God.

\* * *

What does it mean? Not much, in and of itself. If AlphaGo had lost to Lee in March, it would only have been a matter of time before it improved enough to surpass him. Go is constantly evolving. What’s considered optimal play changes quickly. Humans have been honing our collective knowledge of the game for more than 2,500 years—the difference is that AlphaGo can do the same thing much, much faster.

The important thing to take away from this series is not that DeepMind’s AI can learn to conquer Go, but that by extension it can learn to conquer *anything easier than Go*—which amounts to *a lot* of things. The ways in which we might apply these revolutionary advances in machine learning—in machines’ ability to mimic human creativity and intuition—are virtually endless.

But it is with human hands that machines are built, at least for now. In a Reddit discussion, the computer-science scholar Andy Salerno puts it well: “AlphaGo isn’t a mysterious beast from some distant unknown planet. AlphaGo is us,” he wrote. “AlphaGo is our incessant curiosity. AlphaGo is our drive to push ourselves beyond what we thought possible.”

“Lee should feel no shame in his losses,” Salerno continued. “For AlphaGo could never demonstrate its abilities—*our* abilities—if Lee were not there to challenge it.”

[CHRISTOPHER MOYER](https://www.theatlantic.com/author/christopher-moyer/) is a writer and book designer based in Memphis, Tennessee.



第四篇文章(含中文概念)　https://www.wired.com/2017/02/libratus/

# INSIDE LIBRATUS, THE POKER AI THAT OUT-BLUFFED THE BEST HUMANS

![img](https://media.wired.com/photos/59267cfecfe0d93c4743060c/master/w_1200,c_limit/GettyImages-135579222_Feature.jpg)

ROB PALMER/GETTY IMAGES

FOR ALMOST THREE weeks, Dong Kim sat at a casino in Pittsburgh and played poker against a machine. But Kim wasn't just any poker player. This wasn't just any machine. And it wasn't just any game of poker.

Kim, 28, is among the best players in the world. The machine, built by two computer science researchers at Carnegie Mellon, is an [artificially intelligent system](https://www.wired.com/story/guide-artificial-intelligence/) that runs on a Pittsburgh supercomputer. And for twenty straight days, they played no-limit Texas Hold 'Em, [an especially complex form of poker](https://www.wired.com/2017/01/rival-ais-battle-rule-poker-global-politics/) in which betting strategies play out over dozens of hands.

About halfway through the competition, [which ended this week](https://www.wired.com/2017/01/mystery-ai-just-crushed-best-human-players-poker/), Kim started to feel like Libratus could see his cards. "I’m not accusing it of cheating," he said. "It was just that good." So good, in fact, that it beat Kim and three more of the world's top human players—a first for artificial intelligence.

During the competition, the creators of Libratus were coy about how the system worked—how it managed to be so successful, how it mimicked human intuition in a way no other machine ever had. But as it turns out, this AI reached such heights because it wasn't just one AI.



Libratus relied on three different systems that worked together, a reminder that modern AI is driven not by one technology but many. [Deep neural networks](https://www.wired.com/2015/04/jeff-dean/) get most of the attention these days, and for good reason: They power everything from image recognition to translation to search at some of the world's biggest tech companies. But the success of neural nets has also pumped new life into so many other AI techniques that help machines mimic and even surpass human talents.

Libratus, for one, did not use neural networks. Mainly, it relied on a form of AI known as [reinforcement learning](https://www.wired.com/2015/12/teaching-ai-to-play-atari-will-help-robots-make-sense-of-our-world/), a method of extreme trial-and-error. In essence, it played game after game against itself. Google's DeepMind lab used reinforcement learning in building AlphaGo, [the system that that cracked the ancient game of Go ten years ahead of schedule](https://www.wired.com/2016/05/google-alpha-go-ai/), but there's a key difference between the two systems. AlphaGo learned the game by analyzing 30 million Go moves from human players, before refining its skills by playing against itself. By contrast, Libratus learned from scratch.

Through an algorithm called counterfactual regret minimization, it began by playing at random, and eventually, after several months of training and trillions of hands of poker, it too reached a level where it could not just challenge the best humans but play in ways they couldn't—playing a much wider range of bets and randomizing these bets, so that rivals have more trouble guessing what cards it holds. "We give the AI a description of the game. We don't tell it how to play," says Noam Brown, a CMU grad student who built the system alongside his professor, Tuomas Sandholm. "It develops a strategy completely independently from human play, and it can be very different from the way humans play the game."

But that was just the first stage. During the games in Pittsburgh, a second system would analyze the state of play and focus the attention of the first. With help from the second—an "end-game solver" detailed in a [research paper](http://www.cs.cmu.edu/~noamb/papers/17-AAAI-Refinement.pdf)Sandholm and Brown published late Monday—the first system didn't have to run through all the possible scenarios it had explored in the past. It could run through just some of them. Libratus didn't just learn before the match. It learned while it was playing.

These two systems alone would have been effective. But Kim and the other players could still find patterns in the machine's play and exploit them. That's why Brown and Sandholm built a third system. Each evening, Brown would run an algorithm that could identify those patterns and remove them. "It could compute this overnight and have everything in place the next day," he says.

If that seems unfair, [well, it's how AI works](https://www.wired.com/2017/01/ai-conquer-poker-not-without-human-help/). It's not just that AI spans many technologies. Humans are so often in the mix, too, actively improving, running, or augmenting the AI. Libratus is indeed a milestone, displaying a breed of AI that could play a role with everything from Wall Street trading to cybersecurity to auctions and political negotiations. "Poker has been one of the hardest games for AI to crack, because you see only partial information about the game state," says Andrew Ng, who helped found Google's central AI lab and is now chief scientist at Baidu. "There is no single optimal move. Instead, an AI player has to randomize its actions so as to make opponents uncertain when it is bluffing."

Libratus did this in the extreme. It would randomize its bets in ways that are well beyond even the best players. And if that didn't work, Brown's nighttime algorithm(夜间算法) would fill the hole. A finanical trader could work the same way. So could a diplomat. It's a powerful and rather unsettling proposition: a machine that can out-bluff a human.