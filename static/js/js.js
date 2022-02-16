(()=>{
  

 
    deleteMe = document.querySelectorAll(`button[data-gid]`)
    deleteMe.forEach(element => {
        element.addEventListener('click', function(){
            gid = this.getAttribute('data-gid')
            deleteRequest(gid);
            window.location.reload()
        })
    });

    
    
    
    function deleteRequest(gid){
        let httpRequest = new XMLHttpRequest();
        if (!httpRequest) {
                alert('Giving up :( Cannot create an XMLHTTP instance');
                return false;
            }
            httpRequest.onreadystatechange = alertContents;
            httpRequest.open('GET', `/api/delete/${gid}`);
            httpRequest.send();
    
            function alertContents() {
                if (httpRequest.readyState === XMLHttpRequest.DONE) {
                if (httpRequest.status === 200) {
                    alert(httpRequest.responseText);
                } else {
                    alert('There was a problem with the request.');
                }
            }
        }
    }
      
      
})();