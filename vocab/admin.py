from django.contrib import admin


from models import Word_List , Word


class WordListAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Word_List , WordListAdmin)


class WordAdmin(admin.ModelAdmin):
    list_display = [ 'word' ,'example', 'meaning' , 'word_list']
    search_fields = ['word','meaning' ,]
    list_filter = ['word_list__name' ,]

admin.site.register(Word , WordAdmin)



