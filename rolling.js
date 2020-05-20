function Rolling() {
  let rollInput = document.getElementById("input").value;
  let rollOutput = Math.floor(Math.random() * rollInput) + 1;
  if (rollOutput == NaN) {
    let rollOutput = "Specify a number larger than 1";
  };
  document.getElementById("output").innerHTML = rollOutput;
};