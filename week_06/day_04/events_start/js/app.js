document.addEventListener('DOMContentLoaded', () => {

  const handleButtonClick = function(){
    const resultParagraph = document.querySelector('#button-result');
    resultParagraph.textContent = "This Button has been clicked!"
  };

  const button = document.querySelector('#button');
  button.addEventListener('click', handleButtonClick);

  const handleInput = function(event){
    const resultParagraph = document.querySelector('#input-result');
    resultParagraph.textContent = `You typed: ${event.target.value}`;
  };

  const input = document.querySelector('#input');
  input.addEventListener('input', handleInput);

  const handleSelect = function(event) {
    const resultParagraph = document.querySelector('#select-result');
    resultParagraph.textContent = `You selected: ${event.target.value}.`;
  };

  const select = document.querySelector('#select');
  select.addEventListener('input', handleSelect);

  const handleSubmit = function(event) {
    event.preventDefault()
    const resultParagraph = document.querySelector('#form-result');
    resultParagraph.textContent = `It's going to be ${event.target.first_name.value} ${event.target.last_name.value}.`;
  };

  const form = document.querySelector('#form');
  form.addEventListener('submit', handleSubmit);

});
