from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class OnlySuperUsers(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
