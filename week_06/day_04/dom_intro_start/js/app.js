// console.log('app loaded', window);

document.addEventListener('DOMContentLoaded', () => {
    const title = document.querySelector('h1');
    title.textContent = 'JavaScript says HELLO WORLD!';

    // const welcomeParagraph = document.querySelector('#welcome-paragraph');
    // console.log(welcomeParagraph);
    // console.dir(welcomeParagraph);

    // const redElement = document.querySelector('li.red');
    // console.log(redElement);

    // const allLiElements = document.querySelectorAll('li');
    // console.dir(allLiElements);

    // const redListItem = document.querySelector('li.red');
    // redListItem.textContent = "RED!!!";
    // redListItem.classList.add('bold');
    // console.dir(redListItem);

    const newListItem = document.createElement('li');
    newListItem.textContent = 'Purple';
    newListItem.classList.add('purple');

    const list = document.querySelector('ul');
    list.appendChild(newListItem);

});

