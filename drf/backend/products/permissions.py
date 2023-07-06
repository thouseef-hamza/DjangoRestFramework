from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'], 
        
    }
    
    
    def has_permission(self,request,view):
        return super().has_permission(request,view)
    # def has_permission(self,request,view):
    #     user = request.user
    #     print(user)
    #     print(user.get_all_permissions(),"ghjkl")
    #     if user.is_staff:
    #         if user.has_perm("products.add_product"): # "app_name.action_modelname"
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.view_product"):
    #             return True
    #         return False
    #     return False

    
    