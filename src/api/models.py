from django.db import models


""" PLANTS > DISEASES > CANOPIES """


class Predication(models.Model):
    STATUS_CHOICE = (
        0, 'Healthy',
        1, 'Parkinson',
    )

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True, blank=True)
    audio = models.FileField(
        upload_to='audios/', null=False, blank=False,
        help_text="Please record voice [15sec-45sec] voice must be .wmv format")
    mdvp_fo = models.IntegerField(default=0, help_text="Average Vocal Fundamental Frequency")
    mdvp_fhi = models.IntegerField(default=0, help_text="Minimum Vocal Fundamental Frequency")
    mdvp_flo = models.IntegerField(default=0, help_text="Maximum Vocal Fundamental Frequency")
    mdvp_shimmer = models.IntegerField(default=0)
    mdvp_jitter = models.IntegerField(default=0)
    rpde = models.IntegerField(default=0)
    d2 = models.IntegerField(default=0)
    nhr = models.IntegerField(default=0)
    hnr = models.IntegerField(default=0)
    dfa = models.IntegerField(default=0)
    ppe = models.IntegerField(default=0)
    spread1 = models.IntegerField(default=0)
    spread2 = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.user.username
