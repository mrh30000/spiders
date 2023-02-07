function b(e, t) {
                return p(`client=${r}&mysticTime=${e}&product=${i}&key=${t}`)
            }

function p(e) {
                return c.a.createHash("md5").update(e.toString()).digest("hex")
            }