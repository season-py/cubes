(function(jQuery, simpleCart){

    simpleCart({
        checkout: {
            type: "PayPal",
            email: "haishan09@gmail.com",
        },
        cartStyle: "div",
        // currency: "JPY"
        beforeCheckout: beforeCheckout,
        checkoutSuccess: null,
    });


    function beforeCheckout(food_id){   
        $.ajax({   
        type:"post",     
        url:"/food/dislike",
        data: {food_id: food_id},
        success:function(msg){   
            $("#food_dislike_"+ food_id).html(msg);
        },
    });

}(jQuery,simpleCart))
