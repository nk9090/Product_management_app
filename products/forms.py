from cProfile import label
from dataclasses import fields

from django import forms
from . models import Product, Comment

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['image','name','price','category','description' ]
        widgets={
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
          
        }
        labels={
            'name':'enter product name:',
            'image':'Select an image:',
            'category':'Select category:',
            'price':'Enter price:',
            'description':'Enter description'

        }
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment_body',) 
        widgets={
            'comment_body':forms.Textarea(attrs={'class':'form-control'}),
           
          
        }       