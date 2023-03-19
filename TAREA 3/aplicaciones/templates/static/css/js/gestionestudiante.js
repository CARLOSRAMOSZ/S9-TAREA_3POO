(function(){
    const btneliminar=document.querySelectorAll(".btneliminar");

    btneliminar.forEach(btn =>{
        btn.addEventListener('click',(e)=>{
            const confirmacion=confirm('¿Seguro deseas eliminar el registro?');
            if (!confirmacion){
                e.preventDefault();
            }
        });
    });
})();