/** https://school.programmers.co.kr/learn/courses/30/lessons/43162
  solution만 작성
  정리한 내용 : https://ohamin26.tistory.com/42
  작성일 : 24-10-27
*/
function solution(n, computers) {
  let cnt = 0;
  let visited = Array(n).fill(false);

  const dfs = (node) => {
    visited[node] = true;
    for (let neighbor = 0; neighbor < n; neighbor++) {
      if (computers[node][neighbor] === 1 && !visited[neighbor]) {
        console.log(visited);
        dfs(neighbor);
      }
    }
  };

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      dfs(i);
      cnt++;
    }
  }

  return cnt;
}
