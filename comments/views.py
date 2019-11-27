
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from index.models import ArticlePost
from comments.forms import CommentForm
from django.http import HttpResponse,JsonResponse
# 引入评论模块
from comments.models import Comments
# 通知消息
from notifications.signals import notify
from user_profile.models import UserProfile
# 文章评论
@login_required
def post_comment(request, article_id,  parent_comment_id=None):
    article = get_object_or_404(ArticlePost, id=article_id)
    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            # 二级回复
            if parent_comment_id:
                parent_comment = Comments.objects.get(id=parent_comment_id)
                # 若回复层级超过二级，则转换为二级
                new_comment.parent_id = parent_comment.get_root().id
                # 被回复人
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                if not parent_comment.user.is_superuser:
                    notify.send(
                        request.user,
                        recipient=parent_comment.user,
                        verb='回复了你',
                        target=article,
                        action_object=new_comment,
                    )
                return HttpResponse('200 OK')
            new_comment.save()
            if not request.user.is_superuser:
                notify.send(
                    request.user,
                    recipient=UserProfile.objects.filter(is_superuser=1),
                    verb='回复了你',
                    target=article,
                    action_object=new_comment,
                )
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
        # 处理 GET 请求
    elif request.method == 'GET':
        comment_form = CommentForm()
        # 取出文章评论
        comment = Comments.objects.get(id=parent_comment_id)
        context = {
            'comment': comment,
            'comment_form': comment_form,
            'article_id': article_id,
            'parent_comment_id': parent_comment_id,
        }
        return render(request, 'comment/reply.html', context)
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")

