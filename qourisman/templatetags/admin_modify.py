from django.contrib.admin.templatetags.admin_modify import *

original_submit_row = submit_row

@register.inclusion_tag('admin/submit_line.html', takes_context=True)
def submit_row(context):
    ctx = original_submit_row(context)
    ctx.update({
        # Django 1.5.4 always displays Save button, modification makes save button shown conditionally
        'show_save': (context['change'] and context['has_change_permission']) or (context['add'] and context['has_add_permission'])
        })                                                                  
    return ctx 
