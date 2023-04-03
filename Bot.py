from flask import Flask, render_template 
from flask import request
from databseoperations import *
from frontendhelper import *
app = Flask(__name__, static_url_path='')
from HighLevel import *

import sys

#TODO reporoduce what you did in all the other pages from account generator

 # <-- Be aware: the area_input parameter expects a list, not a string



@app.route("/" , methods=['POST','GET'])
def IndexFront():
    return render_template("index.html")
@app.route("/index.html" , methods=['POST','GET'])
def Second():
    return render_template("index.html")
        
@app.route("/pages/forms/accountgenerator.html" , methods=['POST','GET'])
def accountgeneratorFront():
    account_list=database_read_all_accounts()
    print("request recieved at :",request.method, file=sys.stdout)
    if request.method=='POST':
        listu=splitter(request.form["mailss"])
        print(listu, file=sys.stdout)
        Create_n_account(listu)
        return render_template("pages/forms/accountgenerator.html",account_list=account_list)
    if request.method=='GET':
        #print(database_read_all_accounts(), file=sys.stdout)
        print("It's a GET request", file=sys.stdout)
        return render_template("pages/forms/accountgenerator.html", account_list=account_list)
@app.route("/pages/forms/GetFollowers.html" , methods=['POST','GET'])
def GetFollowersFront():
    follower_list=database_read_followers()
 
    if request.method=='POST':
        profile=request.form["profile_id"]
        number=request.form["number"]
        get_followers_high_level(int(number),profile)
        print(profile, file=sys.stdout)
        print(int(number), file=sys.stdout)
        return render_template("pages/forms/GetFollowers.html",follower_list=follower_list)
    if request.method=='GET':
        #print(database_read_all_accounts(), file=sys.stdout)
        print("It's a GET request", file=sys.stdout)
        return render_template("pages/forms/GetFollowers.html", follower_list=follower_list)

@app.route("/pages/forms/LikePost.html" , methods=['POST','GET'])
def LikePostFront():
    account_list=database_read_all_accounts()
    print("request recieved at :",request.method, file=sys.stdout)
    if request.method=='POST':
        link=request.form["link"]
        like_high_level(link)
        print(link, file=sys.stdout)
        return render_template("pages/forms/LikePost.html",account_list=account_list)
    if request.method=='GET':
        #print(database_read_all_accounts(), file=sys.stdout)
        print("It's a GET request", file=sys.stdout)
        return render_template("pages/forms/LikePost.html", account_list=account_list)
@app.route("/pages/forms/CommentPost.html" , methods=['POST','GET'])
def CommentPostFront():
    account_list=database_read_all_accounts()
    print("request recieved at :",request.method, file=sys.stdout)
    if request.method=='POST':
        link=request.form["Link"]
        print(link, file=sys.stdout)
        Comment=request.form["Comment"]
        print(Comment, file=sys.stdout)
        Comment_high_level(link,Comment)
        return render_template("pages/forms/CommentPost.html",account_list=account_list)
    if request.method=='GET':

        print("It's a GET request", file=sys.stdout)
        return render_template("pages/forms/CommentPost.html", account_list=account_list)
@app.route("/pages/forms/Follow.html" , methods=['POST','GET'])
def FollowFront():
    follower_list=database_read_followers()
 
    if request.method=='POST':
        number=request.form["number"]
        follow_high_level(int(number))
        print(int(number), file=sys.stdout)
        return render_template("pages/forms/Follow.html",follower_list=follower_list)
    if request.method=='GET':
        #print(database_read_all_accounts(), file=sys.stdout)
        print("It's a GET request", file=sys.stdout)
        return render_template("pages/forms/Follow.html", follower_list=follower_list)

@app.route("/pages/forms/ChangeBio.html" , methods=['POST','GET'])
def ChangeBioFront():
    account_list=database_read_all_accounts()
    
    if request.method=='POST':
        Bio=request.form["Bio"]
        print(Bio, file=sys.stdout)
        change_bio_high_level(Bio)
        return render_template("pages/forms/ChangeBio.html",account_list=account_list)
    if request.method=='GET':
        #print(database_read_all_accounts(), file=sys.stdout)
        print("It's a GET request", file=sys.stdout)
        return render_template("pages/forms/ChangeBio.html", account_list=account_list)
    
@app.route("/pages/forms/dm.html" , methods=['POST','GET'])
def DMFront():
    account_list=database_read_all_accounts()
    follower_list=database_read_followers()
    dmable = sum(p["dmable"] == 1 for p in follower_list)
    already_dmed = sum(p["already_dmed"] == 1 for p in follower_list)
    
    print("request recieved at :",request.method, file=sys.stdout)
    if request.method=='POST':
        message=request.form["Message"]
        print(message, file=sys.stdout)
        dm_high_level(message)
        already_dmed = sum(p["already_dmed"] == 1 for p in follower_list)
        return render_template("pages/forms/dm.html",account_list=account_list,dmable=dmable,already_dmed=already_dmed)
    if request.method=='GET':
        #print(database_read_all_accounts(), file=sys.stdout)
        print("It's a GET request", file=sys.stdout)
        return render_template("pages/forms/dm.html", account_list=account_list,dmable=dmable,already_dmed=already_dmed)
    
@app.route("/pages/forms/CheckDmable.html" , methods=['POST','GET'])
def CheckdmableFront():
    follower_list=database_read_followers()
    total_checked = sum(p["checked_dmable"] == 1 for p in follower_list)
    if request.method=='POST':
        number=request.form["number"]
        check_dmable_high_level(int(number))
        print(int(number), file=sys.stdout)
        total_checked = sum(p["checked_dmable"] == 1 for p in follower_list)
        return render_template("pages/forms/CheckDmable.html",follower_list=follower_list, total_checked=total_checked)
    if request.method=='GET':
        #print(database_read_all_accounts(), file=sys.stdout)
        print("It's a GET request", file=sys.stdout)
        return render_template("pages/forms/CheckDmable.html", follower_list=follower_list , total_checked=total_checked)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  