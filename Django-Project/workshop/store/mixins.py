from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UploadFile

class UploadOwnerMixin(LoginRequiredMixin):
	"""Verify that the current user is authenticated."""
	def dispatch(self, request, *args, **kwargs):
		# print(self)
		# print(request.user)
		# print(args)
		# print(kwargs)

		# Get the Post
		upload = UploadFile.objects.get(pk=kwargs['pk'])

		# print(post)
		# print(request.user, post.user)

		# Check if the post user == logged in user
		# If they are not the same
		
		# then kick them out
		if upload.user != request.user:
			# return self.handle_no_permission()
			return redirect('error403')
		
		if not request.user.is_authenticated:
			return self.handle_no_permission()
		
		# otherwise let them go ahead
		return super().dispatch(request, *args, **kwargs)