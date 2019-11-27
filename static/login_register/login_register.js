// 用户登录注册加载
// 登录
$('.user_login').click(
    function(){
    var login_html = $('#add_html #change_login').prop("outerHTML");
    $('#title').text('用户登录');
    $('.modal-body div').remove();
    $('.modal-body').append(login_html);
    });

// 注册
$('.user_register').click(
    function(){
        var register_html = $('#add_html #change_register').prop("outerHTML");
        $('#title').text('用户注册');
        $('.modal-body div').remove();
        $('.modal-body').append(register_html);
    });
// 注册页面切换到登录页面
function chang_user_login_click(){
    var login_html = $('#add_html #change_login').prop("outerHTML");
    $('#title').text('用户登录');
    $('.modal-body div').remove();
    $('.modal-body').append(login_html);
    $('#login-fail').html('');
}
// 登录页面切换到注册页面
function chang_user_register_click(){
    var register_html = $('#add_html #change_register').prop("outerHTML");
    $('#title').text('用户注册');
    $('.modal-body div').remove();
    $('.modal-body').append(register_html);
    $('#register-fail').html('');
}
// 用户登录的ajax请求
function login_submit(){
$.ajax({
    cache:false,
    type:"POST",
    url:"/userprofile/login/",
    dataType:'json',
    data:{
        "username":$("#username").val(),
        "password":$("#password").val(),
        // "password2":$("#password2").val(),
        // "email":$("#email").val(),
        "csrfmiddlewaretoken":$('[name="csrfmiddlewaretoken"]').val()
    },
    //通过id找到提交form表单，并将表单转成字符串
    async:true,
    //异步为真，ajax提交的过程中，同时可以做其他的操作
    success:function (data) {
        //jquery3以后，会将回传过来的字符串格式的data自动json解析不用再使用一遍JSON.parse(data)了，不然反而会在控制台报错
        if(data.status=="success"){
            window.location.href = "/";
        }else if(data.status=="fail"){
            $('#login-fail').html(data.msg);
        }
    }
    });
}
//如果显示了错误信息，修改输入框内容，错误信息隐藏
$("input").bind('input propertychange', function() {
    $('#login-fail').html('');
});
// 用户注册的请求
function register_sbumit(){
    $.ajax({
        cache:false,
        type:"POST",
        url:"/userprofile/register/",
        dataType:'json',
        data:{
            "username":$("#username_re").val(),
            "password":$("#password1").val(),
            "password2":$("#password2").val(),
            "email":$("#email").val(),
            "csrfmiddlewaretoken":$('[name="csrfmiddlewaretoken"]').val()
        },
        //通过id找到提交form表单，并将表单转成字符串
        async:true,
        //异步为真，ajax提交的过程中，同时可以做其他的操作
        success:function (data) {
            //jquery3以后，会将回传过来的字符串格式的data自动json解析不用再使用一遍JSON.parse(data)了，不然反而会在控制台报错
            if(data.status == "success"){
                window.location.href = "/";
            }else if(data.status == "fail"){
                $('#register-fail').html(data.msg);
            }
        }
    });
    }
//如果显示了错误信息，修改输入框内容，错误信息隐藏
$("input").bind('input propertychange', function() {
    $('#register-fail').html('');
});