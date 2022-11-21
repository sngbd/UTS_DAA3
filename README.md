# UTS_DAA3

## Manual
| Tombol       | Deskripsi    |
| -----------  | -----------  |
| Klik kanan   | Atur start box (pertama) dan target box (kedua) |
| Klik kiri    | Atur wall |
| Spasi        | Mulai algoritma |

Perbandingan algoritma dilakukan dengan menggunakan flag `--maze`
```
python dijkstra.py --maze
```
dan
```
python a-star.py --maze
```

## Screenshots
### Dijkstra
<img src="./screenshots/dijkstra.png" alt="drawing" width="500"/>

### A*
<img src="./screenshots/a-star.png" alt="drawing" width="500"/>

## Legenda
| Warna        | Deskripsi    |
| -----------  | -----------  |
| ![#00C8C8](https://placehold.co/15x15/00C8C8/00C8C8.png)   | Start Box |
| ![#C8C800](https://placehold.co/15x15/C8C800/C8C800.png)   | Target Box |
| ![#00C800](https://placehold.co/15x15/00C800/00C800.png)   | Visited Box |
| ![#C80000](https://placehold.co/15x15/C80000/C80000.png)   | Queued Box |
| ![#0000C8](https://placehold.co/15x15/0000C8/0000C8.png)   | Path |
| ![#5A5A5A](https://placehold.co/15x15/5A5A5A/5A5A5A.png)   | Wall |
| ![#323232](https://placehold.co/15x15/323232/323232.png)   | Untracked Box |