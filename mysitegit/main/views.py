from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries, Circle, CircleCategory, CircleSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from .forms import NewUserForm

def single_slug(request, single_slug):
      circle_categories = [o.circle_slug for o in CircleCategory.objects.all()]
      if single_slug in circle_categories:
        matching_series = CircleSeries.objects.filter(circle_category__circle_slug=single_slug)
        matching_series2 = CircleSeries.objects.filter(circle_category2__circle_slug=single_slug)
        matching_series3 = CircleSeries.objects.filter(circle_category3__circle_slug=single_slug)
        matching_series4 = CircleSeries.objects.filter(circle_category4__circle_slug=single_slug)

        
        circle_urls_all = {}
        circle_urls1 = {}
        circle_urls2 = {}
        circle_urls3 = {}
        circle_urls4 = {}
        if len(matching_series.all())>0:
            if len(matching_series2.all())>0:
                if len(matching_series3.all())>0:
                    if len(matching_series4.all())>0:
                        for m in matching_series.all():
                            part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                            circle_urls1[m] = part_one.circle_slug
                        for n in matching_series2.all():
                            part_one = Circle.objects.filter(circle_series__circle_series=n.circle_series).earliest("circle_published")
                            circle_urls2[n] = part_one.circle_slug
                        for o in matching_series3.all():
                            part_one = Circle.objects.filter(circle_series__circle_series=o.circle_series).earliest("circle_published")
                            circle_urls3[o] = part_one.circle_slug
                        for p in matching_series4.all():
                            part_one = Circle.objects.filter(circle_series__circle_series=p.circle_series).earliest("circle_published")
                            circle_urls4[p] = part_one.circle_slug

                        circle_urls_all.update(circle_urls1)
                        circle_urls_all.update(circle_urls2)
                        circle_urls_all.update(circle_urls3)
                        circle_urls_all.update(circle_urls4)

                        return render(request,
                                "main/lotus.html",
                                {"part_ones": circle_urls_all})
                    else:
                        for m in matching_series.all():
                            part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                            circle_urls1[m] = part_one.circle_slug
                        for n in matching_series2.all():
                            part_one = Circle.objects.filter(circle_series__circle_series=n.circle_series).earliest("circle_published")
                            circle_urls2[n] = part_one.circle_slug
                        for o in matching_series3.all():
                            part_one = Circle.objects.filter(circle_series__circle_series=o.circle_series).earliest("circle_published")
                            circle_urls3[o] = part_one.circle_slug

                        circle_urls_all.update(circle_urls1)
                        circle_urls_all.update(circle_urls2)
                        circle_urls_all.update(circle_urls3)

                        return render(request,
                                  "main/lotus.html",
                                  {"part_ones": circle_urls_all})

                elif len(matching_series4.all())>0:
                    for m in matching_series.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                        circle_urls1[m] = part_one.circle_slug
                    for n in matching_series2.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=n.circle_series).earliest("circle_published")
                        circle_urls2[n] = part_one.circle_slug
                    for p in matching_series4.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=p.circle_series).earliest("circle_published")
                        circle_urls4[p] = part_one.circle_slug

                    circle_urls_all.update(circle_urls1)
                    circle_urls_all.update(circle_urls2)
                    circle_urls_all.update(circle_urls4)
          
                    return render(request,
                            "main/lotus.html",
                            {"part_ones": circle_urls_all})
                else:
                    for m in matching_series.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                        circle_urls1[m] = part_one.circle_slug
                    for n in matching_series2.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=n.circle_series).earliest("circle_published")
                        circle_urls2[n] = part_one.circle_slug

                    circle_urls_all.update(circle_urls1)
                    circle_urls_all.update(circle_urls2)

                    return render(request,
                            "main/lotus.html",
                            {"part_ones": circle_urls_all})

            elif len(matching_series3.all())>0:
                if len(matching_series4.all())>0:
                    for m in matching_series.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                        circle_urls1[m] = part_one.circle_slug
                    for o in matching_series3.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=o.circle_series).earliest("circle_published")
                        circle_urls3[o] = part_one.circle_slug
                    for p in matching_series4.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=p.circle_series).earliest("circle_published")
                        circle_urls4[p] = part_one.circle_slug

                    circle_urls_all.update(circle_urls1)
                    circle_urls_all.update(circle_urls3)
                    circle_urls_all.update(circle_urls4)

                    return render(request,
                              "main/lotus.html",
                              {"part_ones": circle_urls_all})
                else:
                    for m in matching_series.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                        circle_urls1[m] = part_one.circle_slug
                    for o in matching_series3.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=o.circle_series).earliest("circle_published")
                        circle_urls3[o] = part_one.circle_slug

                    circle_urls_all.update(circle_urls1)
                    circle_urls_all.update(circle_urls3)

                    return render(request,
                            "main/lotus.html",
                            {"part_ones": circle_urls_all})

            elif len(matching_series4.all())>0:
                for m in matching_series.all():
                    part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                    circle_urls1[m] = part_one.circle_slug
                for p in matching_series4.all():
                    part_one = Circle.objects.filter(circle_series__circle_series=p.circle_series).earliest("circle_published")
                    circle_urls4[p] = part_one.circle_slug

                circle_urls_all.update(circle_urls1)
                circle_urls_all.update(circle_urls4)

                return render(request,
                        "main/lotus.html",
                        {"part_ones": circle_urls_all})

        if len(matching_series2.all())>0:
            if len(matching_series3.all())>0:
                if len(matching_series4.all())>0:
                    for n in matching_series2.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=n.circle_series).earliest("circle_published")
                        circle_urls2[n] = part_one.circle_slug
                    for o in matching_series3.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=o.circle_series).earliest("circle_published")
                        circle_urls3[o] = part_one.circle_slug
                    for p in matching_series4.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=p.circle_series).earliest("circle_published")
                        circle_urls4[p] = part_one.circle_slug

                    circle_urls_all.update(circle_urls2)
                    circle_urls_all.update(circle_urls3)
                    circle_urls_all.update(circle_urls4)

                    return render(request,
                            "main/lotus.html",
                            {"part_ones": circle_urls_all})
                else:
                    for n in matching_series2.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=n.circle_series).earliest("circle_published")
                        circle_urls2[n] = part_one.circle_slug
                    for o in matching_series3.all():
                        part_one = Circle.objects.filter(circle_series__circle_series=o.circle_series).earliest("circle_published")
                        circle_urls3[o] = part_one.circle_slug

                    circle_urls_all.update(circle_urls2)
                    circle_urls_all.update(circle_urls3)
                    
                    return render(request,
                            "main/lotus.html",
                            {"part_ones": circle_urls_all})

            elif len(matching_series4.all())>0:
                for n in matching_series2.all():
                    part_one = Circle.objects.filter(circle_series__circle_series=n.circle_series).earliest("circle_published")
                    circle_urls2[n] = part_one.circle_slug
                for p in matching_series4.all():
                    part_one = Circle.objects.filter(circle_series__circle_series=p.circle_series).earliest("circle_published")
                    circle_urls4[p] = part_one.circle_slug
            
                circle_urls_all.update(circle_urls2)
                circle_urls_all.update(circle_urls4)
            
                return render(request,
                        "main/lotus.html",
                        {"part_ones": circle_urls_all})
            else:
                for n in matching_series2.all():
                    part_one = Circle.objects.filter(circle_series__circle_series=n.circle_series).earliest("circle_published")
                    circle_urls2[n] = part_one.circle_slug

                circle_urls_all.update(circle_urls2)

                return render(request,
                        "main/lotus.html",
                        {"part_ones": circle_urls_all})
        if len(matching_series3.all())>0:
            if len(matching_series4.all())>0:
                for o in matching_series3.all():
                    part_one = Circle.objects.filter(circle_series__circle_series=o.circle_series).earliest("circle_published")
                    circle_urls3[o] = part_one.circle_slug
                for p in matching_series4.all():
                    part_one = Circle.objects.filter(circle_series__circle_series=p.circle_series).earliest("circle_published")
                    circle_urls4[p] = part_one.circle_slug

                circle_urls_all.update(circle_urls3)
                circle_urls_all.update(circle_urls4)

                return render(request,
                        "main/lotus.html",
                        {"part_ones": circle_urls_all})
            else:
                for o in matching_series3.all():
                    part_one = Circle.objects.filter(circle_series__circle_series=o.circle_series).earliest("circle_published")
                    circle_urls3[o] = part_one.circle_slug
                circle_urls_all.update(circle_urls3)

                return render(request,
                        "main/lotus.html",
                        {"part_ones": circle_urls_all})

        if len(matching_series4.all())>0:
            for p in matching_series4.all():
                part_one = Circle.objects.filter(circle_series__circle_series=p.circle_series).earliest("circle_published")
                circle_urls4[p] = part_one.circle_slug

            circle_urls_all.update(circle_urls4)

            return render(request,
                  "main/lotus.html",
                  {"part_ones": circle_urls_all})
        else:
            for p in matching_series1.all():
                part_one = Circle.objects.filter(circle_series__circle_series=p.circle_series).earliest("circle_published")
                circle_urls1[p] = part_one.circle_slug
                
            circle_urls_all.update(circle_urls4)

            return render(request,
                      "main/lotus.html",
                      {"part_ones": circle_urls_all})

        return HttpResponse(f"{single_slug} nothing to see here")  


      categories = [c.category_slug for c in TutorialCategory.objects.all()]
      if single_slug in categories:
        matching_series_tut = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)

        series_urls = {}
        for m in matching_series_tut.all():
          part_two = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
          series_urls[m] = part_two.tutorial_slug
        return render(request,
                "main/category.html",
                {"part_ones": series_urls})

      tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]

      if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('tutorial_published')
        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)


        return render(request=request, 
                template_name="main/tutorial.html",
                 context={"tutorial":this_tutorial,
                      "sidebar":tutorials_from_series,
                      "this_tut_idx":this_tutorial_idx})

      if single_slug in circles:
        this_circle = Circle.objects.get(circle_slug=single_slug)
        circles_from_series = Circle.objects.filter(circle_series__circle_series=this_circle.circle_series).order_by('circle_published')
        this_circle_idx = list(circles_from_series).index(this_circle)
        four = range(4)

        return render(request=request, 
                template_name="main/circle.html",
                 context={"tutorial":this_circle,
                      "this_tut_idx":this_circle_idx})

      


        return HttpResponse(f"{single_slug} is a tutorial!!!")

      return HttpResponse(f"{single_slug} does not correspond to anything.")


def home(request):
  return render(request=request,
          template_name="main/home.html",
          context={"categories": TutorialCategory.objects.all()})

def homepage(request):
  return render(request=request,
          template_name="main/categories.html",
          context={"categories": TutorialCategory.objects.all()})

def register(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get("username")
      messages.success(request, f"New Account Created: {username}")
      login(request, user)
      messages.info(request, f"You are now logged in as {username}")
      return redirect("main:homepage")
    else:
      for msg in form.error_messages:
        messages.error(request, f"{msg}: {form.error_messages[msg]}")

  form = NewUserForm
  return render(request, 
          "main/register.html",
          context={"form":form})

def logout_request(request):
  logout(request)
  messages.info(request, "Logged out successfully!")
  return redirect("main:homepage")

def login_request(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged in as {username}")
        return redirect("main:homepage")
      else:
        messages.error(request, "Invalid username or password")

    else:
      messages.error(request, "Invalid username or password")

  form = AuthenticationForm()
  return render(request,
         "main/login.html",
         {"form":form})

