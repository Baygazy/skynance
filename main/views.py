from django.shortcuts import render
from django.views.generic import TemplateView


# Navbar #########################################################

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })


#
# # class NewsView(TemplateView):
# #     template_name = 'views/main/ru/px_index.html'
# #
# #     def get(self, request, *args, **kwargs):
# #         return render(request, self.template_name, context={
# #         })
# #
# #     def post(self, request, *args, **kwargs):
# #         return render(request, self.template_name, context={
# #         })
#
class FaqView(TemplateView):
    template_name = 'faq.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

# Navbar #########################################################

# Sidebar #########################################################

class InvestmentView(TemplateView):
    template_name = 'investment.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class InvestmentsView(TemplateView):
    template_name = 'investments.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class RefillView(TemplateView):
    template_name = 'refill.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class TransactionsView(TemplateView):
    template_name = 'transactions.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class ProfileSettingsView(TemplateView):
    template_name = 'profile-settings.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

# class ChangePasswordView(TemplateView):
#     template_name = 'registration/password_change_form.html'
#
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, context={
#         })
#
#     def post(self, request, *args, **kwargs):
#         return render(request, self.template_name, context={
#         })

class ChatView(TemplateView):
    template_name = 'chat.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

# Sidebar #########################################################
class SideView(TemplateView):
    template_name = 'profile-sidebar-menu.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
            'profile':'profile',
            'investment':'investment',
            'investments':'investments',
            'refill':'refill',
            'transactions':'transactions',
            'profile-settings':'profile-settings',
            'password_change':'password_change',
            'chat':'chat',
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })
# Sidebar #########################################################


# Footer #########################################################

# class LoginView(TemplateView):
#     template_name = 'registration/login.html'
#
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, context={
#         })
#
#     def post(self, request, *args, **kwargs):
#         return render(request, self.template_name, context={
#         })

# Footer #########################################################
