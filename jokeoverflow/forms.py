from django import forms
from jokeoverflow.models import UserProfile, Joke, Video, Comment, Category
from django.contrib.auth.models import User
from django.utils.timezone import now


class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=True, help_text='Please add your date of birth in yyyy-mm-dd format.')
    user_bio = forms.CharField(max_length=256, required=False)
    user_picture = forms.ImageField(required=False)
    image_from = forms.URLField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class JokeForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Give the joke a title.')
    joke_text = forms.CharField(max_length=256, help_text='Tell us your joke!')
    date_added = forms.DateField(widget=forms.HiddenInput)
    upvotes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    downvotes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    flagged = forms.BooleanField(widget=forms.HiddenInput, initial=False)

    class Meta:
        model = Joke
        exclude = ('added_by', 'category',)


class VideoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea, max_length=128, help_text='What\'s the video called?')
    url = forms.URLField(max_length=200, help_text='Please enter the url of the video.')
    upvotes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    downvotes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    rating = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Video
        exclude = ('added_by', 'date_added',)


class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(max_length=256, help_text='Please enter your comments...')

    class Meta:
        model = Comment
        exclude = ('made_by', 'joke', 'date_added')


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the category name.")
    restricted = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
    no_of_jokes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('title',)