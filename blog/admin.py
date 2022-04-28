from statistics import mode
from django.contrib import admin
from .models import Post, Figure


admin.site.register(Figure)

class FigureIline(admin.TabularInline):
    model = Figure
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [FigureIline]