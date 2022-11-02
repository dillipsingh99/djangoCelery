function myFunction(){
    alert("Hello from static files.")
}

const container = document.querySelector('#container');


var nextItem = 1;
var loadMore = function(){
    for(var i=0; i<20; i++){
        var item=document.createElement('li');
        item.innerText = 'Item' + nextItem++;
        HTMLDataListElement.appendChild(item);
    }
}



listElm.addEventListener('scroll', function() {
    if (listElm.scrollTop + listElm.clientHeight >= listElm.scrollHeight) {
      loadMore();
    }
  });


//Initally load some items
loadMore();