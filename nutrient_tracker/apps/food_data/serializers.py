from rest_framework import serializers
from ..food_data.models import Ingredient


class IngredientDataSerializer(serializers.Serializer):
    food_group = serializers.CharField(max_length=150)
    food_name = serializers.CharField(max_length=150)
    quantity = serializers.CharField(max_length=150)
    enercj = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    enercc = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    water = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    prot = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    protpl = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    protan = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    nt = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    trp = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fat = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    facid = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fasat = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    famscis = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fapu = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fapun3 = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fapun6 = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fatrs = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    cho = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    sugar = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    starch = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    polyl = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fibt = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    alc = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    oa = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    ash = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    chorl = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    na = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    k = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    ca = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    p = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    mg = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fe = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    haem = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    nhaem = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    cu = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    se = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    zn = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    id = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vita_rae = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vita_re = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    retol = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    cartbtot = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    carta = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    lutn = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    zea = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    crypxb = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    lycpn = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitd = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    chocaloh = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    chocal = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    ergcal = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vite = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    tocpha = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    tocphb = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    tocphd = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    tocphg = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitk = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitk1 = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitk2 = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    thia = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    ribf = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitb6 = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitb12 = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    niaeq = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    nia = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fol = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    folfd = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    folac = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    vitc = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fasatxr = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    famscxr = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    fapuxr = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    famstxr = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )
    faun = serializers.DecimalField(
        max_digits=10,
        decimal_places=5,
        default=0,
    )


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
