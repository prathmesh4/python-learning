from dataclasses import dataclass,field

@dataclass(order=True)
class Score:
    points:int
    player: str =field(compare=False)
    level: int = field(default=1,compare=False)
    timestamp:str= field(default="", compare=False,repr=False)
class Leaderboard:
    def __init__(self):
        self.scores=[]
    def add_score(self,score):
        self.scores.append(score)
        self.scores.sort(reverse=True)
    def top(self,n):
        return self.scores[:n]
    def display(self):
        print("Leaderboard:")
        for rank,score in enumerate(self.scores,start=1):
            print(
                f"{rank:<3} {score.player:<10}"
                f"{score.points} pts (Level {score.level})"
            )            
leaderboard=Leaderboard()
scores=[
    Score(970, "Prathmesh", 3, "2026-10-31 10:00"),
    Score(950, "Karan", 5, "2026-10-31 10:05"),
    Score(820, "Amit", 4, "2026-10-31 10:10"),
    Score(870, "Priya", 4, "2026-10-31 10:15"),
    Score(680, "Neha", 2, "2026-10-31 10:20"),
    Score(820, "Prathmesh", 3, "2026-10-31 10:25"),
    Score(720, "Sneha", 3, "2026-10-31 10:30"),
    Score(900, "Arjun", 5, "2026-10-31 10:35"),
    Score(790, "Riya", 3, "2026-10-31 10:40"),
    Score(850, "Vikram", 4, "2026-10-31 10:45"),
]
for score in scores:
    leaderboard.add_score(score)
print("Sorting by points (descending):")
for score in leaderboard.scores:
    print(score)
amit_score = Score(820, "Amit", 4)
prathmesh_score = Score(820, "Prathmesh", 3)
print("Equality Check:")
print(
    f"{amit_score.points} pts ({amit_score.player}) == "
    f"{prathmesh_score.points} pts ({prathmesh_score.player}): "
    f"{amit_score == prathmesh_score}"
)
print("Top 3 Players:")
for rank, score in enumerate(leaderboard.top(3), start=1):
    print(
        f"#{rank}  {score.player:<10} "
        f"{score.points} pts  (Level {score.level})"
    )
leaderboard.display()

"""Leaderboard with Sorting
Ordered dataclasses with field(compare=...) controlling sort behavior
Create a Score dataclass with order=True:
- points: int (used in comparisons)
- player: str (compare=False — NOT used in comparisons)
- level: int with default 1 (compare=False)
- timestamp: str (compare=False, repr=False)

Create a Leaderboard class (regular class, not dataclass) that:
- Holds a list of Score objects
- add_score(score) — adds and sorts
- top(n) — returns top n scores
- display() — prints formatted leaderboard

Create 8-10 scores and demonstrate:
1. Sorting works by points only (not player name)
2. Two scores with same points but different players are considered equal by ==
3. Top 3 display
4. Full leaderboard display

Example output:

Leaderboard:
#1  Karan    950 pts  (Level 5)
#2  Priya    870 pts  (Level 4)
#3  Amit     820 pts  (Level 4)
...

820 pts (Amit) == 820 pts (Rahul): True  ← same points, player ignored
"""