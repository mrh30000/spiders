const l = 1111111111111

function getApiKey() {
    var e = (new Date).getTime()
      , r = encryptApiKey();
    return e = encryptTime(e),
    comb(r, e)
}

function encryptApiKey(){
    var e = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
      , r = e.split("")
      , n = r.splice(0, 8);
    return e = r.concat(n).join("")
}

function encryptTime(e){
    var r = (1 * e + l).toString().split("")
      , n = parseInt(10 * Math.random(), 10)
      , t = parseInt(10 * Math.random(), 10)
      , a = parseInt(10 * Math.random(), 10);
    return r.concat([n, t, a]).join("")
}

function comb(e, r) {
    var n = "".concat(e, "|").concat(r);
    return btoa(n)
}

console.log(getApiKey())