from django.db import models

class Call_logs(models.Model):
    unique_id = models.CharField(max_length = 255,null=False)
    id = models.CharField(max_length = 255,primary_key=True, null=False)
    customer_name = models.CharField(max_length = 255,null=False)
    customer_number = models.CharField(max_length = 255,null=False)
    date = models.CharField(max_length = 255,null=False,)
    time = models.CharField(max_length = 255,null=False)
    call_type = models.CharField(max_length = 255,null=False)
    duration = models.CharField(max_length = 255,null=False)
    sales_agent_number = models.CharField(max_length = 255,null=False)
    sales_agent_email = models.CharField(max_length = 255,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.customer_name