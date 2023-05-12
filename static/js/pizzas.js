$(document).ready(function (){
    $('#search-btn').on(types:'click', selector:function(e{
        e.preventDefault()
        var searchText = $('#search-box').val();
        $.ajax(url:
        {
            url: '/pizzas?search_filter' + searchText,
                type: 'GET',
                success: function(resp){
                var newHtml = resp.data.map(d => {
                    return '<div class="one pizza">
                        <a href="/pizzas/${d.id}">
                            <img class="pizza-img" src="${d.firstImage}"/>
                            <h4>{{d.name}}</h4>
                            <p>{{d.description}}</p>
                        </a>
                    </div>'
                });
                $('.pizzas').html(newHtml.join(''));
                $('#search-box').val(value:'');

        },
            error: function(xhr, status, error){
                console.error(error);
            }
        })
    });
});