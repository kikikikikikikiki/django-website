#True1 = True
#True2 = True
#True3 = True
#True4 = True

#True1 = False
#True2 = False
#True3 = False
#True4 = False

circle_urls = {}
circle_urls2 = {}
circle_urls3 = {}
circle_urls4 = {}


def Calculator():
if len(matching_series.all())>0:
    if len(matching_series2.all())>0:
        if len(matching_series3.all())>0:
            if len(matching_series4.all())>0:
                for m in matching_series.all():
                  part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                  circle_urls1[m] = part_one.circle_slug
                for n in matching_series2.all():
                  part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                  circle_urls2[n] = part_one.circle_slug
                for o in matching_series3.all():
                  part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                  circle_urls3[o] = part_one.circle_slug
                for p in matching_series4.all():
                  part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                  circle_urls4[p] = part_one.circle_slug
        
                dict(circle_urls_all).update(circle_urls1)
                dict(circle_urls_all).update(circle_urls2)
                dict(circle_urls_all).update(circle_urls3)
                dict(circle_urls_all).update(circle_urls4)
        
                return render(request,
                        "main/circles.html",
                        {"part_ones": circle_urls_all})
            else:
                for m in matching_series.all():
                  part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                  circle_urls1[m] = part_one.circle_slug
                for n in matching_series2.all():
                  part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                  circle_urls2[n] = part_one.circle_slug
                for o in matching_series3.all():
                  part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
                  circle_urls3[o] = part_one.circle_slug
        
                dict(circle_urls_all).update(circle_urls1)
                dict(circle_urls_all).update(circle_urls2)
                dict(circle_urls_all).update(circle_urls3)
        
                return render(request,
                        "main/circles.html",
                        {"part_ones": circle_urls_all})
        elif len(matching_series4.all())>0:
            for m in matching_series.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls1[m] = part_one.circle_slug
            for n in matching_series2.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls2[n] = part_one.circle_slug
            for p in matching_series4.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls4[p] = part_one.circle_slug
    
            dict(circle_urls_all).update(circle_urls1)
            dict(circle_urls_all).update(circle_urls2)
            dict(circle_urls_all).update(circle_urls4)
    
            return render(request,
                    "main/circles.html",
                    {"part_ones": circle_urls_all})
        else:
            for m in matching_series.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls1[m] = part_one.circle_slug
            for n in matching_series2.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls2[n] = part_one.circle_slug
    
            dict(circle_urls_all).update(circle_urls1)
            dict(circle_urls_all).update(circle_urls2)
    
            return render(request,
                    "main/circles.html",
                    {"part_ones": circle_urls_all})

    if len(matching_series3.all())>0:
        if len(matching_series4.all())>0:

            for m in matching_series.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls1[m] = part_one.circle_slug
            for o in matching_series3.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls3[o] = part_one.circle_slug
            for p in matching_series4.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls4[p] = part_one.circle_slug
    
            dict(circle_urls_all).update(circle_urls1)
            dict(circle_urls_all).update(circle_urls3)
            dict(circle_urls_all).update(circle_urls4)
    
            return render(request,
                    "main/circles.html",
                    {"part_ones": circle_urls_all})
        else:
            for m in matching_series.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls1[m] = part_one.circle_slug
            for o in matching_series3.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls3[o] = part_one.circle_slug
    
            dict(circle_urls_all).update(circle_urls1)
            dict(circle_urls_all).update(circle_urls3)
    
            return render(request,
                    "main/circles.html",
                    {"part_ones": circle_urls_all})
    if len(matching_series4.all())>0:
            for m in matching_series.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls1[m] = part_one.circle_slug
            for p in matching_series4.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls4[p] = part_one.circle_slug

            dict(circle_urls_all).update(circle_urls1)
            dict(circle_urls_all).update(circle_urls4)

            return render(request,
                    "main/circles.html",
                    {"part_ones": circle_urls_all})

if len(matching_series2.all())>0:
    if len(matching_series3.all())>0:
        if len(matching_series4.all())>0:
            for n in matching_series2.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls2[n] = part_one.circle_slug
            for o in matching_series3.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls3[o] = part_one.circle_slug
            for p in matching_series4.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls4[p] = part_one.circle_slug
    
            dict(circle_urls_all).update(circle_urls2)
            dict(circle_urls_all).update(circle_urls3)
            dict(circle_urls_all).update(circle_urls4)
    
            return render(request,
                    "main/circles.html",
                    {"part_ones": circle_urls_all})
        else:
            for n in matching_series2.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls2[n] = part_one.circle_slug
            for o in matching_series3.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls3[o] = part_one.circle_slug
    
            dict(circle_urls_all).update(circle_urls2)
            dict(circle_urls_all).update(circle_urls3)
            return render(request,
                    "main/circles.html",
                    {"part_ones": circle_urls_all})

    elif len(matching_series4.all())>0:
            for n in matching_series2.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls2[n] = part_one.circle_slug
            for p in matching_series4.all():
              part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
              circle_urls4[p] = part_one.circle_slug
    
            dict(circle_urls_all).update(circle_urls2)
            dict(circle_urls_all).update(circle_urls4)
    
            return render(request,
                    "main/circles.html",
                    {"part_ones": circle_urls_all})
    else:
        for n in matching_series2.all():
          part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
          circle_urls2[n] = part_one.circle_slug

        dict(circle_urls_all).update(circle_urls2)

        return render(request,
                "main/circles.html",
                {"part_ones": circle_urls_all})
if len(matching_series3.all())>0:
    if len(matching_series4.all())>0:
        for o in matching_series3.all():
          part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
          circle_urls3[o] = part_one.circle_slug
        for p in matching_series4.all():
          part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
          circle_urls4[p] = part_one.circle_slug

        dict(circle_urls_all).update(circle_urls3)
        dict(circle_urls_all).update(circle_urls4)

        return render(request,
                "main/circles.html",
                {"part_ones": circle_urls_all})
    else:
        for o in matching_series3.all():
          part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
          circle_urls3[o] = part_one.circle_slug

        dict(circle_urls_all).update(circle_urls3)

        return render(request,
                "main/circles.html",
                {"part_ones": circle_urls_all})
if len(matching_series4.all())>0:
        for p in matching_series4.all():
          part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
          circle_urls4[p] = part_one.circle_slug

        dict(circle_urls_all).update(circle_urls4)

        return render(request,
                "main/circles.html",
                {"part_ones": circle_urls_all})
else:
    for p in matching_series1.all():
          part_one = Circle.objects.filter(circle_series__circle_series=m.circle_series).earliest("circle_published")
          circle_urls1[p] = part_one.circle_slug

        dict(circle_urls_all).update(circle_urls4)

        return render(request,
                "main/circles.html",
                {"part_ones": circle_urls_all})
print(0)
return HttpResponse(f"{single_slug} nothing to see here")
             

    Calculator()
