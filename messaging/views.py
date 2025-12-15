from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop.models import Product
from .models import Message
from django.contrib.auth.models import User
from .forms import MessageForm

@login_required
def contact_admin(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Assuming the first superuser is the admin
            admin = User.objects.filter(is_superuser=True).first()
            if admin:
                Message.objects.create(
                    sender=request.user,
                    receiver=admin,
                    product=None,
                    content=form.cleaned_data['content']
                )
                messages.success(request, 'Message sent to admin.')
                return redirect('shop:home')
            else:
                messages.error(request, 'Admin not found.')
    else:
        form = MessageForm()
    return render(request, 'messaging/contact_admin.html', {'form': form})

@login_required
def message_to_seller(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                sender=request.user,
                receiver=product.seller,
                product=product,
                content=form.cleaned_data['content']
            )
            messages.success(request, 'Message sent to seller.')
            return redirect('shop:product_detail', pk=product.id)
    else:
        form = MessageForm()
    return render(request, 'messaging/message_form.html', {'form': form, 'product': product})

@login_required
def inbox(request):
    messages_qs = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'messaging/inbox.html', {'messages': messages_qs})
