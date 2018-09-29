var sampler = {
    colorSample: {
        red: 0,
        green: 0,
        blue: 0
    },
    randomColor: function() {
        this.colorSample.red = parseInt(Math.random() * 256);
        this.colorSample.green = parseInt(Math.random() * 256);
        this.colorSample.blue = parseInt(Math.random() * 256);

        document.getElementById('red').setAttribute('value', `${this.colorSample.red}`);
        document.getElementById('green').setAttribute('value', `${this.colorSample.green}`);
        document.getElementById('blue').setAttribute('value', `${this.colorSample.blue}`);
    },
    showColor: function() {
        let square = document.getElementById('color-square');
        square.setAttribute('data-red', this.colorSample.red);
        square.style.backgroundColor = `rgb(${this.colorSample.red},${this.colorSample.green},${this.colorSample.blue})`;
    }
}

function main() {
    sampler.randomColor();
    sampler.showColor();
}

main();