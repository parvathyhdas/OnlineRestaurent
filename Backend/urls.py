from django.urls import path
from Backend import views

urlpatterns = [path('indexPage/',views.indexPage,name="indexPage"),
               path('categoryPage/',views.categoryPage,name="categoryPage"),
               path('saveCategory/',views.saveCategory,name="saveCategory"),
               path('displayCategory/',views.displayCategory,name="displayCategory"),
               path('editCategory/<int:dataid>/',views.editCategory,name="editCategory"),
               path('updateCategory/<int:dataid>/',views.updateCategory,name="updateCategory"),
               path('deleteCategory/<int:dataid>/',views.deleteCategory,name="deleteCategory"),
               path('itemPage/',views.itemPage,name="itemPage"),
               path('saveItem/',views.saveItem,name="saveItem"),
               path('displayItem/',views.displayItem,name="displayItem"),
               path('editItem/<int:dataid>/',views.editItem,name="editItem"),
               path('updateItem/<int:dataid>/',views.updateItem,name="updateItem"),
               path('deleteItem/<int:dataid>/',views.deleteItem,name="deleteItem"),
               path('admin_login/',views.admin_login,name="admin_login"),
               path('adminLoginPage/',views.adminLoginPage,name="adminLoginPage"),
               path('adminLogout/',views.adminLogout,name="adminLogout"),
               ]