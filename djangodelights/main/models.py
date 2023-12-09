from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, blank=False)


    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeRequirement')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True)

    def __str__(self):
        return self.title

#The amount of each ingredient required for the recipe
class RecipeRequirement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.menu_item.title} - {self.ingredent.name} - {self.ingredent_quantity}"


    def __str__(self):
        return f"{self.menu_item} - {self.quantity}"
    
 


class Purchase(models.Model):
    created_at = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_items = models.ManyToManyField(MenuItem, through='PurchaseItem')

    def calculate_total_price(self):
        total = 0
        for purchase_item in self.purchase_item_set.all():
            total += purchase_item.menu_item.price * purchase_item.quantity
        self.total_price = total
        self.save()

    def save(self, *args, **kwargs):
        self.calculate_total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.created_at}"
    

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()




