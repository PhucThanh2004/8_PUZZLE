# 1. Mục tiêu
Bài toán giải quyết trò chơi 8-Puzzle thông qua việc triển khai và so sánh hiệu suất của nhiều thuật toán tìm kiếm khác nhau. Hệ thống cung cấp tùy chọn để người dùng trải nghiệm các thuật toán như BFS, DFS, IDS, Uniform Cost, A*, IDA*, Greedy Best-First Search, Hill Climbing (bao gồm các biến thể), Simulated Annealing, Beam Search, Genetic Algorithm, Backtracking, cùng các thuật toán dành cho môi trường không chắc chắn như Uncertain BFS, Search with No Observations và Partially Observable DFS. Giao diện trực quan được thiết kế bằng Pygame giúp mô phỏng toàn bộ quá trình giải quyết bài toán.
# 2. Nội dung

## 2.1. Các thuật toán Tìm kiếm không có thông tin (Uninformed Search)

### Thành phần chính của bài toán tìm kiếm

#### Một bài toán tìm kiếm bao gồm các thành phần cơ bản sau:

    •	Không gian trạng thái (State Space): tập hợp tất cả các trạng thái có thể có của bài toán.
    •	**Trạng thái ban đầu (Initial State):** điểm bắt đầu quá trình tìm kiếm.
    •	Tập hành động (Actions): tập các hành động có thể thực hiện để chuyển từ trạng thái này sang trạng thái khác.
    •	Hàm chuyển trạng thái (Transition Model): mô tả kết quả của một hành động khi áp dụng lên trạng thái hiện tại.
    •	Trạng thái đích (Goal Test): điều kiện để xác định trạng thái đích đã đạt được.
    •	Chi phí đường đi (Path Cost): tổng chi phí của chuỗi hành động từ trạng thái ban đầu đến trạng thái đích (thường dùng trong tìm kiếm tối ưu như Uniform Cost Search).
#### Solution là gì?
Solution là một chuỗi các hành động hoặc trạng thái dẫn từ trạng thái ban đầu đến trạng thái mục tiêu (goal state). Trong bối cảnh của trò chơi 8-Puzzle, solution chính là chuỗi di chuyển các ô số để biến cấu hình ban đầu thành cấu hình mục tiêu (thường là sắp xếp từ 1–8, với ô trống ở vị trí cuối).
#### Hình ảnh gif của từng thuật toán khi áp dụng lên trò chơi

| <img src="BFS.gif" width="200"/> | <img src="IDS.gif" width="200"/> | <img src="assets/UC.gif" width="200"/> | <img src="DFS.gif" width="200"/> |
|:--------------------------------:|:--------------------------------:|:--------------------------------:|:--------------------------------:|
| **Mô phỏng BFS**                 | **Mô phỏng IDS**                 | **Mô phỏng UCS**                 | **Mô phỏng DFS**                 |
#### Hình ảnh so sánh hiệu suất của các thuật toán

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
