from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Brand'


class Color(models.Model):
    color_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Color"

    def __str__(self):
        return self.color_name


class Store(models.Model):
    store_name = models.CharField(max_length=50)

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = "Store"


class ScreenSize(models.Model):
    screen_size = models.FloatField()

    def __str__(self):
        return self.screen_size

    class Meta:
        verbose_name = "ScreenSize"


class HardDiskSize(models.Model):
    hard_disk_size = models.IntegerField()

    def __str__(self):
        return str(self.hard_disk_size)

    class Meta:
        verbose_name = "HardDiskSize"


class HardDiskType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "HardDiskType"


class RamSize(models.Model):
    ram = models.IntegerField()

    def __str__(self):
        return str(self.ram)

    class Meta:
        verbose_name = "RamSize"


class RamType(models.Model):
    ram_type = models.CharField(max_length=50)

    def __str__(self):
        return self.ram_type

    class Meta:
        verbose_name = "RamType"


class CPUCo(models.Model):
    cpu_company = models.CharField(max_length=50)

    def __str__(self):
        return self.cpu_company

    class Meta:
        verbose_name = "CPUCo"


class CPUSeries(models.Model):
    cpu_series = models.CharField(max_length=50)

    def __str__(self):
        return self.cpu_series

    class Meta:
        verbose_name = "CPUSeries"


class CPUModel(models.Model):
    cpu_model = models.CharField(max_length=50)

    def __str__(self):
        return self.cpu_model

    class Meta:
        verbose_name = "CPUModel"


class CacheSize(models.Model):
    cache_size = models.IntegerField()

    def __str__(self):
        return str(self.cache_size)

    class Meta:
        verbose_name = "CacheSize"


class GPUCo(models.Model):
    gpu_company = models.CharField(max_length=50)

    def __str__(self):
        return self.gpu_company

    class Meta:
        verbose_name = "GPUCo"


class GPUModel(models.Model):
    gpu_model = models.CharField(max_length=50)

    def __str__(self):
        return self.gpu_model

    class Meta:
        verbose_name = "GPUModel"


class GPUSize(models.Model):
    gpu_size = models.IntegerField()

    def __str__(self):
        return str(self.gpu_size)

    class Meta:
        verbose_name = "GPUSize"


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Category"


class Laptop(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)

    hard_disk_size = models.ForeignKey(HardDiskSize, on_delete=models.CASCADE)
    hard_disk_type = models.ForeignKey(HardDiskType, on_delete=models.CASCADE)

    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    Weight = models.IntegerField()

    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    screen_size = models.ForeignKey(ScreenSize, on_delete=models.CASCADE)

    ram_size = models.ForeignKey(RamSize, on_delete=models.CASCADE)
    ram_type = models.ForeignKey(RamType, on_delete=models.CASCADE)

    cpu_Company = models.ForeignKey(CPUCo, on_delete=models.CASCADE)
    cpu_Model = models.ForeignKey(CPUModel, on_delete=models.CASCADE)
    cpu_series = models.ForeignKey(CPUSeries, on_delete=models.CASCADE)

    cache_size = models.ForeignKey(CacheSize, on_delete=models.CASCADE)

    gpu_Co = models.ForeignKey(GPUCo, on_delete=models.CASCADE)
    gpu_Model = models.ForeignKey(GPUModel, on_delete=models.CASCADE)
    gpu_size = models.ForeignKey(GPUSize, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    price = models.IntegerField()

    def __str__(self):
        return "لپ تاپ" + str(self.screen_size) + "اینچی" + str(self.brand) + "مدل" + str(self.model) + " " + str(
            self.gpu_Model) + " " + str(self.hard_disk_size) + str(self.hard_disk_type) + " " + str(
            self.ram_size) + "GB" + str(self.cpu_Model) + " "

    class Meta:
        verbose_name = "Laptop"
