#######################################################################
#  SingularMS version 1.0                                             #
#######################################################################
#  This file is a part of SingularMS.                                 #
#                                                                     #
#  SingularMs is free software; you can copy, modify, and distribute  #
#  it under the terms of the GNU Affero General Public License        #
#  Version 1.0, 21 May 2007.                                          #
#                                                                     #
#  SingularMS is distributed in the hope that it will be useful, but  #
#  WITHOUT ANY WARRANTY; without even the implied warranty of         #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.               #
#  See the GNU Affero General Public License for more details.        #
#                                                                     #
#  You should have received a copy of the GNU Affero General Public   #
#  License with this program; if not, contact Galotecnia              #
#  at contacto[AT]galotecnia[DOT]org. If you have questions about the #
#  GNU Affero General Public License see "Frequently Asked Questions" #
#  at http://www.gnu.org/licenses/gpl-faq.html                        #
#######################################################################

from django.contrib import admin
from models import Contacto, Direccion, DatoContacto

class DatoContactoInline(admin.options.TabularInline):
    model = DatoContacto
    extra = 1
    
class DireccionInline(admin.options.TabularInline):
    model = Direccion
    extra = 1

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos')
    search_fields = ['nombre', 'apellidos']
    inlines = [DatoContactoInline, DireccionInline]

admin.site.register(Contacto, ContactoAdmin)

class DatoContactoAdmin(admin.ModelAdmin):
    list_display = ('dato', 'clase', 'contacto')
    related_search_fields = {
        'contacto': ('nombre', 'apellidos',),
    }

admin.site.register(DatoContacto, DatoContactoAdmin)

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'tipo', 'contacto')
    related_search_fields = {
        'contacto': ('nombre', 'apellidos',),
    }

admin.site.register(Direccion, DireccionAdmin)
