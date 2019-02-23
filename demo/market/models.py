from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '%s %s' % (self.user_first_name, self.user_last_name)


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_name = models.CharField(max_length=100)
    order_user_id = models.ForeignKey(Users, related_name='orders', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.order_name