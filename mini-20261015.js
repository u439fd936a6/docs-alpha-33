// scratch

const sum = (xs) => xs.reduce((a, b) => a + b, 0);

const uniq = (xs) => [...new Set(xs)];

console.log(uniq(["a", "a", "b"]));
