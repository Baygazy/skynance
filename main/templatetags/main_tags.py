# from event.models import Event
# from event.models import Fighter
# from django import template
#
# register = template.Library()
#
#
# @register.inclusion_tag('event/event_profile_top.html')
# def top_info(event):
#     return {'event': event}
#
#
# @register.inclusion_tag('event/event_top_menu.html')
# def top_menu(event, request):
#     return {'event': event, 'request':request}
#
#
# @register.inclusion_tag('event/slider.html')
# def slider_list():
#     events = Event.objects.order_by('pk').filter(is_finished=False)
#     return {'events': events}
#
# @register.simple_tag
# def event_registration_view_class(fighter):
#     if fighter.paid == 'PAID':
#         if fighter.f_category != fighter.category or fighter.f_belt != fighter.belt or fighter.f_weight != fighter.weight or str(fighter.f_gender) != str(fighter.gender):
#             return "item dark moved"
#         return "item dark"
#     else:
#         return "item dark not-paid"
#
# @register.simple_tag
# def win_class(winner, fighter):
#     if winner and winner == fighter:
#         return 'win'
#     else:
#         return ''
#
# @register.simple_tag
# def bracket_status_class(group_bracket):
#     if group_bracket.status == "FINISHED":
#         return "color: yellow"
#     elif group_bracket.status == "AWARDED":
#         return "color: greenyellow"
#     else:
#         return ""
#
# @register.simple_tag
# def active_inf_class(request ):
#     path = request.path
#     if '/info/' in path :
#         return 'active'
#     else:
#         return ''
#
# @register.simple_tag
# def active_reg_class(request ):
#     path = request.path
#     if '/registration/show/' in path :
#         return 'active'
#     else:
#         return ''
#
# @register.simple_tag
# def active_schedule_class(request ):
#     path = request.path
#     if '/group/bracket/' in path :
#         return 'active'
#     else:
#         return ''
#
# @register.simple_tag
# def give_place(bracket):
#     if bracket.winner and bracket.stage == 1 and bracket.branch == 1:
#         return "final"
#     elif bracket.winner and bracket.stage == 1 and bracket.branch == 2:
#         return "third-place"
#     else:
#         return ""