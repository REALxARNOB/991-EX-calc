let mode = 'deg';
let memory = 0;
let errorState = false;

function display(value) {
    if (errorState) {
        document.getElementById('result').value = '';
        errorState = false;
    }
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
        errorState = true;
    }
}

function clearScreen() {
    document.getElementById('result').value = '';
    errorState = false;
}

function backspace() {
    if (errorState) {
        clearScreen();
        return;
    }
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
    calculate();
    if (!errorState) {
        memory += parseFloat(document.getElementById('result').value);
    }
}

function memorySubtract() {
    calculate();
    if (!errorState) {
        memory -= parseFloat(document.getElementById('result').value);
    }
}

function memoryRecall() {
    if (errorState) {
        clearScreen();
    }
    document.getElementById('result').value = memory;
}

document.addEventListener('keydown', function(event) {
    const key = event.key;

    // Ignore if modifier keys are pressed (e.g. Ctrl+C, Ctrl+V, Ctrl+R)
    if (event.ctrlKey || event.metaKey || event.altKey) {
        return;
    }

    // Allow default behavior for buttons to support keyboard navigation (Tab + Enter)
    if (event.target.tagName === 'BUTTON' && (key === 'Enter' || key === ' ')) {
        return;
    }

    // Numbers (ensure single digit to avoid F-keys)
    if (/^[0-9]$/.test(key)) {
        event.preventDefault();
        display(key);
    }
    // Operators
    else if (['+', '-', '*', '/', '.', '(', ')', '^'].includes(key)) {
        event.preventDefault();
        display(key);
    }
    // Special keys
    else if (key === 'Enter' || key === '=') {
        event.preventDefault();
        calculate();
    } else if (key === 'Backspace') {
        event.preventDefault(); // Prevent browser back navigation
        backspace();
    } else if (key === 'Escape') {
        event.preventDefault();
        clearScreen();
    }
});
