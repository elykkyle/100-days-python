
const solution = (s) => {
  const sArr = s.split('')
  if (sArr.length < 2) { return sArr.length}
  let res = []
  let temp = []

  sArr.forEach(x => {
      if(temp.includes(x)) {
          temp = temp.slice(temp.findIndex(y => y === x ) + 1)
      }
      temp.push(x);
      if (temp.length > res.length) { res = temp}
  })
  return res.length;
}

console.log(solution("nndNfdfdf"))