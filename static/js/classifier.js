const classifier = {
    createColor: function () {
        let red = $('input[name="red"]').val();
        let green = $('input[name="green"]').val();
        let blue = $('input[name="blue"]').val();
        $('#color-square').css('background-color', `rgb(${red},${green},${blue})`);
    },
    init: function () {
        $('#generate').on('click', this.createColor);
        $('#predict').on('click', this.predictColor)
    },
    predictColor: function () {
        fetch('/predict-color', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json; charset=utf-8"
            },
            body: JSON.stringify({
                red: +$('input[name="red"]').val(),
                green: +$('input[name="green"]').val(),
                blue: +$('input[name="blue"]').val()
            })
        })
            .then(data => data.json())
            .then(prediction => classifier.showPrediction(prediction.message))
            .catch(err => console.log(err))
    },
    showPrediction: function (prediction) {
        $('#prediction').text(prediction)
    }
};

classifier.init();