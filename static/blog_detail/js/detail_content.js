// gittalk评论模块的js
// var gitalk = new Gitalk({
// clientID: 'f1bcf5076d860ad1fbb3',
// clientSecret: '20077b4c29e072f218f00221d57089e76ce23dc8',
// repo: 'my_blog_talk',
// owner: 'ShanYonggang',
// admin: ['ShanYonggang'],
// id: location.pathname,
// // id: location.href,      // Ensure uniqueness and length less than 50
// distractionFreeMode: false, // Facebook-like distraction free mode
// });
// gitalk.render('gitalk-container');

// 点赞功能的js
toastr.options = {
        // toastr配置
        "closeButton": false, //是否显示关闭按钮
        "debug": false, //是否使用debug模式
        "progressBar": false, //是否显示进度条，当为false时候不显示；当为true时候，显示进度条，当进度条缩短到0时候，消息通知弹窗消失
        "positionClass": "toast-bottom-center",//显示的动画位置
        "showDuration": "300", //显示的动画时间
        "hideDuration": "300", //消失的动画时间
        "timeOut": "1500", //展现时间
        "extendedTimeOut": "1500", //加长展示时间
        "showEasing": "swing", //显示时的动画缓冲方式
        "hideEasing": "linear", //消失时的动画缓冲方式
        "showMethod": "fadeIn", //显示时的动画方式
        "hideMethod": "fadeOut" //消失时的动画方式
    };
// 用户点赞的ajax请求
function validate_is_like(post_url, id, likes){
    $.ajax({
        cache:false,
        type:"GET",
        url: post_url,
        dataType:'json',
        data: {
            id:id,
            likes:likes,
        },
        async:true,
        //异步为真，ajax提交的过程中，同时可以做其他的操作
        success:function (data) {
            //jquery3以后，会将回传过来的字符串格式的data自动json解析不用再使用一遍JSON.parse(data)了，不然反而会在控制台报错
            if(data.status=="success"){
                toastr.success("点赞成功！");
                $('#likes_number').html('('+data.like+')');
            }else if(data.status=="fail"){
                toastr.success("您已经点赞！");
            }
        }
    });
}

// 文章内图片调整的js
$(document).ready(function(){
    // 根据自己的img位置设计css选择器
    $("#article_body p img").addClass('img-responsive');
    var a_tags = $("#article_body a");
    for(var i=0;i<a_tags.length;i++){
        $(a_tags[i]).attr("target","__blank");
    }
    var a_tags_not = $("#article_body .row a");
    for(var i=0;i<a_tags_not.length;i++){
        $(a_tags_not[i]).removeAttr("target","__blank");
    }
});

// 目录调整的js
$(document).ready(function(){
    // 根据自己的img位置设计css选择器
    columns = $("#article_body h3");
    for(var i=0;i<columns.length;i++) {
        $(columns[i]).attr("id","index_"+i);
        $(".blog_column").append("<li><a href="+"#"+"index_"+i+ ">" + $(columns[i]).text() + "</a></li>");
    }
});

// 滑到微信图标时候显示微信二维码
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

