var sampler = {
    colorSample: {
        red: 0,
        green: 0,
        blue: 0
    },
    init: function () {
        let buttons = $('button').toArray();
        buttons.forEach((button) => {
            button.addEventListener('click', this.sendData)
        });
        sampler.randomColor();
        sampler.showColor();
    },
    randomColor: function () {
        this.colorSample.red = parseInt(Math.random() * 256);
        this.colorSample.green = parseInt(Math.random() * 256);
        this.colorSample.blue = parseInt(Math.random() * 256);
    },
    showColor: function () {
        $('#color-square').css('background-color', `rgb(${this.colorSample.red},${this.colorSample.green},${this.colorSample.blue})`);
    },
    sendData: function (ev) {
        let clickedButton = ev.target;
        dataHandler.addEntry(clickedButton.value);
    }
};

function main() {
    sampler.init()
}

main();