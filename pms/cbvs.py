

from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from horilla_views.generic.cbv import views
from pms import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _trans
from django.contrib import messages

from pms.filters import BonusPointSettingFilter,EmployeeBonusPointFilter
from pms.forms import BonusPointSettingForm,EmployeeBonusPointForm

#================Models for BonusPointSetting==============
class BonusPointSettingSectionView(views.HorillaSectionView):
    """
    BonusPointSetting SectionView
    """

    nav_url = reverse_lazy("bonus-point-setting-nav")
    view_url = reverse_lazy("bonus-point-setting-list-view")
    view_container_id = "listContainer"

    # script_static_paths = [
    #     "static/automation/automation.js",
    # ]

    template_name = "bonus/bonus_point_setting_section.html"



class BonusPointSettingNavView(views.HorillaNavView):
    """
    BonusPointSetting nav view
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.create_attrs = f"""
            hx-get="{reverse_lazy("create-bonus-point-setting")}"
            hx-target="#genericModalBody"
            data-toggle="oh-modal-toggle"
            data-target="#genericModal"
        """

    nav_title = _trans("Bonus Point Setting")
    search_url = reverse_lazy("bonus-point-setting-list-view")
    search_swap_target = "#listContainer"


class BonusPointSettingFormView(views.HorillaFormView):
    """
    BonusPointSettingForm View
    """

    form_class = BonusPointSettingForm
    model = models.BonusPointSetting
    new_display_title = _trans("Create Bonus Point Setting")
    # template_name = "bonus/bonus_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        instance = models.BonusPointSetting.objects.filter(pk=self.kwargs["pk"]).first()
        kwargs["instance"] = instance
        return kwargs
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        return context
    
    def form_invalid(self, form: Any) -> HttpResponse:
       
        if not form.is_valid():
            errors = form.errors.as_data()
            return render(
                self.request, self.template_name, {"form": form, "errors": errors}
            )
        return super().form_invalid(form)
    def form_valid(self, form: BonusPointSettingForm) -> views.HttpResponse:
        if form.is_valid():
            message = "Bonus Point Setting added"
            if form.instance.pk:
                message = "Bonus Point Setting updated"
            form.save()

            messages.success(self.request, _trans(message))
            return self.HttpResponse()
        
        return super().form_valid(form)


class BonusPointSettingListView(views.HorillaListView):
    """
    BnusPointSetting list view
    """
    model = models.BonusPointSetting
    search_url = reverse_lazy("bonus-point-setting-list-view")
    filter_class = BonusPointSettingFilter
    action_method = "action_template"
    # actions = [
    #     {
    #         "action": "Edit",
    #         "icon": "create-outline",
    #         "attrs": """
    #             class="oh-btn oh-btn--light-bkg w-100"
    #             hx-get="{edit_url}?instance_ids={ordered_ids}"
    #             hx-target="#genericModalBody"
    #             data-target="#genericModal"
    #             data-toggle="oh-modal-toggle"
    #         """,
    #     },
    #     {
    #         "action": "Delete",
    #         "icon": "trash-outline",
    #         "attrs": """
    #         class="oh-btn oh-btn--light-bkg w-100 tex-danger"
    #         onclick="
    #             event.stopPropagation();
    #             confirm('Do you want to delete the bonus point setting?','{delete_url}')
    #         "
    #         """,
    #     },
    # ]

    columns = [
        ("Model", "get_model_display"),
        ("Bonus For", "get_bonus_for_display"),
        ("Condition", "get_condition"),
        ("Points", 'points'),
        ("Is Active",'is_active'),
    ]


#================Models for EmployeeBonusPoint==============

class EmployeeBonusPointSectionView(views.HorillaSectionView):
    """
    EmployeeBonusPoint SectionView
    """

    nav_url = reverse_lazy("employee-bonus-point-nav")
    view_url = reverse_lazy("employee-bonus-point-list-view")
    view_container_id = "listContainer"

    # script_static_paths = [
    #     "static/automation/automation.js",
    # ]

    template_name = "bonus/employee_bonus_point_section.html"



class EmployeeBonusPointNavView(views.HorillaNavView):
    """
    BonusPoint nav view
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.create_attrs = f"""
            hx-get="{reverse_lazy("create-employee-bonus-point")}"
            hx-target="#genericModalBody"
            data-toggle="oh-modal-toggle"
            data-target="#genericModal"
        """

    nav_title = _trans("Employee Bonus Point ")
    search_url = reverse_lazy("employee-bonus-point-list-view")
    search_swap_target = "#listContainer"


class EmployeeBonusPointFormView(views.HorillaFormView):
    """
    BonusPointForm View
    """

    form_class = EmployeeBonusPointForm
    model = models.EmployeeBonusPoint
    new_display_title = _trans("Create Employee Bonus Point ")
    # template_name = "bonus/bonus_form.html"
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        return context
    
    def form_invalid(self, form: Any) -> HttpResponse:
       
        if not form.is_valid():
            errors = form.errors.as_data()
            return render(
                self.request, self.template_name, {"form": form, "errors": errors}
            )
        return super().form_invalid(form)
    def form_valid(self, form: EmployeeBonusPointForm) -> views.HttpResponse:
        if form.is_valid():
            message = "Bonus Point added"
            if form.instance.pk:
                message = "Bonus Point updated"
            form.save()

            messages.success(self.request, _trans(message))
            return self.HttpResponse()
        
        return super().form_valid(form)


class EmployeeBonusPointListView(views.HorillaListView):
    """
    BnusPoint list view
    """
    model = models.EmployeeBonusPoint
    search_url = reverse_lazy("employee-bonus-point-list-view")
    filter_class = EmployeeBonusPointFilter
    # actions = [
    #     {
    #         "action": "Edit",
    #         "icon": "create-outline",
    #         "attrs": """
    #             class="oh-btn oh-btn--light-bkg w-100"
    #             hx-get="{edit_url}?instance_ids={ordered_ids}"
    #             hx-target="#genericModalBody"
    #             data-target="#genericModal"
    #             data-toggle="oh-modal-toggle"
    #         """,
    #     },
    #     {
    #         "action": "Delete",
    #         "icon": "trash-outline",
    #         "attrs": """
    #         class="oh-btn oh-btn--light-bkg w-100 tex-danger"
    #         onclick="
    #             event.stopPropagation();
    #             confirm('Do you want to delete the automation?','{delete_url}')
    #         "
    #         """,
    #     },
    # ]

    columns = [
        ("Employee", "employee_id"),
        ("Bonus Point", "bonus_point"),
        ("Based On",'based_on'),

    ]