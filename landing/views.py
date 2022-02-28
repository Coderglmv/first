from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def boards(request, username):
    username = request.user
    return redirect('projects:projects')
