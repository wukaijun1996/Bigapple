from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app04.models import UserToken


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 认证逻辑 ，如果认证通过，返回两个值
        # 如果认证失败,抛出AuthenticationFailed异常
        token = request.GET.get('token')
        if token:
            user_token = UserToken.objects.filter(token=token).first()
            # 认证通过
            if user_token:
                return user_token.user, token
            else:
                raise AuthenticationFailed("认证失败")
        else:
            raise AuthenticationFailed("请求地址中需要携带token")


from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        # 不是超级用户，不能访问
        # 由于认证已经过了 request内就有user对象了，当前登录用户
        user = request.user  # 当前登录用户
        print(user.get_user_type_display())
        if user.user_type == 1:
            return True
        else:
            return False


from rest_framework.views import exception_handler
from rest_framework.response import Response


# 自定义异常处理的方法
def my_exception_handler(exc, context):
    response = exception_handler(exc, context)
    print(exc)
    print(context)
    if response:
        res = Response(data={'code': 10001, 'msg': response.data.get('detail')})
    else:
        # res = Response({'code': 10002, 'msg': '服务器内部错误'})
        res = Response({'code': 10002, 'msg': str(exc)})
    return res


# 自封装Response对象

class APIResponse(Response):
    def __init__(self, code=100, msg='成功', data=None, status=None, headers=None
                 , **kwargs):
        dic = {'code': code, 'msg': msg}
        if data:
            dic = {'code': code, 'msg': msg, 'data': data}
        dic.update(kwargs)
        super().__init__(data=dic, status=status, headers=headers)
