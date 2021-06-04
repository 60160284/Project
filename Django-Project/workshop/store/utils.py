from django.utils.text import slugify
import random
import string



def random_string_generator(chars=10, letters=string.ascii_lowercase + string.ascii_uppercase + string.digits):
	return ( ''.join(random.choice(letters) for i in range(10)))


def unique_slug(instance, new_slug=None):

	print(new_slug)
	if new_slug:
		slug = new_slug
	else:
		slug = random_string_generator(chars=10)

	# print(slug)


	Uploadfile = instance.__class__
	# print(Post)
	query = Uploadfile.objects.filter(slug=slug).exists()
	# print(query)
	if query:
		print('This posts exists already')
		slug = random_string_generator(chars=10)

		return unique_slug(instance, new_slug=slug)
	return slug