# 1. Mục tiêu

Bài toán giải quyết trò chơi 8-Puzzle thông qua việc triển khai và so sánh hiệu suất của nhiều thuật toán tìm kiếm khác nhau. Hệ thống cung cấp tùy chọn để người dùng trải nghiệm các thuật toán như BFS, DFS, IDS, Uniform Cost, A*, IDA*, Greedy Best-First Search, Hill Climbing (bao gồm các biến thể), Simulated Annealing, Beam Search, Genetic Algorithm, Backtracking, cùng các thuật toán dành cho môi trường không chắc chắn như Uncertain BFS, Search with No Observations và Partially Observable DFS. Giao diện trực quan được thiết kế bằng Pygame giúp mô phỏng toàn bộ quá trình giải quyết bài toán.

# 2. Nội dung

## 2.1. Các thuật toán Tìm kiếm không có thông tin (Uninformed Search)

### Thành phần chính của bài toán tìm kiếm

#### Một bài toán tìm kiếm bao gồm các thành phần cơ bản sau:

- **Không gian trạng thái (State Space):** tập hợp tất cả các trạng thái có thể có của bài toán.
- **Trạng thái ban đầu (Initial State):** điểm bắt đầu quá trình tìm kiếm.
- **Tập hành động (Actions):** tập các hành động có thể thực hiện để chuyển từ trạng thái này sang trạng thái khác.
- **Hàm chuyển trạng thái (Transition Model):** mô tả kết quả của một hành động khi áp dụng lên trạng thái hiện tại.
- **Trạng thái đích (Goal Test):** điều kiện để xác định trạng thái đích đã đạt được.
- **Chi phí đường đi (Path Cost):** tổng chi phí của chuỗi hành động từ trạng thái ban đầu đến trạng thái đích (thường dùng trong tìm kiếm tối ưu như Uniform Cost Search).

#### Solution là gì?

Solution là một chuỗi các hành động hoặc trạng thái dẫn từ trạng thái ban đầu đến trạng thái mục tiêu (goal state). Trong bối cảnh của trò chơi 8-Puzzle, solution chính là chuỗi di chuyển các ô số để biến cấu hình ban đầu thành cấu hình mục tiêu (thường là sắp xếp từ 1–8, với ô trống ở vị trí cuối).

#### Hình ảnh gif của từng thuật toán khi áp dụng lên trò chơi

| <img src="assets/BFS.gif" width="200"/> | <img src="assets/IDS.gif" width="200"/> | <img src="assets/UC.gif" width="200"/> | <img src="assets/DFS.gif" width="200"/> |
|:--------------------------------:|:--------------------------------:|:--------------------------------:|:--------------------------------:|
| **Mô phỏng BFS**                 | **Mô phỏng IDS**                 | **Mô phỏng UCS**                 | **Mô phỏng DFS**                 |
#### Hình ảnh so sánh hiệu suất của các thuật toán

| **Criterion**   | **Breadth-First** | **Uniform Cost** | **Depth-First** | **Depth-Bounded** | **Iterative Deepening** |
|-----------------|-------------------|------------------|------------------|---------------------|--------------------------|
| **Complete?**   | yes*              | yes              | no               | no                  | semi                     |
| **Optimal?**    | yes**             | yes              | no               | no                  | yes**                    |
| **Time**        | O(b^d)            | O(b^{⌈C*/ε⌉})     | O(b^m)           | O(b^ℓ)              | O(b^d)                   |
| **Space**       | O(b^d)            | O(b^{⌈C*/ε⌉})     | O(bm)            | O(b^ℓ)              | O(bd)                    |

#### Một vài nhận xét về hiệu suất của các thuật toán trong nhóm này khi áp dụng lên trò chơi 8 ô chữ

    •Breadth-First Search (BFS):
        o	Luôn tìm ra lời giải tối ưu (nếu tồn tại).
        o	Tốn nhiều bộ nhớ do cần lưu trữ toàn bộ frontier.
        o	Hiệu quả với lời giải nông, nhưng dễ bị nghẽn với lời giải sâu.
    •Depth-First Search (DFS):
        o	Bộ nhớ thấp, nhưng dễ rơi vào vòng lặp vô hạn nếu không kiểm soát độ sâu.
        o	Không đảm bảo lời giải tối ưu.
    •Iterative Deepening Search (IDS):
        o	Kết hợp ưu điểm của DFS (ít bộ nhớ) và BFS (tìm lời giải tối ưu).
        o	Chi phí thời gian cao hơn do lặp lại tìm kiếm nhiều lần.
    •Uniform Cost Search:
        o	Tìm lời giải có chi phí thấp nhất (nếu chi phí mỗi bước khác nhau).
        o	Nếu mọi bước có cùng chi phí, tương tự như BFS.

## 2.2.	Các thuật toán tìm kiếm có thông tin (Informed Search)
### Thành phần chính của bài toán tìm kiếm
Ngoài các thành phần cơ bản giống tìm kiếm không có thông tin, các thuật toán có thông tin sử dụng thêm một yếu tố rất quan trọng:

•   Hàm heuristic (h(n)): ước lượng chi phí từ một trạng thái n đến trạng thái đích (goal state). Đây là “thông tin bổ sung” giúp hướng dẫn tìm kiếm hiệu quả hơn.

•   Hàm đánh giá (f(n)): tùy theo thuật toán:

    o   Greedy Best-First: f(n) = h(n)

    o   A*: f(n) = g(n) + h(n), trong đó g(n) là chi phí từ trạng thái ban đầu đến n

    o   IDA*: sử dụng A* lặp theo ngưỡng f(n)

Các heuristic phổ biến trong 8-Puzzle:

•   Misplaced Tiles: số ô sai vị trí

•   Manhattan Distance: tổng khoảng cách theo hàng và cột từ mỗi ô đến vị trí đúng của nó (hiệu quả hơn và phổ biến hơn)

#### Solution là gì?
Tương tự, solution là chuỗi hành động chuyển từ trạng thái ban đầu đến trạng thái đích. Với các thuật toán có thông tin, solution thường ngắn hơn và được tìm thấy nhanh hơn do thuật toán được dẫn đường bởi heuristic.
#### Hình ảnh gif của từng thuật toán khi áp dụng lên trò chơi


| <img src="assets/Greedy.gif" width="200"/> | <img src="assets/A_Star.gif" width="200"/> | <img src="assets/IDA_Star.gif" width="200"/> |
|:--------------------------------:|:--------------------------------:|:--------------------------------:|
| **Mô phỏng Greedy**                 | **Mô phỏng A_Star**                 | **Mô phỏng IDA_Star**                 |
#### Hình ảnh so sánh hiệu suất của các thuật toán

| **Tiêu chí**                      | **Greedy Best-First**     | **A\***                           | **IDA\***                              |
| --------------------------------- | ------------------------- | --------------------------------- | -------------------------------------- |
| **Sử dụng Heuristic?**            | Có (chỉ dùng h(n))        | Có (g(n) + h(n))                  | Có (g(n) + h(n))                       |
| **Hoàn tất (Complete)?**          | Không đảm bảo             | Có (nếu heuristic admissible)     | Có (nếu heuristic admissible)          |
| **Tối ưu (Optimal)?**             | Không                     | Có                                | Có                                     |
| **Độ phức tạp thời gian (Time)**  | O(b^m)                    | O(b^d)                            | O(b^d)                                 |
| **Độ phức tạp bộ nhớ (Space)**    | O(b)                      | O(b^d)                            | O(d)                                   |
| **Hiệu quả Heuristic ảnh hưởng?** | Rất lớn                   | Quan trọng nhưng ổn định hơn      | Cực kỳ quan trọng                      |
| **Nhận xét thêm**                 | Nhanh, nhưng dễ sai hướng | Cân bằng giữa tốc độ và chính xác | Dùng ít bộ nhớ hơn A\*, nhưng chậm hơn |

Chú thích:

b: branching factor (số nhánh trung bình từ mỗi trạng thái)

d: độ sâu của lời giải tối ưu

m: độ sâu tối đa của không gian trạng thái

#### Một vài nhận xét về hiệu suất của các thuật toán trong nhóm này khi áp dụng lên trò chơi 8 ô chữ
    • Greedy Best-First Search:
        o	Tìm nhanh do chỉ quan tâm đến h(n)
        o	Không đảm bảo lời giải tối ưu
        o	Có thể bị mắc kẹt nếu heuristic dẫn sai hướng
    • A_Star:
        o	Tìm lời giải tối ưu nếu heuristic là admissible (không vượt quá chi phí thực tế)
        o	Với heuristic tốt (Manhattan), rất hiệu quả cho 8-Puzzle
        o	Tốn nhiều bộ nhớ hơn Greedy
    • IDA_Star:
        o	Hiệu quả về bộ nhớ hơn A* (dùng DFS theo mức f(n))
        o	Tốc độ chậm hơn A* do lặp lại nhiều lần
        o	Cực kỳ hữu ích khi không đủ bộ nhớ cho A*


## 2.3. Các thuật toán tìm kiếm cục bộ (Local Search)
### Thành phần chính của bài toán tìm kiếm
Tìm kiếm cục bộ là phương pháp không theo dõi toàn bộ đường đi từ trạng thái ban đầu đến đích, mà chỉ quan tâm đến việc cải thiện trạng thái hiện tại. Các thành phần chính bao gồm:

•	Trạng thái hiện tại: một cấu hình của bài toán (ví dụ: cấu trúc 8-Puzzle hiện tại).

•	Hàm đánh giá (Evaluation function): thường là -h(n) (tức là càng ít lỗi thì giá trị càng cao).

•	Láng giềng (Neighbors): các trạng thái có thể đạt được từ trạng thái hiện tại bằng 1 bước di chuyển.

•	Tiêu chí dừng: trạng thái không thể cải thiện thêm (đỉnh cục bộ hoặc cực đại toàn cục).

Không cần lưu toàn bộ đường đi như các thuật toán trước.

#### Solution là gì?
Trong local search, “solution” không nhất thiết phải là đường đi tối ưu mà là một trạng thái đủ tốt hoặc cực đại cục bộ gần với trạng thái đích. 
#### Hình ảnh gif của từng thuật toán khi áp dụng lên trò chơi

| <img src="assets/Simple HC.gif" width="200"/> | <img src="assets/Steepest HC.gif" width="200"/> | <img src="assets/Stochastic HC.gif" width="200"/> |
|:--------------------------------:|:--------------------------------:|:--------------------------------:|
| **Mô phỏng Simple Hill Climbing**                 | **Mô phỏng Steepest Ascent Hill Climbing**                 | **Mô phỏng Stochastic Hill Climbing**                 |

| <img src="assets/SA.gif" width="200"/> | <img src="assets/Beam Search.gif" width="200"/> | <img src="assets/GA.gif" width="200"/> |
|:--------------------------------:|:--------------------------------:|:--------------------------------:|
| **Mô phỏng Simulated Annealing**                 | **Mô phỏng Beam Search**                 | **Mô phỏng Genetic Algorithm**                 |

#### Hình ảnh so sánh hiệu suất của các thuật toán

#### Một vài nhận xét về hiệu suất của các thuật toán trong nhóm này khi áp dụng lên trò chơi 8 ô chữ
    • Simple Hill Climbing:
        o	Dễ cài đặt nhưng dễ kẹt tại đỉnh cục bộ.
        o	Không quay lại trạng thái trước đó → có thể thất bại.
    • Steepest Ascent Hill Climbing:
        o	Tốt hơn simple do chọn neighbor tốt nhất.
        o	Nhưng vẫn có thể mắc kẹt tại đỉnh cục bộ hoặc plateau.
    • Stochastic Hill Climbing:
        o	Tránh được phần nào bẫy nhờ tính ngẫu nhiên.
        o	Nhưng vẫn chưa đủ để đảm bảo tìm được đích.
    • Simulated Annealing:
        o	Có khả năng thoát khỏi đỉnh cục bộ nhờ chấp nhận bước "xấu" với xác suất giảm dần.
        o	Hiệu quả nếu cấu hình nhiệt độ hợp lý.
    • Beam Search:
        o	Giữ k trạng thái tốt nhất mỗi bước → cân bằng giữa breadth và focus.
        o	Đôi khi gặp vấn đề nếu tất cả beam đều đi sai hướng.
    • Genetic Algorithm:
        o	Tìm lời giải bằng cách tiến hóa qua nhiều thế hệ.
        o	Hiệu quả nhưng cần điều chỉnh kỹ mutation rate, selection method,...
        o	Có thể tìm được lời giải tốt nhưng không đảm bảo tối ưu.

