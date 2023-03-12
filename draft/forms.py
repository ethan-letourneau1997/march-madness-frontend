from .models import Team, Player
from crispy_forms.layout import Layout, Submit
from datetime import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Row
from django.forms import formset_factory


from .models import People, Player, Group


class newGroupForm(forms.Form):
    group_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'id': 'floatingName', 'class': 'form-control', 'placeholder': 'group'})
    )
    member_1 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'floatingMember1', 'class': 'form-control', 'placeholder': 'member1'})
    )
    member_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'floatingMember2', 'class': 'form-control', 'placeholder': 'group member 2'})
    )
    member_3 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'floatingMember3', 'class': 'form-control', 'placeholder': 'member 3'})
    )
    member_4 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'floatingMember4', 'class': 'form-control', 'placeholder': 'member 4'})
    )
    member_5 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'floatingMember5', 'class': 'form-control', 'placeholder': 'member1'})
    )
    member_6 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'floatingMember6', 'class': 'form-control', 'placeholder': 'member1'})
    )
    member_7 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'floatingMember7', 'class': 'form-control', 'placeholder': 'member1'})
    )
    member_8 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'floatingMember8', 'class': 'form-control', 'placeholder': 'member1'})
    )
    member_9 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'floatingMember9', 'class': 'form-control', 'placeholder': 'member9'})
    )
    member_10 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'floatingMember10', 'class': 'form-control', 'placeholder': 'member10'})
    )

    def clean_group_name(self):
        group_name = self.cleaned_data.get('group_name')
        # use "iexact" for case-insensitive matching
        if Group.objects.filter(name__iexact=group_name).exists():
            raise forms.ValidationError(
                "A group with this name already exists.")
        return group_name

    def clean_member_1(self):
        member = self.cleaned_data.get('member_1')
        if member:
            if People.objects.filter(name__iexact=member).exists():
                raise forms.ValidationError(
                    "A group with this name already exists.")
        return member

    def clean_member_2(self):
        member = self.cleaned_data.get('member_2')
        if member:
            if People.objects.filter(name__iexact=member).exists():
                raise forms.ValidationError(
                    "A group with this name already exists.")
        return member

    def clean_member_3(self):
        member = self.cleaned_data.get('member_3')
        if member:
            if People.objects.filter(name__iexact=member).exists():
                raise forms.ValidationError(
                    "A group with this name already exists.")
        return member

    def clean_member_4(self):
        member = self.cleaned_data.get('member_4')
        if member:
            if People.objects.filter(name__iexact=member).exists():
                raise forms.ValidationError(
                    "A group with this name already exists.")
        return member

    def clean_member_5(self):
        member = self.cleaned_data.get('member_5')
        if member:
            if People.objects.filter(name__iexact=member).exists():
                raise forms.ValidationError(
                    "A group with this name already exists.")
        return member

    def clean_member_6(self):
        member = self.cleaned_data.get('member_6')
        if member:
            if People.objects.filter(name__iexact=member).exists():
                raise forms.ValidationError(
                    "A group with this name already exists.")
        return member

    def clean_member_7(self):
        member = self.cleaned_data.get('member_7')
        if member:
            if People.objects.filter(name__iexact=member).exists():
                raise forms.ValidationError(
                    "A group with this name already exists.")
        return member

    def clean_member_8(self):
        member = self.cleaned_data.get('member_8')
        if member:
            if People.objects.filter(name__iexact=member).exists():
                raise forms.ValidationError(
                    "A group with this name already exists.")
        return member

    def clean_member_9(self):
        member = self.cleaned_data.get('member_9')
        if member:
            if People.objects.filter(name__iexact=member).exists():
                raise forms.ValidationError(
                    "A group with this name already exists.")
        return member

    def clean_member_10(self):
        member = self.cleaned_data.get('member_10')
        if member:
            if People.objects.filter(name__iexact=member).exists():
                raise forms.ValidationError(
                    "A group with this name already exists.")
        return member


# select form


class PlayerSelectForm(forms.Form):
    player = forms.ModelChoiceField(queryset=Player.objects.none())
    group_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    def __init__(self, remaining_players, group_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player'].queryset = remaining_players
        self.fields['group_id'].initial = group_id
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy(
            'draft', kwargs={'group_id': group_id})
        self.helper.form_class = 'player-form'
        self.helper.form_show_labels = False
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(
                'player',
                css_class='form-group col-md-12 mb-0'
            ),
            FormActions(
                Submit('submit', 'Add Player',
                       css_class='shadow btn btn-outline-danger mx-auto d-block w-100 mt-2')
            )
        )


# change admin player sorting order


class PeopleAdminForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(
        queryset=Player.objects.order_by('id'),
        widget=FilteredSelectMultiple('Players', False)
    )

    class Meta:
        model = People
        fields = '__all__'
