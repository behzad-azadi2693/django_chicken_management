from django.contrib import messages
from django.forms import fields, formset_factory, modelformset_factory
from django.forms.formsets import ManagementForm
from django.forms.models import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from .models import (
            FarmManage, Farms, Function, ImageLabratore, ImageMedician, Incaome, Losses, MakBery, ProfileChickens, 
            Schedule, Vaccination, Manufacturing, Medician, labratore
        )
from .forms import (
            FarmForm, FunctionForm, ImageLabratoreForm, ImageMedicianForm, IncaomForm, LabratoreForm, LossesForm, 
            ManufacturingForm, ProfilechickenForm, ScheduleForm, MakeBeryForm, 
            VaccinationForm,MedicianForm, ManagerForm, ImageMedician
        )
from django.db.models import Sum
# Create your views here.

def farms(request):
    farms = Farms.objects.all().only('pk','image','name_type','active','date_start').order_by('-active','-id')
    
    context = {
        'farms':farms
    }

    return render(request, 'farms.html', context)


def farm(request, pk):
    farm = get_object_or_404(Farms, pk=pk)
    manage = FarmManage.objects.filter(which_farm=farm)
    context = {
        'farm':farm,
        'manage':manage
    }
    return render(request, 'farm.html', context)


def create_farm(request):
    form = FarmForm()

    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            return redirect('farms:farm', obj.pk)
        else:
            form = FarmForm(request.POST, request.FILES)
            context = {
                'form':form
            }
            return render(request, 'create.html', context)
    else:
        return render(request, 'create.html',{'form':form})

def edit_farm(request, pk):
    obj = get_object_or_404(Farms, pk=pk)

    if not obj.active:
        messages.warning(request, 'این مزرعه فعال نمی باشد', 'warning')
        return redirect('farms:farm', obj.pk)

    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            return redirect('farms:farm', obj.pk)
        else:
            form = FarmForm(request.POST, request.FILES)
            context = {
                'form':form
            }
            return render(request, 'create.html', context)
    else:
        form = FarmForm(instance=obj)
        return render(request, 'create.html',{'form':form})


def profilechicken(request, pk):
    obj = get_object_or_404(Farms, pk=pk)
    profile = ProfileChickens.objects.filter(which_farm=obj).first()

    context = {
        'profile':profile
    }

    return render(request, 'medicians.html', context)

def create_profilechicken(request, pk):
    obj = get_object_or_404(Farms, pk=pk)

    check = ProfileChickens.objects.filter(which_farm=obj).first()

    if not obj.active:
        messages.warning(request, 'این مزرعه فعال نمی باشد', 'warning')
        return redirect('farms:farm', obj.pk)

    if check is not None:
        messages.error(request, 'این مزرعه زیر کشت می باشد', 'error')
        return redirect('farms:farm', obj.pk)

    if request.method == 'POST':
        form = ProfilechickenForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            return redirect('farms:profilechicken', obj.pk)
        else:
            form = ProfilechickenForm(request.POST)
            context = {
                'form':form
            }
            return render(request, 'create.html', context)
    else:
            data = {'which_farm':obj}
            form = ProfilechickenForm(initial=data)
            return render(request, 'create.html',{'form':form})


def edit_profilechicken(request, pk):
    obj = get_object_or_404(ProfileChickens, pk=pk)
    
    if not obj.which_farm.active:
        messages.warning(request, 'این مزرعه فعال نمی باشد', 'warning')
        return redirect('farms:profilechicken', obj.which_farm.pk)
    
    if request.method == 'POST':
        form = ProfilechickenForm(request.POST, instance=obj)
        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            return redirect('farms:profilechicken', obj.pk)
        else:
            form = ProfilechickenForm(request.POST)
            context = {
                'form':form
            }
            return render(request, 'create.html', context)

    else:
        form = ProfilechickenForm(instance=obj)
        return render(request, 'create.html',{'form':form})   

def vaccinations(request, pk):
    obj = get_object_or_404(Farms, pk=pk)

    queries = obj.farm_vaccination.all()

    context = {
        'vaccinations':queries
    }

    return render(request, 'medicians.html', context)

def create_vaccination(request, pk):
    obj = get_object_or_404(Farms, pk=pk)

    if not obj.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', obj.pk)

    if request.method == 'POST':
        form = VaccinationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            return redirect('farms:vaccinations', obj.pk)
        else:
            form = VaccinationForm(request.POST)
            context = {
                'form':form
            }
            return render(request, 'create.html', context)
    else:
        data = {'which_farm': obj}
        form = VaccinationForm(initial=data)
        return render(request, 'create.html',{'form':form})

def edit_vaccination(request, pk):
    obj = get_object_or_404(Vaccination, pk=pk)
    if not obj.which_farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:vaccinations', obj.which_farm.pk)

    if request.method == 'POST':
        form = VaccinationForm(request.POST, instance=obj)
        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            return redirect('farms:vaccination', obj.pk)
        else:
            form = VaccinationForm(request.POST)
            context = {
                'form':form
            }
            return render(request, 'create.html', context)

    else:
        form = VaccinationForm(instance=obj)
        return render(request, 'create.html',{'form':form})
























def functions(request, pk):
    farm = get_object_or_404(Farms, pk=pk)

    functions = Function.objects.filter(which_farm=farm)

    context = {
        'functions': functions
    }

    return render(request, 'medicians.html', context)

def create_function(request, pk):
    farm = get_object_or_404(Farms, pk=pk)

    if not farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', farm.pk)

    if request.method == 'POST':
        form = FunctionForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            return redirect('farms:functions', farm.pk)
        else:
            form = FunctionForm(request.POST)
            return render(request, 'create.html', {'form':form})
    else:
        data = {'which_farm': farm}
        form = FunctionForm(initial=data)
        return render(request, 'create.html', {'form':form})

def edit_function(request, pk):
    farm = get_object_or_404(Function, pk=pk)

    if not farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', farm.pk)

    if request.method == 'POST':
        form = FunctionForm(request.POST, instance=farm)

        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            pk = obj.which_farm.pk
            return redirect('farms:functions', pk)
        else:
            return render(request, 'create.html', {'form':form})
    else:
        form = FunctionForm(instance=farm)
        return render(request, 'create.html', {'form':form})


def schedules(request, pk):
    farm = get_object_or_404(Farms, pk=pk)

    schedules = Schedule.objects.filter(which_farm=farm)

    context = {
        'schedules': schedules
    }

    return render(request, 'medicians.html', context)

def create_schedule(request, pk):
    farm = get_object_or_404(Farms, pk=pk)

    if not farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', farm.pk)

    if request.method == 'POST':
        form = ScheduleForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            return redirect('farms:schedules', farm.pk)
        else:
            form = ScheduleForm(request.POST)
            return render(request, 'create.html', {'form':form})
    else:
        data = {'which_farm': farm}
        form = ScheduleForm(initial=data)
        return render(request, 'create.html', {'form':form})

def edit_schedule(request, pk):
    obj = get_object_or_404(Schedule, pk=pk)

    if not obj.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', obj.pk)

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=obj)

        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            pk = obj.which_farm.pk
            return redirect('farms:schedules', pk)
        else:
            return render(request, 'create.html', {'form':form})
    else:
        form = ScheduleForm(instance=obj)
        return render(request, 'create.html', {'form':form})

def edit_manage(request, pk):
    user = get_object_or_404(FarmManage, pk=pk)

    if not user.which_farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', user.which_farm.pk)

    if request.method == 'POST':
        form = ManagerForm(request.POST, instance=user)
        if form.is_valid():
            obj = form.save()
            pk = obj.which_farm.pk
            return redirect('farms:farm', pk)
        else:
            return render(request, 'create.html', {'form':form})

    else:
        form = ManagerForm(instance=user)
        return render(request, 'create.html', {'form':form})

def create_manage(request, pk):    
    farm = get_object_or_404(Farms, pk=pk)
    manageformset = modelformset_factory(FarmManage, ManagerForm, fields=('__all__'), extra=3)

    if not farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', farm.pk)

    if request.method == 'POST':
        formset = manageformset(data=request.POST)
        formset.save()
        return redirect('farms:farm', farm.pk)

    else:
        form = manageformset(queryset=FarmManage.objects.none(), initial=[
            {'which_farm':farm},
            {'which_farm':farm},
            {'which_farm':farm},
            ])
        context = {
            'formset':form
        }
        return render(request, 'create.html', context)

def make_bery(request, pk):
    farm = get_object_or_404(Farms, pk=pk)
    all_mak_bery = MakBery.objects.filter(which_farm=farm)
    return render(request, 'medicians.html', {'all_mak_bery':all_mak_bery})

def create_make_bery(request, pk):
    farm = get_object_or_404(Farms, pk=pk)

    if not farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', farm.pk)

    if request.method == 'POST':
        form = MakeBeryForm(request.POST)
        if form.is_valid():
            obj = form.save()
            pk = obj.which_farm.pk
            return redirect('farms:make_bery', pk)
        else:
            return render(request, 'create.html', {'form':form})
    else:
        data = {'which_farm':farm}
        form = MakeBeryForm(initial=data)
        return render(request, 'create.html', {'form':form})

def edit_make_bery(request, pk):
    obj = get_object_or_404(MakBery, pk=pk)

    if not obj.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', obj.pk)

    if request.method == 'POST':
        form = MakeBeryForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            pk = obj.which_farm.pk
            return redirect('farms:schedule', pk)
        else:
            return render(request, 'schedule/html', {'form':form})
    else:
        form = MakeBeryForm(instance=obj)
        return render(request, 'create.html', {'form':form})

def medicians(request, pk):
    farm = get_object_or_404(Farms, pk=pk)
    all_medician = Medician.objects.filter(which_farm=farm).order_by('-date')
    print(all_medician)
    context = {
        'all_medician':all_medician,
    }

    return render(request, 'medicians.html', context)

def create_medician(request, pk):
    farm = get_object_or_404(Farms, pk=pk)

    if not farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', farm.pk)

    if request.method == 'POST':
        form = MedicianForm(request.POST)
        if form.is_valid():
            obj = form.save()
            pk = obj.which_farm.pk
            return redirect('farms:medicians', pk)
        else:
            return render(request, 'create.html',{'form':form})

    else:
        data = {'which_farm':farm}
        form = MedicianForm(initial=data)
        return render(request, 'create.html', {'form':form})

def edit_medician(request, pk):
    obj = get_object_or_404(Medician, pk=pk)

    if not obj.which_farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:medicians', obj.which_farm.pk)

    if request.method == 'POST':
        form = MedicianForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            pk = obj.which_farm.pk
            return redirect('farms:medicians', pk)
        else:
            return render(request, 'create.html',{'form':form})
            
    else:
        form = MedicianForm(instance=obj)
        return render(request, 'create.html', {'form':form})


def add_image_to_medician(request, pk):
    mdc = get_object_or_404(Medician, pk=pk)

    if not mdc.which_farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:medicians', mdc.which_farm.pk)

    if request.method == 'POST':
        form = ImageMedicianForm(request.POST, request.FILES)
        if form.is_valid():
            for file in form:
                form.save()
            pk = mdc.which_farm.pk
            return redirect('farms:medicians', pk)
        else:
            return render(request, 'create.html', {'form':form})
    else:
        data = {'which_medician':mdc}
        form = ImageMedicianForm(initial=data)
        return render(request, 'create.html', {'form':form})

def all_image_medician(request, pk):
    obj = get_object_or_404(Medician, pk=pk)
    imgs = ImageMedician.objects.filter(which_medician=obj)
    return render(request, 'show_image.html', {'imgsM':imgs})

def remove_image_medician(request, pk):
    img = get_object_or_404(ImageMedician, pk=pk)

    if not img.which_medician.which_farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:all_image_medician', img.which_medician.pk)

    pk = img.which_medician.pk
    img.delete()
    return redirect('farms:all_image_medician', pk)


def labratores(request, pk):
    farm = get_object_or_404(Farms, pk=pk)
    all_labratore = labratore.objects.filter(which_farm=farm).order_by('-date')

    context = {
        'all_labratore':all_labratore
    }

    return render(request, 'medicians.html', context)

def create_labratore(request, pk):
    farm = get_object_or_404(Farms, pk=pk)

    if not farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', farm.pk)

    if request.method == 'POST':
        form = LabratoreForm(request.POST)
        if form.is_valid():
            obj = form.save()
            pk = obj.which_farm.pk
            return redirect('farms:labratores', pk)
        else:
            return render(request, 'create.html',{'form':form})

    else:
        data = {'which_farm':farm}
        form = LabratoreForm(initial=data)
        return render(request, 'create.html', {'form':form})

def edit_labratore(request, pk):
    obj = get_object_or_404(labratore, pk=pk)

    if not obj.which_farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:labratores', obj.which_farm.pk)

    if request.method == 'POST':
        form = LabratoreForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            pk = obj.which_farm.pk
            return redirect('farms:labratores', pk)
        else:
            return render(request, 'create.html',{'form':form})
            
    else:
        form = LabratoreForm(instance=obj)
        return render(request, 'create.html', {'form':form})


def add_image_to_labratore(request, pk):
    lab = get_object_or_404(labratore, pk=pk)

    if not lab.which_farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:labratores', lab.which_farm.pk)

    if request.method == 'POST':
        form = ImageLabratoreForm(request.POST, request.FILES)
        if form.is_valid():
            for image in request.FILES.getlist('image'):
                ImageLabratore.objects.create(image=image, labratore=lab)
            pk = lab.which_farm.pk
            return redirect('farms:labratores', pk)
        else:
            return render(request, 'create.html', {'form':form})
    else:
        data = {'labratore':lab}
        form = ImageLabratoreForm(initial=data)
        return render(request, 'create.html', {'form':form})

def all_image_labratore(request, pk):
    obj = get_object_or_404(labratore, pk=pk)
    imgs = ImageLabratore.objects.filter(labratore = obj)
    return render(request, 'show_image.html', {'imgsA':imgs})

def remove_image_labratore(request, pk):
    img = get_object_or_404(ImageLabratore, pk=pk)

    if not img.labratore.which_farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:all_image_labratore', img.labratore.pk)

    pk = img.labratore.pk
    img.delete()
    return redirect('farms:all_image_labratore', pk)

def manufacturing_farm(request, pk):
    obj = get_object_or_404(Farms, pk=pk)
    manu = obj.farm_manufacturing.all()

    sum_broken = manu.aggregate(Sum('Broken'))
    sum_normal = manu.aggregate(Sum('normal'))
    sum_eggyolk = manu.aggregate(Sum('eggـyolk'))

    context = {
        'broken' :sum_broken['Broken__sum'],
        'normal' :sum_normal['normal__sum'],
        'eggyolk':sum_eggyolk['eggـyolk__sum'],
        'manu': manu
    }

    return render(request, 'manufacturing_farm.html', context)

def create_manufacturing(request, pk):
    obj = get_object_or_404(Farms, pk=pk)

    if not obj.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', obj.pk)

    if request.method == 'POST':
        form = ManufacturingForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            return redirect('farms:manufacturing_farm', obj.which_farm.pk)
        else:
            form = ManufacturingForm(request.POST)
            context = {
                'form':form
            }
            return render(request, 'create.html', context)
    else:
        data = {'which_farm': obj}
        form = ManufacturingForm(initial=data)
        return render(request, 'create.html',{'form':form})

def edit_manufacturing(request, pk):
    obj = get_object_or_404(Manufacturing, pk=pk)

    if not obj.which_farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', obj.pk)

    if request.method == 'POST':
        form = ManufacturingForm(request.POST, instance=obj)
        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            return redirect('farms:manufacturing_farm', obj.which_farm.pk)
        else:
            form = ManufacturingForm(request.POST)
            context = {
                'form':form
            }
            return render(request, 'create.html', context)

    else:
        form = ManufacturingForm(instance=obj)
        return render(request, 'create.html',{'form':form})

def losses(request, pk):
    farm = get_object_or_404(Farms, pk=pk)

    all_losses = Losses.objects.filter(which_farm=farm)
    
    sum_hit_back = all_losses.aggregate(Sum('hit_back'))
    sum_sickness = all_losses.aggregate(Sum('sickness'))
    sum_suffocation = all_losses.aggregate(Sum('suffocation'))
    sum_physics = all_losses.aggregate(Sum('physics'))

    context = {
        'hit_back' :sum_hit_back['hit_back__sum'],
        'sickness' :sum_sickness['sickness__sum'],
        'suffocation':sum_suffocation['suffocation__sum'],
        'physics':sum_physics['physics__sum'],
        'losses':all_losses,
    }
    print(context)

    return render(request, 'losse.html', context)

def losse(request, pk):
    losse = get_object_or_404(Losses ,pk=pk)

    context = {
        'losse':losse
    }
    return render(request, 'losse.html', context)

def create_losse(request, pk):
    obj = get_object_or_404(Farms, pk=pk)

    if not obj.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', obj.pk)

    if request.method == 'POST':
        form = LossesForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            return redirect('farms:losse', obj.pk)
        else:
            form = LossesForm(request.POST)
            return render(request, 'create.html', {'form':form})
    else:
        data = {'which_farm': obj}
        form = LossesForm(initial=data)
        return render(request, 'create.html', {'form':form})

def edit_losse(request, pk):
    obj = get_object_or_404(Losses, pk=pk)

    if not obj.which_farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:losse', obj.pk)

    if request.method == 'POST':
        form = LossesForm(request.POST, instance=obj)

        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            return redirect('farms:losse', obj.pk)
        else:
            form = LossesForm(request.POST)
            return render(request, 'create.html', {'form':form})
    else:
        form = LossesForm(instance=obj)
        return render(request, 'create.html', {'form':form})














def incaomes(request, pk):
    farm = get_object_or_404(Farms, pk=pk)

    incaomes = Incaome.objects.filter(which_farm =farm)

    context = {
        'incaomes':incaomes
    }
    return render(request, 'incaomes.html', context)

def create_incaome(request, pk):
    farm = get_object_or_404(Farms, pk=pk)

    if not farm.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', farm.pk)

    if request.method == 'POST':
        form = IncaomForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            return redirect('farms:incomes', farm.pk)
        else:
            form = IncaomForm(request.POST)
            return render(request, 'create.html', {'form':form})
    else:
        data = {'which_farm': farm}
        form = IncaomForm(initial=data)
        return render(request, 'create.html', {'form':form})

def edit_incaome(request, pk):
    obj = get_object_or_404(Incaome, pk=pk)

    if not obj.active:
        messages.error(request, 'این مزرعه فعال نمی باشد', 'error')
        return redirect('farms:farm', obj.pk)

    if request.method == 'POST':
        form = IncaomForm(request.POST, instance=obj)

        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save()
            pk = obj.which_farm.pk
            return redirect('farms:incaomes', pk)
        else:
            return render(request, 'create.html', {'form':form})
    else:
        form = IncaomForm(instance=obj)
        return render(request, 'create.html', {'form':form})