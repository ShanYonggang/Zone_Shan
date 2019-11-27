$(document).ready(function(){
    $("#wechat_show").mousemove(
        function (event) {
            $("#image_show")[0].style.display = 'block';
        }
    );
    $("#wechat_show").mouseleave(
        function (event) {
            $("#image_show")[0].style.display = 'none';
        }
    );
})

//  根据用户ip统计用户访问主页的次数
var cur_url = window.location.href;
function visit_web() {
    $.ajax({
        cache:false,
        type:"POST",
        url: "/visit_web/",
        dataType:'json',
        data: {
            cur_url:cur_url,
            "csrfmiddlewaretoken":$('[name="csrfmiddlewaretoken"]').val()
        },
        async:true,
        //异步为真，ajax提交的过程中，同时可以做其他的操作
        success:function (response) {
            if(response.status=="success"){
                console.log(response.msg);
            }else if(response.status=="fail"){
                console.log(response.msg);
            }
        }
    });
}
window.onload = visit_web;   //  网页加载完成后运行