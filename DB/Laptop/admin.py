from django.contrib import admin
from .models import Brand, Color, Store, ScreenSize, HardDiskSize, HardDiskType, \
    RamSize, RamType, CPUCo, CPUSeries, CPUModel, CacheSize, GPUCo, GPUModel, \
    GPUSize, Category, Laptop

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['color_name']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_name']

@admin.register(ScreenSize)
class ScreenSizeAdmin(admin.ModelAdmin):
    list_display = ['screen_size']

@admin.register(HardDiskSize)
class HardDiskSizeAdmin(admin.ModelAdmin):
    list_display = ['hard_disk_size']

@admin.register(HardDiskType)
class HardDiskTypeAdmin(admin.ModelAdmin):
    list_display = ['type']

@admin.register(RamSize)
class RamSizeAdmin(admin.ModelAdmin):
    list_display = ['ram']

@admin.register(RamType)
class RamTypeAdmin(admin.ModelAdmin):
    list_display = ['ram_type']

@admin.register(CPUCo)
class CPUCoAdmin(admin.ModelAdmin):
    list_display = ['cpu_company']

@admin.register(CPUSeries)
class CPUSeriesAdmin(admin.ModelAdmin):
    list_display = ['cpu_series']

@admin.register(CPUModel)
class CPUModelAdmin(admin.ModelAdmin):
    list_display = ['cpu_model']

@admin.register(CacheSize)
class CacheSizeAdmin(admin.ModelAdmin):
    list_display = ['cache_size']

@admin.register(GPUCo)
class GPUCoAdmin(admin.ModelAdmin):
    list_display = ['gpu_company']

@admin.register(GPUModel)
class GPUModelAdmin(admin.ModelAdmin):
    list_display = ['gpu_model']

@admin.register(GPUSize)
class GPUSizeAdmin(admin.ModelAdmin):
    list_display = ['gpu_size']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['model', 'price', 'brand', 'color', 'store']
