from django.shortcuts import render
from .models import Account
from decimal import Decimal

def home(request):
    return render(request, "home.html")

def create_account(request):

    message = ""

    if request.method == "POST":

        account_number = int(request.POST["account_number"])

        name = request.POST["name"]

        address = request.POST["address"]

        phone_number = int(request.POST["phone_number"])

        balance = float(request.POST["balance"])

        Account.objects.create(
            account_number=account_number,
            name=name,
            address=address,
            phone_number=phone_number,
            balance=balance
        )

        message = "ACCOUNT CREATED"

        return render(
            request,
            "create_account.html",
            {"message": message}
        )

    return render(request, "create_account.html")


def all_accounts(request):

    accounts = Account.objects.all()

    return render(
        request,
        "all_accounts.html",
        {
            "accounts": accounts
        }
    )

def get_account(request):

    account = None
    message = ""

    if request.method == "POST":

        account_number = request.POST["account_number"]

        try:

            account = Account.objects.get(
                account_number=account_number
            )

        except Account.DoesNotExist:

            message = "Account Not Found!"

    return render(
        request,
        "get_account.html",
        {
            "account": account,
            "message": message
        }
    )


def deposit(request):

    account = None
    message = ""
    error = ""

    if request.method == "POST":

        account_number = request.POST["account_number"]
        amount = Decimal(request.POST["amount"])

        try:

            account = Account.objects.get(
                account_number=account_number
            )

            account.balance += amount
            account.save()

            message = "Deposit Successful!"

        except Account.DoesNotExist:

            error = "Account Not Found!"

    return render(
        request,
        "deposit.html",
        {
            "account": account,
            "message": message,
            "error": error
        }
    )
def withdraw(request):
    account = None
    message = ""
    error = ""

    if request.method == "POST":

        account_number = request.POST["account_number"]
        amount = Decimal(request.POST["amount"])

        try:

            account = Account.objects.get(
                account_number=account_number
            )
            if amount <= account.balance:
                account.balance -= amount
                account.save()

                message = "Withdrawn Successful!"
            else:
                message="INSUFFICIENT AMOUNT"

        except Account.DoesNotExist:

            error = "Account Not Found!"

    return render(
        request,
        "withdraw.html",
        {
            "account": account,
            "message": message,
            "error": error
        }
    )
    
def update_account(request):
    message = ""

    if request.method == "POST":

        account_number = request.POST["account_number"]

        try:

            account = Account.objects.get(
                account_number=account_number
            )

            account.name = request.POST["name"]
            account.phone_number = request.POST["phone_number"]
            account.address = request.POST["address"]

            account.save()

            message = "Account Updated Successfully!"

        except Account.DoesNotExist:

            message = "Account Not Found!"

    return render(
        request,
        "update_account.html",
        {
            "message": message
        }
    )


def delete_account(request):
    message = ""

    if request.method == "POST":

        account_number = request.POST["account_number"]

        try:

            account = Account.objects.get(
                account_number=account_number
            )

            account.delete()

            message = "Account Deleted Successfully!"

        except Account.DoesNotExist:

            message = "Account Not Found!"

    return render(
        request,
        "delete_account.html",
        {
            "message": message
        }
    )
