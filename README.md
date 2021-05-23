# tic-tac-toe-minimax
Tic-Tac-Toe дээр Minimax AI алгоритмын хэрэгжилт 

<p align="center">
	<img src="https://raw.githubusercontent.com/anhbaysgalan1/tic-tac-toe/master/preview/minimax_img.png"></img>
</p>

## Оршил
AI ашиглан тогмоолыг шийдвэрлэхийн тулд хайлтын модон дээр суурьласан min-max алгоритмыг хэрэгжүүлж байна. Тоглоомын модонд зангилаа бүрт т

2-р хэсэгт зангилаанаас тоглоомиын хариу үйлдлийн шийдвэрүүдийг гаргаж эхэлдэг . Энэхүү үйлдлүүд нь модны үе болгонд хийгдэж байдаг ба хэрвээ тоглоомын самбар дүүрсэн тохиолдолд тэнцсэн гэж үзнэ.

## Minimax гэж юу вэ?
Minimax нь 2 тоглогчтой тоглоом дээр хэрэгждэг алгиритм tic-tac-toe, шатар гэх мэт тоглоомууд дээр хэрэгжиж болдог. Математик дүрслэлд: нэг тоглогч ялдаг (+1) нөгөө тоглогч ялагддаг (-1) or эсвэл хэн ч ялахгүй байж болох боломжтой. (0).

## Хэрхэн ажилладаг вэ?
Рекуссив хайлттай алгоритм юм. Одоогийн тоглоомын state дээр тулгуурлаж дараагийн боломжит үйлдлийг тооцоолдог, дараа бүх боломжит үйлдлээр тоглож үздэг ба тоглоом үйлдэлгүй болох хүртэл ажилладаг. (ажиллууллж *min* and *max*) 
## Understanding the Algorithm
ЭНэ алгормит нь Algorithms in a Nutshell гэх номонд дурдагддаг.(George Heineman; Gary Pollice; Stanley Selkow, 2009). Pseudocode:

```
minimax(state, depth, player)

	if (player = max) then
		best = [null, -infinity]
	else
		best = [null, +infinity]

	if (depth = 0 or gameover) then
		score = evaluate this state for player.    #Тоглогчийн state ийн шинэчлэх хэсэг
		return [null, score]

	for each valid move m for player in state s do
		execute move m on s
		[move, score] = minimax(s, depth - 1, -player)
		undo move m on s

		if (player = max) then
			if score > best.score then best = [move, score]
		else
			if score < best.score then best = [move, score]

	return best # хамгийн шилдэг үйлдлийг тооцоолох
end
```

Pseudocode оо той нийлүүлж ажиллуулах хэсэг Python. Python нийт холбосон ажиллуулж байгаа хэсэг нь repo-д байгаа болно:
> board = [
>	[0, 0, 0],
>	[0, 0, 0],
>	[0, 0, 0]
> ]

> MAX = +1

> MIN = -1

MAX нь X эсвэл O ба MIN нь O эсвэл X, аль нь ч байж болно. Тоглоомын хавтан 3x3.

```python
def minimax(state, depth, player):
```
* **state**: Одоогийн тоглоомын байдал tic-tac-toe (зангилаа)
* **depth**: Зангилаан дээр байх тоглоомын index
* **player**: *MAX* эсвэл *MIN* тоглогч

```python
if player == MAX:
	return [-1, -1, -хязгааргүй]
else:
	return [-1, -1, +хязгааргүй]
```

2 тоглогч байж болох хамгийн муу онооноос эхлэнэ. Хэрвээ тоглогч нь MAX бол,оноо нь -хязгааргүй. Хэрвээ тоглогч MIN бол, оноо нь +хязгааргүй. **Note:** *хязгааргүй нь * inf ийн alias болно (Python дээр байдаг math ийн liblary гаас авсан болно).

Хавтан дээрхи хамгийн шилдэг үйлдэл нь [-1, -1] (row болон column) гэх мэт бүх зүглүү.

```python
if depth == 0 or game_over(state):
	score = evaluate(state)
	return score
```

Хэрвээ depth нь 0 байвал, тоглолт үргэлжлэх боломжгүй.Хэрвээ аль нэг тоглочг нь ялсан тохиолдолд MAX, MIN нь дууссан. Тэгхээр тухайн үед хадгалж байсан бүх state ийг буцаана.
a
* If MAX ялвал: return +1
* If MIN ялвал: return -1
* Else: return 0 (тэнцэх)

Одоо рекурсив хэсэг эхлэнэ.

```python
for cell in empty_cells(state):
	x, y = cell[0], cell[1]
	state[x][y] = player
	score = minimax(state, depth - 1, -player)
	state[x][y] = 0
	score[0], score[1] = x, y
```

Бүх боломжит үйлдэлд (empty cells):
* **x**: receives cell row index
* **y**: receives cell column index
* **state[x][y]**: [боломжит_row][боломжит_col] MAX эсвэл MIN дээр хэрэгжүүлэх хэсэг
* **score = minimax(state, depth - 1, -player)**:
  * state: is the current board in recursion;
  * depth -1: index of the next state;
  * -player: хэрвээ тоглогч MAX байвал(+1) нөгөөдөх нь MIN (-1) гэх мэт.

Нүүдэл нь (+1 or -1) 

Одоогийн хэсэг нь нүүдлийг байж болох хамгийн сайн score той харьцуулах.

```python
if player == MAX:
	if score[2] > best[2]:
		best = score
else:
	if score[2] < best[2]:
		best = score
```

Алгоритмын сүүлийн хэсэг:

```python
def minimax(state, depth, player):
	if player == MAX:
		best = [-1, -1, -хязгааргүй]
	else:
		best = [-1, -1, +хязгааргүй]

	if depth == 0 or game_over(state):
		score = evaluate(state)
		return [-1, -1, score]

	for cell in empty_cells(state):
		x, y = cell[0], cell[1]
		state[x][y] = player
		score = minimax(state, depth - 1, -player)
		state[x][y] = 0
		score[0], score[1] = x, y

		if player == MAX:
			if score[2] > best[2]:
				best = score
		else:
			if score[2] < best[2]:
				best = score

	return best
```

## Game Tree
Below, the best move is on the middle because the max value is on 2nd node on left. Хамгийн шилдэг үйлдэл нь дунд нь байгаа учир нь max утга нь 2 дох зангилааны зүүн хэсэгт байрлаж байгаа

<p align="center">
	<img src="https://raw.githubusercontent.com/anhbaysgalan1/tic-tac-toe/master/preview/tic-tac-toe-minimax-game-tree.png"></img>
</p>

Хэрвээ сайн харвал depth нь боардны боломжит бүх үйлдэлтэй тэнцүү.

Тоглоомын мод:

<p align="center">
	<img src="https://raw.githubusercontent.com/anhbaysgalan1/tic-tac-toe/master/preview/simplified-g-tree.png"></img>
</p>

Энэхүү мод нь 11 зангилаатай. Бүтэн тоглоомын мод нь 549.946 зангилаатай! Та статик global хувьсагч бичиж тэрийгээ ихэсгэж багасган minimax алгоримтыг function болгон дээр дуудаж ажиллуулах боломжтой.

Шатар гэх мэт илүү төвөгтэй тоглоомонд бүхий нь тоглоомын модонд хайхад хэцүү байдаг, гэхдээ Alpha–beta прунин нь minimax ийг хурдасгах боломжтой аргаглалуудын нэг. Энэ нь модны хэрэгцээгүй мөчрүүдийг зангилаанууд дээр устгаж ажилладаг.  Илүү их мэдээллийг:

* Book: George T. Heineman; Gary Pollice; Stanley Selkow. Algorithms in a nutshell. O'Reilly, 2009.
* Wikipédia: <https://en.wikipedia.org/wiki/Minimax>
* Nanyang Technological University: <https://www.ntu.edu.sg/home/ehchua/programming/java/JavaGame_TicTacToe_AI.html>
