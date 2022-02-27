$(function(){
    //Init
    const socket = io('http://localhost:8000')
    socket.on('connect', function(){ console.log("Connected");});

    socket.on("update", (data) => {
      console.log(data);
    });

    function myFunction(){
      socket.send("Export CSV");
    }
    

  });

  