/** https://school.programmers.co.kr/learn/courses/30/lessons/150368
  solution만 작성
  정리한 내용 : https://ohamin26.tistory.com/43
  작성일 : 24-10-29
*/
function solution(users, emoticons) {
  var answer = [0, 0];
  let info = [];

  const price = () => {
    let result = [0, 0];

    users.map((user) => {
      let total = 0;
      emoticons.map((emoticon, idx) => {
        if (user[0] <= info[idx]) {
          total += emoticon - (emoticon * info[idx]) / 100;
        }
      });

      if (total >= user[1]) {
        total = 0;
        result[0] += 1;
      } else {
        result[1] += total;
      }

      if (
        answer[0] < result[0] ||
        (answer[0] === result[0] && answer[1] < result[1])
      ) {
        answer = [...result];
      }
    });
  };

  const dfs = (depth) => {
    if (depth === emoticons.length) {
      price();
      return true;
    }

    for (let i = 40; i >= 10; i -= 10) {
      info[depth] = i;
      console.log(info);
      dfs(depth + 1);
    }
  };

  dfs(0);

  return answer;
}
