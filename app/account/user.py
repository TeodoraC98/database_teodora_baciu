from flask import Blueprint,render_template,redirect,url_for,request,flash
from app.models.users import User
from app.models.orders import Invoice,Invoice_Details
from flask_login import current_user, login_user, logout_user
from app.forms.forms_user import LogIn, RegistrationUser
from app.database import db_session
import sqlalchemy as sql
user_bp = Blueprint('account',__name__,template_folder='templates/account')
class_frm={

 }
@user_bp.route('/account/profile')
def profile():
   # the get_list_invoice_by_user(id) function returns all invoices for the current user
   list_invoices=Invoice.get_list_invoice_by_user(current_user.id)
   # for invoice in list_invoices:
         # invoice_det=Invoice_Details.get_invoice_details_by_id_invoice(invoice.id)
   return render_template("profile.html",  list_invoices = list_invoices)


 
# in the login.html page an user can create an account or log in to an existing account
# the login.html page contains the form for authentication and registration
# this root is for authentication of an existing user
@user_bp.route('/account/login',methods=['POST','GET'])
def login():
   #  checks if the user is logged in 
    if current_user.is_authenticated:
      #  if logged in, the user is redirected to the profile page
       return redirect(url_for('account.profile'))
    
    formLogin = LogIn(request.form)
    formReg = RegistrationUser(request.form)

   # if the request comes from the checkout page,
   # the next redirects the user back to the checkout page
    next=request.args.get("next")
    
    if formLogin.validate():
       user = db_session.scalar(sql.select(User).where(User.email == formLogin.email.data))
       if user is None or not user.check_password(formLogin.password.data):
         # through the access_frm class it determines which form will be displayed to the user
         # in this case is the log in form
         class_frm["cls_login"]="access_frm"      
         class_frm["cls_reg"]=""
         flash("Invalid email or password!")
         return redirect(url_for('account.login'))
      #  user is logged in
       login_user(user)
       if next:
         #  user is redirected to the page that required to the user be connected in order to  get accesss 
          return redirect(next)
       else:
         return redirect(url_for('account.profile'))
   #  if the user fail to get conected is redirected to the login page
    class_frm["cls_login"]="access_frm"
    class_frm["cls_reg"]=""
    flash("Invalid date!")
    return render_template("login.html", formReg=formReg, formLogin=formLogin,
                            class_frm_log=class_frm["cls_login"], class_frm_reg=class_frm["cls_reg"])

@user_bp.route("/account/logout")
def logout():
   logout_user()
   return redirect(url_for('account.login'))

# this root is for creating an account
@user_bp.route("/account/register", methods=['GET','POST'])
def register_user():
   form = RegistrationUser(request.form)
   if request.method == 'POST' and form.validate():
      first_name = form.name.data
      surname = form.surname.data
      email = form.email.data
      tel= form.phone.data
      password = form.password.data
      user = User(first_name,surname,tel,email)
      user.set_password(password)
      # register_user() returns true if the user was successfully inserted into the database 
      # and false if there is an account in the database with the same email address
      is_register = user.register_user()
      if(is_register):
         flash("Your account has been created successfully.")
         return redirect(url_for('account.login'))
      else:
         class_frm["cls_login"]=" "
         class_frm["cls_reg"]="access_frm"
         flash("An account already exist with the email enterd!")
   else:
      # the information profided by the user fails the form validation 
      class_frm["cls_login"]=" "
      class_frm["cls_reg"]="access_frm"
      flash("Something got wrong!","danger")
   return redirect(url_for("account.login"))


