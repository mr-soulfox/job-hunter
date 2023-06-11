let hrefToReturn = [];
let elements = document.getElementsByClassName("app-aware-link  update-components-actor__container-link relative display-flex flex-grow-1");

for (let i = 0; i < elements.length; i++) {
    hrefToReturn.push(elements[i].href);
}

return hrefToReturn;
