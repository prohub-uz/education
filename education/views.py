from education.services.Clients.Views.GetListSpecialitiesView import GetListSpecialities
from education.services.Clients.Views.GetModulesView import GetModules
from education.services.Clients.Views.ModuleDetailView import ModuleDetailView
from education.services.Clients.Views.GetLessonsListView import GetLessonsListView
from education.services.Clients.Views.LessonDetailView import LessonDetailView

# Get list of Specialities
GetListSpecialities = GetListSpecialities().as_view()


# Get modules by speciality
GetModules = GetModules().as_view()


# Get module by id
ModuleDetailView = ModuleDetailView.as_view()

# Get list of Lessons
GetLessonsListView = GetLessonsListView().as_view()


# Get lesson by id
LessonDetailView = LessonDetailView.as_view()