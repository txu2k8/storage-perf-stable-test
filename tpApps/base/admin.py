from django.contrib import admin
from tpApps.base.models import Project, GlobalEnv, GlobalWorkflow,  GlobalLabel, TestTask


class ReadOnlyModelAdmin(admin.ModelAdmin):
    """ModelAdmin class that prevents modifications through the admin.

    The changelist and the detail view work, but a 403 is returned
    if one actually tries to edit an object.
    """

    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    # Allow viewing objects but not actually changing them
    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return True
        return super(ReadOnlyModelAdmin, self).has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False


class ReadAndDeleteModelAdmin(admin.ModelAdmin):
    """ModelAdmin class that prevents modifications through the admin.

    The changelist and the detail view work, but a 403 is returned
    if one actually tries to edit an object.
    """

    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    # Allow viewing objects but not actually changing them
    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return True
        return super(ReadAndDeleteModelAdmin, self).has_change_permission(request, obj)


class ProjectForm(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'status', 'creator')
    list_display_links = ('id', 'name', )
    list_filter = ('status', )
    list_per_page = 20
    ordering = ('id',)
    fieldsets = ([
        '项目', {
            'fields': ('name', 'version', 'creator', 'updater', 'status', 'description')
        }],
    )


admin.site.register(Project, ProjectForm)


class GlobalEnvForm(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'status')
    list_display_links = ('id', 'name')
    list_filter = ('status', )
    list_per_page = 20
    ordering = ('id',)
    fieldsets = ([
        '全局环境配置', {
            'fields': ('name', 'project', 'config', 'data', 'description', 'status')
        }],)


admin.site.register(GlobalEnv, GlobalEnvForm)


class GlobalWorkflowForm(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'status')
    list_display_links = ('id', 'name')
    list_filter = ('status', )
    list_per_page = 20
    ordering = ('id',)
    fieldsets = ([
        '工作流', {
            'fields': ('name', 'project', 'workflow', 'description', 'status')
        }],)


admin.site.register(GlobalWorkflow, GlobalWorkflowForm)


class GlobalLabelForm(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'status')
    list_display_links = ('id', 'name')
    list_filter = ('status', )
    list_per_page = 20
    ordering = ('id',)
    fieldsets = ([
        '标签', {
            'fields': ('name', 'project', 'description', 'status')
        }],)


admin.site.register(GlobalLabel, GlobalLabelForm)


class TestTaskForm(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'status')
    list_display_links = ('id', 'name')
    list_filter = ('status', )
    list_per_page = 20
    ordering = ('id',)
    fieldsets = ([
        '任务', {
            'fields': ('name', 'project', 'description', 'status')
        }],)


admin.site.register(TestTask, TestTaskForm)
