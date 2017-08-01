
#versionupdate
def versionList(request):
    if not _islogin(request):
        return HttpResponseRedirect(page404)
    constantJson = _get_constant(request)
    version = VersionUp.objects
    constantJson['version'] = version
    return render_to_response('version/index.html',constantJson,context_instance=RequestContext(request))

def versionadd(request):
    now_time = strftime("%Y%m%d ")
    
    if not _islogin(request):
        return HttpResponseRedirect('/page-404.htm')
    constantJson = _get_constant(request)
    
        
        
    
    return render_to_response('version/add.html',constantJson,context_instance=RequestContext(request))
 

def versionupdate(request):
    now_time = strftime("%Y%m%d") 
    if not _islogin(request):
        return HttpResponseRedirect('/page-404.htm')
    constantJson = _get_constant(request)
    if request.method == 'POST':        
        ver = VersionUp()
        ver.add_time = strftime("%Y-%m-%d %H:%M:%S")
        ver.summary = request.POST['summary']
        ver.readmecontent = request.POST['readmecontent']
        ver.state = 1
        ver.save()
        constantJson['now_time'] = now_time
        path = r"/var/www/html/lingyun/mp/version/"+ str(now_time) + '/source'
        mkdir(path)
        path1 =  r"/var/www/html/lingyun/mp/version/"+ str(now_time)
        f=open(path1+ '/'+ 'hello.txt',"w+")        
        f.writelines(ver.readmecontent)
        f.close()
        return HttpResponseRedirect('/management/version/update.html')
    return render_to_response('version/update.html',constantJson,context_instance=RequestContext(request))


def versionupdate2(request):
    now_time = strftime("%Y%m%d") 
    constantJson = _get_constant(request)
    if request.method == 'POST':
        myFile =request.FILES.get("myfile", None)
        if not myFile:
            return HttpResponse("no files for upload!")
        path = r"/var/www/html/lingyun/mp/version/"+ str(now_time) + '/source'
        destination = open(os.path.join(path,myFile.name),'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
            destination.close()
    return render_to_response('version/index.html',constantJson,context_instance=RequestContext(request))


def mkdir(path):    
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

def zip_file():
    try:        
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED
    now_time = strftime("%Y-%m-%d ")
    path = "///var/www/html/lingyun/mp/version/"+ now_time  #要进行压缩的文档目录
    start = path.rfind(os.sep) + 1
    filename = '///var/www/html/lingyun/mp/version/ '+ now_time  #压缩后的文件名
    z = zipfile.ZipFile(filename,mode = "w",compression = compression)
    try:
        for dirpath,dirs,files in os.walk(path):
            for file in files:
                if file == filename or file == "zip.py":
                    continue
                print(file)
            z_path = os.path.join(dirpath,file)
            z.write(z_path,z_path[start:])
        z.close()
    except:
        if z:
            z.close()
    

