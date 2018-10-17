const dataHandler = {
  addEntry: function(buttonLabel) {
      fetch('/add-entry', {
          method: "POST",
          headers: {
                "Content-Type": "application/json; charset=utf-8"
            },
            body: JSON.stringify({
                red: sampler.colorSample.red,
                green: sampler.colorSample.green,
                blue: sampler.colorSample.blue,
                color_label: buttonLabel
            })
      })
          .then(response => response.json())
          .then(data => {
              console.log(data);
              sampler.randomColor();
              sampler.showColor();
            }
          )
  }
};