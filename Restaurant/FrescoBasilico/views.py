from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import FormView, ListView, CreateView, DetailView
from .models import ( Meals, Reservation)
from random import shuffle
from User.models import Profile, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from .forms import ReservationForm, CommentForm
from random import shuffle
from datetime import date
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

# Create your views here.
class DashboardView(View):
    def get(self, request):
        pizzas = Meals.objects.filter(type_of_food = 1)
        pastas = Meals.objects.filter(type_of_food = 2)
        ctx = {"pizzas" : pizzas, "pastas" : pastas }
        return render(request, "FrescoBasilico/index.html", ctx)

class BlogView(View):
    def get(self, request):
        ctx = {}
        return render(request, "FrescoBasilico/04_blog.html", ctx)

class ContactView(View):
    def get(self, request):
        ctx = {}
        return render(request, "FrescoBasilico/05_contact.html", ctx)

class ElementsView(View):
    def get(self, request):
        ctx = {}
        return render(request, "FrescoBasilico/06_elements.html", ctx)

class AboutUsView(View):
    def get(self, request):
        ctx = {}
        comments = list(Comment.objects.all())
        shuffle(comments)
        comment1 = comments[0]
        comment2 = comments[1]
        comment3 = comments[2]
        ctx["comment1"] = comment1
        ctx["comment2"] = comment2
        ctx["comment3"] = comment3
        return render(request, "FrescoBasilico/about_us.html", ctx)

class MenuView(View):
    def get(self, request):
        pizzas = Meals.objects.filter(type_of_food = "1")
        pastas = Meals.objects.filter(type_of_food = "2")
        ctx = {"pizzas" : pizzas, "pastas" : pastas}
        return render(request, "FrescoBasilico/menu.html", ctx)

class ModificationView(View):
    def get(self, request):
        ctx = {}
        return render(request, "FrescoBasilico/modification.html", ctx)

    def post(self, request, template='FrescoBasilico/modification.html', ctx=None):
        reservation_no = request.POST.get("res_no", False)
        res = int(reservation_no)
        return redirect(f'/reservation/{res}')

class AddReservationView(View):
    def get(self, request):
        last_reservation= Reservation.objects.latest('id')
        form = ReservationForm()
        ctx = {"form": form, "last_reservation" : last_reservation}
        return render(request, "FrescoBasilico/new_reserve.html", ctx)

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_no = form.cleaned_data["phone_no"]
            reservation_date = form.cleaned_data["reservation_date"]
            reservation_time = form.cleaned_data["reservation_time"]
            table_number = form.cleaned_data["table_number"]
            special_needs = form.cleaned_data["special_needs"]



            if Reservation.objects.filter(table_number=table_number,
                                            date_reserved=reservation_date,
                                            time = reservation_time).exists():

                ctx = {}
                message = "Table already booked try another time, date or table"
                ctx['message'] = message
                ctx ["form"]= form
                return render(request, "FrescoBasilico/new_reserve.html", ctx)

            elif reservation_date < datetime.date.today():
                ctx = {}
                message = "Date must be in future or today"
                ctx['message'] = message
                ctx ["form"]= form
                return render(request, "FrescoBasilico/new_reserve.html", ctx)


                ctx = {}
                message = "Table already booked try another time, date or table"
                ctx['message'] = message
                ctx ["form"]= form
                return render(request, "FrescoBasilico/new_reserve.html", ctx)

            else:
                reservation = Reservation.objects.create(
                    first_name =  first_name,
                    last_name = last_name,
                    email = email,
                    phone =  phone_no,
                    table_number = table_number,
                    time = reservation_time,
                    date_reserved = reservation_date,
                    comment = special_needs,
                    )
                last_reservation= Reservation.objects.latest('id')
                ctx = {}
                message = "Reservation done!!! Reservation number below:"
                ctx['new_reservation'] = last_reservation
                ctx['message'] = message
                ctx ["form"]= form
                return render(request, "FrescoBasilico/new_reserve.html", ctx)

class LeaveACommentView(View):
    def get(self, request):
        form = CommentForm()
        ctx = {"form": form}
        return render(request, "FrescoBasilico/leave_a_comment.html", ctx)
    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data["author"]
            text = form.cleaned_data["text"]
            comment = Comment.objects.create(
                author =  author,
                text = text,
                )
            messages.success(
                self.request,
                "Thank you for your comment!")
            return redirect("comment")

        ctx = {"form": form}
        return render(request, "FrescoBasilico/leave_a_comment.html", ctx)

class reservation_modify_id(View):
    def get(self, request, id):

        try:
            reservation = Reservation.objects.get(pk=id)
        except Reservation.DoesNotExist:
            return render(request, "FrescoBasilico/error_reservation.html")
        else:
            ctx = {}
            ctx['reservation'] = reservation
            return render(request, 'FrescoBasilico/edit_reservation.html', ctx)

    def post(self, request, id, template='FrescoBasilico/edit_reservation.html', ctx=None):
        old_reservation = Reservation.objects.get(pk=id)
        first_name = request.POST.get("first_name", False)
        last_name = request.POST.get("last_name", False)
        email = request.POST.get("email", False)
        phone = request.POST.get("phone", False)
        reservation_date = request.POST.get("date", False)
        reservation_time = str(request.POST.get("time"))
        table_number = int(request.POST.get("table"))
        special_needs= request.POST.get("needs", False)

        if Reservation.objects.filter(table_number=table_number,
                                        date_reserved=reservation_date,
                                        time = reservation_time).exists():
            ctx = {}
            message = "Table already booked try another time, date or table"
            ctx['message'] = message
            return render(request, template, ctx)

        else:
            if first_name and last_name and email and phone and reservation_time and reservation_date and table_number:
                new_reservation = Reservation()
                new_reservation.first_name = first_name
                new_reservation.last_name = last_name
                new_reservation.mail = email
                new_reservation.phone = phone
                new_reservation.table_number = table_number
                new_reservation.time = reservation_time
                new_reservation.date_reserved = reservation_date
                new_reservation.comment = special_needs
                new_reservation.save()
                old_reservation.delete()
                last_reservation = Reservation.objects.latest('id')
                ctx = {}
                message = "Modification done!!! Modified reservation new number below:"
                ctx['new_reservation'] = last_reservation
                ctx['message'] = message
                return render(request, template, ctx)
            else:
                if not ctx:
                    ctx = {}
                message = "Wypełnij poprawnie wszystkie pola!"
                ctx['message'] = message
                return render(request, template, ctx)
