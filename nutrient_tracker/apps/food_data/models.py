from django.db import models


# Create your models here.
class Recipe(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    estimated_time = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"


class Ingredient(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)
    food_group = models.CharField(max_length=150)
    food_name = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    enercj = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    enercc = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    water = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    prot = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    protpl = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    protan = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    nt = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    trp = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fat = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    facid = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fasat = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    famscis = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fapu = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fapun3 = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fapun6 = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fatrs = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    cho = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    sugar = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    starch = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    polyl = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fibt = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    alc = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    oa = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    ash = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    chorl = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    na = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    k = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    ca = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    p = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    mg = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fe = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    haem = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    nhaem = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    cu = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    se = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    zn = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    id = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vita_rae = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vita_re = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    retol = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    cartbtot = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    carta = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    lutn = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    zea = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    crypxb = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    lycpn = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitd = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    chocaloh = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    chocal = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    ergcal = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vite = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    tocpha = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    tocphb = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    tocphd = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    tocphg = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitk = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitk1 = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitk2 = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    thia = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    ribf = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitb6 = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitb12 = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    niaeq = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    nia = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fol = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    folfd = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    folac = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitc = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fasatxr = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    famscxr = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fapuxr = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    famstxr = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    faun = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )

    def __str__(self):
        return self.food_name

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"
