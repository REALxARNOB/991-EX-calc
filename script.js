let mode = 'deg';
let memory = 0;

function display(value) {
    document.getElementById('result').value += value;
}

function calculate() {
    let p = document.getElementById('result').value;
    try {
        const scope = {};
        if (mode === 'deg') {
            scope.sin = (x) => math.sin(math.unit(x, 'deg'));
            scope.cos = (x) => math.cos(math.unit(x, 'deg'));
            scope.tan = (x) => math.tan(math.unit(x, 'deg'));
        }
        let q = math.evaluate(p, scope);
        document.getElementById('result').value = q;
    } catch (e) {
        document.getElementById('result').value = 'Error';
    }
}

function clearScreen() {
    document.getElementById('result').value = '';
}

function backspace() {
    let p = document.getElementById('result').value;
    document.getElementById('result').value = p.substring(0, p.length - 1);
}

function toggleMode() {
    mode = mode === 'deg' ? 'rad' : 'deg';
    document.getElementById('mode').innerText = mode;
}

function memoryClear() {
    memory = 0;
}

function memoryAdd() {
    memory += parseFloat(document.getElementById('result').value);
}

function memorySubtract() {
    memory -= parseFloat(document.getElementById('result').value);
}

function memoryRecall() {
    document.getElementById('result').value = memory;
}
