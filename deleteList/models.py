from django.db import models

class DeleteTransaction(models.Model):

    def __str__(self):
        return str(self.id)

class DeleteArray(models.Model):
    transaction = models.ForeignKey(DeleteTransaction, on_delete=models.CASCADE, related_name='array')
    blog = models.ForeignKey('posts.Post', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.transaction_id) + ":" + str(self.blog_id)