from django.db import models


class MediaTypes(models.Model):
    name = models.CharField(max_length=120)


class Genres(models.Model):
    name = models.CharField(max_length=120)


class Artists(models.Model):
    name = models.CharField(max_length=120)


class Albums(models.Model):
    title = models.CharField(max_length=160)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name="albums")


class Tracks(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name="tracks")
    mediaType = models.ForeignKey(MediaTypes, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    composer = models.CharField(max_length=220, null=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)


class Playlists(models.Model):
    name = models.CharField(max_length=120)


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlists, on_delete=models.CASCADE)
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("playlist", "track"),)


class Employees(models.Model):
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    reportsTo = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True
    )
    birthDate = models.DateTimeField()
    hireDate = models.DateTimeField()
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    postalCode = models.CharField(max_length=10)
    phone = models.CharField(max_length=24)
    fax = models.CharField(max_length=24)
    email = models.CharField(max_length=60)


class Customers(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=20)
    company = models.CharField(max_length=80, null=True)
    address = models.CharField(max_length=70, null=True)
    city = models.CharField(max_length=40, null=True)
    state = models.CharField(max_length=40, null=True)
    country = models.CharField(max_length=40, null=True)
    postalCode = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=24, null=True)
    fax = models.CharField(max_length=24, null=True)
    email = models.CharField(max_length=60)
    supportRep = models.ForeignKey(
        Employees, on_delete=models.CASCADE, null=True, blank=True
    )


class Invoices(models.Model):
    billingAddress = models.CharField(max_length=70, null=True)
    billingCity = models.CharField(max_length=40, null=True)
    billingCountry = models.CharField(max_length=40, null=True)
    billingPostalCode = models.CharField(max_length=10, null=True)
    billingState = models.CharField(max_length=40, null=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    invoiceDate = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)


class InvoiceItems(models.Model):
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE)
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)
