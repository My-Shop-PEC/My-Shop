from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrdersView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    create_user_form,
    manager_view,
    custom_login,
    add_subscription,
    remove_subscription,
    SubscriptionSummaryView,
    StoreKeeperView,
    dashboard,
    modify_order,
    AllIngredientView,
    ingredient_quantity_update,
    ModifyCustomUserView,
    CookInfo,
    skip_sub,
    CookView,
    addIngredient,
    createItem,
    ReviewOrderView,
    AddFranchiseView,
    AdminView,
    ReviewView,
    IndexPage,
    paymentTrue,
    payment_razorpay,
    handlerequest,
    create_employee_form,
    create_user_form,
    complete_profile,
    MembershipView,
    payment_razorpay2,
    MembershipPriceView,
    handlerequest2,
    invoicegenerator
)

app_name = 'shop'

urlpatterns = [
    path('printinvoice/<int:id>/', invoicegenerator, name = 'invoicegenerator'),
    path('membership_price/',MembershipPriceView,name = 'membership_price'),
    path('payment_razorpay2/<int:amt>/<slug>',payment_razorpay2,name = 'payment_razorpay2'),
    path('complete_profile/',complete_profile,name='complete_profile'),
    path('register_user/',create_user_form,name='register_user'),
    path('handlerequest/', handlerequest, name = 'handlerequest'),
    path('handlerequest2/<slug>/', handlerequest2, name = 'handlerequest2'),
    path('payment_razorpay',payment_razorpay,name = 'payment_razorpay'),
    path('paymenttrue/<int:id>',paymentTrue,name = 'paymenttrue'),
    path('',HomeView, name = 'home'),
    path('custom_login/',custom_login,name = 'custom_login'),
    path('register_employee/',create_employee_form,name='register_employee'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('order-summary/', SubscriptionSummaryView, name='order-summary'),
    path('subscription-summary/', SubscriptionSummaryView, name='subscription-summary'),
    path('orders/', OrdersView.as_view(), name='orders'),
    #path('product/<slug>/', ItemDetailView.as_view(), name='product'),
     path('product/<slug>/', ItemDetailView, name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('manager_view/<slug>/',manager_view,name = 'manager_view'),
    path('manager_view/',manager_view,name = 'manager_view'),
    path('add-subscription/<slug>/',add_subscription, name ='add-subscription'),
    path('remove-subscription/<slug>/',remove_subscription, name ='remove-subscription'),
    path('storekeeper-view',StoreKeeperView,name = 'storekeeper-view'),
    path('dashboard',dashboard,name = 'dashboard'),
    path('modify_order/<int:id>/<slug>/',modify_order,name = 'modify-order'),
    path('all_ingredients/',AllIngredientView,name = 'all-ingredients'),
    path('ingredient-quantity-update/<int:id>/',ingredient_quantity_update,name='ingredient-quantity-update'),
    path('modify_user',ModifyCustomUserView,name = 'modify-user'),
    path('cook-info/<int:id>',CookInfo,name='cook-info'),
    path('skip-sub/<int:id>/<int:sub_id>',skip_sub,name='skip-sub'),
    path('cook-view',CookView,name='cook-view'),
    path('add-ingredient',addIngredient,name='add-ingredient'),
    path('add-item',createItem,name='add-item'),
    path('review-order/<int:id>',ReviewOrderView,name='review-order'),
    path('add-franchise/',AddFranchiseView,name='add-franchise'),
    path('admin-view/',AdminView,name='admin-view'),
    path('review-something',ReviewView,name = 'review-something'),
    path('index-page',IndexPage,name='index-page'),
    path('membership/',MembershipView,name ='membership'),
    
]

