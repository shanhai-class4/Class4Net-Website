// 切换回复表单的显示与隐藏
function toggleReplyForm(button) {
    var form = button.parentNode.nextElementSibling;
    form.style.display = (form.style.display === 'none') ? 'block' : 'none';
}

// 删除评论
function deleteComment(button) {
    var comment = button.parentNode.parentNode.parentNode;
    comment.parentNode.removeChild(comment);
}

// 添加回复
function addReply(button) {
    var form = button.parentNode;
    var replyContent = form.querySelector('textarea').value.trim();
    if (replyContent !== '') {
        var parentComment = form.parentNode;
        var commentList = parentComment.querySelector('.comment-list');

        // Create new reply element
        var reply = document.createElement('li');
        reply.className = 'main-content-no-shadow';
        reply.innerHTML = `
            <div>
                <strong>用户:</strong>
                <p>${replyContent}</p>
                <div class="comment-actions">
                    <button onclick="toggleReplyForm(this)">回复</button>
                    <button onclick="deleteComment(this)">删除</button>
                </div>
                <form class="reply-form">
                    <textarea placeholder="在此处输入回复内容..."></textarea>
                    <button type="button" onclick="addReply(this)">提交</button>
                </form>
                <ul class="comment-list"></ul>
            </div>
        `;

        // Append new reply to comment list
        if (commentList === null) {
            commentList = document.createElement('ul');
            commentList.className = 'comment-list';
            parentComment.appendChild(commentList);
        }
        commentList.appendChild(reply);

        // Clear reply form
        form.querySelector('textarea').value = '';

        // Send reply to server
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/comment/new/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            content: replyContent,
            parent_id: parentComment.dataset.id // 发送父评论 ID
        }));
        xhr.onload = function() {
            if (xhr.status == 200) {
                console.log('回复提交成功');
                // Optionally reload the page to show the reply from the server
                location.reload();
            } else {
                console.log('回复提交失败');
            }
        };
    }
}

// 添加评论
function addComment() {
    var commentContent = document.getElementById('commentContent').value.trim();
    var articleId = document.getElementById('articleId').value; // 获取父文章 ID
    if (commentContent !== '') {
        var commentList = document.getElementById('commentList');

        // Create new comment element
        var comment = document.createElement('li');
        comment.className = 'main-content-no-shadow';
        comment.innerHTML = `
            <div>
                <strong>用户:</strong>
                <p>${commentContent}</p>
                <div class="comment-actions">
                    <button onclick="toggleReplyForm(this)">回复</button>
                    <button onclick="deleteComment(this)">删除</button>
                </div>
                <form class="reply-form">
                    <textarea placeholder="在此处输入回复内容..."></textarea>
                    <button type="button" onclick="addReply(this)">提交</button>
                </form>
                <ul class="comment-list"></ul>
            </div>
        `;

        // Append new comment to comment list
        commentList.appendChild(comment);

        // Clear comment form
        document.getElementById('commentContent').value = '';

        // Send comment to server
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/comment/new/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            content: commentContent,
            parent_id: articleId // 发送父文章 ID
        }));
        xhr.onload = function() {
            if (xhr.status == 200) {
                console.log('评论提交成功');
                // Optionally reload the page to show the comment from the server
                location.reload();
            } else {
                console.log('评论提交失败');
            }
        };
    }
}
