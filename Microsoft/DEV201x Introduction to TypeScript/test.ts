function formatCommandline(c: string[]|string) {
    if(typeof c === 'string') {
        return c.trim();
    } else {
        return c.join(' ');
    }
}

type int = number;

var x : int = 9.7;