from django.db import models
from sqlalchemy import null


# class Call_logs(models.Model):
#     unique_id = models.CharField(max_length = 255,null=False)
#     id = models.CharField(max_length = 255,primary_key=True, null=False)
#     customer_name = models.CharField(max_length = 255,null=False)
#     customer_number = models.CharField(max_length = 255,null=False)
#     date = models.CharField(max_length = 255,null=False,)
#     time = models.CharField(max_length = 255,null=False)
#     call_type = models.CharField(max_length = 255,null=False)
#     duration = models.CharField(max_length = 255,null=False)
#     sales_agent_number = models.CharField(max_length = 255,null=False)
#     sales_agent_email = models.CharField(max_length = 255,null=False)
#     created_at = models.DateTimeField(auto_now_add=True)



class AccountAccount(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    deprecated = models.BooleanField(blank=True, null=True)
    user_type = models.ForeignKey(related_name='+',to = 'AccountAccountType', on_delete = models.DO_NOTHING)
    internal_type = models.CharField(max_length=255, blank=True, null=True)
    internal_group = models.CharField(max_length=255, blank=True, null=True)
    reconcile = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    group = models.ForeignKey(related_name='+',to = 'AccountGroup', on_delete = models.DO_NOTHING, blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    is_off_balance = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account'
        unique_together = (('code', 'company'),)


class AccountAccountAccountJournalRel(models.Model):
    account_account = models.OneToOneField(AccountAccount, on_delete = models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(related_name='+',to = 'AccountJournal', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_account_journal_rel'
        unique_together = (('account_account', 'account_journal'),)


class AccountAccountAccountTag(models.Model):
    account_account = models.OneToOneField(AccountAccount, on_delete = models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(related_name='+',to = 'AccountAccountTag', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_account_tag'
        unique_together = (('account_account', 'account_account_tag'),)


class AccountAccountTag(models.Model):
    name = models.CharField(max_length=255)
    applicability = models.CharField(max_length=255)
    color = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    tax_negate = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_tag'


class AccountAccountTagAccountMoveLineRel(models.Model):
    account_move_line = models.OneToOneField('AccountMoveLine', on_delete = models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(related_name='+',to = AccountAccountTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_move_line_rel'
        unique_together = (('account_move_line', 'account_account_tag'),)


class AccountAccountTagAccountTaxRepartitionLineRel(models.Model):
    account_tax_repartition_line = models.OneToOneField('AccountTaxRepartitionLine', on_delete = models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(related_name='+',to = AccountAccountTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_tax_repartition_line_rel'
        unique_together = (('account_tax_repartition_line', 'account_account_tag'),)


class AccountAccountTagProductTemplateRel(models.Model):
    product_template = models.OneToOneField('ProductTemplate', on_delete = models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(related_name='+',to = AccountAccountTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_product_template_rel'
        unique_together = (('product_template', 'account_account_tag'),)


class AccountAccountTaxDefaultRel(models.Model):
    account = models.OneToOneField(AccountAccount, on_delete = models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(related_name='+',to = 'AccountTax', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tax_default_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountTemplate(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    user_type = models.ForeignKey(related_name='+',to = 'AccountAccountType', on_delete = models.DO_NOTHING)
    reconcile = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    nocreate = models.BooleanField(blank=True, null=True)
    chart_template = models.ForeignKey(related_name='+',to = 'AccountChartTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_template'


class AccountAccountTemplateAccountTag(models.Model):
    account_account_template = models.OneToOneField(AccountAccountTemplate, on_delete = models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(related_name='+',to = AccountAccountTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_account_tag'
        unique_together = (('account_account_template', 'account_account_tag'),)


class AccountAccountTemplateTaxRel(models.Model):
    account = models.OneToOneField(AccountAccountTemplate, on_delete = models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(related_name='+',to = 'AccountTaxTemplate', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_tax_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountType(models.Model):
    name = models.CharField(max_length=255)
    include_initial_balance = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=255)
    internal_group = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_type'


class AccountAccruedOrdersWizard(models.Model):
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_accrued_orders_wizard'


class AccountAnalyticAccount(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    group = models.ForeignKey(related_name='+',to = 'AccountAnalyticGroup', on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_account'


class AccountAnalyticDefault(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    analytic = models.ForeignKey(related_name='+',to = AccountAnalyticAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = 'ProductProduct', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_stop = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_default'


class AccountAnalyticDefaultAccountAnalyticTagRel(models.Model):
    account_analytic_default = models.OneToOneField(AccountAnalyticDefault, on_delete = models.DO_NOTHING, primary_key=True)
    account_analytic_tag = models.ForeignKey(related_name='+',to = 'AccountAnalyticTag', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_default_account_analytic_tag_rel'
        unique_together = (('account_analytic_default', 'account_analytic_tag'),)


class AccountAnalyticDistribution(models.Model):
    account = models.ForeignKey(related_name='+',to = AccountAnalyticAccount, on_delete = models.DO_NOTHING)
    percentage = models.FloatField()
    tag = models.ForeignKey(related_name='+',to = 'AccountAnalyticTag', on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_distribution'


class AccountAnalyticGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    parent_path = models.CharField(max_length=255, blank=True, null=True)
    complete_name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_group'


class AccountAnalyticLine(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    unit_amount = models.FloatField(blank=True, null=True)
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(related_name='+',to = AccountAnalyticAccount, on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(related_name='+',to = AccountAnalyticGroup, on_delete = models.DO_NOTHING, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = 'ProductProduct', on_delete = models.DO_NOTHING, blank=True, null=True)
    general_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(related_name='+',to = 'AccountMoveLine', on_delete = models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    so_line = models.ForeignKey(related_name='+',to = 'SaleOrderLine', on_delete = models.DO_NOTHING, db_column='so_line', blank=True, null=True)
    task = models.ForeignKey(related_name='+',to = 'ProjectTask', on_delete = models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(related_name='+',to = 'ProjectProject', on_delete = models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(related_name='+',to = 'HrEmployee', on_delete = models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(related_name='+',to = 'HrDepartment', on_delete = models.DO_NOTHING, blank=True, null=True)
    holiday = models.ForeignKey(related_name='+',to = 'HrLeave', on_delete = models.DO_NOTHING, blank=True, null=True)
    global_leave = models.ForeignKey(related_name='+',to = 'ResourceCalendarLeaves', on_delete = models.DO_NOTHING, blank=True, null=True)
    timesheet_invoice_type = models.CharField(max_length=255, blank=True, null=True)
    timesheet_invoice = models.ForeignKey(related_name='+',to = 'AccountMove', on_delete = models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(related_name='+',to = 'SaleOrder', on_delete = models.DO_NOTHING, blank=True, null=True)
    is_so_line_edited = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_line'


class AccountAnalyticLineTagRel(models.Model):
    line = models.OneToOneField(AccountAnalyticLine, on_delete = models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(related_name='+',to = 'AccountAnalyticTag', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_line_tag_rel'
        unique_together = (('line', 'tag'),)


class AccountAnalyticTag(models.Model):
    name = models.CharField(max_length=255)
    color = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    active_analytic_distribution = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag'


class AccountAnalyticTagAccountMoveLineRel(models.Model):
    account_move_line = models.OneToOneField('AccountMoveLine', on_delete = models.DO_NOTHING, primary_key=True)
    account_analytic_tag = models.ForeignKey(related_name='+',to = AccountAnalyticTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag_account_move_line_rel'
        unique_together = (('account_move_line', 'account_analytic_tag'),)


class AccountAnalyticTagHrExpenseRel(models.Model):
    hr_expense = models.OneToOneField('HrExpense', on_delete = models.DO_NOTHING, primary_key=True)
    account_analytic_tag = models.ForeignKey(related_name='+',to = AccountAnalyticTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag_hr_expense_rel'
        unique_together = (('hr_expense', 'account_analytic_tag'),)


class AccountAnalyticTagProjectTaskRel(models.Model):
    account_analytic_tag = models.OneToOneField(AccountAnalyticTag, on_delete = models.DO_NOTHING, primary_key=True)
    project_task = models.ForeignKey(related_name='+',to = 'ProjectTask', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag_project_task_rel'
        unique_together = (('account_analytic_tag', 'project_task'),)


class AccountAnalyticTagPurchaseOrderLineRel(models.Model):
    purchase_order_line = models.OneToOneField('PurchaseOrderLine', on_delete = models.DO_NOTHING, primary_key=True)
    account_analytic_tag = models.ForeignKey(related_name='+',to = AccountAnalyticTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag_purchase_order_line_rel'
        unique_together = (('purchase_order_line', 'account_analytic_tag'),)


class AccountAnalyticTagSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine', on_delete = models.DO_NOTHING, primary_key=True)
    account_analytic_tag = models.ForeignKey(related_name='+',to = AccountAnalyticTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag_sale_order_line_rel'
        unique_together = (('sale_order_line', 'account_analytic_tag'),)


class AccountAutomaticEntryWizard(models.Model):
    action = models.CharField(max_length=255)
    date = models.DateField()
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    percentage = models.FloatField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    account_type = models.CharField(max_length=255, blank=True, null=True)
    destination_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_automatic_entry_wizard'


class AccountAutomaticEntryWizardAccountMoveLineRel(models.Model):
    account_automatic_entry_wizard = models.OneToOneField(AccountAutomaticEntryWizard, on_delete = models.DO_NOTHING, primary_key=True)
    account_move_line = models.ForeignKey(related_name='+',to = 'AccountMoveLine', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_automatic_entry_wizard_account_move_line_rel'
        unique_together = (('account_automatic_entry_wizard', 'account_move_line'),)


class AccountBankStatement(models.Model):
    sequence_prefix = models.CharField(max_length=255, blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    date_done = models.DateTimeField(blank=True, null=True)
    balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=255)
    journal = models.ForeignKey(related_name='+',to = 'AccountJournal', on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    total_entry_encoding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    difference = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    cashbox_start = models.ForeignKey(related_name='+',to = 'AccountBankStatementCashbox', on_delete = models.DO_NOTHING, blank=True, null=True)
    cashbox_end = models.ForeignKey(related_name='+',to = 'AccountBankStatementCashbox', on_delete = models.DO_NOTHING, blank=True, null=True)
    previous_statement = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    is_valid_balance_start = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement'


class AccountBankStatementCashbox(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_cashbox'


class AccountBankStatementClosebalance(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_closebalance'


class AccountBankStatementLine(models.Model):
    move = models.ForeignKey(related_name='+',to = 'AccountMove', on_delete = models.DO_NOTHING)
    statement = models.ForeignKey(related_name='+',to = AccountBankStatement, on_delete = models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=255, blank=True, null=True)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    transaction_type = models.CharField(max_length=255, blank=True, null=True)
    payment_ref = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    foreign_currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    amount_residual = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    is_reconciled = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_line'


class AccountCashRounding(models.Model):
    name = models.CharField(max_length=255)
    rounding = models.FloatField()
    strategy = models.CharField(max_length=255)
    rounding_method = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_cash_rounding'


class AccountCashboxLine(models.Model):
    coin_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    number = models.IntegerField(blank=True, null=True)
    cashbox = models.ForeignKey(related_name='+',to = AccountBankStatementCashbox, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_cashbox_line'


class AccountChartTemplate(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    code_digits = models.IntegerField()
    visible = models.BooleanField(blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING)
    use_anglo_saxon = models.BooleanField(blank=True, null=True)
    complete_tax_set = models.BooleanField(blank=True, null=True)
    bank_account_code_prefix = models.CharField(max_length=255)
    cash_account_code_prefix = models.CharField(max_length=255)
    transfer_account_code_prefix = models.CharField(max_length=255)
    income_currency_exchange_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    account_journal_suspense_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_journal_payment_debit_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_journal_payment_credit_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    default_cash_difference_income_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    default_cash_difference_expense_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    default_pos_receivable_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_account_receivable = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_account_payable = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_account_expense_categ = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_account_income_categ = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_account_expense = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_account_income = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_stock_account_input_categ = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_tax_payable_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_tax_receivable_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_advance_tax_payment_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_cash_basis_base_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_chart_template'


class AccountCommonJournalReport(models.Model):
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    amount_currency = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report'


class AccountCommonJournalReportAccountJournalRel(models.Model):
    account_common_journal_report = models.OneToOneField(AccountCommonJournalReport, on_delete = models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(related_name='+',to = 'AccountJournal', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report_account_journal_rel'
        unique_together = (('account_common_journal_report', 'account_journal'),)


class AccountCommonReport(models.Model):
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_common_report'


class AccountCommonReportAccountJournalRel(models.Model):
    account_common_report = models.OneToOneField(AccountCommonReport, on_delete = models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(related_name='+',to = 'AccountJournal', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_report_account_journal_rel'
        unique_together = (('account_common_report', 'account_journal'),)


class AccountEdiDocument(models.Model):
    move = models.ForeignKey(related_name='+',to = 'AccountMove', on_delete = models.DO_NOTHING)
    edi_format = models.ForeignKey(related_name='+',to = 'AccountEdiFormat', on_delete = models.DO_NOTHING)
    attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    blocking_level = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_edi_document'
        unique_together = (('edi_format', 'move'),)


class AccountEdiFormat(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(unique=True, max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_edi_format'


class AccountEdiFormatAccountJournalRel(models.Model):
    account_journal = models.OneToOneField('AccountJournal', on_delete = models.DO_NOTHING, primary_key=True)
    account_edi_format = models.ForeignKey(related_name='+',to = AccountEdiFormat, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_edi_format_account_journal_rel'
        unique_together = (('account_journal', 'account_edi_format'),)


class AccountFinancialYearOp(models.Model):
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_financial_year_op'


class AccountFiscalPosition(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    note = models.TextField(blank=True, null=True)
    auto_apply = models.BooleanField(blank=True, null=True)
    vat_required = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    country_group = models.ForeignKey(related_name='+',to = 'ResCountryGroup', on_delete = models.DO_NOTHING, blank=True, null=True)
    zip_from = models.CharField(max_length=255, blank=True, null=True)
    zip_to = models.CharField(max_length=255, blank=True, null=True)
    foreign_vat = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position'


class AccountFiscalPositionAccount(models.Model):
    position = models.ForeignKey(related_name='+',to = AccountFiscalPosition, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    account_src = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING)
    account_dest = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account'
        unique_together = (('position', 'account_src', 'account_dest'),)


class AccountFiscalPositionAccountTemplate(models.Model):
    position = models.ForeignKey(related_name='+',to = 'AccountFiscalPositionTemplate', on_delete = models.DO_NOTHING)
    account_src = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING)
    account_dest = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account_template'


class AccountFiscalPositionResCountryStateRel(models.Model):
    account_fiscal_position = models.OneToOneField(AccountFiscalPosition, on_delete = models.DO_NOTHING, primary_key=True)
    res_country_state = models.ForeignKey(related_name='+',to = 'ResCountryState', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_res_country_state_rel'
        unique_together = (('account_fiscal_position', 'res_country_state'),)


class AccountFiscalPositionTax(models.Model):
    position = models.ForeignKey(related_name='+',to = AccountFiscalPosition, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    tax_src = models.ForeignKey(related_name='+',to = 'AccountTax', on_delete = models.DO_NOTHING)
    tax_dest = models.ForeignKey(related_name='+',to = 'AccountTax', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax'
        unique_together = (('position', 'tax_src', 'tax_dest'),)


class AccountFiscalPositionTaxTemplate(models.Model):
    position = models.ForeignKey(related_name='+',to = 'AccountFiscalPositionTemplate', on_delete = models.DO_NOTHING)
    tax_src = models.ForeignKey(related_name='+',to = 'AccountTaxTemplate', on_delete = models.DO_NOTHING)
    tax_dest = models.ForeignKey(related_name='+',to = 'AccountTaxTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax_template'


class AccountFiscalPositionTemplate(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    chart_template = models.ForeignKey(related_name='+',to = AccountChartTemplate, on_delete = models.DO_NOTHING)
    note = models.TextField(blank=True, null=True)
    auto_apply = models.BooleanField(blank=True, null=True)
    vat_required = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    country_group = models.ForeignKey(related_name='+',to = 'ResCountryGroup', on_delete = models.DO_NOTHING, blank=True, null=True)
    zip_from = models.CharField(max_length=255, blank=True, null=True)
    zip_to = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template'


class AccountFiscalPositionTemplateResCountryStateRel(models.Model):
    account_fiscal_position_template = models.OneToOneField(AccountFiscalPositionTemplate, on_delete = models.DO_NOTHING, primary_key=True)
    res_country_state = models.ForeignKey(related_name='+',to = 'ResCountryState', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template_res_country_state_rel'
        unique_together = (('account_fiscal_position_template', 'res_country_state'),)


class AccountFullReconcile(models.Model):
    name = models.CharField(max_length=255)
    exchange_move = models.ForeignKey(related_name='+',to = 'AccountMove', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_full_reconcile'


class AccountGroup(models.Model):
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    parent_path = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    code_prefix_start = models.CharField(max_length=255, blank=True, null=True)
    code_prefix_end = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_group'


class AccountGroupTemplate(models.Model):
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    code_prefix_start = models.CharField(max_length=255, blank=True, null=True)
    code_prefix_end = models.CharField(max_length=255, blank=True, null=True)
    chart_template = models.ForeignKey(related_name='+',to = AccountChartTemplate, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_group_template'


class AccountIncoterms(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_incoterms'


class AccountInvoiceSend(models.Model):
    is_email = models.BooleanField(blank=True, null=True)
    is_print = models.BooleanField(blank=True, null=True)
    printed = models.BooleanField(blank=True, null=True)
    composer = models.ForeignKey(related_name='+',to = 'MailComposeMessage', on_delete = models.DO_NOTHING)
    template = models.ForeignKey(related_name='+',to = 'MailTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    snailmail_is_letter = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_send'


class AccountInvoiceTransactionRel(models.Model):
    invoice = models.OneToOneField('AccountMove', on_delete = models.DO_NOTHING, primary_key=True)
    transaction = models.ForeignKey(related_name='+',to = 'PaymentTransaction', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_transaction_rel'
        unique_together = (('invoice', 'transaction'),)


class AccountJournal(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5)
    active = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=255)
    default_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    suspense_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    restrict_mode_hash_table = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    invoice_reference_type = models.CharField(max_length=255)
    invoice_reference_model = models.CharField(max_length=255)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    refund_sequence = models.BooleanField(blank=True, null=True)
    sequence_override_regex = models.TextField(blank=True, null=True)
    profit_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    loss_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    bank_account = models.ForeignKey(related_name='+',to = 'ResPartnerBank', on_delete = models.DO_NOTHING, blank=True, null=True)
    bank_statements_source = models.CharField(max_length=255, blank=True, null=True)
    sale_activity_type = models.ForeignKey(related_name='+',to = 'MailActivityType', on_delete = models.DO_NOTHING, blank=True, null=True)
    sale_activity_user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    sale_activity_note = models.TextField(blank=True, null=True)
    alias = models.ForeignKey(related_name='+',to = 'MailAlias', on_delete = models.DO_NOTHING, blank=True, null=True)
    secure_sequence = models.ForeignKey(related_name='+',to = 'IrSequence', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    show_on_dashboard = models.BooleanField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal'
        unique_together = (('code', 'company'),)


class AccountJournalAccountJournalGroupRel(models.Model):
    account_journal_group = models.OneToOneField('AccountJournalGroup', on_delete = models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_journal_group_rel'
        unique_together = (('account_journal_group', 'account_journal'),)


class AccountJournalAccountPrintJournalRel(models.Model):
    account_print_journal = models.OneToOneField('AccountPrintJournal', on_delete = models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_print_journal_rel'
        unique_together = (('account_print_journal', 'account_journal'),)


class AccountJournalAccountReconcileModelRel(models.Model):
    account_reconcile_model = models.OneToOneField('AccountReconcileModel', on_delete = models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_reconcile_model_rel'
        unique_together = (('account_reconcile_model', 'account_journal'),)


class AccountJournalAccountReconcileModelTemplateRel(models.Model):
    account_reconcile_model_template = models.OneToOneField('AccountReconcileModelTemplate', on_delete = models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_reconcile_model_template_rel'
        unique_together = (('account_reconcile_model_template', 'account_journal'),)


class AccountJournalGroup(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_group'


class AccountMove(models.Model):
    sequence_prefix = models.CharField(max_length=255, blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    ref = models.CharField(max_length=255, blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255)
    posted_before = models.BooleanField(blank=True, null=True)
    move_type = models.CharField(max_length=255)
    to_check = models.BooleanField(blank=True, null=True)
    journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    commercial_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    is_move_sent = models.BooleanField(blank=True, null=True)
    partner_bank = models.ForeignKey(related_name='+',to = 'ResPartnerBank', on_delete = models.DO_NOTHING, blank=True, null=True)
    payment_reference = models.CharField(max_length=255, blank=True, null=True)
    payment = models.ForeignKey(related_name='+',to = 'AccountPayment', on_delete = models.DO_NOTHING, blank=True, null=True)
    statement_line = models.ForeignKey(related_name='+',to = AccountBankStatementLine, on_delete = models.DO_NOTHING, blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_untaxed_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total_in_currency_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_state = models.CharField(max_length=255, blank=True, null=True)
    tax_cash_basis_rec = models.ForeignKey(related_name='+',to = 'AccountPartialReconcile', on_delete = models.DO_NOTHING, blank=True, null=True)
    tax_cash_basis_origin_move = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    always_tax_exigible = models.BooleanField(blank=True, null=True)
    auto_post = models.BooleanField(blank=True, null=True)
    reversed_entry = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    fiscal_position = models.ForeignKey(related_name='+',to = AccountFiscalPosition, on_delete = models.DO_NOTHING, blank=True, null=True)
    invoice_user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    invoice_date_due = models.DateField(blank=True, null=True)
    invoice_origin = models.CharField(max_length=255, blank=True, null=True)
    invoice_payment_term = models.ForeignKey(related_name='+',to = 'AccountPaymentTerm', on_delete = models.DO_NOTHING, blank=True, null=True)
    invoice_incoterm = models.ForeignKey(related_name='+',to = AccountIncoterms, on_delete = models.DO_NOTHING, blank=True, null=True)
    qr_code_method = models.CharField(max_length=255, blank=True, null=True)
    invoice_source_email = models.CharField(max_length=255, blank=True, null=True)
    invoice_partner_display_name = models.CharField(max_length=255, blank=True, null=True)
    invoice_cash_rounding = models.ForeignKey(related_name='+',to = AccountCashRounding, on_delete = models.DO_NOTHING, blank=True, null=True)
    secure_sequence_number = models.IntegerField(blank=True, null=True)
    inalterable_hash = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    edi_state = models.CharField(max_length=255, blank=True, null=True)
    campaign = models.ForeignKey(related_name='+',to = 'UtmCampaign', on_delete = models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey(related_name='+',to = 'UtmSource', on_delete = models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey(related_name='+',to = 'UtmMedium', on_delete = models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey(related_name='+',to = 'CrmTeam', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner_shipping = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    stock_move = models.ForeignKey(related_name='+',to = 'StockMove', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move'


class AccountMoveAccountInvoiceSendRel(models.Model):
    account_invoice_send = models.OneToOneField(AccountInvoiceSend, on_delete = models.DO_NOTHING, primary_key=True)
    account_move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_account_invoice_send_rel'
        unique_together = (('account_invoice_send', 'account_move'),)


class AccountMoveAccountResequenceWizardRel(models.Model):
    account_resequence_wizard = models.OneToOneField('AccountResequenceWizard', on_delete = models.DO_NOTHING, primary_key=True)
    account_move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_account_resequence_wizard_rel'
        unique_together = (('account_resequence_wizard', 'account_move'),)


class AccountMoveLine(models.Model):
    move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING)
    move_name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    parent_state = models.CharField(max_length=255, blank=True, null=True)
    journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    company_currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_root_id = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reconciled = models.BooleanField(blank=True, null=True)
    blocked = models.BooleanField(blank=True, null=True)
    date_maturity = models.DateField(blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = 'ProductProduct', on_delete = models.DO_NOTHING, blank=True, null=True)
    reconcile_model = models.ForeignKey(related_name='+',to = 'AccountReconcileModel', on_delete = models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey(related_name='+',to = 'AccountPayment', on_delete = models.DO_NOTHING, blank=True, null=True)
    statement_line = models.ForeignKey(related_name='+',to = AccountBankStatementLine, on_delete = models.DO_NOTHING, blank=True, null=True)
    statement = models.ForeignKey(related_name='+',to = AccountBankStatement, on_delete = models.DO_NOTHING, blank=True, null=True)
    group_tax = models.ForeignKey(related_name='+',to = 'AccountTax', on_delete = models.DO_NOTHING, blank=True, null=True)
    tax_line = models.ForeignKey(related_name='+',to = 'AccountTax', on_delete = models.DO_NOTHING, blank=True, null=True)
    tax_group = models.ForeignKey(related_name='+',to = 'AccountTaxGroup', on_delete = models.DO_NOTHING, blank=True, null=True)
    tax_base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tax_repartition_line = models.ForeignKey(related_name='+',to = 'AccountTaxRepartitionLine', on_delete = models.DO_NOTHING, blank=True, null=True)
    tax_audit = models.CharField(max_length=255, blank=True, null=True)
    tax_tag_invert = models.BooleanField(blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    full_reconcile = models.ForeignKey(related_name='+',to = AccountFullReconcile, on_delete = models.DO_NOTHING, blank=True, null=True)
    matching_number = models.CharField(max_length=255, blank=True, null=True)
    analytic_account = models.ForeignKey(related_name='+',to = AccountAnalyticAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    display_type = models.CharField(max_length=255, blank=True, null=True)
    is_rounding_line = models.BooleanField(blank=True, null=True)
    exclude_from_invoice_tab = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_anglo_saxon_line = models.BooleanField(blank=True, null=True)
    expense = models.ForeignKey(related_name='+',to = 'HrExpense', on_delete = models.DO_NOTHING, blank=True, null=True)
    purchase_line = models.ForeignKey(related_name='+',to = 'PurchaseOrderLine', on_delete = models.DO_NOTHING, blank=True, null=True)
    is_landed_costs_line = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line'


class AccountMoveLineAccountTaxRel(models.Model):
    account_move_line = models.OneToOneField(AccountMoveLine, on_delete = models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey(related_name='+',to = 'AccountTax', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_line_account_tax_rel'
        unique_together = (('account_move_line', 'account_tax'),)


class AccountMovePurchaseOrderRel(models.Model):
    purchase_order = models.OneToOneField('PurchaseOrder', on_delete = models.DO_NOTHING, primary_key=True)
    account_move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_purchase_order_rel'
        unique_together = (('purchase_order', 'account_move'),)


class AccountMoveReversal(models.Model):
    date_mode = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    refund_method = models.CharField(max_length=255)
    journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_reversal'


class AccountMoveReversalMove(models.Model):
    reversal = models.OneToOneField(AccountMoveReversal, on_delete = models.DO_NOTHING, primary_key=True)
    move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_reversal_move'
        unique_together = (('reversal', 'move'),)


class AccountMoveReversalNewMove(models.Model):
    reversal = models.OneToOneField(AccountMoveReversal, on_delete = models.DO_NOTHING, primary_key=True)
    new_move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_reversal_new_move'
        unique_together = (('reversal', 'new_move'),)


class AccountPartialReconcile(models.Model):
    debit_move = models.ForeignKey(related_name='+',to = AccountMoveLine, on_delete = models.DO_NOTHING)
    credit_move = models.ForeignKey(related_name='+',to = AccountMoveLine, on_delete = models.DO_NOTHING)
    full_reconcile = models.ForeignKey(related_name='+',to = AccountFullReconcile, on_delete = models.DO_NOTHING, blank=True, null=True)
    debit_currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    credit_currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    max_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_partial_reconcile'


class AccountPayment(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING)
    is_reconciled = models.BooleanField(blank=True, null=True)
    is_matched = models.BooleanField(blank=True, null=True)
    partner_bank = models.ForeignKey(related_name='+',to = 'ResPartnerBank', on_delete = models.DO_NOTHING, blank=True, null=True)
    is_internal_transfer = models.BooleanField(blank=True, null=True)
    paired_internal_transfer_payment = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    payment_method_line = models.ForeignKey(related_name='+',to = 'AccountPaymentMethodLine', on_delete = models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey(related_name='+',to = 'AccountPaymentMethod', on_delete = models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_type = models.CharField(max_length=255)
    partner_type = models.CharField(max_length=255)
    payment_reference = models.CharField(max_length=255, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    outstanding_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    destination_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    destination_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_transaction = models.ForeignKey(related_name='+',to = 'PaymentTransaction', on_delete = models.DO_NOTHING, blank=True, null=True)
    payment_token = models.ForeignKey(related_name='+',to = 'PaymentToken', on_delete = models.DO_NOTHING, blank=True, null=True)
    source_payment = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment'


class AccountPaymentAccountBankStatementLineRel(models.Model):
    account_bank_statement_line = models.OneToOneField(AccountBankStatementLine, on_delete = models.DO_NOTHING, primary_key=True)
    account_payment = models.ForeignKey(related_name='+',to = AccountPayment, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_payment_account_bank_statement_line_rel'
        unique_together = (('account_bank_statement_line', 'account_payment'),)


class AccountPaymentMethod(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_method'
        unique_together = (('code', 'payment_type'),)


class AccountPaymentMethodLine(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    payment_method = models.ForeignKey(related_name='+',to = AccountPaymentMethod, on_delete = models.DO_NOTHING)
    payment_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_acquirer = models.ForeignKey(related_name='+',to = 'PaymentAcquirer', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_method_line'


class AccountPaymentRegister(models.Model):
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    communication = models.CharField(max_length=255, blank=True, null=True)
    group_payment = models.BooleanField(blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    partner_bank = models.ForeignKey(related_name='+',to = 'ResPartnerBank', on_delete = models.DO_NOTHING, blank=True, null=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)
    partner_type = models.CharField(max_length=255, blank=True, null=True)
    source_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    source_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    source_currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    can_edit_wizard = models.BooleanField(blank=True, null=True)
    can_group_payments = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    payment_method_line = models.ForeignKey(related_name='+',to = AccountPaymentMethodLine, on_delete = models.DO_NOTHING, blank=True, null=True)
    payment_difference_handling = models.CharField(max_length=255, blank=True, null=True)
    writeoff_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    writeoff_label = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_token = models.ForeignKey(related_name='+',to = 'PaymentToken', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_register'


class AccountPaymentRegisterMoveLineRel(models.Model):
    wizard = models.OneToOneField(AccountPaymentRegister, on_delete = models.DO_NOTHING, primary_key=True)
    line = models.ForeignKey(related_name='+',to = AccountMoveLine, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_payment_register_move_line_rel'
        unique_together = (('wizard', 'line'),)


class AccountPaymentTerm(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term'


class AccountPaymentTermLine(models.Model):
    value = models.CharField(max_length=255)
    value_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days = models.IntegerField()
    day_of_the_month = models.IntegerField(blank=True, null=True)
    option = models.CharField(max_length=255)
    payment = models.ForeignKey(related_name='+',to = AccountPaymentTerm, on_delete = models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term_line'


class AccountPrintJournal(models.Model):
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    amount_currency = models.BooleanField(blank=True, null=True)
    sort_selection = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account_print_journal'


class AccountReconcileModel(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField()
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    rule_type = models.CharField(max_length=255)
    auto_reconcile = models.BooleanField(blank=True, null=True)
    to_check = models.BooleanField(blank=True, null=True)
    matching_order = models.CharField(max_length=255)
    match_text_location_label = models.BooleanField(blank=True, null=True)
    match_text_location_note = models.BooleanField(blank=True, null=True)
    match_text_location_reference = models.BooleanField(blank=True, null=True)
    match_nature = models.CharField(max_length=255)
    match_amount = models.CharField(max_length=255, blank=True, null=True)
    match_amount_min = models.FloatField(blank=True, null=True)
    match_amount_max = models.FloatField(blank=True, null=True)
    match_label = models.CharField(max_length=255, blank=True, null=True)
    match_label_param = models.CharField(max_length=255, blank=True, null=True)
    match_note = models.CharField(max_length=255, blank=True, null=True)
    match_note_param = models.CharField(max_length=255, blank=True, null=True)
    match_transaction_type = models.CharField(max_length=255, blank=True, null=True)
    match_transaction_type_param = models.CharField(max_length=255, blank=True, null=True)
    match_same_currency = models.BooleanField(blank=True, null=True)
    allow_payment_tolerance = models.BooleanField(blank=True, null=True)
    payment_tolerance_param = models.FloatField(blank=True, null=True)
    payment_tolerance_type = models.CharField(max_length=255)
    match_partner = models.BooleanField(blank=True, null=True)
    past_months_limit = models.IntegerField(blank=True, null=True)
    decimal_separator = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model'


class AccountReconcileModelAnalyticTagRel(models.Model):
    account_reconcile_model_line = models.OneToOneField('AccountReconcileModelLine', on_delete = models.DO_NOTHING, primary_key=True)
    account_analytic_tag = models.ForeignKey(related_name='+',to = AccountAnalyticTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_analytic_tag_rel'
        unique_together = (('account_reconcile_model_line', 'account_analytic_tag'),)


class AccountReconcileModelLine(models.Model):
    model = models.ForeignKey(related_name='+',to = AccountReconcileModel, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING)
    journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    amount_type = models.CharField(max_length=255)
    force_tax_included = models.BooleanField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amount_string = models.CharField(max_length=255)
    analytic_account = models.ForeignKey(related_name='+',to = AccountAnalyticAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line'


class AccountReconcileModelLineAccountTaxRel(models.Model):
    account_reconcile_model_line = models.OneToOneField(AccountReconcileModelLine, on_delete = models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey(related_name='+',to = 'AccountTax', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line_account_tax_rel'
        unique_together = (('account_reconcile_model_line', 'account_tax'),)


class AccountReconcileModelLineTemplate(models.Model):
    model = models.ForeignKey(related_name='+',to = 'AccountReconcileModelTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    amount_type = models.CharField(max_length=255)
    amount_string = models.CharField(max_length=255, blank=True, null=True)
    force_tax_included = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line_template'


class AccountReconcileModelLineTemplateAccountTaxTemplateRel(models.Model):
    account_reconcile_model_line_template = models.OneToOneField(AccountReconcileModelLineTemplate, on_delete = models.DO_NOTHING, primary_key=True)
    account_tax_template = models.ForeignKey(related_name='+',to = 'AccountTaxTemplate', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line_template_account_tax_template_rel'
        unique_together = (('account_reconcile_model_line_template', 'account_tax_template'),)


class AccountReconcileModelPartnerMapping(models.Model):
    model = models.ForeignKey(related_name='+',to = AccountReconcileModel, on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    payment_ref_regex = models.CharField(max_length=255, blank=True, null=True)
    narration_regex = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_partner_mapping'


class AccountReconcileModelResPartnerCategoryRel(models.Model):
    account_reconcile_model = models.OneToOneField(AccountReconcileModel, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner_category = models.ForeignKey(related_name='+',to = 'ResPartnerCategory', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_res_partner_category_rel'
        unique_together = (('account_reconcile_model', 'res_partner_category'),)


class AccountReconcileModelResPartnerRel(models.Model):
    account_reconcile_model = models.OneToOneField(AccountReconcileModel, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_res_partner_rel'
        unique_together = (('account_reconcile_model', 'res_partner'),)


class AccountReconcileModelTemplate(models.Model):
    chart_template = models.ForeignKey(related_name='+',to = AccountChartTemplate, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField()
    rule_type = models.CharField(max_length=255)
    auto_reconcile = models.BooleanField(blank=True, null=True)
    to_check = models.BooleanField(blank=True, null=True)
    matching_order = models.CharField(max_length=255, blank=True, null=True)
    match_text_location_label = models.BooleanField(blank=True, null=True)
    match_text_location_note = models.BooleanField(blank=True, null=True)
    match_text_location_reference = models.BooleanField(blank=True, null=True)
    match_nature = models.CharField(max_length=255)
    match_amount = models.CharField(max_length=255, blank=True, null=True)
    match_amount_min = models.FloatField(blank=True, null=True)
    match_amount_max = models.FloatField(blank=True, null=True)
    match_label = models.CharField(max_length=255, blank=True, null=True)
    match_label_param = models.CharField(max_length=255, blank=True, null=True)
    match_note = models.CharField(max_length=255, blank=True, null=True)
    match_note_param = models.CharField(max_length=255, blank=True, null=True)
    match_transaction_type = models.CharField(max_length=255, blank=True, null=True)
    match_transaction_type_param = models.CharField(max_length=255, blank=True, null=True)
    match_same_currency = models.BooleanField(blank=True, null=True)
    allow_payment_tolerance = models.BooleanField(blank=True, null=True)
    payment_tolerance_param = models.FloatField(blank=True, null=True)
    payment_tolerance_type = models.CharField(max_length=255)
    match_partner = models.BooleanField(blank=True, null=True)
    decimal_separator = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_template'


class AccountReconcileModelTemplateResPartnerCategoryRel(models.Model):
    account_reconcile_model_template = models.OneToOneField(AccountReconcileModelTemplate, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner_category = models.ForeignKey(related_name='+',to = 'ResPartnerCategory', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_template_res_partner_category_rel'
        unique_together = (('account_reconcile_model_template', 'res_partner_category'),)


class AccountReconcileModelTemplateResPartnerRel(models.Model):
    account_reconcile_model_template = models.OneToOneField(AccountReconcileModelTemplate, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_template_res_partner_rel'
        unique_together = (('account_reconcile_model_template', 'res_partner'),)


class AccountResequenceWizard(models.Model):
    first_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    ordering = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_resequence_wizard'


class AccountSetupBankManualConfig(models.Model):
    res_partner_bank = models.ForeignKey(related_name='+',to = 'ResPartnerBank', on_delete = models.DO_NOTHING)
    new_journal_name = models.CharField(max_length=255)
    num_journals_without_account = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_setup_bank_manual_config'


class AccountTax(models.Model):
    name = models.CharField(max_length=255)
    type_tax_use = models.CharField(max_length=255)
    tax_scope = models.CharField(max_length=255, blank=True, null=True)
    amount_type = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    sequence = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    description = models.CharField(max_length=255, blank=True, null=True)
    price_include = models.BooleanField(blank=True, null=True)
    include_base_amount = models.BooleanField(blank=True, null=True)
    is_base_affected = models.BooleanField(blank=True, null=True)
    analytic = models.BooleanField(blank=True, null=True)
    tax_group = models.ForeignKey(related_name='+',to = 'AccountTaxGroup', on_delete = models.DO_NOTHING)
    tax_exigibility = models.CharField(max_length=255, blank=True, null=True)
    cash_basis_transition_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax'
        unique_together = (('name', 'company', 'type_tax_use', 'tax_scope'),)


class AccountTaxCarryoverLine(models.Model):
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    date = models.DateField()
    tax_report_line = models.ForeignKey(related_name='+',to = 'AccountTaxReportLine', on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    foreign_vat_fiscal_position = models.ForeignKey(related_name='+',to = AccountFiscalPosition, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_carryover_line'


class AccountTaxFiliationRel(models.Model):
    parent_tax = models.OneToOneField(AccountTax, on_delete = models.DO_NOTHING, db_column='parent_tax', primary_key=True)
    child_tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING, db_column='child_tax')

    class Meta:
        managed = False
        db_table = 'account_tax_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTaxGroup(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    preceding_subtotal = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_group'


class AccountTaxPurchaseOrderLineRel(models.Model):
    purchase_order_line = models.OneToOneField('PurchaseOrderLine', on_delete = models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_purchase_order_line_rel'
        unique_together = (('purchase_order_line', 'account_tax'),)


class AccountTaxRepartitionFinancialTags(models.Model):
    account_tax_repartition_line_template = models.OneToOneField('AccountTaxRepartitionLineTemplate', on_delete = models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(related_name='+',to = AccountAccountTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_financial_tags'
        unique_together = (('account_tax_repartition_line_template', 'account_account_tag'),)


class AccountTaxRepartitionLine(models.Model):
    factor_percent = models.FloatField()
    repartition_type = models.CharField(max_length=255)
    account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    invoice_tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING, blank=True, null=True)
    refund_tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    use_in_tax_closing = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_line'


class AccountTaxRepartitionLineTemplate(models.Model):
    factor_percent = models.FloatField()
    repartition_type = models.CharField(max_length=255)
    account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    invoice_tax = models.ForeignKey(related_name='+',to = 'AccountTaxTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    refund_tax = models.ForeignKey(related_name='+',to = 'AccountTaxTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    use_in_tax_closing = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_line_template'


class AccountTaxRepartitionMinusReportLine(models.Model):
    account_tax_repartition_line_template = models.OneToOneField(AccountTaxRepartitionLineTemplate, on_delete = models.DO_NOTHING, primary_key=True)
    account_tax_report_line = models.ForeignKey(related_name='+',to = 'AccountTaxReportLine', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_minus_report_line'
        unique_together = (('account_tax_repartition_line_template', 'account_tax_report_line'),)


class AccountTaxRepartitionPlusReportLine(models.Model):
    account_tax_repartition_line_template = models.OneToOneField(AccountTaxRepartitionLineTemplate, on_delete = models.DO_NOTHING, primary_key=True)
    account_tax_report_line = models.ForeignKey(related_name='+',to = 'AccountTaxReportLine', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_plus_report_line'
        unique_together = (('account_tax_repartition_line_template', 'account_tax_report_line'),)


class AccountTaxReport(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_report'


class AccountTaxReportLine(models.Model):
    name = models.CharField(max_length=255)
    report_action = models.ForeignKey(related_name='+',to = 'IrActWindow', on_delete = models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    parent_path = models.CharField(max_length=255, blank=True, null=True)
    report = models.ForeignKey(related_name='+',to = AccountTaxReport, on_delete = models.DO_NOTHING)
    tag_name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    formula = models.CharField(max_length=255, blank=True, null=True)
    carry_over_condition_method = models.CharField(max_length=255, blank=True, null=True)
    carry_over_destination_line = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    is_carryover_persistent = models.BooleanField(blank=True, null=True)
    is_carryover_used_in_balance = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_report_line'


class AccountTaxReportLineTagsRel(models.Model):
    account_account_tag = models.OneToOneField(AccountAccountTag, on_delete = models.DO_NOTHING, primary_key=True)
    account_tax_report_line = models.ForeignKey(related_name='+',to = AccountTaxReportLine, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_report_line_tags_rel'
        unique_together = (('account_account_tag', 'account_tax_report_line'),)


class AccountTaxSaleAdvancePaymentInvRel(models.Model):
    sale_advance_payment_inv = models.OneToOneField('SaleAdvancePaymentInv', on_delete = models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_sale_advance_payment_inv_rel'
        unique_together = (('sale_advance_payment_inv', 'account_tax'),)


class AccountTaxSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine', on_delete = models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_sale_order_line_rel'
        unique_together = (('sale_order_line', 'account_tax'),)


class AccountTaxTemplate(models.Model):
    chart_template = models.ForeignKey(related_name='+',to = AccountChartTemplate, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=255)
    type_tax_use = models.CharField(max_length=255)
    tax_scope = models.CharField(max_length=255, blank=True, null=True)
    amount_type = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    description = models.CharField(max_length=255, blank=True, null=True)
    price_include = models.BooleanField(blank=True, null=True)
    include_base_amount = models.BooleanField(blank=True, null=True)
    is_base_affected = models.BooleanField(blank=True, null=True)
    analytic = models.BooleanField(blank=True, null=True)
    tax_group = models.ForeignKey(related_name='+',to = AccountTaxGroup, on_delete = models.DO_NOTHING, blank=True, null=True)
    tax_exigibility = models.CharField(max_length=255, blank=True, null=True)
    cash_basis_transition_account = models.ForeignKey(related_name='+',to = AccountAccountTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_template'
        unique_together = (('name', 'type_tax_use', 'tax_scope', 'chart_template'),)


class AccountTaxTemplateFiliationRel(models.Model):
    parent_tax = models.OneToOneField(AccountTaxTemplate, on_delete = models.DO_NOTHING, db_column='parent_tax', primary_key=True)
    child_tax = models.ForeignKey(related_name='+',to = AccountTaxTemplate, on_delete = models.DO_NOTHING, db_column='child_tax')

    class Meta:
        managed = False
        db_table = 'account_tax_template_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTourUploadBill(models.Model):
    selection = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tour_upload_bill'


class AccountTourUploadBillEmailConfirm(models.Model):
    email_alias = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tour_upload_bill_email_confirm'


class AccountTourUploadBillIrAttachmentsRel(models.Model):
    account_tour_upload_bill = models.OneToOneField(AccountTourUploadBill, on_delete = models.DO_NOTHING, primary_key=True)
    ir_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tour_upload_bill_ir_attachments_rel'
        unique_together = (('account_tour_upload_bill', 'ir_attachment'),)


class AccountUnreconcile(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_unreconcile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(related_name='+',to = AuthGroup, on_delete = models.DO_NOTHING)
    permission = models.ForeignKey(related_name='+',to = 'AuthPermission', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(related_name='+',to = 'DjangoContentType', on_delete = models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthTotpDevice(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    scope = models.CharField(max_length=255, blank=True, null=True)
    index = models.CharField(max_length=8, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_totp_device'


class AuthTotpWizard(models.Model):
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    secret = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    qrcode = models.BinaryField(blank=True, null=True)
    code = models.CharField(max_length=7, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_totp_wizard'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(related_name='+',to = AuthUser, on_delete = models.DO_NOTHING)
    group = models.ForeignKey(related_name='+',to = AuthGroup, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(related_name='+',to = AuthUser, on_delete = models.DO_NOTHING)
    permission = models.ForeignKey(related_name='+',to = AuthPermission, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BarcodeNomenclature(models.Model):
    name = models.CharField(max_length=32)
    upc_ean_conv = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcode_nomenclature'


class BarcodeRule(models.Model):
    name = models.CharField(max_length=32)
    barcode_nomenclature = models.ForeignKey(related_name='+',to = BarcodeNomenclature, on_delete = models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    encoding = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    pattern = models.CharField(max_length=32)
    alias = models.CharField(max_length=32)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcode_rule'


class BaseAutomation(models.Model):
    action_server = models.ForeignKey(related_name='+',to = 'IrActServer', on_delete = models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)
    trigger = models.CharField(max_length=255)
    trg_date = models.ForeignKey(related_name='+',to = 'IrModelFields', on_delete = models.DO_NOTHING, blank=True, null=True)
    trg_date_range = models.IntegerField(blank=True, null=True)
    trg_date_range_type = models.CharField(max_length=255, blank=True, null=True)
    trg_date_calendar = models.ForeignKey(related_name='+',to = 'ResourceCalendar', on_delete = models.DO_NOTHING, blank=True, null=True)
    filter_pre_domain = models.CharField(max_length=255, blank=True, null=True)
    filter_domain = models.CharField(max_length=255, blank=True, null=True)
    last_run = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_automation'


class BaseAutomationIrModelFieldsRel(models.Model):
    base_automation = models.OneToOneField(BaseAutomation, on_delete = models.DO_NOTHING, primary_key=True)
    ir_model_fields = models.ForeignKey(related_name='+',to = 'IrModelFields', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_automation_ir_model_fields_rel'
        unique_together = (('base_automation', 'ir_model_fields'),)


class BaseAutomationOnchangeFieldsRel(models.Model):
    base_automation = models.OneToOneField(BaseAutomation, on_delete = models.DO_NOTHING, primary_key=True)
    ir_model_fields = models.ForeignKey(related_name='+',to = 'IrModelFields', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_automation_onchange_fields_rel'
        unique_together = (('base_automation', 'ir_model_fields'),)


class BaseDocumentLayout(models.Model):
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    report_layout = models.ForeignKey(related_name='+',to = 'ReportLayout', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_document_layout'


class BaseEnableProfilingWizard(models.Model):
    duration = models.CharField(max_length=255, blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_enable_profiling_wizard'


class BaseGeoProvider(models.Model):
    tech_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_geo_provider'


class BaseImportImport(models.Model):
    res_model = models.CharField(max_length=255, blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_import'


class BaseImportMapping(models.Model):
    res_model = models.CharField(max_length=255, blank=True, null=True)
    column_name = models.CharField(max_length=255, blank=True, null=True)
    field_name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_mapping'


class BaseImportTestsModelsChar(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char'


class BaseImportTestsModelsCharNoreadonly(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_noreadonly'


class BaseImportTestsModelsCharReadonly(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_readonly'


class BaseImportTestsModelsCharRequired(models.Model):
    value = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_required'


class BaseImportTestsModelsCharStates(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_states'


class BaseImportTestsModelsCharStillreadonly(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_stillreadonly'


class BaseImportTestsModelsComplex(models.Model):
    f = models.FloatField(blank=True, null=True)
    m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c = models.CharField(max_length=255, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    d = models.DateField(blank=True, null=True)
    dt = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_complex'


class BaseImportTestsModelsFloat(models.Model):
    value = models.FloatField(blank=True, null=True)
    value2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_float'


class BaseImportTestsModelsM2O(models.Model):
    value = models.ForeignKey(related_name='+',to = 'BaseImportTestsModelsM2ORelated', on_delete = models.DO_NOTHING, db_column='value', blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o'


class BaseImportTestsModelsM2ORelated(models.Model):
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_related'


class BaseImportTestsModelsM2ORequired(models.Model):
    value = models.ForeignKey(related_name='+',to = 'BaseImportTestsModelsM2ORequiredRelated', on_delete = models.DO_NOTHING, db_column='value')
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required'


class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required_related'


class BaseImportTestsModelsO2M(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m'


class BaseImportTestsModelsO2MChild(models.Model):
    parent = models.ForeignKey(related_name='+',to = BaseImportTestsModelsO2M, on_delete = models.DO_NOTHING, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m_child'


class BaseImportTestsModelsPreview(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    somevalue = models.IntegerField()
    othervalue = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_preview'


class BaseLanguageExport(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    data = models.BinaryField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_export'


class BaseLanguageImport(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    data = models.BinaryField()
    filename = models.CharField(max_length=255)
    overwrite = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_import'


class BaseLanguageInstall(models.Model):
    lang = models.CharField(max_length=255)
    overwrite = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_install'


class BaseModuleUninstall(models.Model):
    show_all = models.BooleanField(blank=True, null=True)
    module = models.ForeignKey(related_name='+',to = 'IrModuleModule', on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_uninstall'


class BaseModuleUpdate(models.Model):
    updated = models.IntegerField(blank=True, null=True)
    added = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_update'


class BaseModuleUpgrade(models.Model):
    module_info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_upgrade'


class BasePartnerMergeAutomaticWizard(models.Model):
    group_by_email = models.BooleanField(blank=True, null=True)
    group_by_name = models.BooleanField(blank=True, null=True)
    group_by_is_company = models.BooleanField(blank=True, null=True)
    group_by_vat = models.BooleanField(blank=True, null=True)
    group_by_parent_id = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=255)
    number_group = models.IntegerField(blank=True, null=True)
    current_line = models.ForeignKey(related_name='+',to = 'BasePartnerMergeLine', on_delete = models.DO_NOTHING, blank=True, null=True)
    dst_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    exclude_contact = models.BooleanField(blank=True, null=True)
    exclude_journal_item = models.BooleanField(blank=True, null=True)
    maximum_group = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard'


class BasePartnerMergeAutomaticWizardResPartnerRel(models.Model):
    base_partner_merge_automatic_wizard = models.OneToOneField(BasePartnerMergeAutomaticWizard, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard_res_partner_rel'
        unique_together = (('base_partner_merge_automatic_wizard', 'res_partner'),)


class BasePartnerMergeLine(models.Model):
    wizard = models.ForeignKey(related_name='+',to = BasePartnerMergeAutomaticWizard, on_delete = models.DO_NOTHING, blank=True, null=True)
    min_id = models.IntegerField(blank=True, null=True)
    aggr_ids = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_line'


class BaseUpdateTranslations(models.Model):
    lang = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_update_translations'


class BusBus(models.Model):
    channel = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_bus'


class BusPresence(models.Model):
    user = models.OneToOneField('ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    last_poll = models.DateTimeField(blank=True, null=True)
    last_presence = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    guest = models.OneToOneField('MailGuest', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_presence'


class CalendarAlarm(models.Model):
    name = models.CharField(max_length=255)
    alarm_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    interval = models.CharField(max_length=255)
    duration_minutes = models.IntegerField(blank=True, null=True)
    mail_template = models.ForeignKey(related_name='+',to = 'MailTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sms_template = models.ForeignKey(related_name='+',to = 'SmsTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_alarm'


class CalendarAlarmCalendarEventRel(models.Model):
    calendar_event = models.OneToOneField('CalendarEvent', on_delete = models.DO_NOTHING, primary_key=True)
    calendar_alarm = models.ForeignKey(related_name='+',to = CalendarAlarm, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_alarm_calendar_event_rel'
        unique_together = (('calendar_event', 'calendar_alarm'),)


class CalendarAttendee(models.Model):
    event = models.ForeignKey(related_name='+',to = 'CalendarEvent', on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    common_name = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    availability = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_attendee'


class CalendarEvent(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    videocall_location = models.CharField(max_length=255, blank=True, null=True)
    privacy = models.CharField(max_length=255)
    show_as = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    allday = models.BooleanField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    res_model = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING, blank=True, null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    recurrency = models.BooleanField(blank=True, null=True)
    recurrence = models.ForeignKey(related_name='+',to = 'CalendarRecurrence', on_delete = models.DO_NOTHING, blank=True, null=True)
    follow_recurrence = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    opportunity = models.ForeignKey(related_name='+',to = 'CrmLead', on_delete = models.DO_NOTHING, blank=True, null=True)
    google_id = models.CharField(max_length=255, blank=True, null=True)
    need_sync = models.BooleanField(blank=True, null=True)
    microsoft_id = models.CharField(max_length=255, blank=True, null=True)
    need_sync_m = models.BooleanField(blank=True, null=True)
    microsoft_recurrence_master_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event'


class CalendarEventResPartnerRel(models.Model):
    res_partner = models.OneToOneField('ResPartner', on_delete = models.DO_NOTHING, primary_key=True)
    calendar_event = models.ForeignKey(related_name='+',to = CalendarEvent, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_event_res_partner_rel'
        unique_together = (('res_partner', 'calendar_event'),)


class CalendarEventType(models.Model):
    name = models.CharField(unique=True, max_length=255)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event_type'


class CalendarFilters(models.Model):
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)
    partner_checked = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_filters'
        unique_together = (('user', 'partner'),)


class CalendarRecurrence(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    base_event = models.ForeignKey(related_name='+',to = CalendarEvent, on_delete = models.DO_NOTHING, blank=True, null=True)
    event_tz = models.CharField(max_length=255, blank=True, null=True)
    rrule = models.CharField(max_length=255, blank=True, null=True)
    rrule_type = models.CharField(max_length=255, blank=True, null=True)
    end_type = models.CharField(max_length=255, blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    mon = models.BooleanField(blank=True, null=True)
    tue = models.BooleanField(blank=True, null=True)
    wed = models.BooleanField(blank=True, null=True)
    thu = models.BooleanField(blank=True, null=True)
    fri = models.BooleanField(blank=True, null=True)
    sat = models.BooleanField(blank=True, null=True)
    sun = models.BooleanField(blank=True, null=True)
    month_by = models.CharField(max_length=255, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    weekday = models.CharField(max_length=255, blank=True, null=True)
    byday = models.CharField(max_length=255, blank=True, null=True)
    until = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    google_id = models.CharField(max_length=255, blank=True, null=True)
    need_sync = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    microsoft_id = models.CharField(max_length=255, blank=True, null=True)
    need_sync_m = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_recurrence'


class CashBoxOut(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_out'


class ChangePasswordUser(models.Model):
    wizard = models.ForeignKey(related_name='+',to = 'ChangePasswordWizard', on_delete = models.DO_NOTHING)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    user_login = models.CharField(max_length=255, blank=True, null=True)
    new_passwd = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_user'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_wizard'


class ConfirmStockSms(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confirm_stock_sms'


class CrmConvertLeadMassLeadRel(models.Model):
    crm_lead2opportunity_partner_mass = models.OneToOneField('CrmLead2OpportunityPartnerMass', on_delete = models.DO_NOTHING, primary_key=True)
    crm_lead = models.ForeignKey(related_name='+',to = 'CrmLead', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_convert_lead_mass_lead_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'crm_lead'),)


class CrmLead(models.Model):
    campaign = models.ForeignKey(related_name='+',to = 'UtmCampaign', on_delete = models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey(related_name='+',to = 'UtmSource', on_delete = models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey(related_name='+',to = 'UtmMedium', on_delete = models.DO_NOTHING, blank=True, null=True)
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    phone_sanitized = models.CharField(max_length=255, blank=True, null=True)
    email_normalized = models.CharField(max_length=255, blank=True, null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    email_cc = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey(related_name='+',to = 'CrmTeam', on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    referred = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=255)
    priority = models.CharField(max_length=255, blank=True, null=True)
    stage = models.ForeignKey(related_name='+',to = 'CrmStage', on_delete = models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    expected_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prorated_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recurring_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recurring_plan = models.ForeignKey(related_name='+',to = 'CrmRecurringPlan', on_delete = models.DO_NOTHING, db_column='recurring_plan', blank=True, null=True)
    recurring_revenue_monthly = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recurring_revenue_monthly_prorated = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    date_action_last = models.DateTimeField(blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    day_open = models.FloatField(blank=True, null=True)
    day_close = models.FloatField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    date_conversion = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    function = models.CharField(max_length=255, blank=True, null=True)
    title = models.ForeignKey(related_name='+',to = 'ResPartnerTitle', on_delete = models.DO_NOTHING, db_column='title', blank=True, null=True)
    email_from = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    phone_state = models.CharField(max_length=255, blank=True, null=True)
    email_state = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    lang = models.ForeignKey(related_name='+',to = 'ResLang', on_delete = models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey(related_name='+',to = 'ResCountryState', on_delete = models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    automated_probability = models.FloatField(blank=True, null=True)
    lost_reason = models.ForeignKey(related_name='+',to = 'CrmLostReason', on_delete = models.DO_NOTHING, db_column='lost_reason', blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    reveal_id = models.CharField(max_length=255, blank=True, null=True)
    x_secondary_phone = models.CharField(max_length=13, blank=True, null=True)
    x_secondary_mobile = models.CharField(max_length=13, blank=True, null=True)
    x_vertical = models.CharField(max_length=255, blank=True, null=True)
    x_total_budget = models.CharField(max_length=255, blank=True, null=True)
    x_monthly_budget = models.CharField(max_length=255, blank=True, null=True)
    x_purpose_of_investment = models.CharField(max_length=255, blank=True, null=True)
    x_interest_in_location = models.CharField(db_column='x_interest_In_location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    x_whatsapp_ref = models.CharField(max_length=255, blank=True, null=True)
    x_user_type_ref = models.CharField(max_length=255, blank=True, null=True)
    x_status_ref = models.CharField(max_length=255, blank=True, null=True)
    x_source_ref = models.CharField(max_length=255, blank=True, null=True)
    x_property_type = models.CharField(max_length=255, blank=True, null=True)
    x_residential_status_ref = models.CharField(max_length=255, blank=True, null=True)
    x_associate_network_person = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, db_column='x_associate_network_person', blank=True, null=True)
    x_share_lead_with = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='x_share_lead_with', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead'

    def __str__(self):
        return self.name


class CrmLead2OpportunityPartner(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    lead = models.ForeignKey(related_name='+',to = CrmLead, on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey(related_name='+',to = 'CrmTeam', on_delete = models.DO_NOTHING, blank=True, null=True)
    force_assignment = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner'


class CrmLead2OpportunityPartnerMass(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    lead = models.ForeignKey(related_name='+',to = CrmLead, on_delete = models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey(related_name='+',to = 'CrmTeam', on_delete = models.DO_NOTHING, blank=True, null=True)
    force_assignment = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    deduplicate = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner_mass'


class CrmLead2OpportunityPartnerMassResUsersRel(models.Model):
    crm_lead2opportunity_partner_mass = models.OneToOneField(CrmLead2OpportunityPartnerMass, on_delete = models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner_mass_res_users_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'res_users'),)


class CrmLeadCrmLead2OpportunityPartnerMassRel(models.Model):
    crm_lead2opportunity_partner_mass = models.OneToOneField(CrmLead2OpportunityPartnerMass, on_delete = models.DO_NOTHING, primary_key=True)
    crm_lead = models.ForeignKey(related_name='+',to = CrmLead, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_crm_lead2opportunity_partner_mass_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'crm_lead'),)


class CrmLeadCrmLead2OpportunityPartnerRel(models.Model):
    crm_lead2opportunity_partner = models.OneToOneField(CrmLead2OpportunityPartner, on_delete = models.DO_NOTHING, primary_key=True)
    crm_lead = models.ForeignKey(related_name='+',to = CrmLead, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_crm_lead2opportunity_partner_rel'
        unique_together = (('crm_lead2opportunity_partner', 'crm_lead'),)


class CrmLeadLost(models.Model):
    lost_reason = models.ForeignKey(related_name='+',to = 'CrmLostReason', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_lost'


class CrmLeadPlsUpdate(models.Model):
    pls_start_date = models.DateField()
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_pls_update'


class CrmLeadPlsUpdateCrmLeadScoringFrequencyFieldRel(models.Model):
    crm_lead_pls_update = models.OneToOneField(CrmLeadPlsUpdate, on_delete = models.DO_NOTHING, primary_key=True)
    crm_lead_scoring_frequency_field = models.ForeignKey(related_name='+',to = 'CrmLeadScoringFrequencyField', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_pls_update_crm_lead_scoring_frequency_field_rel'
        unique_together = (('crm_lead_pls_update', 'crm_lead_scoring_frequency_field'),)


class CrmLeadProjectSalesCallLogsRel(models.Model):
    crm_lead = models.OneToOneField(CrmLead, on_delete = models.DO_NOTHING, primary_key=True)
    project_sales_call_logs = models.ForeignKey(related_name='+',to = 'ProjectSalesCallLogs', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_project_sales_call_logs_rel'
        unique_together = (('crm_lead', 'project_sales_call_logs'),)


class CrmLeadScoringFrequency(models.Model):
    variable = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    won_count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lost_count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    team = models.ForeignKey(related_name='+',to = 'CrmTeam', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_scoring_frequency'


class CrmLeadScoringFrequencyField(models.Model):
    field = models.ForeignKey(related_name='+',to = 'IrModelFields', on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_scoring_frequency_field'


class CrmLostReason(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lost_reason'


class CrmMergeOpportunity(models.Model):
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey(related_name='+',to = 'CrmTeam', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_merge_opportunity'


class CrmQuotationPartner(models.Model):
    action = models.CharField(max_length=255)
    lead = models.ForeignKey(related_name='+',to = CrmLead, on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_quotation_partner'


class CrmRecurringPlan(models.Model):
    name = models.CharField(max_length=255)
    number_of_months = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_recurring_plan'


class CrmStage(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    is_won = models.BooleanField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    team = models.ForeignKey(related_name='+',to = 'CrmTeam', on_delete = models.DO_NOTHING, blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_stage'


class CrmTag(models.Model):
    name = models.CharField(unique=True, max_length=255)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_tag'


class CrmTagRel(models.Model):
    lead = models.OneToOneField(CrmLead, on_delete = models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(related_name='+',to = CrmTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_tag_rel'
        unique_together = (('lead', 'tag'),)


class CrmTeam(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    use_quotations = models.BooleanField(blank=True, null=True)
    invoiced_target = models.FloatField(blank=True, null=True)
    alias = models.ForeignKey(related_name='+',to = 'MailAlias', on_delete = models.DO_NOTHING)
    use_leads = models.BooleanField(blank=True, null=True)
    use_opportunities = models.BooleanField(blank=True, null=True)
    assignment_optout = models.BooleanField(blank=True, null=True)
    assignment_domain = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_team'


class CrmTeamMember(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    crm_team = models.ForeignKey(related_name='+',to = CrmTeam, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    assignment_domain = models.CharField(max_length=255, blank=True, null=True)
    assignment_optout = models.BooleanField(blank=True, null=True)
    assignment_max = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_team_member'


class DecimalPrecision(models.Model):
    name = models.CharField(unique=True, max_length=255)
    digits = models.IntegerField()
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision'


class DigestDigest(models.Model):
    name = models.CharField(max_length=255)
    periodicity = models.CharField(max_length=255)
    next_run_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    kpi_res_users_connected = models.BooleanField(blank=True, null=True)
    kpi_mail_message_total = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    kpi_account_total_revenue = models.BooleanField(blank=True, null=True)
    kpi_all_sale_total = models.BooleanField(blank=True, null=True)
    kpi_crm_lead_created = models.BooleanField(blank=True, null=True)
    kpi_crm_opportunities_won = models.BooleanField(blank=True, null=True)
    kpi_project_task_opened = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digest_digest'


class DigestDigestResUsersRel(models.Model):
    digest_digest = models.OneToOneField(DigestDigest, on_delete = models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'digest_digest_res_users_rel'
        unique_together = (('digest_digest', 'res_users'),)


class DigestTip(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    tip_description = models.TextField(blank=True, null=True)
    group = models.ForeignKey(related_name='+',to = 'ResGroups', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digest_tip'


class DigestTipResUsersRel(models.Model):
    digest_tip = models.OneToOneField(DigestTip, on_delete = models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'digest_tip_res_users_rel'
        unique_together = (('digest_tip', 'res_users'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(related_name='+',to = 'DjangoContentType', on_delete = models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = AuthUser, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmailTemplateAttachmentRel(models.Model):
    email_template = models.OneToOneField('MailTemplate', on_delete = models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_attachment_rel'
        unique_together = (('email_template', 'attachment'),)


class EmployeeCategoryRel(models.Model):
    emp = models.OneToOneField('HrEmployee', on_delete = models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey(related_name='+',to = 'HrEmployeeCategory', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_category_rel'
        unique_together = (('emp', 'category'),)


class ExpenseTax(models.Model):
    expense = models.OneToOneField('HrExpense', on_delete = models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'expense_tax'
        unique_together = (('expense', 'tax'),)


class ExpiryPickingConfirmation(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expiry_picking_confirmation'


class ExpiryPickingConfirmationStockPickingRel(models.Model):
    expiry_picking_confirmation = models.OneToOneField(ExpiryPickingConfirmation, on_delete = models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(related_name='+',to = 'StockPicking', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'expiry_picking_confirmation_stock_picking_rel'
        unique_together = (('expiry_picking_confirmation', 'stock_picking'),)


class ExpiryPickingConfirmationStockProductionLotRel(models.Model):
    expiry_picking_confirmation = models.OneToOneField(ExpiryPickingConfirmation, on_delete = models.DO_NOTHING, primary_key=True)
    stock_production_lot = models.ForeignKey(related_name='+',to = 'StockProductionLot', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'expiry_picking_confirmation_stock_production_lot_rel'
        unique_together = (('expiry_picking_confirmation', 'stock_production_lot'),)


class FetchmailServer(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    server = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    server_type = models.CharField(max_length=255)
    is_ssl = models.BooleanField(blank=True, null=True)
    attach = models.BooleanField(blank=True, null=True)
    original = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    object = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    configuration = models.TextField(blank=True, null=True)
    script = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fetchmail_server'


class GoogleCalendarAccountReset(models.Model):
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    delete_policy = models.CharField(max_length=255)
    sync_policy = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'google_calendar_account_reset'


class GoogleCalendarCredentials(models.Model):
    calendar_rtoken = models.CharField(max_length=255, blank=True, null=True)
    calendar_token = models.CharField(max_length=255, blank=True, null=True)
    calendar_token_validity = models.DateTimeField(blank=True, null=True)
    calendar_sync_token = models.CharField(max_length=255, blank=True, null=True)
    calendar_cal_id = models.CharField(max_length=255, blank=True, null=True)
    synchronization_stopped = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'google_calendar_credentials'


class GoogleDriveConfig(models.Model):
    name = models.CharField(max_length=255)
    model = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING)
    filter = models.ForeignKey(related_name='+',to = 'IrFilters', on_delete = models.DO_NOTHING, blank=True, null=True)
    google_drive_template_url = models.CharField(max_length=255)
    name_template = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'google_drive_config'


class HrAttendance(models.Model):
    employee = models.ForeignKey(related_name='+',to = 'HrEmployee', on_delete = models.DO_NOTHING)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(blank=True, null=True)
    worked_hours = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_attendance'


class HrAttendanceOvertime(models.Model):
    employee = models.ForeignKey(related_name='+',to = 'HrEmployee', on_delete = models.DO_NOTHING)
    date = models.DateField(blank=True, null=True)
    duration = models.FloatField()
    duration_real = models.FloatField(blank=True, null=True)
    adjustment = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_attendance_overtime'
        unique_together = (('employee', 'date'),)


class HrContract(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    structure_type = models.ForeignKey(related_name='+',to = 'HrPayrollStructureType', on_delete = models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(related_name='+',to = 'HrEmployee', on_delete = models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(related_name='+',to = 'HrDepartment', on_delete = models.DO_NOTHING, blank=True, null=True)
    job = models.ForeignKey(related_name='+',to = 'HrJob', on_delete = models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    trial_date_end = models.DateField(blank=True, null=True)
    resource_calendar = models.ForeignKey(related_name='+',to = 'ResourceCalendar', on_delete = models.DO_NOTHING, blank=True, null=True)
    wage = models.DecimalField(max_digits=65535, decimal_places=65535)
    notes = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    contract_type = models.ForeignKey(related_name='+',to = 'HrContractType', on_delete = models.DO_NOTHING, blank=True, null=True)
    kanban_state = models.CharField(max_length=255, blank=True, null=True)
    hr_responsible = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_contract'


class HrContractType(models.Model):
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_contract_type'


class HrDepartment(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    complete_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey(related_name='+',to = 'HrEmployee', on_delete = models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_department'


class HrDepartmentMailChannelRel(models.Model):
    mail_channel = models.OneToOneField('MailChannel', on_delete = models.DO_NOTHING, primary_key=True)
    hr_department = models.ForeignKey(related_name='+',to = HrDepartment, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_department_mail_channel_rel'
        unique_together = (('mail_channel', 'hr_department'),)


class HrDepartureReason(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_departure_reason'


class HrDepartureWizard(models.Model):
    departure_reason = models.ForeignKey(related_name='+',to = HrDepartureReason, on_delete = models.DO_NOTHING)
    departure_description = models.TextField(blank=True, null=True)
    departure_date = models.DateField()
    employee = models.ForeignKey(related_name='+',to = 'HrEmployee', on_delete = models.DO_NOTHING)
    archive_private_address = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    set_date_end = models.BooleanField(blank=True, null=True)
    cancel_leaves = models.BooleanField(blank=True, null=True)
    archive_allocation = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_departure_wizard'


class HrEmployee(models.Model):
    resource = models.ForeignKey(related_name='+',to = 'ResourceResource', on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    resource_calendar = models.ForeignKey(related_name='+',to = 'ResourceCalendar', on_delete = models.DO_NOTHING, blank=True, null=True)
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(related_name='+',to = HrDepartment, on_delete = models.DO_NOTHING, blank=True, null=True)
    job = models.ForeignKey(related_name='+',to = 'HrJob', on_delete = models.DO_NOTHING, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    address = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    work_phone = models.CharField(max_length=255, blank=True, null=True)
    mobile_phone = models.CharField(max_length=255, blank=True, null=True)
    work_email = models.CharField(max_length=255, blank=True, null=True)
    work_location = models.ForeignKey(related_name='+',to = 'HrWorkLocation', on_delete = models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    coach = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    employee_type = models.CharField(max_length=255)
    address_home = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    marital = models.CharField(max_length=255, blank=True, null=True)
    spouse_complete_name = models.CharField(max_length=255, blank=True, null=True)
    spouse_birthdate = models.DateField(blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    country_of_birth = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, db_column='country_of_birth', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    ssnid = models.CharField(max_length=255, blank=True, null=True)
    sinid = models.CharField(max_length=255, blank=True, null=True)
    identification_id = models.CharField(max_length=255, blank=True, null=True)
    passport_id = models.CharField(max_length=255, blank=True, null=True)
    bank_account = models.ForeignKey(related_name='+',to = 'ResPartnerBank', on_delete = models.DO_NOTHING, blank=True, null=True)
    permit_no = models.CharField(max_length=255, blank=True, null=True)
    visa_no = models.CharField(max_length=255, blank=True, null=True)
    visa_expire = models.DateField(blank=True, null=True)
    work_permit_expiration_date = models.DateField(blank=True, null=True)
    work_permit_scheduled_activity = models.BooleanField(blank=True, null=True)
    additional_note = models.TextField(blank=True, null=True)
    certificate = models.CharField(max_length=255, blank=True, null=True)
    study_field = models.CharField(max_length=255, blank=True, null=True)
    study_school = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact = models.CharField(max_length=255, blank=True, null=True)
    emergency_phone = models.CharField(max_length=255, blank=True, null=True)
    km_home_work = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    barcode = models.CharField(unique=True, max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=255, blank=True, null=True)
    departure_reason = models.ForeignKey(related_name='+',to = HrDepartureReason, on_delete = models.DO_NOTHING, blank=True, null=True)
    departure_description = models.TextField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    vehicle = models.CharField(max_length=255, blank=True, null=True)
    contract = models.ForeignKey(related_name='+',to = HrContract, on_delete = models.DO_NOTHING, blank=True, null=True)
    contract_warning = models.BooleanField(blank=True, null=True)
    first_contract_date = models.DateField(blank=True, null=True)
    expense_manager = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    leave_manager = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    email_sent = models.BooleanField(blank=True, null=True)
    ip_connected = models.BooleanField(blank=True, null=True)
    manually_set_present = models.BooleanField(blank=True, null=True)
    hr_presence_state_display = models.CharField(max_length=255, blank=True, null=True)
    timesheet_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_attendance = models.ForeignKey(related_name='+',to = HrAttendance, on_delete = models.DO_NOTHING, blank=True, null=True)
    last_check_in = models.DateTimeField(blank=True, null=True)
    last_check_out = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee'
        unique_together = (('user', 'company'),)


class HrEmployeeCategory(models.Model):
    name = models.CharField(unique=True, max_length=255)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee_category'


class HrEmployeeHrLeaveAllocationRel(models.Model):
    hr_leave_allocation = models.OneToOneField('HrLeaveAllocation', on_delete = models.DO_NOTHING, primary_key=True)
    hr_employee = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_employee_hr_leave_allocation_rel'
        unique_together = (('hr_leave_allocation', 'hr_employee'),)


class HrEmployeeHrLeaveRel(models.Model):
    hr_leave = models.OneToOneField('HrLeave', on_delete = models.DO_NOTHING, primary_key=True)
    hr_employee = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_employee_hr_leave_rel'
        unique_together = (('hr_leave', 'hr_employee'),)


class HrExpense(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)
    employee = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING)
    product = models.ForeignKey(related_name='+',to = 'ProductProduct', on_delete = models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING, blank=True, null=True)
    unit_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    untaxed_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_amount_company = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING)
    analytic_account = models.ForeignKey(related_name='+',to = AccountAnalyticAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    payment_mode = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    sheet = models.ForeignKey(related_name='+',to = 'HrExpenseSheet', on_delete = models.DO_NOTHING, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    is_refused = models.BooleanField(blank=True, null=True)
    sample = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order = models.ForeignKey(related_name='+',to = 'SaleOrder', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_expense'


class HrExpenseApproveDuplicate(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_expense_approve_duplicate'


class HrExpenseApproveDuplicateHrExpenseSheetRel(models.Model):
    hr_expense_approve_duplicate = models.OneToOneField(HrExpenseApproveDuplicate, on_delete = models.DO_NOTHING, primary_key=True)
    hr_expense_sheet = models.ForeignKey(related_name='+',to = 'HrExpenseSheet', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_expense_approve_duplicate_hr_expense_sheet_rel'
        unique_together = (('hr_expense_approve_duplicate', 'hr_expense_sheet'),)


class HrExpenseHrExpenseApproveDuplicateRel(models.Model):
    hr_expense_approve_duplicate = models.OneToOneField(HrExpenseApproveDuplicate, on_delete = models.DO_NOTHING, primary_key=True)
    hr_expense = models.ForeignKey(related_name='+',to = HrExpense, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_expense_hr_expense_approve_duplicate_rel'
        unique_together = (('hr_expense_approve_duplicate', 'hr_expense'),)


class HrExpenseHrExpenseRefuseWizardRel(models.Model):
    hr_expense_refuse_wizard = models.OneToOneField('HrExpenseRefuseWizard', on_delete = models.DO_NOTHING, primary_key=True)
    hr_expense = models.ForeignKey(related_name='+',to = HrExpense, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_expense_hr_expense_refuse_wizard_rel'
        unique_together = (('hr_expense_refuse_wizard', 'hr_expense'),)


class HrExpenseRefuseWizard(models.Model):
    reason = models.CharField(max_length=255)
    hr_expense_sheet = models.ForeignKey(related_name='+',to = 'HrExpenseSheet', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_expense_refuse_wizard'


class HrExpenseSheet(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    payment_state = models.CharField(max_length=255, blank=True, null=True)
    employee = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING)
    address = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    bank_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)
    account_move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(related_name='+',to = HrDepartment, on_delete = models.DO_NOTHING, blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_expense_sheet'


class HrHolidaysSummaryEmployee(models.Model):
    date_from = models.DateField()
    holiday_type = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_holidays_summary_employee'


class HrJob(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    expected_employees = models.IntegerField(blank=True, null=True)
    no_of_employee = models.IntegerField(blank=True, null=True)
    no_of_recruitment = models.IntegerField(blank=True, null=True)
    no_of_hired_employee = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    department = models.ForeignKey(related_name='+',to = HrDepartment, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_job'
        unique_together = (('name', 'company', 'department'),)


class HrLeave(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    private_name = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    report_note = models.TextField(blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING, blank=True, null=True)
    holiday_status = models.ForeignKey(related_name='+',to = 'HrLeaveType', on_delete = models.DO_NOTHING)
    holiday_allocation = models.ForeignKey(related_name='+',to = 'HrLeaveAllocation', on_delete = models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING, blank=True, null=True)
    employee_company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(related_name='+',to = HrDepartment, on_delete = models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    number_of_days = models.FloatField(blank=True, null=True)
    duration_display = models.CharField(max_length=255, blank=True, null=True)
    meeting = models.ForeignKey(related_name='+',to = CalendarEvent, on_delete = models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    holiday_type = models.CharField(max_length=255)
    multi_employee = models.BooleanField(blank=True, null=True)
    category = models.ForeignKey(related_name='+',to = HrEmployeeCategory, on_delete = models.DO_NOTHING, blank=True, null=True)
    mode_company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    first_approver = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING, blank=True, null=True)
    second_approver = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING, blank=True, null=True)
    request_date_from = models.DateField(blank=True, null=True)
    request_date_to = models.DateField(blank=True, null=True)
    request_hour_from = models.CharField(max_length=255, blank=True, null=True)
    request_hour_to = models.CharField(max_length=255, blank=True, null=True)
    request_date_from_period = models.CharField(max_length=255, blank=True, null=True)
    request_unit_half = models.BooleanField(blank=True, null=True)
    request_unit_hours = models.BooleanField(blank=True, null=True)
    request_unit_custom = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    overtime = models.ForeignKey(related_name='+',to = HrAttendanceOvertime, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave'


class HrLeaveAccrualLevel(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    accrual_plan = models.ForeignKey(related_name='+',to = 'HrLeaveAccrualPlan', on_delete = models.DO_NOTHING)
    start_count = models.IntegerField(blank=True, null=True)
    start_type = models.CharField(max_length=255)
    is_based_on_worked_time = models.BooleanField(blank=True, null=True)
    added_value = models.FloatField()
    added_value_type = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    week_day = models.CharField(max_length=255)
    first_day = models.IntegerField(blank=True, null=True)
    second_day = models.IntegerField(blank=True, null=True)
    first_month_day = models.IntegerField(blank=True, null=True)
    first_month = models.CharField(max_length=255, blank=True, null=True)
    second_month_day = models.IntegerField(blank=True, null=True)
    second_month = models.CharField(max_length=255, blank=True, null=True)
    yearly_month = models.CharField(max_length=255, blank=True, null=True)
    yearly_day = models.IntegerField(blank=True, null=True)
    maximum_leave = models.FloatField(blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    action_with_unused_accruals = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave_accrual_level'


class HrLeaveAccrualPlan(models.Model):
    name = models.CharField(max_length=255)
    time_off_type = models.ForeignKey(related_name='+',to = 'HrLeaveType', on_delete = models.DO_NOTHING, blank=True, null=True)
    transition_mode = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave_accrual_plan'


class HrLeaveAllocation(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    private_name = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    holiday_status = models.ForeignKey(related_name='+',to = 'HrLeaveType', on_delete = models.DO_NOTHING)
    employee = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING, blank=True, null=True)
    employee_company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    number_of_days = models.FloatField(blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    approver = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING, blank=True, null=True)
    holiday_type = models.CharField(max_length=255)
    multi_employee = models.BooleanField(blank=True, null=True)
    mode_company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(related_name='+',to = HrDepartment, on_delete = models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(related_name='+',to = HrEmployeeCategory, on_delete = models.DO_NOTHING, blank=True, null=True)
    lastcall = models.DateField(blank=True, null=True)
    nextcall = models.DateField(blank=True, null=True)
    allocation_type = models.CharField(max_length=255)
    accrual_plan = models.ForeignKey(related_name='+',to = HrLeaveAccrualPlan, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    overtime = models.ForeignKey(related_name='+',to = HrAttendanceOvertime, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave_allocation'


class HrLeaveType(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    create_calendar_meeting = models.BooleanField(blank=True, null=True)
    color_name = models.CharField(max_length=255)
    color = models.IntegerField(blank=True, null=True)
    icon = models.ForeignKey(related_name='+',to = 'IrAttachment', on_delete = models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    responsible = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    leave_validation_type = models.CharField(max_length=255, blank=True, null=True)
    requires_allocation = models.CharField(max_length=255)
    employee_requests = models.CharField(max_length=255)
    allocation_validation_type = models.CharField(max_length=255, blank=True, null=True)
    time_type = models.CharField(max_length=255, blank=True, null=True)
    request_unit = models.CharField(max_length=255)
    unpaid = models.BooleanField(blank=True, null=True)
    leave_notif_subtype = models.ForeignKey(related_name='+',to = 'MailMessageSubtype', on_delete = models.DO_NOTHING, blank=True, null=True)
    allocation_notif_subtype = models.ForeignKey(related_name='+',to = 'MailMessageSubtype', on_delete = models.DO_NOTHING, blank=True, null=True)
    support_document = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    timesheet_generate = models.BooleanField(blank=True, null=True)
    timesheet_project = models.ForeignKey(related_name='+',to = 'ProjectProject', on_delete = models.DO_NOTHING, blank=True, null=True)
    timesheet_task = models.ForeignKey(related_name='+',to = 'ProjectTask', on_delete = models.DO_NOTHING, blank=True, null=True)
    overtime_deductible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave_type'


class HrPayrollStructureType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    default_resource_calendar = models.ForeignKey(related_name='+',to = 'ResourceCalendar', on_delete = models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_payroll_structure_type'


class HrPlan(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_plan'


class HrPlanActivityType(models.Model):
    activity_type = models.ForeignKey(related_name='+',to = 'MailActivityType', on_delete = models.DO_NOTHING, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    responsible = models.CharField(max_length=255)
    responsible_0 = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='responsible_id', blank=True, null=True)  # Field renamed because of name conflict.
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_plan_activity_type'


class HrPlanHrPlanActivityTypeRel(models.Model):
    hr_plan = models.OneToOneField(HrPlan, on_delete = models.DO_NOTHING, primary_key=True)
    hr_plan_activity_type = models.ForeignKey(related_name='+',to = HrPlanActivityType, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_plan_hr_plan_activity_type_rel'
        unique_together = (('hr_plan', 'hr_plan_activity_type'),)


class HrPlanWizard(models.Model):
    plan = models.ForeignKey(related_name='+',to = HrPlan, on_delete = models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_plan_wizard'


class HrWorkLocation(models.Model):
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    address = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    location_number = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_work_location'


class IapAccount(models.Model):
    service_name = models.CharField(max_length=255, blank=True, null=True)
    account_token = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iap_account'


class IapAccountResCompanyRel(models.Model):
    iap_account = models.OneToOneField(IapAccount, on_delete = models.DO_NOTHING, primary_key=True)
    res_company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iap_account_res_company_rel'
        unique_together = (('iap_account', 'res_company'),)


class IrActClient(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=255)
    binding_view_types = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=255)
    target = models.CharField(max_length=255, blank=True, null=True)
    res_model = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255)
    params_store = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=255)
    binding_view_types = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=255)
    report_type = models.CharField(max_length=255)
    report_name = models.CharField(max_length=255)
    report_file = models.CharField(max_length=255, blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    paperformat = models.ForeignKey(related_name='+',to = 'ReportPaperformat', on_delete = models.DO_NOTHING, blank=True, null=True)
    print_report_name = models.CharField(max_length=255, blank=True, null=True)
    attachment_use = models.BooleanField(blank=True, null=True)
    attachment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=255)
    binding_view_types = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    crud_model = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING, blank=True, null=True)
    link_field = models.ForeignKey(related_name='+',to = 'IrModelFields', on_delete = models.DO_NOTHING, blank=True, null=True)
    template = models.ForeignKey(related_name='+',to = 'MailTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    activity_type = models.ForeignKey(related_name='+',to = 'MailActivityType', on_delete = models.DO_NOTHING, blank=True, null=True)
    activity_summary = models.CharField(max_length=255, blank=True, null=True)
    activity_note = models.TextField(blank=True, null=True)
    activity_date_deadline_range = models.IntegerField(blank=True, null=True)
    activity_date_deadline_range_type = models.CharField(max_length=255, blank=True, null=True)
    activity_user_type = models.CharField(max_length=255, blank=True, null=True)
    activity_user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    activity_user_field_name = models.CharField(max_length=255, blank=True, null=True)
    sms_template = models.ForeignKey(related_name='+',to = 'SmsTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    sms_mass_keep_log = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_server'


class IrActServerGroupRel(models.Model):
    act = models.OneToOneField(IrActServer, on_delete = models.DO_NOTHING, primary_key=True)
    gid = models.ForeignKey(related_name='+',to = 'ResGroups', on_delete = models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_server_group_rel'
        unique_together = (('act', 'gid'),)


class IrActServerResPartnerRel(models.Model):
    ir_act_server = models.OneToOneField(IrActServer, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_act_server_res_partner_rel'
        unique_together = (('ir_act_server', 'res_partner'),)


class IrActUrl(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=255)
    binding_view_types = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    url = models.TextField()
    target = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=255)
    binding_view_types = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    view = models.ForeignKey(related_name='+',to = 'IrUiView', on_delete = models.DO_NOTHING, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=255)
    res_id = models.IntegerField(blank=True, null=True)
    res_model = models.CharField(max_length=255)
    target = models.CharField(max_length=255, blank=True, null=True)
    view_mode = models.CharField(max_length=255)
    usage = models.CharField(max_length=255, blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    search_view = models.ForeignKey(related_name='+',to = 'IrUiView', on_delete = models.DO_NOTHING, blank=True, null=True)
    filter = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    act = models.OneToOneField(IrActWindow, on_delete = models.DO_NOTHING, primary_key=True)
    gid = models.ForeignKey(related_name='+',to = 'ResGroups', on_delete = models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_window_group_rel'
        unique_together = (('act', 'gid'),)


class IrActWindowView(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    view = models.ForeignKey(related_name='+',to = 'IrUiView', on_delete = models.DO_NOTHING, blank=True, null=True)
    view_mode = models.CharField(max_length=255)
    act_window = models.ForeignKey(related_name='+',to = IrActWindow, on_delete = models.DO_NOTHING, blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)


class IrActions(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey(related_name='+',to = 'IrModel', on_delete = models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=255)
    binding_view_types = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_actions'


class IrActionsTodo(models.Model):
    action_id = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_actions_todo'


class IrAsset(models.Model):
    name = models.CharField(max_length=255)
    bundle = models.CharField(max_length=255)
    directive = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255)
    target = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_asset'


class IrAttachment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    res_model = models.CharField(max_length=255, blank=True, null=True)
    res_field = models.CharField(max_length=255, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=255)
    url = models.CharField(max_length=1024, blank=True, null=True)
    public = models.BooleanField(blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    db_datas = models.BinaryField(blank=True, null=True)
    store_fname = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=40, blank=True, null=True)
    mimetype = models.CharField(max_length=255, blank=True, null=True)
    index_content = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    original = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_attachment'


class IrConfigParameter(models.Model):
    key = models.CharField(unique=True, max_length=255)
    value = models.TextField()
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter'


class IrCron(models.Model):
    ir_actions_server = models.ForeignKey(related_name='+',to = IrActServer, on_delete = models.DO_NOTHING)
    cron_name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)
    interval_number = models.IntegerField(blank=True, null=True)
    interval_type = models.CharField(max_length=255, blank=True, null=True)
    numbercall = models.IntegerField(blank=True, null=True)
    doall = models.BooleanField(blank=True, null=True)
    nextcall = models.DateTimeField()
    lastcall = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_cron'


class IrCronTrigger(models.Model):
    cron = models.ForeignKey(related_name='+',to = IrCron, on_delete = models.DO_NOTHING, blank=True, null=True)
    call_at = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_cron_trigger'


class IrDefault(models.Model):
    field = models.ForeignKey(related_name='+',to = 'IrModelFields', on_delete = models.DO_NOTHING)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    condition = models.CharField(max_length=255, blank=True, null=True)
    json_value = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_default'


class IrDemo(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo'


class IrDemoFailure(models.Model):
    module = models.ForeignKey(related_name='+',to = 'IrModuleModule', on_delete = models.DO_NOTHING)
    error = models.CharField(max_length=255, blank=True, null=True)
    wizard = models.ForeignKey(related_name='+',to = 'IrDemoFailureWizard', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo_failure'


class IrDemoFailureWizard(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo_failure_wizard'


class IrExports(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports'


class IrExportsLine(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    export = models.ForeignKey(related_name='+',to = IrExports, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports_line'


class IrFilters(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    domain = models.TextField()
    context = models.TextField()
    sort = models.TextField()
    model_id = models.CharField(max_length=255)
    is_default = models.BooleanField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_filters'
        unique_together = (('name', 'model_id', 'user', 'action_id'),)


class IrLogging(models.Model):
    create_uid = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    dbname = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    path = models.CharField(max_length=255)
    func = models.CharField(max_length=255)
    line = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ir_logging'


class IrMailServer(models.Model):
    name = models.CharField(max_length=255)
    from_filter = models.CharField(max_length=255, blank=True, null=True)
    smtp_host = models.CharField(max_length=255)
    smtp_port = models.IntegerField()
    smtp_authentication = models.CharField(max_length=255)
    smtp_user = models.CharField(max_length=255, blank=True, null=True)
    smtp_pass = models.CharField(max_length=255, blank=True, null=True)
    smtp_encryption = models.CharField(max_length=255)
    smtp_ssl_certificate = models.BinaryField(blank=True, null=True)
    smtp_ssl_private_key = models.BinaryField(blank=True, null=True)
    smtp_debug = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_mail_server'


class IrModel(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(unique=True, max_length=255)
    order = models.CharField(max_length=255)
    info = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    transient = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_mail_thread = models.BooleanField(blank=True, null=True)
    is_mail_activity = models.BooleanField(blank=True, null=True)
    is_mail_blacklist = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model'


class IrModelAccess(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING)
    group = models.ForeignKey(related_name='+',to = 'ResGroups', on_delete = models.DO_NOTHING, blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_access'


class IrModelConstraint(models.Model):
    name = models.CharField(max_length=255)
    definition = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING, db_column='model')
    module = models.ForeignKey(related_name='+',to = 'IrModuleModule', on_delete = models.DO_NOTHING, db_column='module')
    type = models.CharField(max_length=1)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_constraint'
        unique_together = (('name', 'module'),)


class IrModelData(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    noupdate = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_data'
        unique_together = (('module', 'name'),)


class IrModelFields(models.Model):
    name = models.CharField(max_length=255)
    complete_name = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255)
    relation = models.CharField(max_length=255, blank=True, null=True)
    relation_field = models.CharField(max_length=255, blank=True, null=True)
    relation_field_0 = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, db_column='relation_field_id', blank=True, null=True)  # Field renamed because of name conflict.
    model_0 = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING, db_column='model_id')  # Field renamed because of name conflict.
    field_description = models.CharField(max_length=255)
    help = models.TextField(blank=True, null=True)
    ttype = models.CharField(max_length=255)
    copied = models.BooleanField(blank=True, null=True)
    related = models.CharField(max_length=255, blank=True, null=True)
    related_field = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    required = models.BooleanField(blank=True, null=True)
    readonly = models.BooleanField(blank=True, null=True)
    index = models.BooleanField(blank=True, null=True)
    translate = models.BooleanField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=255)
    on_delete = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    group_expand = models.BooleanField(blank=True, null=True)
    selectable = models.BooleanField(blank=True, null=True)
    relation_table = models.CharField(max_length=255, blank=True, null=True)
    column1 = models.CharField(max_length=255, blank=True, null=True)
    column2 = models.CharField(max_length=255, blank=True, null=True)
    compute = models.TextField(blank=True, null=True)
    depends = models.CharField(max_length=255, blank=True, null=True)
    store = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tracking = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_fields'
        unique_together = (('model', 'name'),)


class IrModelFieldsGroupRel(models.Model):
    field = models.OneToOneField(IrModelFields, on_delete = models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey(related_name='+',to = 'ResGroups', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_model_fields_group_rel'
        unique_together = (('field', 'group'),)


class IrModelFieldsSelection(models.Model):
    field = models.ForeignKey(related_name='+',to = IrModelFields, on_delete = models.DO_NOTHING)
    value = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_fields_selection'
        unique_together = (('field', 'value'),)


class IrModelRelation(models.Model):
    name = models.CharField(max_length=255)
    model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING, db_column='model')
    module = models.ForeignKey(related_name='+',to = 'IrModuleModule', on_delete = models.DO_NOTHING, db_column='module')
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_relation'


class IrModuleCategory(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    exclusive = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_category'


class IrModuleModule(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=16, blank=True, null=True)
    latest_version = models.CharField(max_length=255, blank=True, null=True)
    shortdesc = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(related_name='+',to = IrModuleCategory, on_delete = models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    application = models.BooleanField(blank=True, null=True)
    demo = models.BooleanField(blank=True, null=True)
    web = models.BooleanField(blank=True, null=True)
    license = models.CharField(max_length=32, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    auto_install = models.BooleanField(blank=True, null=True)
    to_buy = models.BooleanField(blank=True, null=True)
    maintainer = models.CharField(max_length=255, blank=True, null=True)
    contributors = models.TextField(blank=True, null=True)
    published_version = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    menus_by_module = models.TextField(blank=True, null=True)
    reports_by_module = models.TextField(blank=True, null=True)
    views_by_module = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module'


class IrModuleModuleDependency(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    module = models.ForeignKey(related_name='+',to = IrModuleModule, on_delete = models.DO_NOTHING, blank=True, null=True)
    auto_install_required = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_dependency'


class IrModuleModuleExclusion(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    module = models.ForeignKey(related_name='+',to = IrModuleModule, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_exclusion'


class IrProfile(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    session = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    init_stack_trace = models.TextField(blank=True, null=True)
    sql = models.TextField(blank=True, null=True)
    traces_async = models.TextField(blank=True, null=True)
    traces_sync = models.TextField(blank=True, null=True)
    qweb = models.TextField(blank=True, null=True)
    entry_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_profile'


class IrProperty(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    res_id = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    fields = models.ForeignKey(related_name='+',to = IrModelFields, on_delete = models.DO_NOTHING)
    value_float = models.FloatField(blank=True, null=True)
    value_integer = models.IntegerField(blank=True, null=True)
    value_text = models.TextField(blank=True, null=True)
    value_binary = models.BinaryField(blank=True, null=True)
    value_reference = models.CharField(max_length=255, blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_property'


class IrRule(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING)
    domain_force = models.TextField(blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    global_field = models.BooleanField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'ir_rule'


class IrSequence(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    implementation = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    prefix = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    number_next = models.IntegerField()
    number_increment = models.IntegerField()
    padding = models.IntegerField()
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    use_date_range = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence'


class IrSequenceDateRange(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    sequence = models.ForeignKey(related_name='+',to = IrSequence, on_delete = models.DO_NOTHING)
    number_next = models.IntegerField()
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence_date_range'


class IrServerObjectLines(models.Model):
    server = models.ForeignKey(related_name='+',to = IrActServer, on_delete = models.DO_NOTHING, blank=True, null=True)
    col1 = models.ForeignKey(related_name='+',to = IrModelFields, on_delete = models.DO_NOTHING, db_column='col1')
    value = models.TextField()
    evaluation_type = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_server_object_lines'


class IrTranslation(models.Model):
    name = models.CharField(max_length=255)
    res_id = models.IntegerField(blank=True, null=True)
    lang = models.ForeignKey(related_name='+',to = 'ResLang', on_delete = models.DO_NOTHING, db_column='lang', blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    src = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_translation'
        unique_together = (('type', 'lang'), ('type', 'lang', 'name', 'res_id'), ('type', 'name', 'lang', 'res_id'),)


class IrUiMenu(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    parent_path = models.CharField(max_length=255, blank=True, null=True)
    web_icon = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_menu'


class IrUiMenuGroupRel(models.Model):
    menu = models.OneToOneField(IrUiMenu, on_delete = models.DO_NOTHING, primary_key=True)
    gid = models.ForeignKey(related_name='+',to = 'ResGroups', on_delete = models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_ui_menu_group_rel'
        unique_together = (('menu', 'gid'),)


class IrUiView(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    arch_db = models.TextField(blank=True, null=True)
    arch_fs = models.CharField(max_length=255, blank=True, null=True)
    arch_updated = models.BooleanField(blank=True, null=True)
    arch_prev = models.TextField(blank=True, null=True)
    inherit = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    field_parent = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    customize_show = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_view'


class IrUiViewCustom(models.Model):
    ref = models.ForeignKey(related_name='+',to = IrUiView, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    arch = models.TextField()
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_custom'


class IrUiViewGroupRel(models.Model):
    view = models.OneToOneField(IrUiView, on_delete = models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey(related_name='+',to = 'ResGroups', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_group_rel'
        unique_together = (('view', 'group'),)


class JournalAccountControlRel(models.Model):
    journal = models.OneToOneField(AccountJournal, on_delete = models.DO_NOTHING, primary_key=True)
    account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'journal_account_control_rel'
        unique_together = (('journal', 'account'),)


class JournalAccountTypeControlRel(models.Model):
    journal = models.OneToOneField(AccountJournal, on_delete = models.DO_NOTHING, primary_key=True)
    type = models.ForeignKey(related_name='+',to = AccountAccountType, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'journal_account_type_control_rel'
        unique_together = (('journal', 'type'),)


class MailActivity(models.Model):
    res_model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING)
    res_model_0 = models.CharField(db_column='res_model', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    res_id = models.IntegerField()
    res_name = models.CharField(max_length=255, blank=True, null=True)
    activity_type = models.ForeignKey(related_name='+',to = 'MailActivityType', on_delete = models.DO_NOTHING, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    date_deadline = models.DateField()
    automated = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    request_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    recommended_activity_type = models.ForeignKey(related_name='+',to = 'MailActivityType', on_delete = models.DO_NOTHING, blank=True, null=True)
    previous_activity_type = models.ForeignKey(related_name='+',to = 'MailActivityType', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    calendar_event = models.ForeignKey(related_name='+',to = CalendarEvent, on_delete = models.DO_NOTHING, blank=True, null=True)
    note_0 = models.ForeignKey(related_name='+',to = 'NoteNote', on_delete = models.DO_NOTHING, db_column='note_id', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'mail_activity'


class MailActivityRel(models.Model):
    activity = models.OneToOneField('MailActivityType', on_delete = models.DO_NOTHING, primary_key=True)
    recommended = models.ForeignKey(related_name='+',to = 'MailActivityType', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_activity_rel'
        unique_together = (('activity', 'recommended'),)


class MailActivityType(models.Model):
    name = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    delay_count = models.IntegerField(blank=True, null=True)
    delay_unit = models.CharField(max_length=255)
    delay_from = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)
    decoration_type = models.CharField(max_length=255, blank=True, null=True)
    res_model = models.CharField(max_length=255, blank=True, null=True)
    triggered_next_type = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    chaining_type = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    default_user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    default_note = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_activity_type'


class MailActivityTypeMailTemplateRel(models.Model):
    mail_activity_type = models.OneToOneField(MailActivityType, on_delete = models.DO_NOTHING, primary_key=True)
    mail_template = models.ForeignKey(related_name='+',to = 'MailTemplate', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_activity_type_mail_template_rel'
        unique_together = (('mail_activity_type', 'mail_template'),)


class MailAlias(models.Model):
    alias_name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    alias_model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING)
    alias_user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    alias_defaults = models.TextField()
    alias_force_thread_id = models.IntegerField(blank=True, null=True)
    alias_parent_model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING, blank=True, null=True)
    alias_parent_thread_id = models.IntegerField(blank=True, null=True)
    alias_contact = models.CharField(max_length=255)
    alias_bounced_content = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_alias'


class MailBlacklist(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_blacklist'


class MailBlacklistRemove(models.Model):
    email = models.CharField(max_length=255)
    reason = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_blacklist_remove'


class MailChannel(models.Model):
    alias = models.ForeignKey(related_name='+',to = MailAlias, on_delete = models.DO_NOTHING)
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    channel_type = models.CharField(max_length=255, blank=True, null=True)
    default_display_mode = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=50, blank=True, null=True)
    public = models.CharField(max_length=255)
    group_public = models.ForeignKey(related_name='+',to = 'ResGroups', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel'


class MailChannelPartner(models.Model):
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    guest = models.ForeignKey(related_name='+',to = 'MailGuest', on_delete = models.DO_NOTHING, blank=True, null=True)
    channel = models.ForeignKey(related_name='+',to = MailChannel, on_delete = models.DO_NOTHING)
    custom_channel_name = models.CharField(max_length=255, blank=True, null=True)
    fetched_message = models.ForeignKey(related_name='+',to = 'MailMessage', on_delete = models.DO_NOTHING, blank=True, null=True)
    seen_message = models.ForeignKey(related_name='+',to = 'MailMessage', on_delete = models.DO_NOTHING, blank=True, null=True)
    fold_state = models.CharField(max_length=255, blank=True, null=True)
    is_minimized = models.BooleanField(blank=True, null=True)
    is_pinned = models.BooleanField(blank=True, null=True)
    last_interest_dt = models.DateTimeField(blank=True, null=True)
    rtc_inviting_session = models.ForeignKey(related_name='+',to = 'MailChannelRtcSession', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel_partner'
        unique_together = (('channel', 'guest'), ('channel', 'partner'),)


class MailChannelResGroupsRel(models.Model):
    mail_channel = models.OneToOneField(MailChannel, on_delete = models.DO_NOTHING, primary_key=True)
    res_groups = models.ForeignKey(related_name='+',to = 'ResGroups', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_channel_res_groups_rel'
        unique_together = (('mail_channel', 'res_groups'),)


class MailChannelRtcSession(models.Model):
    channel_partner = models.OneToOneField(MailChannelPartner, on_delete = models.DO_NOTHING)
    channel = models.ForeignKey(related_name='+',to = MailChannel, on_delete = models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_screen_sharing_on = models.BooleanField(blank=True, null=True)
    is_camera_on = models.BooleanField(blank=True, null=True)
    is_muted = models.BooleanField(blank=True, null=True)
    is_deaf = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel_rtc_session'


class MailComposeMessage(models.Model):
    lang = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    template = models.ForeignKey(related_name='+',to = 'MailTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'MailMessage', on_delete = models.DO_NOTHING, blank=True, null=True)
    layout = models.CharField(max_length=255, blank=True, null=True)
    add_sign = models.BooleanField(blank=True, null=True)
    email_from = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    composition_mode = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    record_name = models.CharField(max_length=255, blank=True, null=True)
    use_active_domain = models.BooleanField(blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    message_type = models.CharField(max_length=255)
    subtype = models.ForeignKey(related_name='+',to = 'MailMessageSubtype', on_delete = models.DO_NOTHING, blank=True, null=True)
    mail_activity_type = models.ForeignKey(related_name='+',to = MailActivityType, on_delete = models.DO_NOTHING, blank=True, null=True)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    reply_to_force_new = models.BooleanField(blank=True, null=True)
    is_log = models.BooleanField(blank=True, null=True)
    notify = models.BooleanField(blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    auto_delete_message = models.BooleanField(blank=True, null=True)
    mail_server = models.ForeignKey(related_name='+',to = IrMailServer, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_compose_message'


class MailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.OneToOneField(MailComposeMessage, on_delete = models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class MailComposeMessageResPartnerRel(models.Model):
    wizard = models.OneToOneField(MailComposeMessage, on_delete = models.DO_NOTHING, primary_key=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_res_partner_rel'
        unique_together = (('wizard', 'partner'),)


class MailFollowers(models.Model):
    res_model = models.CharField(max_length=255)
    res_id = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_followers'
        unique_together = (('res_model', 'res_id', 'partner'),)


class MailFollowersMailMessageSubtypeRel(models.Model):
    mail_followers = models.OneToOneField(MailFollowers, on_delete = models.DO_NOTHING, primary_key=True)
    mail_message_subtype = models.ForeignKey(related_name='+',to = 'MailMessageSubtype', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_followers_mail_message_subtype_rel'
        unique_together = (('mail_followers', 'mail_message_subtype'),)


class MailGuest(models.Model):
    name = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_guest'


class MailIceServer(models.Model):
    server_type = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    credential = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_ice_server'


class MailMail(models.Model):
    mail_message = models.ForeignKey(related_name='+',to = 'MailMessage', on_delete = models.DO_NOTHING)
    body_html = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    is_notification = models.BooleanField(blank=True, null=True)
    email_to = models.TextField(blank=True, null=True)
    email_cc = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    failure_type = models.CharField(max_length=255, blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    scheduled_date = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fetchmail_server = models.ForeignKey(related_name='+',to = FetchmailServer, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mail'


class MailMailResPartnerRel(models.Model):
    mail_mail = models.OneToOneField(MailMail, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mail_res_partner_rel'
        unique_together = (('mail_mail', 'res_partner'),)


class MailMessage(models.Model):
    subject = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    record_name = models.CharField(max_length=255, blank=True, null=True)
    message_type = models.CharField(max_length=255)
    subtype = models.ForeignKey(related_name='+',to = 'MailMessageSubtype', on_delete = models.DO_NOTHING, blank=True, null=True)
    mail_activity_type = models.ForeignKey(related_name='+',to = MailActivityType, on_delete = models.DO_NOTHING, blank=True, null=True)
    is_internal = models.BooleanField(blank=True, null=True)
    email_from = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    author_guest = models.ForeignKey(related_name='+',to = MailGuest, on_delete = models.DO_NOTHING, blank=True, null=True)
    reply_to_force_new = models.BooleanField(blank=True, null=True)
    message_id = models.CharField(max_length=255, blank=True, null=True)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    mail_server = models.ForeignKey(related_name='+',to = IrMailServer, on_delete = models.DO_NOTHING, blank=True, null=True)
    email_layout_xmlid = models.CharField(max_length=255, blank=True, null=True)
    add_sign = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message'


class MailMessageReaction(models.Model):
    message = models.ForeignKey(related_name='+',to = MailMessage, on_delete = models.DO_NOTHING)
    content = models.CharField(max_length=255)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    guest = models.ForeignKey(related_name='+',to = MailGuest, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message_reaction'
        unique_together = (('message', 'content', 'guest'), ('message', 'content', 'partner'),)


class MailMessageResPartnerRel(models.Model):
    mail_message = models.OneToOneField(MailMessage, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageResPartnerStarredRel(models.Model):
    mail_message = models.OneToOneField(MailMessage, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_starred_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageSubtype(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    internal = models.BooleanField(blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    relation_field = models.CharField(max_length=255, blank=True, null=True)
    res_model = models.CharField(max_length=255, blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    hidden = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message_subtype'


class MailNotification(models.Model):
    mail_message = models.ForeignKey(related_name='+',to = MailMessage, on_delete = models.DO_NOTHING)
    mail_mail = models.ForeignKey(related_name='+',to = MailMail, on_delete = models.DO_NOTHING, blank=True, null=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    notification_type = models.CharField(max_length=255)
    notification_status = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.BooleanField(blank=True, null=True)
    read_date = models.DateTimeField(blank=True, null=True)
    failure_type = models.CharField(max_length=255, blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    sms = models.ForeignKey(related_name='+',to = 'SmsSms', on_delete = models.DO_NOTHING, blank=True, null=True)
    sms_number = models.CharField(max_length=255, blank=True, null=True)
    letter = models.ForeignKey(related_name='+',to = 'SnailmailLetter', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_notification'


class MailNotificationMailResendMessageRel(models.Model):
    mail_resend_message = models.OneToOneField('MailResendMessage', on_delete = models.DO_NOTHING, primary_key=True)
    mail_notification = models.ForeignKey(related_name='+',to = MailNotification, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_notification_mail_resend_message_rel'
        unique_together = (('mail_resend_message', 'mail_notification'),)


class MailResendCancel(models.Model):
    model = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_cancel'


class MailResendMessage(models.Model):
    mail_message = models.ForeignKey(related_name='+',to = MailMessage, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_message'


class MailResendPartner(models.Model):
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    resend = models.BooleanField(blank=True, null=True)
    resend_wizard = models.ForeignKey(related_name='+',to = MailResendMessage, on_delete = models.DO_NOTHING, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_partner'


class MailShortcode(models.Model):
    source = models.CharField(max_length=255)
    substitution = models.TextField()
    description = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_shortcode'


class MailTemplate(models.Model):
    lang = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    subject = models.CharField(max_length=255, blank=True, null=True)
    email_from = models.CharField(max_length=255, blank=True, null=True)
    use_default_to = models.BooleanField(blank=True, null=True)
    email_to = models.CharField(max_length=255, blank=True, null=True)
    partner_to = models.CharField(max_length=255, blank=True, null=True)
    email_cc = models.CharField(max_length=255, blank=True, null=True)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    report_name = models.CharField(max_length=255, blank=True, null=True)
    report_template = models.ForeignKey(related_name='+',to = IrActReportXml, on_delete = models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    mail_server = models.ForeignKey(related_name='+',to = IrMailServer, on_delete = models.DO_NOTHING, blank=True, null=True)
    scheduled_date = models.CharField(max_length=255, blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    ref_ir_act_window = models.ForeignKey(related_name='+',to = IrActWindow, on_delete = models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_template'


class MailTemplatePreview(models.Model):
    mail_template = models.ForeignKey(related_name='+',to = MailTemplate, on_delete = models.DO_NOTHING)
    resource_ref = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    error_msg = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_template_preview'


class MailTrackingValue(models.Model):
    field = models.ForeignKey(related_name='+',to = IrModelFields, on_delete = models.DO_NOTHING, db_column='field')
    field_desc = models.CharField(max_length=255)
    field_type = models.CharField(max_length=255, blank=True, null=True)
    old_value_integer = models.IntegerField(blank=True, null=True)
    old_value_float = models.FloatField(blank=True, null=True)
    old_value_monetary = models.FloatField(blank=True, null=True)
    old_value_char = models.CharField(max_length=255, blank=True, null=True)
    old_value_text = models.TextField(blank=True, null=True)
    old_value_datetime = models.DateTimeField(blank=True, null=True)
    new_value_integer = models.IntegerField(blank=True, null=True)
    new_value_float = models.FloatField(blank=True, null=True)
    new_value_monetary = models.FloatField(blank=True, null=True)
    new_value_char = models.CharField(max_length=255, blank=True, null=True)
    new_value_text = models.TextField(blank=True, null=True)
    new_value_datetime = models.DateTimeField(blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    mail_message = models.ForeignKey(related_name='+',to = MailMessage, on_delete = models.DO_NOTHING)
    tracking_sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_tracking_value'


class MailWizardInvite(models.Model):
    res_model = models.CharField(max_length=255)
    res_id = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    send_mail = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite'


class MailWizardInviteResPartnerRel(models.Model):
    mail_wizard_invite = models.OneToOneField(MailWizardInvite, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite_res_partner_rel'
        unique_together = (('mail_wizard_invite', 'res_partner'),)


class MeetingCategoryRel(models.Model):
    event = models.OneToOneField(CalendarEvent, on_delete = models.DO_NOTHING, primary_key=True)
    type = models.ForeignKey(related_name='+',to = CalendarEventType, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'meeting_category_rel'
        unique_together = (('event', 'type'),)


class MergeOpportunityRel(models.Model):
    merge = models.OneToOneField(CrmMergeOpportunity, on_delete = models.DO_NOTHING, primary_key=True)
    opportunity = models.ForeignKey(related_name='+',to = CrmLead, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'merge_opportunity_rel'
        unique_together = (('merge', 'opportunity'),)


class MessageAttachmentRel(models.Model):
    message = models.OneToOneField(MailMessage, on_delete = models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'message_attachment_rel'
        unique_together = (('message', 'attachment'),)


class MicrosoftCalendarAccountReset(models.Model):
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    delete_policy = models.CharField(max_length=255)
    sync_policy = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microsoft_calendar_account_reset'


class NoteNote(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    open = models.BooleanField(blank=True, null=True)
    date_done = models.DateField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_note'


class NoteStage(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    fold = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_stage'


class NoteStageRel(models.Model):
    note = models.OneToOneField(NoteNote, on_delete = models.DO_NOTHING, primary_key=True)
    stage = models.ForeignKey(related_name='+',to = NoteStage, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'note_stage_rel'
        unique_together = (('note', 'stage'),)


class NoteTag(models.Model):
    name = models.CharField(unique=True, max_length=255)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_tag'


class NoteTagsRel(models.Model):
    note = models.OneToOneField(NoteNote, on_delete = models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(related_name='+',to = NoteTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'note_tags_rel'
        unique_together = (('note', 'tag'),)


class PaymentAcquirer(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    provider = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    allow_tokenization = models.BooleanField(blank=True, null=True)
    capture_manually = models.BooleanField(blank=True, null=True)
    redirect_form_view = models.ForeignKey(related_name='+',to = IrUiView, on_delete = models.DO_NOTHING, blank=True, null=True)
    inline_form_view = models.ForeignKey(related_name='+',to = IrUiView, on_delete = models.DO_NOTHING, blank=True, null=True)
    fees_active = models.BooleanField(blank=True, null=True)
    fees_dom_fixed = models.FloatField(blank=True, null=True)
    fees_dom_var = models.FloatField(blank=True, null=True)
    fees_int_fixed = models.FloatField(blank=True, null=True)
    fees_int_var = models.FloatField(blank=True, null=True)
    display_as = models.CharField(max_length=255, blank=True, null=True)
    pre_msg = models.TextField(blank=True, null=True)
    pending_msg = models.TextField(blank=True, null=True)
    auth_msg = models.TextField(blank=True, null=True)
    done_msg = models.TextField(blank=True, null=True)
    cancel_msg = models.TextField(blank=True, null=True)
    support_authorization = models.BooleanField(blank=True, null=True)
    support_fees_computation = models.BooleanField(blank=True, null=True)
    support_tokenization = models.BooleanField(blank=True, null=True)
    support_refund = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    module = models.ForeignKey(related_name='+',to = IrModuleModule, on_delete = models.DO_NOTHING, blank=True, null=True)
    module_state = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    qr_code = models.BooleanField(blank=True, null=True)
    so_reference_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_acquirer'


class PaymentAcquirerOnboardingWizard(models.Model):
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    paypal_user_type = models.CharField(max_length=255, blank=True, null=True)
    paypal_email_account = models.CharField(max_length=255, blank=True, null=True)
    paypal_seller_account = models.CharField(max_length=255, blank=True, null=True)
    paypal_pdt_token = models.CharField(max_length=255, blank=True, null=True)
    stripe_secret_key = models.CharField(max_length=255, blank=True, null=True)
    stripe_publishable_key = models.CharField(max_length=255, blank=True, null=True)
    manual_name = models.CharField(max_length=255, blank=True, null=True)
    journal_name = models.CharField(max_length=255, blank=True, null=True)
    acc_number = models.CharField(max_length=255, blank=True, null=True)
    manual_post_msg = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_acquirer_onboarding_wizard'


class PaymentAcquirerPaymentIconRel(models.Model):
    payment_acquirer = models.OneToOneField(PaymentAcquirer, on_delete = models.DO_NOTHING, primary_key=True)
    payment_icon = models.ForeignKey(related_name='+',to = 'PaymentIcon', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_acquirer_payment_icon_rel'
        unique_together = (('payment_acquirer', 'payment_icon'),)


class PaymentCountryRel(models.Model):
    payment = models.OneToOneField(PaymentAcquirer, on_delete = models.DO_NOTHING, primary_key=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_country_rel'
        unique_together = (('payment', 'country'),)


class PaymentIcon(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_icon'


class PaymentLinkWizard(models.Model):
    res_model = models.CharField(max_length=255)
    res_id = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    amount_max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    acquirer = models.ForeignKey(related_name='+',to = PaymentAcquirer, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_link_wizard'


class PaymentRefundWizard(models.Model):
    payment = models.ForeignKey(related_name='+',to = AccountPayment, on_delete = models.DO_NOTHING, blank=True, null=True)
    amount_to_refund = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_refund_wizard'


class PaymentToken(models.Model):
    acquirer = models.ForeignKey(related_name='+',to = PaymentAcquirer, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=255)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    acquirer_ref = models.CharField(max_length=255)
    verified = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_token'


class PaymentTransaction(models.Model):
    acquirer = models.ForeignKey(related_name='+',to = PaymentAcquirer, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    reference = models.CharField(unique=True, max_length=255)
    acquirer_reference = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING)
    fees = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    token = models.ForeignKey(related_name='+',to = PaymentToken, on_delete = models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=255)
    state_message = models.TextField(blank=True, null=True)
    last_state_change = models.DateTimeField(blank=True, null=True)
    operation = models.CharField(max_length=255, blank=True, null=True)
    payment = models.ForeignKey(related_name='+',to = AccountPayment, on_delete = models.DO_NOTHING, blank=True, null=True)
    source_transaction = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    is_post_processed = models.BooleanField(blank=True, null=True)
    tokenize = models.BooleanField(blank=True, null=True)
    landing_route = models.CharField(max_length=255, blank=True, null=True)
    callback_model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING, blank=True, null=True)
    callback_res_id = models.IntegerField(blank=True, null=True)
    callback_method = models.CharField(max_length=255, blank=True, null=True)
    callback_hash = models.CharField(max_length=255, blank=True, null=True)
    callback_is_done = models.BooleanField(blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    partner_lang = models.CharField(max_length=255, blank=True, null=True)
    partner_email = models.CharField(max_length=255, blank=True, null=True)
    partner_address = models.CharField(max_length=255, blank=True, null=True)
    partner_zip = models.CharField(max_length=255, blank=True, null=True)
    partner_city = models.CharField(max_length=255, blank=True, null=True)
    partner_state = models.ForeignKey(related_name='+',to = 'ResCountryState', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner_country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner_phone = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_transaction'


class PhoneBlacklist(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    number = models.CharField(unique=True, max_length=255)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_blacklist'


class PhoneBlacklistRemove(models.Model):
    phone = models.CharField(max_length=255)
    reason = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_blacklist_remove'


class PortalShare(models.Model):
    res_model = models.CharField(max_length=255)
    res_id = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_share'


class PortalShareResPartnerRel(models.Model):
    portal_share = models.OneToOneField(PortalShare, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_share_res_partner_rel'
        unique_together = (('portal_share', 'res_partner'),)


class PortalWizard(models.Model):
    welcome_message = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_wizard'


class PortalWizardResPartnerRel(models.Model):
    portal_wizard = models.OneToOneField(PortalWizard, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_wizard_res_partner_rel'
        unique_together = (('portal_wizard', 'res_partner'),)


class PortalWizardUser(models.Model):
    wizard = models.ForeignKey(related_name='+',to = PortalWizard, on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    email = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_wizard_user'


class ProcurementGroup(models.Model):
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    move_type = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale = models.ForeignKey(related_name='+',to = 'SaleOrder', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_group'


class ProductAttrExclusionValueIdsRel(models.Model):
    product_template_attribute_exclusion = models.OneToOneField('ProductTemplateAttributeExclusion', on_delete = models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey(related_name='+',to = 'ProductTemplateAttributeValue', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attr_exclusion_value_ids_rel'
        unique_together = (('product_template_attribute_exclusion', 'product_template_attribute_value'),)


class ProductAttribute(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    create_variant = models.CharField(max_length=255)
    display_type = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute'


class ProductAttributeCustomValue(models.Model):
    custom_product_template_attribute_value = models.ForeignKey(related_name='+',to = 'ProductTemplateAttributeValue', on_delete = models.DO_NOTHING)
    custom_value = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order_line = models.ForeignKey(related_name='+',to = 'SaleOrderLine', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_custom_value'
        unique_together = (('custom_product_template_attribute_value', 'sale_order_line'),)


class ProductAttributeProductTemplateRel(models.Model):
    product_attribute = models.OneToOneField(ProductAttribute, on_delete = models.DO_NOTHING, primary_key=True)
    product_template = models.ForeignKey(related_name='+',to = 'ProductTemplate', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_product_template_rel'
        unique_together = (('product_attribute', 'product_template'),)


class ProductAttributeValue(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    attribute = models.ForeignKey(related_name='+',to = ProductAttribute, on_delete = models.DO_NOTHING)
    is_custom = models.BooleanField(blank=True, null=True)
    html_color = models.CharField(max_length=255, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_value'
        unique_together = (('name', 'attribute'),)


class ProductAttributeValueProductTemplateAttributeLineRel(models.Model):
    product_attribute_value = models.OneToOneField(ProductAttributeValue, on_delete = models.DO_NOTHING, primary_key=True)
    product_template_attribute_line = models.ForeignKey(related_name='+',to = 'ProductTemplateAttributeLine', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_value_product_template_attribute_line_rel'
        unique_together = (('product_attribute_value', 'product_template_attribute_line'),)


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    complete_name = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    parent_path = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    removal_strategy = models.ForeignKey(related_name='+',to = 'ProductRemoval', on_delete = models.DO_NOTHING, blank=True, null=True)
    packaging_reserve_method = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductConfiguratorCustomAttributeValueRel(models.Model):
    sale_product_configurator = models.OneToOneField('SaleProductConfigurator', on_delete = models.DO_NOTHING, primary_key=True)
    product_attribute_custom_value = models.ForeignKey(related_name='+',to = ProductAttributeCustomValue, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_configurator_custom_attribute_value_rel'
        unique_together = (('sale_product_configurator', 'product_attribute_custom_value'),)


class ProductConfiguratorNoVariantAttributeValueRel(models.Model):
    sale_product_configurator = models.OneToOneField('SaleProductConfigurator', on_delete = models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey(related_name='+',to = 'ProductTemplateAttributeValue', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_configurator_no_variant_attribute_value_rel'
        unique_together = (('sale_product_configurator', 'product_template_attribute_value'),)


class ProductConfiguratorTemplateAttributeValueRel(models.Model):
    sale_product_configurator = models.OneToOneField('SaleProductConfigurator', on_delete = models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey(related_name='+',to = 'ProductTemplateAttributeValue', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_configurator_template_attribute_value_rel'
        unique_together = (('sale_product_configurator', 'product_template_attribute_value'),)


class ProductFetchImageWizard(models.Model):
    nb_products_selected = models.IntegerField(blank=True, null=True)
    nb_products_to_process = models.IntegerField(blank=True, null=True)
    nb_products_unable_to_process = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_fetch_image_wizard'


class ProductFetchImageWizardProductProductRel(models.Model):
    product_fetch_image_wizard = models.OneToOneField(ProductFetchImageWizard, on_delete = models.DO_NOTHING, primary_key=True)
    product_product = models.ForeignKey(related_name='+',to = 'ProductProduct', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_fetch_image_wizard_product_product_rel'
        unique_together = (('product_fetch_image_wizard', 'product_product'),)


class ProductLabelLayout(models.Model):
    print_format = models.CharField(max_length=255)
    custom_quantity = models.IntegerField()
    extra_html = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    picking_quantity = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product_label_layout'


class ProductLabelLayoutProductProductRel(models.Model):
    product_label_layout = models.OneToOneField(ProductLabelLayout, on_delete = models.DO_NOTHING, primary_key=True)
    product_product = models.ForeignKey(related_name='+',to = 'ProductProduct', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_label_layout_product_product_rel'
        unique_together = (('product_label_layout', 'product_product'),)


class ProductLabelLayoutProductTemplateRel(models.Model):
    product_label_layout = models.OneToOneField(ProductLabelLayout, on_delete = models.DO_NOTHING, primary_key=True)
    product_template = models.ForeignKey(related_name='+',to = 'ProductTemplate', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_label_layout_product_template_rel'
        unique_together = (('product_label_layout', 'product_template'),)


class ProductLabelLayoutStockMoveLineRel(models.Model):
    product_label_layout = models.OneToOneField(ProductLabelLayout, on_delete = models.DO_NOTHING, primary_key=True)
    stock_move_line = models.ForeignKey(related_name='+',to = 'StockMoveLine', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_label_layout_stock_move_line_rel'
        unique_together = (('product_label_layout', 'stock_move_line'),)


class ProductMargin(models.Model):
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    invoice_state = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_margin'


class ProductOptionalRel(models.Model):
    src = models.OneToOneField('ProductTemplate', on_delete = models.DO_NOTHING, primary_key=True)
    dest = models.ForeignKey(related_name='+',to = 'ProductTemplate', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_optional_rel'
        unique_together = (('src', 'dest'),)


class ProductPackaging(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = 'ProductProduct', on_delete = models.DO_NOTHING, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sales = models.BooleanField(blank=True, null=True)
    package_type = models.ForeignKey(related_name='+',to = 'StockPackageType', on_delete = models.DO_NOTHING, blank=True, null=True)
    purchase = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_packaging'


class ProductPricelist(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    discount_policy = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist'


class ProductPricelistItem(models.Model):
    product_tmpl = models.ForeignKey(related_name='+',to = 'ProductTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = 'ProductProduct', on_delete = models.DO_NOTHING, blank=True, null=True)
    categ = models.ForeignKey(related_name='+',to = ProductCategory, on_delete = models.DO_NOTHING, blank=True, null=True)
    min_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    applied_on = models.CharField(max_length=255)
    base = models.CharField(max_length=255)
    base_pricelist = models.ForeignKey(related_name='+',to = ProductPricelist, on_delete = models.DO_NOTHING, blank=True, null=True)
    pricelist = models.ForeignKey(related_name='+',to = ProductPricelist, on_delete = models.DO_NOTHING)
    price_surcharge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_round = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_min_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_max_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    compute_price = models.CharField(max_length=255)
    fixed_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    percent_price = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist_item'


class ProductProduct(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    default_code = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    product_tmpl = models.ForeignKey(related_name='+',to = 'ProductTemplate', on_delete = models.DO_NOTHING)
    barcode = models.CharField(unique=True, max_length=255, blank=True, null=True)
    combination_indices = models.CharField(max_length=255, blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    can_image_variant_1024_be_zoomed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    image_fetch_pending = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_product'
        unique_together = (('product_tmpl', 'combination_indices'),)


class ProductProductStockTrackConfirmationRel(models.Model):
    stock_track_confirmation = models.OneToOneField('StockTrackConfirmation', on_delete = models.DO_NOTHING, primary_key=True)
    product_product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_product_stock_track_confirmation_rel'
        unique_together = (('stock_track_confirmation', 'product_product'),)


class ProductRemoval(models.Model):
    name = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_removal'


class ProductReplenish(models.Model):
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    product_tmpl = models.ForeignKey(related_name='+',to = 'ProductTemplate', on_delete = models.DO_NOTHING)
    product_has_variants = models.BooleanField()
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING)
    quantity = models.FloatField()
    date_planned = models.DateTimeField()
    warehouse = models.ForeignKey(related_name='+',to = 'StockWarehouse', on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_replenish'


class ProductReplenishStockLocationRouteRel(models.Model):
    product_replenish = models.OneToOneField(ProductReplenish, on_delete = models.DO_NOTHING, primary_key=True)
    stock_location_route = models.ForeignKey(related_name='+',to = 'StockLocationRoute', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_replenish_stock_location_route_rel'
        unique_together = (('product_replenish', 'stock_location_route'),)


class ProductSupplierTaxesRel(models.Model):
    prod = models.OneToOneField('ProductTemplate', on_delete = models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_supplier_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductSupplierinfo(models.Model):
    name = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, db_column='name')
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_code = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    product_tmpl = models.ForeignKey(related_name='+',to = 'ProductTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    delay = models.IntegerField()
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_supplierinfo'


class ProductSupplierinfoStockReplenishmentInfoRel(models.Model):
    stock_replenishment_info = models.OneToOneField('StockReplenishmentInfo', on_delete = models.DO_NOTHING, primary_key=True)
    product_supplierinfo = models.ForeignKey(related_name='+',to = ProductSupplierinfo, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_supplierinfo_stock_replenishment_info_rel'
        unique_together = (('stock_replenishment_info', 'product_supplierinfo'),)


class ProductTaxesRel(models.Model):
    prod = models.OneToOneField('ProductTemplate', on_delete = models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductTemplate(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_purchase = models.TextField(blank=True, null=True)
    description_sale = models.TextField(blank=True, null=True)
    detailed_type = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    categ = models.ForeignKey(related_name='+',to = ProductCategory, on_delete = models.DO_NOTHING)
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sale_ok = models.BooleanField(blank=True, null=True)
    purchase_ok = models.BooleanField(blank=True, null=True)
    uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING)
    uom_po = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    default_code = models.CharField(max_length=255, blank=True, null=True)
    can_image_1024_be_zoomed = models.BooleanField(blank=True, null=True)
    has_configurable_attributes = models.BooleanField(blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    service_type = models.CharField(max_length=255, blank=True, null=True)
    sale_line_warn = models.CharField(max_length=255)
    sale_line_warn_msg = models.TextField(blank=True, null=True)
    expense_policy = models.CharField(max_length=255, blank=True, null=True)
    invoice_policy = models.CharField(max_length=255, blank=True, null=True)
    sale_delay = models.FloatField(blank=True, null=True)
    tracking = models.CharField(max_length=255)
    description_picking = models.TextField(blank=True, null=True)
    description_pickingout = models.TextField(blank=True, null=True)
    description_pickingin = models.TextField(blank=True, null=True)
    can_be_expensed = models.BooleanField(blank=True, null=True)
    service_tracking = models.CharField(max_length=255, blank=True, null=True)
    use_expiration_date = models.BooleanField(blank=True, null=True)
    expiration_time = models.IntegerField(blank=True, null=True)
    use_time = models.IntegerField(blank=True, null=True)
    removal_time = models.IntegerField(blank=True, null=True)
    alert_time = models.IntegerField(blank=True, null=True)
    purchase_method = models.CharField(max_length=255, blank=True, null=True)
    purchase_line_warn = models.CharField(max_length=255)
    purchase_line_warn_msg = models.TextField(blank=True, null=True)
    service_to_purchase = models.BooleanField(blank=True, null=True)
    landed_cost_ok = models.BooleanField(blank=True, null=True)
    split_method_landed_cost = models.CharField(max_length=255, blank=True, null=True)
    product_add_mode = models.CharField(max_length=255, blank=True, null=True)
    service_upsell_threshold = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template'


class ProductTemplateAttributeExclusion(models.Model):
    product_template_attribute_value = models.ForeignKey(related_name='+',to = 'ProductTemplateAttributeValue', on_delete = models.DO_NOTHING, blank=True, null=True)
    product_tmpl = models.ForeignKey(related_name='+',to = ProductTemplate, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_exclusion'


class ProductTemplateAttributeLine(models.Model):
    active = models.BooleanField(blank=True, null=True)
    product_tmpl = models.ForeignKey(related_name='+',to = ProductTemplate, on_delete = models.DO_NOTHING)
    attribute = models.ForeignKey(related_name='+',to = ProductAttribute, on_delete = models.DO_NOTHING)
    value_count = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_line'


class ProductTemplateAttributeValue(models.Model):
    ptav_active = models.BooleanField(blank=True, null=True)
    product_attribute_value = models.ForeignKey(related_name='+',to = ProductAttributeValue, on_delete = models.DO_NOTHING)
    attribute_line = models.ForeignKey(related_name='+',to = ProductTemplateAttributeLine, on_delete = models.DO_NOTHING)
    price_extra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_tmpl = models.ForeignKey(related_name='+',to = ProductTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    attribute = models.ForeignKey(related_name='+',to = ProductAttribute, on_delete = models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_value'
        unique_together = (('attribute_line', 'product_attribute_value'),)


class ProductTemplateAttributeValueSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine', on_delete = models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey(related_name='+',to = ProductTemplateAttributeValue, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_value_sale_order_line_rel'
        unique_together = (('sale_order_line', 'product_template_attribute_value'),)


class ProductVariantCombination(models.Model):
    product_product = models.OneToOneField(ProductProduct, on_delete = models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey(related_name='+',to = ProductTemplateAttributeValue, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_variant_combination'
        unique_together = (('product_product', 'product_template_attribute_value'),)


class ProjectCollaborator(models.Model):
    project = models.ForeignKey(related_name='+',to = 'ProjectProject', on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_collaborator'
        unique_together = (('project', 'partner'),)


class ProjectCreateInvoice(models.Model):
    project = models.ForeignKey(related_name='+',to = 'ProjectProject', on_delete = models.DO_NOTHING)
    sale_order = models.ForeignKey(related_name='+',to = 'SaleOrder', on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_create_invoice'


class ProjectCreateSaleOrder(models.Model):
    project = models.ForeignKey(related_name='+',to = 'ProjectProject', on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    sale_order = models.ForeignKey(related_name='+',to = 'SaleOrder', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_create_sale_order'


class ProjectCreateSaleOrderLine(models.Model):
    wizard = models.ForeignKey(related_name='+',to = ProjectCreateSaleOrder, on_delete = models.DO_NOTHING)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    price_unit = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_create_sale_order_line'
        unique_together = (('wizard', 'employee'),)


class ProjectDeleteWizard(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_delete_wizard'


class ProjectDeleteWizardProjectProjectRel(models.Model):
    project_delete_wizard = models.OneToOneField(ProjectDeleteWizard, on_delete = models.DO_NOTHING, primary_key=True)
    project_project = models.ForeignKey(related_name='+',to = 'ProjectProject', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_delete_wizard_project_project_rel'
        unique_together = (('project_delete_wizard', 'project_project'),)


class ProjectFavoriteUserRel(models.Model):
    project = models.OneToOneField('ProjectProject', on_delete = models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_favorite_user_rel'
        unique_together = (('project', 'user'),)


class ProjectMilestone(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    project = models.ForeignKey(related_name='+',to = 'ProjectProject', on_delete = models.DO_NOTHING)
    deadline = models.DateField(blank=True, null=True)
    is_reached = models.BooleanField(blank=True, null=True)
    reached_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_milestone'


class ProjectProject(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    alias = models.ForeignKey(related_name='+',to = MailAlias, on_delete = models.DO_NOTHING)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner_email = models.CharField(max_length=255, blank=True, null=True)
    partner_phone = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    analytic_account = models.ForeignKey(related_name='+',to = AccountAnalyticAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    label_tasks = models.CharField(max_length=255, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    privacy_visibility = models.CharField(max_length=255)
    date_start = models.DateField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    allow_subtasks = models.BooleanField(blank=True, null=True)
    allow_recurring_tasks = models.BooleanField(blank=True, null=True)
    allow_task_dependencies = models.BooleanField(blank=True, null=True)
    rating_request_deadline = models.DateTimeField(blank=True, null=True)
    rating_active = models.BooleanField(blank=True, null=True)
    rating_status = models.CharField(max_length=255)
    rating_status_period = models.CharField(max_length=255)
    stage = models.ForeignKey(related_name='+',to = 'ProjectProjectStage', on_delete = models.DO_NOTHING, blank=True, null=True)
    last_update = models.ForeignKey(related_name='+',to = 'ProjectUpdate', on_delete = models.DO_NOTHING, blank=True, null=True)
    last_update_status = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_line = models.ForeignKey(related_name='+',to = 'SaleOrderLine', on_delete = models.DO_NOTHING, blank=True, null=True)
    allow_timesheets = models.BooleanField(blank=True, null=True)
    allow_billable = models.BooleanField(blank=True, null=True)
    timesheet_product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_project'


class ProjectProjectProjectTagsRel(models.Model):
    project_project = models.OneToOneField(ProjectProject, on_delete = models.DO_NOTHING, primary_key=True)
    project_tags = models.ForeignKey(related_name='+',to = 'ProjectTags', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_project_project_tags_rel'
        unique_together = (('project_project', 'project_tags'),)


class ProjectProjectProjectTaskTypeDeleteWizardRel(models.Model):
    project_task_type_delete_wizard = models.OneToOneField('ProjectTaskTypeDeleteWizard', on_delete = models.DO_NOTHING, primary_key=True)
    project_project = models.ForeignKey(related_name='+',to = ProjectProject, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_project_project_task_type_delete_wizard_rel'
        unique_together = (('project_task_type_delete_wizard', 'project_project'),)


class ProjectProjectStage(models.Model):
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    mail_template = models.ForeignKey(related_name='+',to = MailTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_project_stage'


class ProjectSaleLineEmployeeMap(models.Model):
    project = models.ForeignKey(related_name='+',to = ProjectProject, on_delete = models.DO_NOTHING)
    employee = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING)
    sale_line = models.ForeignKey(related_name='+',to = 'SaleOrderLine', on_delete = models.DO_NOTHING, blank=True, null=True)
    price_unit = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_cost_changed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_sale_line_employee_map'
        unique_together = (('project', 'employee'),)


class ProjectSalesCallLogs(models.Model):
    client_id = models.CharField(max_length=255, blank=True, null=True)
    sale_agent_id = models.CharField(max_length=255, blank=True, null=True)
    already_assign_agent_id = models.CharField(max_length=255, blank=True, null=True)
    crm_lead_id = models.CharField(max_length=255, blank=True, null=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)
    client_number = models.CharField(max_length=255, blank=True, null=True)
    sale_agent_name = models.CharField(max_length=255, blank=True, null=True)
    sale_agent_number = models.CharField(max_length=255, blank=True, null=True)
    call_duration = models.CharField(max_length=255, blank=True, null=True)
    call_type = models.CharField(max_length=255, blank=True, null=True)
    call_time = models.CharField(max_length=255, blank=True, null=True)
    call_date = models.CharField(max_length=255, blank=True, null=True)
    qualified_call = models.CharField(max_length=255, blank=True, null=True)
    verified_call = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_sales_call_logs'


class ProjectShareWizard(models.Model):
    res_model = models.CharField(max_length=255)
    res_id = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    access_mode = models.CharField(max_length=255, blank=True, null=True)
    display_access_mode = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_share_wizard'


class ProjectShareWizardResPartnerRel(models.Model):
    project_share_wizard = models.OneToOneField(ProjectShareWizard, on_delete = models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_share_wizard_res_partner_rel'
        unique_together = (('project_share_wizard', 'res_partner'),)


class ProjectTags(models.Model):
    name = models.CharField(unique=True, max_length=255)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_tags'


class ProjectTagsProjectTaskRel(models.Model):
    project_task = models.OneToOneField('ProjectTask', on_delete = models.DO_NOTHING, primary_key=True)
    project_tags = models.ForeignKey(related_name='+',to = ProjectTags, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_tags_project_task_rel'
        unique_together = (('project_task', 'project_tags'),)


class ProjectTask(models.Model):
    rating_last_value = models.FloatField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    email_cc = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    stage = models.ForeignKey(related_name='+',to = 'ProjectTaskType', on_delete = models.DO_NOTHING, blank=True, null=True)
    kanban_state = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_assign = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(related_name='+',to = ProjectProject, on_delete = models.DO_NOTHING, blank=True, null=True)
    display_project = models.ForeignKey(related_name='+',to = ProjectProject, on_delete = models.DO_NOTHING, blank=True, null=True)
    planned_hours = models.FloatField(blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner_email = models.CharField(max_length=255, blank=True, null=True)
    partner_phone = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    color = models.IntegerField(blank=True, null=True)
    displayed_image = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    email_from = models.CharField(max_length=255, blank=True, null=True)
    working_hours_open = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    working_hours_close = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    working_days_open = models.FloatField(blank=True, null=True)
    working_days_close = models.FloatField(blank=True, null=True)
    recurring_task = models.BooleanField(blank=True, null=True)
    recurrence = models.ForeignKey(related_name='+',to = 'ProjectTaskRecurrence', on_delete = models.DO_NOTHING, blank=True, null=True)
    analytic_account = models.ForeignKey(related_name='+',to = AccountAnalyticAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    sale_order = models.ForeignKey(related_name='+',to = 'SaleOrder', on_delete = models.DO_NOTHING, blank=True, null=True)
    sale_line = models.ForeignKey(related_name='+',to = 'SaleOrderLine', on_delete = models.DO_NOTHING, blank=True, null=True)
    remaining_hours = models.FloatField(blank=True, null=True)
    effective_hours = models.FloatField(blank=True, null=True)
    total_hours_spent = models.FloatField(blank=True, null=True)
    progress = models.FloatField(blank=True, null=True)
    overtime = models.FloatField(blank=True, null=True)
    subtask_effective_hours = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task'


class ProjectTaskCreateTimesheet(models.Model):
    time_spent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    task = models.ForeignKey(related_name='+',to = ProjectTask, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_create_timesheet'


class ProjectTaskRecurrence(models.Model):
    next_recurrence_date = models.DateField(blank=True, null=True)
    recurrence_left = models.IntegerField(blank=True, null=True)
    repeat_interval = models.IntegerField(blank=True, null=True)
    repeat_unit = models.CharField(max_length=255, blank=True, null=True)
    repeat_type = models.CharField(max_length=255, blank=True, null=True)
    repeat_until = models.DateField(blank=True, null=True)
    repeat_number = models.IntegerField(blank=True, null=True)
    repeat_on_month = models.CharField(max_length=255, blank=True, null=True)
    repeat_on_year = models.CharField(max_length=255, blank=True, null=True)
    mon = models.BooleanField(blank=True, null=True)
    tue = models.BooleanField(blank=True, null=True)
    wed = models.BooleanField(blank=True, null=True)
    thu = models.BooleanField(blank=True, null=True)
    fri = models.BooleanField(blank=True, null=True)
    sat = models.BooleanField(blank=True, null=True)
    sun = models.BooleanField(blank=True, null=True)
    repeat_day = models.CharField(max_length=255, blank=True, null=True)
    repeat_week = models.CharField(max_length=255, blank=True, null=True)
    repeat_weekday = models.CharField(max_length=255, blank=True, null=True)
    repeat_month = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_recurrence'


class ProjectTaskType(models.Model):
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    legend_blocked = models.CharField(max_length=255)
    legend_done = models.CharField(max_length=255)
    legend_normal = models.CharField(max_length=255)
    mail_template = models.ForeignKey(related_name='+',to = MailTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    rating_template = models.ForeignKey(related_name='+',to = MailTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    auto_validation_kanban_state = models.BooleanField(blank=True, null=True)
    is_closed = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_type'


class ProjectTaskTypeDeleteWizard(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_type_delete_wizard'


class ProjectTaskTypeProjectTaskTypeDeleteWizardRel(models.Model):
    project_task_type_delete_wizard = models.OneToOneField(ProjectTaskTypeDeleteWizard, on_delete = models.DO_NOTHING, primary_key=True)
    project_task_type = models.ForeignKey(related_name='+',to = ProjectTaskType, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_task_type_project_task_type_delete_wizard_rel'
        unique_together = (('project_task_type_delete_wizard', 'project_task_type'),)


class ProjectTaskTypeRel(models.Model):
    type = models.OneToOneField(ProjectTaskType, on_delete = models.DO_NOTHING, primary_key=True)
    project = models.ForeignKey(related_name='+',to = ProjectProject, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_task_type_rel'
        unique_together = (('type', 'project'),)


class ProjectTaskUserRel(models.Model):
    task = models.ForeignKey(related_name='+',to = ProjectTask, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    stage = models.ForeignKey(related_name='+',to = ProjectTaskType, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_user_rel'
        unique_together = (('task', 'user'),)


class ProjectUpdate(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    email_cc = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    progress = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    project = models.ForeignKey(related_name='+',to = ProjectProject, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_update'


class PurchaseOrder(models.Model):
    access_token = models.CharField(max_length=255, blank=True, null=True)
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    priority = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=255, blank=True, null=True)
    partner_ref = models.CharField(max_length=255, blank=True, null=True)
    date_order = models.DateTimeField()
    date_approve = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    dest_address = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING)
    state = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    invoice_count = models.IntegerField(blank=True, null=True)
    invoice_status = models.CharField(max_length=255, blank=True, null=True)
    date_planned = models.DateTimeField(blank=True, null=True)
    date_calendar_start = models.DateTimeField(blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fiscal_position = models.ForeignKey(related_name='+',to = AccountFiscalPosition, on_delete = models.DO_NOTHING, blank=True, null=True)
    payment_term = models.ForeignKey(related_name='+',to = AccountPaymentTerm, on_delete = models.DO_NOTHING, blank=True, null=True)
    incoterm = models.ForeignKey(related_name='+',to = AccountIncoterms, on_delete = models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING)
    currency_rate = models.FloatField(blank=True, null=True)
    mail_reminder_confirmed = models.BooleanField(blank=True, null=True)
    mail_reception_confirmed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    picking_type = models.ForeignKey(related_name='+',to = 'StockPickingType', on_delete = models.DO_NOTHING)
    group = models.ForeignKey(related_name='+',to = ProcurementGroup, on_delete = models.DO_NOTHING, blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order'


class PurchaseOrderLine(models.Model):
    name = models.TextField()
    sequence = models.IntegerField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom_qty = models.FloatField(blank=True, null=True)
    date_planned = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING, db_column='product_uom', blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_tax = models.FloatField(blank=True, null=True)
    order = models.ForeignKey(related_name='+',to = PurchaseOrder, on_delete = models.DO_NOTHING)
    account_analytic = models.ForeignKey(related_name='+',to = AccountAnalyticAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = 'ResCompany', on_delete = models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    qty_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_received_method = models.CharField(max_length=255, blank=True, null=True)
    qty_received = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_received_manual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    product_packaging = models.ForeignKey(related_name='+',to = ProductPackaging, on_delete = models.DO_NOTHING, blank=True, null=True)
    product_packaging_qty = models.FloatField(blank=True, null=True)
    display_type = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    orderpoint = models.ForeignKey(related_name='+',to = 'StockWarehouseOrderpoint', on_delete = models.DO_NOTHING, blank=True, null=True)
    product_description_variants = models.CharField(max_length=255, blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    sale_order = models.ForeignKey(related_name='+',to = 'SaleOrder', on_delete = models.DO_NOTHING, blank=True, null=True)
    sale_line = models.ForeignKey(related_name='+',to = 'SaleOrderLine', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_line'


class PurchaseOrderStockPickingRel(models.Model):
    purchase_order = models.OneToOneField(PurchaseOrder, on_delete = models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(related_name='+',to = 'StockPicking', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'purchase_order_stock_picking_rel'
        unique_together = (('purchase_order', 'stock_picking'),)


class RatingRating(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    res_name = models.CharField(max_length=255, blank=True, null=True)
    res_model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING, blank=True, null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    res_id = models.IntegerField()
    parent_res_name = models.CharField(max_length=255, blank=True, null=True)
    parent_res_model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING, blank=True, null=True)
    parent_res_model_0 = models.CharField(db_column='parent_res_model', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    parent_res_id = models.IntegerField(blank=True, null=True)
    rated_partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    rating_text = models.CharField(max_length=255, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    message = models.ForeignKey(related_name='+',to = MailMessage, on_delete = models.DO_NOTHING, blank=True, null=True)
    is_internal = models.BooleanField(blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    consumed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    publisher_comment = models.TextField(blank=True, null=True)
    publisher = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING, blank=True, null=True)
    publisher_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating_rating'


class RelModulesLangexport(models.Model):
    wiz = models.OneToOneField(BaseLanguageExport, on_delete = models.DO_NOTHING, primary_key=True)
    module = models.ForeignKey(related_name='+',to = IrModuleModule, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_modules_langexport'
        unique_together = (('wiz', 'module'),)


class RelServerActions(models.Model):
    server = models.OneToOneField(IrActServer, on_delete = models.DO_NOTHING, primary_key=True)
    action = models.ForeignKey(related_name='+',to = IrActServer, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_server_actions'
        unique_together = (('server', 'action'),)


class ReportLayout(models.Model):
    view = models.ForeignKey(related_name='+',to = IrUiView, on_delete = models.DO_NOTHING)
    image = models.CharField(max_length=255, blank=True, null=True)
    pdf = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_layout'


class ReportPaperformat(models.Model):
    name = models.CharField(max_length=255)
    default = models.BooleanField(blank=True, null=True)
    format = models.CharField(max_length=255, blank=True, null=True)
    margin_top = models.FloatField(blank=True, null=True)
    margin_bottom = models.FloatField(blank=True, null=True)
    margin_left = models.FloatField(blank=True, null=True)
    margin_right = models.FloatField(blank=True, null=True)
    page_height = models.IntegerField(blank=True, null=True)
    page_width = models.IntegerField(blank=True, null=True)
    orientation = models.CharField(max_length=255, blank=True, null=True)
    header_line = models.BooleanField(blank=True, null=True)
    header_spacing = models.IntegerField(blank=True, null=True)
    disable_shrinking = models.BooleanField(blank=True, null=True)
    dpi = models.IntegerField()
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_paperformat'


class ResBank(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey(related_name='+',to = 'ResCountryState', on_delete = models.DO_NOTHING, db_column='state', blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, db_column='country', blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    bic = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_bank'


class ResCompany(models.Model):
    name = models.CharField(unique=True, max_length=255)
    partner = models.ForeignKey(related_name='+',to = 'ResPartner', on_delete = models.DO_NOTHING)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    report_header = models.TextField(blank=True, null=True)
    report_footer = models.TextField(blank=True, null=True)
    company_details = models.TextField(blank=True, null=True)
    logo_web = models.BinaryField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    company_registry = models.CharField(max_length=255, blank=True, null=True)
    paperformat = models.ForeignKey(related_name='+',to = ReportPaperformat, on_delete = models.DO_NOTHING, blank=True, null=True)
    external_report_layout = models.ForeignKey(related_name='+',to = IrUiView, on_delete = models.DO_NOTHING, blank=True, null=True)
    base_onboarding_company_state = models.CharField(max_length=255, blank=True, null=True)
    font = models.CharField(max_length=255, blank=True, null=True)
    primary_color = models.CharField(max_length=255, blank=True, null=True)
    secondary_color = models.CharField(max_length=255, blank=True, null=True)
    layout_background = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    resource_calendar = models.ForeignKey(related_name='+',to = 'ResourceCalendar', on_delete = models.DO_NOTHING, blank=True, null=True)
    snailmail_color = models.BooleanField(blank=True, null=True)
    snailmail_cover = models.BooleanField(blank=True, null=True)
    snailmail_duplex = models.BooleanField(blank=True, null=True)
    fiscalyear_last_day = models.IntegerField()
    fiscalyear_last_month = models.CharField(max_length=255)
    period_lock_date = models.DateField(blank=True, null=True)
    fiscalyear_lock_date = models.DateField(blank=True, null=True)
    tax_lock_date = models.DateField(blank=True, null=True)
    transfer_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    expects_chart_of_accounts = models.BooleanField(blank=True, null=True)
    chart_template = models.ForeignKey(related_name='+',to = AccountChartTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    bank_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    default_cash_difference_income_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    default_cash_difference_expense_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_journal_suspense_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_journal_payment_debit_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_journal_payment_credit_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    transfer_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    account_sale_tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_purchase_tax = models.ForeignKey(related_name='+',to = AccountTax, on_delete = models.DO_NOTHING, blank=True, null=True)
    tax_calculation_rounding_method = models.CharField(max_length=255, blank=True, null=True)
    currency_exchange_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    income_currency_exchange_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    anglo_saxon_accounting = models.BooleanField(blank=True, null=True)
    property_stock_account_input_categ = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    incoterm = models.ForeignKey(related_name='+',to = AccountIncoterms, on_delete = models.DO_NOTHING, blank=True, null=True)
    qr_code = models.BooleanField(blank=True, null=True)
    invoice_is_email = models.BooleanField(blank=True, null=True)
    invoice_is_print = models.BooleanField(blank=True, null=True)
    account_opening_move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_opening_date = models.DateField()
    account_setup_bank_data_state = models.CharField(max_length=255, blank=True, null=True)
    account_setup_fy_data_state = models.CharField(max_length=255, blank=True, null=True)
    account_setup_coa_state = models.CharField(max_length=255, blank=True, null=True)
    account_setup_taxes_state = models.CharField(max_length=255, blank=True, null=True)
    account_onboarding_invoice_layout_state = models.CharField(max_length=255, blank=True, null=True)
    account_onboarding_create_invoice_state = models.CharField(max_length=255, blank=True, null=True)
    account_onboarding_sale_tax_state = models.CharField(max_length=255, blank=True, null=True)
    account_invoice_onboarding_state = models.CharField(max_length=255, blank=True, null=True)
    account_dashboard_onboarding_state = models.CharField(max_length=255, blank=True, null=True)
    invoice_terms = models.TextField(blank=True, null=True)
    terms_type = models.CharField(max_length=255, blank=True, null=True)
    invoice_terms_html = models.TextField(blank=True, null=True)
    account_setup_bill_state = models.CharField(max_length=255, blank=True, null=True)
    account_default_pos_receivable_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    expense_accrual_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    revenue_accrual_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    automatic_entry_default_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_fiscal_country = models.ForeignKey(related_name='+',to = 'ResCountry', on_delete = models.DO_NOTHING, blank=True, null=True)
    tax_exigibility = models.BooleanField(blank=True, null=True)
    tax_cash_basis_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_cash_basis_base_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    payment_acquirer_onboarding_state = models.CharField(max_length=255, blank=True, null=True)
    payment_onboarding_payment_method = models.CharField(max_length=255, blank=True, null=True)
    invoice_is_snailmail = models.BooleanField(blank=True, null=True)
    portal_confirmation_sign = models.BooleanField(blank=True, null=True)
    portal_confirmation_pay = models.BooleanField(blank=True, null=True)
    quotation_validity_days = models.IntegerField(blank=True, null=True)
    sale_quotation_onboarding_state = models.CharField(max_length=255, blank=True, null=True)
    sale_onboarding_order_confirmation_state = models.CharField(max_length=255, blank=True, null=True)
    sale_onboarding_sample_quotation_state = models.CharField(max_length=255, blank=True, null=True)
    sale_onboarding_payment_method = models.CharField(max_length=255, blank=True, null=True)
    sale_order_template = models.ForeignKey(related_name='+',to = 'SaleOrderTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    nomenclature = models.ForeignKey(related_name='+',to = BarcodeNomenclature, on_delete = models.DO_NOTHING, blank=True, null=True)
    internal_transit_location = models.ForeignKey(related_name='+',to = 'StockLocation', on_delete = models.DO_NOTHING, blank=True, null=True)
    stock_move_email_validation = models.BooleanField(blank=True, null=True)
    stock_mail_confirmation_template = models.ForeignKey(related_name='+',to = MailTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    annual_inventory_month = models.CharField(max_length=255, blank=True, null=True)
    annual_inventory_day = models.IntegerField(blank=True, null=True)
    stock_move_sms_validation = models.BooleanField(blank=True, null=True)
    stock_sms_confirmation_template = models.ForeignKey(related_name='+',to = 'SmsTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    has_received_warning_stock_sms = models.BooleanField(blank=True, null=True)
    security_lead = models.FloatField()
    hr_presence_control_email_amount = models.IntegerField(blank=True, null=True)
    hr_presence_control_ip_list = models.CharField(max_length=255, blank=True, null=True)
    social_twitter = models.CharField(max_length=255, blank=True, null=True)
    social_facebook = models.CharField(max_length=255, blank=True, null=True)
    social_github = models.CharField(max_length=255, blank=True, null=True)
    social_linkedin = models.CharField(max_length=255, blank=True, null=True)
    social_youtube = models.CharField(max_length=255, blank=True, null=True)
    social_instagram = models.CharField(max_length=255, blank=True, null=True)
    hr_presence_last_compute_date = models.DateTimeField(blank=True, null=True)
    project_time_mode = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING, blank=True, null=True)
    timesheet_encode_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING, blank=True, null=True)
    internal_project = models.ForeignKey(related_name='+',to = ProjectProject, on_delete = models.DO_NOTHING, blank=True, null=True)
    po_lead = models.FloatField()
    po_lock = models.CharField(max_length=255, blank=True, null=True)
    po_double_validation = models.CharField(max_length=255, blank=True, null=True)
    po_double_validation_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    leave_timesheet_task = models.ForeignKey(related_name='+',to = ProjectTask, on_delete = models.DO_NOTHING, blank=True, null=True)
    days_to_purchase = models.FloatField(blank=True, null=True)
    lc_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    hr_attendance_overtime = models.BooleanField(blank=True, null=True)
    overtime_start_date = models.DateField(blank=True, null=True)
    overtime_company_threshold = models.IntegerField(blank=True, null=True)
    overtime_employee_threshold = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_company'


class ResCompanyUsersRel(models.Model):
    cid = models.OneToOneField(ResCompany, on_delete = models.DO_NOTHING, db_column='cid', primary_key=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_company_users_rel'
        unique_together = (('cid', 'user'),)


class ResConfig(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config'


class ResConfigInstaller(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_installer'


class ResConfigSettings(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    user_default_rights = models.BooleanField(blank=True, null=True)
    external_email_server_default = models.BooleanField(blank=True, null=True)
    module_base_import = models.BooleanField(blank=True, null=True)
    module_google_calendar = models.BooleanField(blank=True, null=True)
    module_microsoft_calendar = models.BooleanField(blank=True, null=True)
    module_mail_plugin = models.BooleanField(blank=True, null=True)
    module_google_drive = models.BooleanField(blank=True, null=True)
    module_google_spreadsheet = models.BooleanField(blank=True, null=True)
    module_auth_oauth = models.BooleanField(blank=True, null=True)
    module_auth_ldap = models.BooleanField(blank=True, null=True)
    module_base_gengo = models.BooleanField(blank=True, null=True)
    module_account_inter_company_rules = models.BooleanField(blank=True, null=True)
    module_pad = models.BooleanField(blank=True, null=True)
    module_voip = models.BooleanField(blank=True, null=True)
    module_web_unsplash = models.BooleanField(blank=True, null=True)
    module_partner_autocomplete = models.BooleanField(blank=True, null=True)
    module_base_geolocalize = models.BooleanField(blank=True, null=True)
    module_google_recaptcha = models.BooleanField(blank=True, null=True)
    group_multi_currency = models.BooleanField(blank=True, null=True)
    show_effect = models.BooleanField(blank=True, null=True)
    profiling_enabled_until = models.DateTimeField(blank=True, null=True)
    module_product_images = models.BooleanField(blank=True, null=True)
    fail_counter = models.IntegerField(blank=True, null=True)
    alias_domain = models.CharField(max_length=255, blank=True, null=True)
    restrict_template_rendering = models.BooleanField(blank=True, null=True)
    use_twilio_rtc_servers = models.BooleanField(blank=True, null=True)
    twilio_account_sid = models.CharField(max_length=255, blank=True, null=True)
    twilio_account_token = models.CharField(max_length=255, blank=True, null=True)
    group_analytic_accounting = models.BooleanField(blank=True, null=True)
    auth_signup_reset_password = models.BooleanField(blank=True, null=True)
    auth_signup_uninvited = models.CharField(max_length=255, blank=True, null=True)
    auth_signup_template_user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    group_discount_per_so_line = models.BooleanField(blank=True, null=True)
    group_uom = models.BooleanField(blank=True, null=True)
    group_product_variant = models.BooleanField(blank=True, null=True)
    module_sale_product_configurator = models.BooleanField(blank=True, null=True)
    module_sale_product_matrix = models.BooleanField(blank=True, null=True)
    group_stock_packaging = models.BooleanField(blank=True, null=True)
    group_product_pricelist = models.BooleanField(blank=True, null=True)
    group_sale_pricelist = models.BooleanField(blank=True, null=True)
    product_pricelist_setting = models.CharField(max_length=255, blank=True, null=True)
    product_weight_in_lbs = models.CharField(max_length=255, blank=True, null=True)
    product_volume_volume_in_cubic_feet = models.CharField(max_length=255, blank=True, null=True)
    digest_emails = models.BooleanField(blank=True, null=True)
    digest = models.ForeignKey(related_name='+',to = DigestDigest, on_delete = models.DO_NOTHING, blank=True, null=True)
    chart_template = models.ForeignKey(related_name='+',to = AccountChartTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    module_account_accountant = models.BooleanField(blank=True, null=True)
    group_analytic_tags = models.BooleanField(blank=True, null=True)
    group_warning_account = models.BooleanField(blank=True, null=True)
    group_cash_rounding = models.BooleanField(blank=True, null=True)
    group_show_line_subtotals_tax_excluded = models.BooleanField(blank=True, null=True)
    group_show_line_subtotals_tax_included = models.BooleanField(blank=True, null=True)
    group_show_sale_receipts = models.BooleanField(blank=True, null=True)
    group_show_purchase_receipts = models.BooleanField(blank=True, null=True)
    show_line_subtotals_tax_selection = models.CharField(max_length=255)
    module_account_budget = models.BooleanField(blank=True, null=True)
    module_account_payment = models.BooleanField(blank=True, null=True)
    module_account_reports = models.BooleanField(blank=True, null=True)
    module_account_check_printing = models.BooleanField(blank=True, null=True)
    module_account_batch_payment = models.BooleanField(blank=True, null=True)
    module_account_sepa = models.BooleanField(blank=True, null=True)
    module_account_sepa_direct_debit = models.BooleanField(blank=True, null=True)
    module_l10n_fr_fec_import = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_qif = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_ofx = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_csv = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_camt = models.BooleanField(blank=True, null=True)
    module_currency_rate_live = models.BooleanField(blank=True, null=True)
    module_account_intrastat = models.BooleanField(blank=True, null=True)
    module_product_margin = models.BooleanField(blank=True, null=True)
    module_l10n_eu_oss = models.BooleanField(blank=True, null=True)
    module_account_taxcloud = models.BooleanField(blank=True, null=True)
    module_account_invoice_extract = models.BooleanField(blank=True, null=True)
    module_snailmail_account = models.BooleanField(blank=True, null=True)
    use_invoice_terms = models.BooleanField(blank=True, null=True)
    group_auto_done_setting = models.BooleanField(blank=True, null=True)
    module_sale_margin = models.BooleanField(blank=True, null=True)
    use_quotation_validity_days = models.BooleanField(blank=True, null=True)
    group_warning_sale = models.BooleanField(blank=True, null=True)
    group_sale_delivery_address = models.BooleanField(blank=True, null=True)
    group_proforma_sales = models.BooleanField(blank=True, null=True)
    default_invoice_policy = models.CharField(max_length=255, blank=True, null=True)
    deposit_default_product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    module_delivery = models.BooleanField(blank=True, null=True)
    module_delivery_dhl = models.BooleanField(blank=True, null=True)
    module_delivery_fedex = models.BooleanField(blank=True, null=True)
    module_delivery_ups = models.BooleanField(blank=True, null=True)
    module_delivery_usps = models.BooleanField(blank=True, null=True)
    module_delivery_bpost = models.BooleanField(blank=True, null=True)
    module_delivery_easypost = models.BooleanField(blank=True, null=True)
    module_product_email_template = models.BooleanField(blank=True, null=True)
    module_sale_coupon = models.BooleanField(blank=True, null=True)
    module_sale_amazon = models.BooleanField(blank=True, null=True)
    automatic_invoice = models.BooleanField(blank=True, null=True)
    invoice_mail_template = models.ForeignKey(related_name='+',to = MailTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    confirmation_mail_template = models.ForeignKey(related_name='+',to = MailTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    group_sale_order_template = models.BooleanField(blank=True, null=True)
    module_sale_quotation_builder = models.BooleanField(blank=True, null=True)
    group_use_lead = models.BooleanField(blank=True, null=True)
    group_use_recurring_revenues = models.BooleanField(blank=True, null=True)
    is_membership_multi = models.BooleanField(blank=True, null=True)
    crm_use_auto_assignment = models.BooleanField(blank=True, null=True)
    crm_auto_assignment_action = models.CharField(max_length=255, blank=True, null=True)
    crm_auto_assignment_interval_type = models.CharField(max_length=255, blank=True, null=True)
    crm_auto_assignment_interval_number = models.IntegerField(blank=True, null=True)
    crm_auto_assignment_run_datetime = models.DateTimeField(blank=True, null=True)
    module_crm_iap_mine = models.BooleanField(blank=True, null=True)
    module_crm_iap_enrich = models.BooleanField(blank=True, null=True)
    module_website_crm_iap_reveal = models.BooleanField(blank=True, null=True)
    lead_enrich_auto = models.CharField(max_length=255, blank=True, null=True)
    lead_mining_in_pipeline = models.BooleanField(blank=True, null=True)
    predictive_lead_scoring_start_date_str = models.CharField(max_length=255, blank=True, null=True)
    predictive_lead_scoring_fields_str = models.CharField(max_length=255, blank=True, null=True)
    module_product_expiry = models.BooleanField(blank=True, null=True)
    group_stock_production_lot = models.BooleanField(blank=True, null=True)
    group_lot_on_delivery_slip = models.BooleanField(blank=True, null=True)
    group_stock_tracking_lot = models.BooleanField(blank=True, null=True)
    group_stock_tracking_owner = models.BooleanField(blank=True, null=True)
    group_stock_adv_location = models.BooleanField(blank=True, null=True)
    group_warning_stock = models.BooleanField(blank=True, null=True)
    group_stock_sign_delivery = models.BooleanField(blank=True, null=True)
    module_stock_picking_batch = models.BooleanField(blank=True, null=True)
    group_stock_picking_wave = models.BooleanField(blank=True, null=True)
    module_stock_barcode = models.BooleanField(blank=True, null=True)
    module_stock_sms = models.BooleanField(blank=True, null=True)
    module_quality_control = models.BooleanField(blank=True, null=True)
    module_quality_control_worksheet = models.BooleanField(blank=True, null=True)
    group_stock_multi_locations = models.BooleanField(blank=True, null=True)
    group_stock_storage_categories = models.BooleanField(blank=True, null=True)
    group_stock_reception_report = models.BooleanField(blank=True, null=True)
    group_stock_auto_reception_report = models.BooleanField(blank=True, null=True)
    module_stock_landed_costs = models.BooleanField(blank=True, null=True)
    group_lot_on_invoice = models.BooleanField(blank=True, null=True)
    group_display_incoterm = models.BooleanField(blank=True, null=True)
    use_security_lead = models.BooleanField(blank=True, null=True)
    default_picking_policy = models.CharField(max_length=255)
    module_hr_presence = models.BooleanField(blank=True, null=True)
    module_hr_skills = models.BooleanField(blank=True, null=True)
    hr_presence_control_login = models.BooleanField(blank=True, null=True)
    hr_presence_control_email = models.BooleanField(blank=True, null=True)
    hr_presence_control_ip = models.BooleanField(blank=True, null=True)
    module_hr_attendance = models.BooleanField(blank=True, null=True)
    hr_employee_self_edit = models.BooleanField(blank=True, null=True)
    expense_alias_prefix = models.CharField(max_length=255, blank=True, null=True)
    use_mailgateway = models.BooleanField(blank=True, null=True)
    module_hr_payroll_expense = models.BooleanField(blank=True, null=True)
    module_hr_expense_extract = models.BooleanField(blank=True, null=True)
    module_project_forecast = models.BooleanField(blank=True, null=True)
    module_hr_timesheet = models.BooleanField(blank=True, null=True)
    group_subtask_project = models.BooleanField(blank=True, null=True)
    group_project_rating = models.BooleanField(blank=True, null=True)
    group_project_stages = models.BooleanField(blank=True, null=True)
    group_project_recurring_tasks = models.BooleanField(blank=True, null=True)
    group_project_task_dependencies = models.BooleanField(blank=True, null=True)
    geoloc_provider = models.ForeignKey(related_name='+',to = BaseGeoProvider, on_delete = models.DO_NOTHING, blank=True, null=True)
    geoloc_provider_googlemap_key = models.CharField(max_length=255, blank=True, null=True)
    google_drive_authorization_code = models.CharField(max_length=255, blank=True, null=True)
    is_google_drive_token_generated = models.BooleanField(blank=True, null=True)
    cal_client_id = models.CharField(max_length=255, blank=True, null=True)
    cal_client_secret = models.CharField(max_length=255, blank=True, null=True)
    cal_microsoft_client_id = models.CharField(max_length=255, blank=True, null=True)
    cal_microsoft_client_secret = models.CharField(max_length=255, blank=True, null=True)
    google_custom_search_key = models.CharField(max_length=255, blank=True, null=True)
    google_pse_id = models.CharField(max_length=255, blank=True, null=True)
    recaptcha_public_key = models.CharField(max_length=255, blank=True, null=True)
    recaptcha_private_key = models.CharField(max_length=255, blank=True, null=True)
    recaptcha_min_score = models.FloatField(blank=True, null=True)
    module_project_timesheet_synchro = models.BooleanField(blank=True, null=True)
    module_project_timesheet_holidays = models.BooleanField(blank=True, null=True)
    reminder_user_allow = models.BooleanField(blank=True, null=True)
    reminder_manager_allow = models.BooleanField(blank=True, null=True)
    group_expiry_date_on_delivery_slip = models.BooleanField(blank=True, null=True)
    lock_confirmed_po = models.BooleanField(blank=True, null=True)
    po_order_approval = models.BooleanField(blank=True, null=True)
    default_purchase_method = models.CharField(max_length=255, blank=True, null=True)
    group_warning_purchase = models.BooleanField(blank=True, null=True)
    module_account_3way_match = models.BooleanField(blank=True, null=True)
    module_purchase_requisition = models.BooleanField(blank=True, null=True)
    module_purchase_product_matrix = models.BooleanField(blank=True, null=True)
    use_po_lead = models.BooleanField(blank=True, null=True)
    group_send_reminder = models.BooleanField(blank=True, null=True)
    module_stock_dropshipping = models.BooleanField(blank=True, null=True)
    is_installed_sale = models.BooleanField(blank=True, null=True)
    invoice_policy = models.BooleanField(blank=True, null=True)
    group_attendance_use_pin = models.BooleanField(blank=True, null=True)
    hr_attendance_overtime = models.BooleanField(blank=True, null=True)
    overtime_start_date = models.DateField(blank=True, null=True)
    overtime_company_threshold = models.IntegerField(blank=True, null=True)
    overtime_employee_threshold = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_settings'


class ResCountry(models.Model):
    name = models.CharField(unique=True, max_length=255)
    code = models.CharField(unique=True, max_length=2, blank=True, null=True)
    address_format = models.TextField(blank=True, null=True)
    address_view = models.ForeignKey(related_name='+',to = IrUiView, on_delete = models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = 'ResCurrency', on_delete = models.DO_NOTHING, blank=True, null=True)
    phone_code = models.IntegerField(blank=True, null=True)
    name_position = models.CharField(max_length=255, blank=True, null=True)
    vat_label = models.CharField(max_length=255, blank=True, null=True)
    state_required = models.BooleanField(blank=True, null=True)
    zip_required = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country'


class ResCountryGroup(models.Model):
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_group'


class ResCountryGroupPricelistRel(models.Model):
    pricelist = models.OneToOneField(ProductPricelist, on_delete = models.DO_NOTHING, primary_key=True)
    res_country_group = models.ForeignKey(related_name='+',to = ResCountryGroup, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_group_pricelist_rel'
        unique_together = (('pricelist', 'res_country_group'),)


class ResCountryResCountryGroupRel(models.Model):
    res_country = models.OneToOneField(ResCountry, on_delete = models.DO_NOTHING, primary_key=True)
    res_country_group = models.ForeignKey(related_name='+',to = ResCountryGroup, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_res_country_group_rel'
        unique_together = (('res_country', 'res_country_group'),)


class ResCountryState(models.Model):
    country = models.ForeignKey(related_name='+',to = ResCountry, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_state'
        unique_together = (('country', 'code'),)


class ResCurrency(models.Model):
    name = models.CharField(unique=True, max_length=255)
    symbol = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    decimal_places = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    currency_unit_label = models.CharField(max_length=255, blank=True, null=True)
    currency_subunit_label = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency'


class ResCurrencyRate(models.Model):
    name = models.DateField()
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = ResCurrency, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency_rate'
        unique_together = (('name', 'currency', 'company'),)


class ResGroups(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    category = models.ForeignKey(related_name='+',to = IrModuleCategory, on_delete = models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    share = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_groups'
        unique_together = (('category', 'name'),)


class ResGroupsImpliedRel(models.Model):
    gid = models.OneToOneField(ResGroups, on_delete = models.DO_NOTHING, db_column='gid', primary_key=True)
    hid = models.ForeignKey(related_name='+',to = ResGroups, on_delete = models.DO_NOTHING, db_column='hid')

    class Meta:
        managed = False
        db_table = 'res_groups_implied_rel'
        unique_together = (('gid', 'hid'),)


class ResGroupsReportRel(models.Model):
    uid = models.OneToOneField(IrActReportXml, on_delete = models.DO_NOTHING, db_column='uid', primary_key=True)
    gid = models.ForeignKey(related_name='+',to = ResGroups, on_delete = models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_report_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsUsersRel(models.Model):
    gid = models.OneToOneField(ResGroups, on_delete = models.DO_NOTHING, db_column='gid', primary_key=True)
    uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'res_groups_users_rel'
        unique_together = (('gid', 'uid'),)


class ResLang(models.Model):
    name = models.CharField(unique=True, max_length=255)
    code = models.CharField(unique=True, max_length=255)
    iso_code = models.CharField(max_length=255, blank=True, null=True)
    url_code = models.CharField(unique=True, max_length=255)
    active = models.BooleanField(blank=True, null=True)
    direction = models.CharField(max_length=255)
    date_format = models.CharField(max_length=255)
    time_format = models.CharField(max_length=255)
    week_start = models.CharField(max_length=255)
    grouping = models.CharField(max_length=255)
    decimal_point = models.CharField(max_length=255)
    thousands_sep = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_lang'


class ResPartner(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    title = models.ForeignKey(related_name='+',to = 'ResPartnerTitle', on_delete = models.DO_NOTHING, db_column='title', blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    tz = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, blank=True, null=True)
    vat = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    employee = models.BooleanField(blank=True, null=True)
    function = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey(related_name='+',to = ResCountryState, on_delete = models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = ResCountry, on_delete = models.DO_NOTHING, blank=True, null=True)
    partner_latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner_longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    is_company = models.BooleanField(blank=True, null=True)
    industry = models.ForeignKey(related_name='+',to = 'ResPartnerIndustry', on_delete = models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    partner_share = models.BooleanField(blank=True, null=True)
    commercial_partner = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    commercial_company_name = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    email_normalized = models.CharField(max_length=255, blank=True, null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    signup_token = models.CharField(max_length=255, blank=True, null=True)
    signup_type = models.CharField(max_length=255, blank=True, null=True)
    signup_expiration = models.DateTimeField(blank=True, null=True)
    team = models.ForeignKey(related_name='+',to = CrmTeam, on_delete = models.DO_NOTHING, blank=True, null=True)
    phone_sanitized = models.CharField(max_length=255, blank=True, null=True)
    debit_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    invoice_warn = models.CharField(max_length=255, blank=True, null=True)
    invoice_warn_msg = models.TextField(blank=True, null=True)
    supplier_rank = models.IntegerField(blank=True, null=True)
    customer_rank = models.IntegerField(blank=True, null=True)
    sale_warn = models.CharField(max_length=255, blank=True, null=True)
    sale_warn_msg = models.TextField(blank=True, null=True)
    calendar_last_notif_ack = models.DateTimeField(blank=True, null=True)
    picking_warn = models.CharField(max_length=255, blank=True, null=True)
    picking_warn_msg = models.TextField(blank=True, null=True)
    date_localization = models.DateField(blank=True, null=True)
    purchase_warn = models.CharField(max_length=255, blank=True, null=True)
    purchase_warn_msg = models.TextField(blank=True, null=True)
    x_whatsapp = models.CharField(max_length=255, blank=True, null=True)
    x_source = models.CharField(max_length=255, blank=True, null=True)
    x_status = models.CharField(max_length=255, blank=True, null=True)
    x_user_type = models.CharField(max_length=255, blank=True, null=True)
    x_residential_status = models.CharField(max_length=255, blank=True, null=True)
    x_approved_network_associate = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner'


class ResPartnerBank(models.Model):
    active = models.BooleanField(blank=True, null=True)
    acc_number = models.CharField(max_length=255)
    sanitized_acc_number = models.CharField(max_length=255, blank=True, null=True)
    acc_holder_name = models.CharField(max_length=255, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING)
    bank = models.ForeignKey(related_name='+',to = ResBank, on_delete = models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = ResCurrency, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_bank'
        unique_together = (('sanitized_acc_number', 'company'),)


class ResPartnerCategory(models.Model):
    name = models.CharField(max_length=255)
    color = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    parent_path = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_category'


class ResPartnerIap(models.Model):
    partner = models.OneToOneField(ResPartner, on_delete = models.DO_NOTHING)
    iap_search_domain = models.CharField(max_length=255, blank=True, null=True)
    iap_enrich_info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_iap'


class ResPartnerIndustry(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_industry'


class ResPartnerResPartnerCategoryRel(models.Model):
    category = models.OneToOneField(ResPartnerCategory, on_delete = models.DO_NOTHING, primary_key=True)
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_res_partner_category_rel'
        unique_together = (('category', 'partner'),)


class ResPartnerTitle(models.Model):
    name = models.CharField(max_length=255)
    shortcut = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'ResUsers', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_title'


class ResUsers(models.Model):
    active = models.BooleanField(blank=True, null=True)
    login = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    share = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    totp_secret = models.CharField(max_length=255, blank=True, null=True)
    notification_type = models.CharField(max_length=255)
    odoobot_state = models.CharField(max_length=255, blank=True, null=True)
    odoobot_failed = models.BooleanField(blank=True, null=True)
    sale_team = models.ForeignKey(related_name='+',to = CrmTeam, on_delete = models.DO_NOTHING, blank=True, null=True)
    target_sales_won = models.IntegerField(blank=True, null=True)
    target_sales_done = models.IntegerField(blank=True, null=True)
    target_sales_invoiced = models.IntegerField(blank=True, null=True)
    microsoft_calendar_rtoken = models.CharField(max_length=255, blank=True, null=True)
    microsoft_calendar_token = models.CharField(max_length=255, blank=True, null=True)
    microsoft_calendar_token_validity = models.DateTimeField(blank=True, null=True)
    google_cal_account = models.OneToOneField(GoogleCalendarCredentials, on_delete = models.DO_NOTHING, blank=True, null=True)
    microsoft_calendar_sync_token = models.CharField(max_length=255, blank=True, null=True)
    microsoft_synchronization_stopped = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users'


class ResUsersApikeys(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING)
    scope = models.CharField(max_length=255, blank=True, null=True)
    index = models.CharField(max_length=8, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_apikeys'


class ResUsersApikeysDescription(models.Model):
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_apikeys_description'


class ResUsersIdentitycheck(models.Model):
    request = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_identitycheck'


class ResUsersLog(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_log'


class ResUsersSettings(models.Model):
    user = models.OneToOneField(ResUsers, on_delete = models.DO_NOTHING)
    is_discuss_sidebar_category_channel_open = models.BooleanField(blank=True, null=True)
    is_discuss_sidebar_category_chat_open = models.BooleanField(blank=True, null=True)
    push_to_talk_key = models.CharField(max_length=255, blank=True, null=True)
    use_push_to_talk = models.BooleanField(blank=True, null=True)
    voice_active_duration = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_settings'


class ResUsersSettingsVolumes(models.Model):
    user_setting = models.ForeignKey(related_name='+',to = ResUsersSettings, on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    guest = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_settings_volumes'
        unique_together = (('user_setting', 'guest'), ('user_setting', 'partner'),)


class ResetViewArchWizard(models.Model):
    view = models.ForeignKey(related_name='+',to = IrUiView, on_delete = models.DO_NOTHING, blank=True, null=True)
    reset_mode = models.CharField(max_length=255)
    compare_view = models.ForeignKey(related_name='+',to = IrUiView, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reset_view_arch_wizard'


class ResourceCalendar(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    hours_per_day = models.FloatField(blank=True, null=True)
    tz = models.CharField(max_length=255)
    two_weeks_calendar = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar'


class ResourceCalendarAttendance(models.Model):
    name = models.CharField(max_length=255)
    dayofweek = models.CharField(max_length=255)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    hour_from = models.FloatField()
    hour_to = models.FloatField()
    calendar = models.ForeignKey(related_name='+',to = ResourceCalendar, on_delete = models.DO_NOTHING)
    day_period = models.CharField(max_length=255)
    resource = models.ForeignKey(related_name='+',to = 'ResourceResource', on_delete = models.DO_NOTHING, blank=True, null=True)
    week_type = models.CharField(max_length=255, blank=True, null=True)
    display_type = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar_attendance'


class ResourceCalendarLeaves(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    calendar = models.ForeignKey(related_name='+',to = ResourceCalendar, on_delete = models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    resource = models.ForeignKey(related_name='+',to = 'ResourceResource', on_delete = models.DO_NOTHING, blank=True, null=True)
    time_type = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    holiday = models.ForeignKey(related_name='+',to = HrLeave, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar_leaves'


class ResourceResource(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    resource_type = models.CharField(max_length=255)
    user = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, blank=True, null=True)
    time_efficiency = models.FloatField()
    calendar = models.ForeignKey(related_name='+',to = ResourceCalendar, on_delete = models.DO_NOTHING)
    tz = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_resource'


class ResourceTest(models.Model):
    resource = models.ForeignKey(related_name='+',to = ResourceResource, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    resource_calendar = models.ForeignKey(related_name='+',to = ResourceCalendar, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_test'


class RuleGroupRel(models.Model):
    rule_group = models.OneToOneField(IrRule, on_delete = models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey(related_name='+',to = ResGroups, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rule_group_rel'
        unique_together = (('rule_group', 'group'),)


class SaleAdvancePaymentInv(models.Model):
    advance_payment_method = models.CharField(max_length=255)
    deduct_down_payments = models.BooleanField(blank=True, null=True)
    has_down_payments = models.BooleanField(blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = ResCurrency, on_delete = models.DO_NOTHING, blank=True, null=True)
    fixed_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deposit_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_start_invoice_timesheet = models.DateField(blank=True, null=True)
    date_end_invoice_timesheet = models.DateField(blank=True, null=True)
    invoicing_timesheet_enabled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_advance_payment_inv'


class SaleOrder(models.Model):
    campaign = models.ForeignKey(related_name='+',to = 'UtmCampaign', on_delete = models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey(related_name='+',to = 'UtmSource', on_delete = models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey(related_name='+',to = 'UtmMedium', on_delete = models.DO_NOTHING, blank=True, null=True)
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255, blank=True, null=True)
    client_order_ref = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    date_order = models.DateTimeField()
    validity_date = models.DateField(blank=True, null=True)
    require_signature = models.BooleanField(blank=True, null=True)
    require_payment = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING)
    partner_invoice = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING)
    partner_shipping = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING)
    pricelist = models.ForeignKey(related_name='+',to = ProductPricelist, on_delete = models.DO_NOTHING)
    currency = models.ForeignKey(related_name='+',to = ResCurrency, on_delete = models.DO_NOTHING, blank=True, null=True)
    analytic_account = models.ForeignKey(related_name='+',to = AccountAnalyticAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    invoice_status = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_term = models.ForeignKey(related_name='+',to = AccountPaymentTerm, on_delete = models.DO_NOTHING, blank=True, null=True)
    fiscal_position = models.ForeignKey(related_name='+',to = AccountFiscalPosition, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    team = models.ForeignKey(related_name='+',to = CrmTeam, on_delete = models.DO_NOTHING, blank=True, null=True)
    signed_by = models.CharField(max_length=255, blank=True, null=True)
    signed_on = models.DateTimeField(blank=True, null=True)
    commitment_date = models.DateTimeField(blank=True, null=True)
    show_update_pricelist = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order_template = models.ForeignKey(related_name='+',to = 'SaleOrderTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    opportunity = models.ForeignKey(related_name='+',to = CrmLead, on_delete = models.DO_NOTHING, blank=True, null=True)
    incoterm = models.ForeignKey(related_name='+',to = AccountIncoterms, on_delete = models.DO_NOTHING, db_column='incoterm', blank=True, null=True)
    picking_policy = models.CharField(max_length=255)
    warehouse = models.ForeignKey(related_name='+',to = 'StockWarehouse', on_delete = models.DO_NOTHING)
    procurement_group = models.ForeignKey(related_name='+',to = ProcurementGroup, on_delete = models.DO_NOTHING, blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(related_name='+',to = ProjectProject, on_delete = models.DO_NOTHING, blank=True, null=True)
    margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    margin_percent = models.FloatField(blank=True, null=True)
    report_grids = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order'


class SaleOrderCancel(models.Model):
    order = models.ForeignKey(related_name='+',to = SaleOrder, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_cancel'


class SaleOrderLine(models.Model):
    order = models.ForeignKey(related_name='+',to = SaleOrder, on_delete = models.DO_NOTHING)
    name = models.TextField()
    sequence = models.IntegerField(blank=True, null=True)
    invoice_status = models.CharField(max_length=255, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_tax = models.FloatField(blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce_taxinc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce_taxexcl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING, db_column='product_uom', blank=True, null=True)
    qty_delivered_method = models.CharField(max_length=255, blank=True, null=True)
    qty_delivered = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_delivered_manual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    untaxed_amount_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    untaxed_amount_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    salesman = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(related_name='+',to = ResCurrency, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    order_partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    is_expense = models.BooleanField(blank=True, null=True)
    is_downpayment = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    customer_lead = models.FloatField()
    display_type = models.CharField(max_length=255, blank=True, null=True)
    product_packaging = models.ForeignKey(related_name='+',to = ProductPackaging, on_delete = models.DO_NOTHING, blank=True, null=True)
    product_packaging_qty = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    route = models.ForeignKey(related_name='+',to = 'StockLocationRoute', on_delete = models.DO_NOTHING, blank=True, null=True)
    is_service = models.BooleanField(blank=True, null=True)
    project = models.ForeignKey(related_name='+',to = ProjectProject, on_delete = models.DO_NOTHING, blank=True, null=True)
    task = models.ForeignKey(related_name='+',to = ProjectTask, on_delete = models.DO_NOTHING, blank=True, null=True)
    margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    margin_percent = models.FloatField(blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_hours = models.FloatField(blank=True, null=True)
    has_displayed_warning_upsell = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_line'


class SaleOrderLineInvoiceRel(models.Model):
    invoice_line = models.OneToOneField(AccountMoveLine, on_delete = models.DO_NOTHING, primary_key=True)
    order_line = models.ForeignKey(related_name='+',to = SaleOrderLine, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_line_invoice_rel'
        unique_together = (('invoice_line', 'order_line'),)


class SaleOrderOption(models.Model):
    order = models.ForeignKey(related_name='+',to = SaleOrder, on_delete = models.DO_NOTHING, blank=True, null=True)
    line = models.ForeignKey(related_name='+',to = SaleOrderLine, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_option'


class SaleOrderTagRel(models.Model):
    order = models.OneToOneField(SaleOrder, on_delete = models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(related_name='+',to = CrmTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_tag_rel'
        unique_together = (('order', 'tag'),)


class SaleOrderTemplate(models.Model):
    name = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    number_of_days = models.IntegerField(blank=True, null=True)
    require_signature = models.BooleanField(blank=True, null=True)
    require_payment = models.BooleanField(blank=True, null=True)
    mail_template = models.ForeignKey(related_name='+',to = MailTemplate, on_delete = models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_template'


class SaleOrderTemplateLine(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    sale_order_template = models.ForeignKey(related_name='+',to = SaleOrderTemplate, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING, blank=True, null=True)
    display_type = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_template_line'


class SaleOrderTemplateOption(models.Model):
    sale_order_template = models.ForeignKey(related_name='+',to = SaleOrderTemplate, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_template_option'


class SaleOrderTransactionRel(models.Model):
    transaction = models.OneToOneField(PaymentTransaction, on_delete = models.DO_NOTHING, primary_key=True)
    sale_order = models.ForeignKey(related_name='+',to = SaleOrder, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_transaction_rel'
        unique_together = (('transaction', 'sale_order'),)


class SalePaymentAcquirerOnboardingWizard(models.Model):
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    paypal_user_type = models.CharField(max_length=255, blank=True, null=True)
    paypal_email_account = models.CharField(max_length=255, blank=True, null=True)
    paypal_seller_account = models.CharField(max_length=255, blank=True, null=True)
    paypal_pdt_token = models.CharField(max_length=255, blank=True, null=True)
    stripe_secret_key = models.CharField(max_length=255, blank=True, null=True)
    stripe_publishable_key = models.CharField(max_length=255, blank=True, null=True)
    manual_name = models.CharField(max_length=255, blank=True, null=True)
    journal_name = models.CharField(max_length=255, blank=True, null=True)
    acc_number = models.CharField(max_length=255, blank=True, null=True)
    manual_post_msg = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_payment_acquirer_onboarding_wizard'


class SaleProductConfigurator(models.Model):
    product_template = models.ForeignKey(related_name='+',to = ProductTemplate, on_delete = models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    pricelist = models.ForeignKey(related_name='+',to = ProductPricelist, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_product_configurator'


class ShopProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    price = models.IntegerField()
    sub_category = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'shop_product'


class SmsCancel(models.Model):
    model = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_cancel'


class SmsComposer(models.Model):
    composition_mode = models.CharField(max_length=255)
    res_model = models.CharField(max_length=255, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    res_ids = models.CharField(max_length=255, blank=True, null=True)
    use_active_domain = models.BooleanField(blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    mass_keep_log = models.BooleanField(blank=True, null=True)
    mass_force_send = models.BooleanField(blank=True, null=True)
    mass_use_blacklist = models.BooleanField(blank=True, null=True)
    recipient_single_number_itf = models.CharField(max_length=255, blank=True, null=True)
    number_field_name = models.CharField(max_length=255, blank=True, null=True)
    numbers = models.CharField(max_length=255, blank=True, null=True)
    template = models.ForeignKey(related_name='+',to = 'SmsTemplate', on_delete = models.DO_NOTHING, blank=True, null=True)
    body = models.TextField()
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_composer'


class SmsResend(models.Model):
    mail_message = models.ForeignKey(related_name='+',to = MailMessage, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_resend'


class SmsResendRecipient(models.Model):
    sms_resend = models.ForeignKey(related_name='+',to = SmsResend, on_delete = models.DO_NOTHING)
    notification = models.ForeignKey(related_name='+',to = MailNotification, on_delete = models.DO_NOTHING)
    resend = models.BooleanField(blank=True, null=True)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    sms_number = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_resend_recipient'


class SmsSms(models.Model):
    number = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    mail_message = models.ForeignKey(related_name='+',to = MailMessage, on_delete = models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=255)
    failure_type = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_sms'


class SmsTemplate(models.Model):
    lang = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    model = models.ForeignKey(related_name='+',to = IrModel, on_delete = models.DO_NOTHING)
    model_0 = models.CharField(db_column='model', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    body = models.CharField(max_length=255)
    sidebar_action = models.ForeignKey(related_name='+',to = IrActWindow, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_template'


class SmsTemplatePreview(models.Model):
    sms_template = models.ForeignKey(related_name='+',to = SmsTemplate, on_delete = models.DO_NOTHING)
    lang = models.CharField(max_length=255, blank=True, null=True)
    resource_ref = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_template_preview'


class SnailmailConfirmInvoice(models.Model):
    model_name = models.CharField(max_length=255, blank=True, null=True)
    invoice_send = models.ForeignKey(related_name='+',to = AccountInvoiceSend, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_confirm_invoice'


class SnailmailLetter(models.Model):
    user = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, blank=True, null=True)
    model = models.CharField(max_length=255)
    res_id = models.IntegerField()
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    report_template = models.ForeignKey(related_name='+',to = IrActReportXml, on_delete = models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    color = models.BooleanField(blank=True, null=True)
    cover = models.BooleanField(blank=True, null=True)
    duplex = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=255)
    error_code = models.CharField(max_length=255, blank=True, null=True)
    info_msg = models.CharField(max_length=255, blank=True, null=True)
    message = models.ForeignKey(related_name='+',to = MailMessage, on_delete = models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state_0 = models.ForeignKey(related_name='+',to = ResCountryState, on_delete = models.DO_NOTHING, db_column='state_id', blank=True, null=True)  # Field renamed because of name conflict.
    country = models.ForeignKey(related_name='+',to = ResCountry, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter'


class SnailmailLetterCancel(models.Model):
    model = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter_cancel'


class SnailmailLetterFormatError(models.Model):
    message = models.ForeignKey(related_name='+',to = MailMessage, on_delete = models.DO_NOTHING, blank=True, null=True)
    snailmail_cover = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter_format_error'


class SnailmailLetterMissingRequiredFields(models.Model):
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    letter = models.ForeignKey(related_name='+',to = SnailmailLetter, on_delete = models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey(related_name='+',to = ResCountryState, on_delete = models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(related_name='+',to = ResCountry, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter_missing_required_fields'


class StockAssignSerial(models.Model):
    move = models.ForeignKey(related_name='+',to = 'StockMove', on_delete = models.DO_NOTHING, blank=True, null=True)
    next_serial_number = models.CharField(max_length=255)
    next_serial_count = models.IntegerField()
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_assign_serial'


class StockBackorderConfirmation(models.Model):
    show_transfers = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_backorder_confirmation'


class StockBackorderConfirmationLine(models.Model):
    backorder_confirmation = models.ForeignKey(related_name='+',to = StockBackorderConfirmation, on_delete = models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey(related_name='+',to = 'StockPicking', on_delete = models.DO_NOTHING, blank=True, null=True)
    to_backorder = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_backorder_confirmation_line'


class StockChangeProductQty(models.Model):
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    product_tmpl = models.ForeignKey(related_name='+',to = ProductTemplate, on_delete = models.DO_NOTHING)
    new_quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_change_product_qty'


class StockConflictQuantRel(models.Model):
    stock_inventory_conflict = models.OneToOneField('StockInventoryConflict', on_delete = models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey(related_name='+',to = 'StockQuant', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_conflict_quant_rel'
        unique_together = (('stock_inventory_conflict', 'stock_quant'),)


class StockImmediateTransfer(models.Model):
    show_transfers = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_immediate_transfer'


class StockImmediateTransferLine(models.Model):
    immediate_transfer = models.ForeignKey(related_name='+',to = StockImmediateTransfer, on_delete = models.DO_NOTHING)
    picking = models.ForeignKey(related_name='+',to = 'StockPicking', on_delete = models.DO_NOTHING)
    to_immediate = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_immediate_transfer_line'


class StockInventoryAdjustmentName(models.Model):
    inventory_adjustment_name = models.CharField(max_length=255, blank=True, null=True)
    show_info = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory_adjustment_name'


class StockInventoryAdjustmentNameStockQuantRel(models.Model):
    stock_inventory_adjustment_name = models.OneToOneField(StockInventoryAdjustmentName, on_delete = models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey(related_name='+',to = 'StockQuant', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_adjustment_name_stock_quant_rel'
        unique_together = (('stock_inventory_adjustment_name', 'stock_quant'),)


class StockInventoryConflict(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory_conflict'


class StockInventoryConflictStockQuantRel(models.Model):
    stock_inventory_conflict = models.OneToOneField(StockInventoryConflict, on_delete = models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey(related_name='+',to = 'StockQuant', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_conflict_stock_quant_rel'
        unique_together = (('stock_inventory_conflict', 'stock_quant'),)


class StockInventoryWarning(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory_warning'


class StockInventoryWarningStockQuantRel(models.Model):
    stock_inventory_warning = models.OneToOneField(StockInventoryWarning, on_delete = models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey(related_name='+',to = 'StockQuant', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_warning_stock_quant_rel'
        unique_together = (('stock_inventory_warning', 'stock_quant'),)


class StockLandedCost(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    target_model = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    account_move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING)
    vendor_bill = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_landed_cost'


class StockLandedCostLines(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    cost = models.ForeignKey(related_name='+',to = StockLandedCost, on_delete = models.DO_NOTHING)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    split_method = models.CharField(max_length=255)
    account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_landed_cost_lines'


class StockLandedCostStockPickingRel(models.Model):
    stock_landed_cost = models.OneToOneField(StockLandedCost, on_delete = models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(related_name='+',to = 'StockPicking', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_landed_cost_stock_picking_rel'
        unique_together = (('stock_landed_cost', 'stock_picking'),)


class StockLocation(models.Model):
    name = models.CharField(max_length=255)
    complete_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    usage = models.CharField(max_length=255)
    location = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    posx = models.IntegerField(blank=True, null=True)
    posy = models.IntegerField(blank=True, null=True)
    posz = models.IntegerField(blank=True, null=True)
    parent_path = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    scrap_location = models.BooleanField(blank=True, null=True)
    return_location = models.BooleanField(blank=True, null=True)
    removal_strategy = models.ForeignKey(related_name='+',to = ProductRemoval, on_delete = models.DO_NOTHING, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    cyclic_inventory_frequency = models.IntegerField(blank=True, null=True)
    last_inventory_date = models.DateField(blank=True, null=True)
    next_inventory_date = models.DateField(blank=True, null=True)
    storage_category = models.ForeignKey(related_name='+',to = 'StockStorageCategory', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    valuation_in_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    valuation_out_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_location'
        unique_together = (('barcode', 'company'),)


class StockLocationRoute(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    product_selectable = models.BooleanField(blank=True, null=True)
    product_categ_selectable = models.BooleanField(blank=True, null=True)
    warehouse_selectable = models.BooleanField(blank=True, null=True)
    packaging_selectable = models.BooleanField(blank=True, null=True)
    supplied_wh = models.ForeignKey(related_name='+',to = 'StockWarehouse', on_delete = models.DO_NOTHING, blank=True, null=True)
    supplier_wh = models.ForeignKey(related_name='+',to = 'StockWarehouse', on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_selectable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_location_route'


class StockLocationRouteCateg(models.Model):
    route = models.OneToOneField(StockLocationRoute, on_delete = models.DO_NOTHING, primary_key=True)
    categ = models.ForeignKey(related_name='+',to = ProductCategory, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_categ'
        unique_together = (('route', 'categ'),)


class StockLocationRouteMove(models.Model):
    move = models.OneToOneField('StockMove', on_delete = models.DO_NOTHING, primary_key=True)
    route = models.ForeignKey(related_name='+',to = StockLocationRoute, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_move'
        unique_together = (('move', 'route'),)


class StockLocationRoutePackaging(models.Model):
    route = models.OneToOneField(StockLocationRoute, on_delete = models.DO_NOTHING, primary_key=True)
    packaging = models.ForeignKey(related_name='+',to = ProductPackaging, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_packaging'
        unique_together = (('route', 'packaging'),)


class StockLocationRouteStockRulesReportRel(models.Model):
    stock_rules_report = models.OneToOneField('StockRulesReport', on_delete = models.DO_NOTHING, primary_key=True)
    stock_location_route = models.ForeignKey(related_name='+',to = StockLocationRoute, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_stock_rules_report_rel'
        unique_together = (('stock_rules_report', 'stock_location_route'),)


class StockMove(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    date_deadline = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    description_picking = models.TextField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING, db_column='product_uom')
    location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    location_dest = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey(related_name='+',to = 'StockPicking', on_delete = models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    price_unit = models.FloatField(blank=True, null=True)
    origin = models.CharField(max_length=255, blank=True, null=True)
    procure_method = models.CharField(max_length=255)
    scrapped = models.BooleanField(blank=True, null=True)
    group = models.ForeignKey(related_name='+',to = ProcurementGroup, on_delete = models.DO_NOTHING, blank=True, null=True)
    rule = models.ForeignKey(related_name='+',to = 'StockRule', on_delete = models.DO_NOTHING, blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    delay_alert_date = models.DateTimeField(blank=True, null=True)
    picking_type = models.ForeignKey(related_name='+',to = 'StockPickingType', on_delete = models.DO_NOTHING, blank=True, null=True)
    is_inventory = models.BooleanField(blank=True, null=True)
    origin_returned_move = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    restrict_partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey(related_name='+',to = 'StockWarehouse', on_delete = models.DO_NOTHING, blank=True, null=True)
    additional = models.BooleanField(blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    package_level = models.ForeignKey(related_name='+',to = 'StockPackageLevel', on_delete = models.DO_NOTHING, blank=True, null=True)
    next_serial = models.CharField(max_length=255, blank=True, null=True)
    next_serial_count = models.IntegerField(blank=True, null=True)
    orderpoint = models.ForeignKey(related_name='+',to = 'StockWarehouseOrderpoint', on_delete = models.DO_NOTHING, blank=True, null=True)
    reservation_date = models.DateField(blank=True, null=True)
    product_packaging = models.ForeignKey(related_name='+',to = ProductPackaging, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    to_refund = models.BooleanField(blank=True, null=True)
    analytic_account_line = models.ForeignKey(related_name='+',to = AccountAnalyticLine, on_delete = models.DO_NOTHING, blank=True, null=True)
    sale_line = models.ForeignKey(related_name='+',to = SaleOrderLine, on_delete = models.DO_NOTHING, blank=True, null=True)
    purchase_line = models.ForeignKey(related_name='+',to = PurchaseOrderLine, on_delete = models.DO_NOTHING, blank=True, null=True)
    created_purchase_line = models.ForeignKey(related_name='+',to = PurchaseOrderLine, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move'


class StockMoveLine(models.Model):
    picking = models.ForeignKey(related_name='+',to = 'StockPicking', on_delete = models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(related_name='+',to = StockMove, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_done = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    package = models.ForeignKey(related_name='+',to = 'StockQuantPackage', on_delete = models.DO_NOTHING, blank=True, null=True)
    package_level = models.ForeignKey(related_name='+',to = 'StockPackageLevel', on_delete = models.DO_NOTHING, blank=True, null=True)
    lot = models.ForeignKey(related_name='+',to = 'StockProductionLot', on_delete = models.DO_NOTHING, blank=True, null=True)
    lot_name = models.CharField(max_length=255, blank=True, null=True)
    result_package = models.ForeignKey(related_name='+',to = 'StockQuantPackage', on_delete = models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField()
    owner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    location_dest = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    state = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    description_picking = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move_line'


class StockMoveLineConsumeRel(models.Model):
    consume_line = models.OneToOneField(StockMoveLine, on_delete = models.DO_NOTHING, primary_key=True)
    produce_line = models.ForeignKey(related_name='+',to = StockMoveLine, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_move_line_consume_rel'
        unique_together = (('consume_line', 'produce_line'),)


class StockMoveMoveRel(models.Model):
    move_orig = models.OneToOneField(StockMove, on_delete = models.DO_NOTHING, primary_key=True)
    move_dest = models.ForeignKey(related_name='+',to = StockMove, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_move_move_rel'
        unique_together = (('move_orig', 'move_dest'),)


class StockOrderpointSnooze(models.Model):
    predefined_date = models.CharField(max_length=255, blank=True, null=True)
    snoozed_until = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_orderpoint_snooze'


class StockOrderpointSnoozeStockWarehouseOrderpointRel(models.Model):
    stock_orderpoint_snooze = models.OneToOneField(StockOrderpointSnooze, on_delete = models.DO_NOTHING, primary_key=True)
    stock_warehouse_orderpoint = models.ForeignKey(related_name='+',to = 'StockWarehouseOrderpoint', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_orderpoint_snooze_stock_warehouse_orderpoint_rel'
        unique_together = (('stock_orderpoint_snooze', 'stock_warehouse_orderpoint'),)


class StockPackageDestination(models.Model):
    picking = models.ForeignKey(related_name='+',to = 'StockPicking', on_delete = models.DO_NOTHING)
    location_dest = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_package_destination'


class StockPackageLevel(models.Model):
    package = models.ForeignKey(related_name='+',to = 'StockQuantPackage', on_delete = models.DO_NOTHING)
    picking = models.ForeignKey(related_name='+',to = 'StockPicking', on_delete = models.DO_NOTHING, blank=True, null=True)
    location_dest = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_package_level'


class StockPackageType(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    packaging_length = models.IntegerField(blank=True, null=True)
    max_weight = models.FloatField(blank=True, null=True)
    barcode = models.CharField(unique=True, max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_package_type'


class StockPackageTypeStockPutawayRuleRel(models.Model):
    stock_putaway_rule = models.OneToOneField('StockPutawayRule', on_delete = models.DO_NOTHING, primary_key=True)
    stock_package_type = models.ForeignKey(related_name='+',to = StockPackageType, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_package_type_stock_putaway_rule_rel'
        unique_together = (('stock_putaway_rule', 'stock_package_type'),)


class StockPicking(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    backorder = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    move_type = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey(related_name='+',to = ProcurementGroup, on_delete = models.DO_NOTHING, blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateTimeField(blank=True, null=True)
    has_deadline_issue = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    location_dest = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    picking_type = models.ForeignKey(related_name='+',to = 'StockPickingType', on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    printed = models.BooleanField(blank=True, null=True)
    is_locked = models.BooleanField(blank=True, null=True)
    immediate_transfer = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale = models.ForeignKey(related_name='+',to = SaleOrder, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking'
        unique_together = (('name', 'company'),)


class StockPickingBackorderRel(models.Model):
    stock_backorder_confirmation = models.OneToOneField(StockBackorderConfirmation, on_delete = models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(related_name='+',to = StockPicking, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_backorder_rel'
        unique_together = (('stock_backorder_confirmation', 'stock_picking'),)


class StockPickingSmsRel(models.Model):
    confirm_stock_sms = models.OneToOneField(ConfirmStockSms, on_delete = models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(related_name='+',to = StockPicking, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_sms_rel'
        unique_together = (('confirm_stock_sms', 'stock_picking'),)


class StockPickingTransferRel(models.Model):
    stock_immediate_transfer = models.OneToOneField(StockImmediateTransfer, on_delete = models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(related_name='+',to = StockPicking, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_transfer_rel'
        unique_together = (('stock_immediate_transfer', 'stock_picking'),)


class StockPickingType(models.Model):
    name = models.CharField(max_length=255)
    color = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    sequence_0 = models.ForeignKey(related_name='+',to = IrSequence, on_delete = models.DO_NOTHING, db_column='sequence_id', blank=True, null=True)  # Field renamed because of name conflict.
    sequence_code = models.CharField(max_length=255)
    default_location_src = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    default_location_dest = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=255)
    return_picking_type = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    show_entire_packs = models.BooleanField(blank=True, null=True)
    warehouse = models.ForeignKey(related_name='+',to = 'StockWarehouse', on_delete = models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    use_create_lots = models.BooleanField(blank=True, null=True)
    use_existing_lots = models.BooleanField(blank=True, null=True)
    print_label = models.BooleanField(blank=True, null=True)
    show_operations = models.BooleanField(blank=True, null=True)
    show_reserved = models.BooleanField(blank=True, null=True)
    reservation_method = models.CharField(max_length=255)
    reservation_days_before = models.IntegerField(blank=True, null=True)
    reservation_days_before_priority = models.IntegerField(blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking_type'


class StockProductionLot(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    ref = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    use_date = models.DateTimeField(blank=True, null=True)
    removal_date = models.DateTimeField(blank=True, null=True)
    alert_date = models.DateTimeField(blank=True, null=True)
    product_expiry_reminded = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_production_lot'


class StockPutawayRule(models.Model):
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(related_name='+',to = ProductCategory, on_delete = models.DO_NOTHING, blank=True, null=True)
    location_in = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    location_out = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    storage_category = models.ForeignKey(related_name='+',to = 'StockStorageCategory', on_delete = models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_putaway_rule'


class StockQuant(models.Model):
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    lot = models.ForeignKey(related_name='+',to = StockProductionLot, on_delete = models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(related_name='+',to = 'StockQuantPackage', on_delete = models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    reserved_quantity = models.FloatField()
    in_date = models.DateTimeField()
    inventory_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inventory_diff_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inventory_date = models.DateField(blank=True, null=True)
    inventory_quantity_set = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)
    removal_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant'


class StockQuantPackage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    package_type = models.ForeignKey(related_name='+',to = StockPackageType, on_delete = models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    package_use = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant_package'


class StockQuantStockRequestCountRel(models.Model):
    stock_request_count = models.OneToOneField('StockRequestCount', on_delete = models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey(related_name='+',to = StockQuant, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_quant_stock_request_count_rel'
        unique_together = (('stock_request_count', 'stock_quant'),)


class StockQuantStockTrackConfirmationRel(models.Model):
    stock_track_confirmation = models.OneToOneField('StockTrackConfirmation', on_delete = models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey(related_name='+',to = StockQuant, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_quant_stock_track_confirmation_rel'
        unique_together = (('stock_track_confirmation', 'stock_quant'),)


class StockQuantityHistory(models.Model):
    inventory_datetime = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quantity_history'


class StockReplenishmentInfo(models.Model):
    orderpoint = models.ForeignKey(related_name='+',to = 'StockWarehouseOrderpoint', on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_replenishment_info'


class StockRequestCount(models.Model):
    inventory_date = models.DateField()
    user = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, blank=True, null=True)
    set_count = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_request_count'


class StockReturnPicking(models.Model):
    picking = models.ForeignKey(related_name='+',to = StockPicking, on_delete = models.DO_NOTHING, blank=True, null=True)
    move_dest_exists = models.BooleanField(blank=True, null=True)
    original_location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    parent_location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_return_picking'


class StockReturnPickingLine(models.Model):
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    wizard = models.ForeignKey(related_name='+',to = StockReturnPicking, on_delete = models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(related_name='+',to = StockMove, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    to_refund = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_return_picking_line'


class StockRouteProduct(models.Model):
    route = models.OneToOneField(StockLocationRoute, on_delete = models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey(related_name='+',to = ProductTemplate, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_product'
        unique_together = (('route', 'product'),)


class StockRouteWarehouse(models.Model):
    route = models.OneToOneField(StockLocationRoute, on_delete = models.DO_NOTHING, primary_key=True)
    warehouse = models.ForeignKey(related_name='+',to = 'StockWarehouse', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_warehouse'
        unique_together = (('route', 'warehouse'),)


class StockRule(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    group_propagation_option = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey(related_name='+',to = ProcurementGroup, on_delete = models.DO_NOTHING, blank=True, null=True)
    action = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    location_src = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey(related_name='+',to = StockLocationRoute, on_delete = models.DO_NOTHING)
    procure_method = models.CharField(max_length=255)
    route_sequence = models.IntegerField(blank=True, null=True)
    picking_type = models.ForeignKey(related_name='+',to = StockPickingType, on_delete = models.DO_NOTHING)
    delay = models.IntegerField(blank=True, null=True)
    partner_address = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    propagate_carrier = models.BooleanField(blank=True, null=True)
    warehouse = models.ForeignKey(related_name='+',to = 'StockWarehouse', on_delete = models.DO_NOTHING, blank=True, null=True)
    propagate_warehouse = models.ForeignKey(related_name='+',to = 'StockWarehouse', on_delete = models.DO_NOTHING, blank=True, null=True)
    auto = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_rule'


class StockRulesReport(models.Model):
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    product_tmpl = models.ForeignKey(related_name='+',to = ProductTemplate, on_delete = models.DO_NOTHING)
    product_has_variants = models.BooleanField()
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_rules_report'


class StockRulesReportStockWarehouseRel(models.Model):
    stock_rules_report = models.OneToOneField(StockRulesReport, on_delete = models.DO_NOTHING, primary_key=True)
    stock_warehouse = models.ForeignKey(related_name='+',to = 'StockWarehouse', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_rules_report_stock_warehouse_rel'
        unique_together = (('stock_rules_report', 'stock_warehouse'),)


class StockSchedulerCompute(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_scheduler_compute'


class StockScrap(models.Model):
    message_main_attachment = models.ForeignKey(related_name='+',to = IrAttachment, on_delete = models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    origin = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    product_uom = models.ForeignKey(related_name='+',to = 'UomUom', on_delete = models.DO_NOTHING)
    lot = models.ForeignKey(related_name='+',to = StockProductionLot, on_delete = models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(related_name='+',to = StockQuantPackage, on_delete = models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(related_name='+',to = StockMove, on_delete = models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey(related_name='+',to = StockPicking, on_delete = models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    scrap_location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    scrap_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    state = models.CharField(max_length=255, blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_scrap'


class StockStorageCategory(models.Model):
    name = models.CharField(max_length=255)
    max_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    allow_new_product = models.CharField(max_length=255)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_storage_category'


class StockStorageCategoryCapacity(models.Model):
    storage_category = models.ForeignKey(related_name='+',to = StockStorageCategory, on_delete = models.DO_NOTHING)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    package_type = models.ForeignKey(related_name='+',to = StockPackageType, on_delete = models.DO_NOTHING, blank=True, null=True)
    quantity = models.FloatField()
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_storage_category_capacity'
        unique_together = (('package_type', 'storage_category'), ('product', 'storage_category'),)


class StockTraceabilityReport(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_traceability_report'


class StockTrackConfirmation(models.Model):
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_track_confirmation'


class StockTrackLine(models.Model):
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING, blank=True, null=True)
    wizard = models.ForeignKey(related_name='+',to = StockTrackConfirmation, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_track_line'


class StockValuationAdjustmentLines(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    cost = models.ForeignKey(related_name='+',to = StockLandedCost, on_delete = models.DO_NOTHING)
    cost_line = models.ForeignKey(related_name='+',to = StockLandedCostLines, on_delete = models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(related_name='+',to = StockMove, on_delete = models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    former_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    additional_landed_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    final_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_valuation_adjustment_lines'


class StockValuationLayer(models.Model):
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    stock_valuation_layer = models.ForeignKey(related_name='+',to = 'self', on_delete = models.DO_NOTHING, blank=True, null=True)
    stock_move = models.ForeignKey(related_name='+',to = StockMove, on_delete = models.DO_NOTHING, blank=True, null=True)
    account_move = models.ForeignKey(related_name='+',to = AccountMove, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    stock_landed_cost = models.ForeignKey(related_name='+',to = StockLandedCost, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_valuation_layer'


class StockValuationLayerRevaluation(models.Model):
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    added_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    reason = models.CharField(max_length=255, blank=True, null=True)
    account_journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_valuation_layer_revaluation'


class StockWarehouse(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    partner = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)
    view_location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    lot_stock = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    code = models.CharField(max_length=5)
    reception_steps = models.CharField(max_length=255)
    delivery_steps = models.CharField(max_length=255)
    wh_input_stock_loc = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    wh_qc_stock_loc = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    wh_output_stock_loc = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    wh_pack_stock_loc = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING, blank=True, null=True)
    mto_pull = models.ForeignKey(related_name='+',to = StockRule, on_delete = models.DO_NOTHING, blank=True, null=True)
    pick_type = models.ForeignKey(related_name='+',to = StockPickingType, on_delete = models.DO_NOTHING, blank=True, null=True)
    pack_type = models.ForeignKey(related_name='+',to = StockPickingType, on_delete = models.DO_NOTHING, blank=True, null=True)
    out_type = models.ForeignKey(related_name='+',to = StockPickingType, on_delete = models.DO_NOTHING, blank=True, null=True)
    in_type = models.ForeignKey(related_name='+',to = StockPickingType, on_delete = models.DO_NOTHING, blank=True, null=True)
    int_type = models.ForeignKey(related_name='+',to = StockPickingType, on_delete = models.DO_NOTHING, blank=True, null=True)
    return_type = models.ForeignKey(related_name='+',to = StockPickingType, on_delete = models.DO_NOTHING, blank=True, null=True)
    crossdock_route = models.ForeignKey(related_name='+',to = StockLocationRoute, on_delete = models.DO_NOTHING, blank=True, null=True)
    reception_route = models.ForeignKey(related_name='+',to = StockLocationRoute, on_delete = models.DO_NOTHING, blank=True, null=True)
    delivery_route = models.ForeignKey(related_name='+',to = StockLocationRoute, on_delete = models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    buy_to_resupply = models.BooleanField(blank=True, null=True)
    buy_pull = models.ForeignKey(related_name='+',to = StockRule, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_warehouse'
        unique_together = (('code', 'company'), ('name', 'company'),)


class StockWarehouseOrderpoint(models.Model):
    name = models.CharField(max_length=255)
    trigger = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    snoozed_until = models.DateField(blank=True, null=True)
    warehouse = models.ForeignKey(related_name='+',to = StockWarehouse, on_delete = models.DO_NOTHING)
    location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    product_category = models.ForeignKey(related_name='+',to = ProductCategory, on_delete = models.DO_NOTHING, blank=True, null=True)
    product_min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_max_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_multiple = models.DecimalField(max_digits=65535, decimal_places=65535)
    group = models.ForeignKey(related_name='+',to = ProcurementGroup, on_delete = models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING)
    route = models.ForeignKey(related_name='+',to = StockLocationRoute, on_delete = models.DO_NOTHING, blank=True, null=True)
    qty_to_order = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    supplier = models.ForeignKey(related_name='+',to = ProductSupplierinfo, on_delete = models.DO_NOTHING, blank=True, null=True)
    vendor = models.ForeignKey(related_name='+',to = ResPartner, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_warehouse_orderpoint'
        unique_together = (('product', 'location', 'company'),)


class StockWarnInsufficientQtyScrap(models.Model):
    product = models.ForeignKey(related_name='+',to = ProductProduct, on_delete = models.DO_NOTHING)
    location = models.ForeignKey(related_name='+',to = StockLocation, on_delete = models.DO_NOTHING)
    quantity = models.FloatField()
    product_uom_name = models.CharField(max_length=255)
    scrap = models.ForeignKey(related_name='+',to = StockScrap, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_warn_insufficient_qty_scrap'


class StockWhResupplyTable(models.Model):
    supplied_wh = models.OneToOneField(StockWarehouse, on_delete = models.DO_NOTHING, primary_key=True)
    supplier_wh = models.ForeignKey(related_name='+',to = StockWarehouse, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_wh_resupply_table'
        unique_together = (('supplied_wh', 'supplier_wh'),)


class SummaryEmpRel(models.Model):
    sum = models.OneToOneField(HrHolidaysSummaryEmployee, on_delete = models.DO_NOTHING, primary_key=True)
    emp = models.ForeignKey(related_name='+',to = HrEmployee, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'summary_emp_rel'
        unique_together = (('sum', 'emp'),)


class TaskDependenciesRel(models.Model):
    task = models.OneToOneField(ProjectTask, on_delete = models.DO_NOTHING, primary_key=True)
    depends_on = models.ForeignKey(related_name='+',to = ProjectTask, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'task_dependencies_rel'
        unique_together = (('task', 'depends_on'),)


class TaxAdjustmentsWizard(models.Model):
    reason = models.CharField(max_length=255)
    journal = models.ForeignKey(related_name='+',to = AccountJournal, on_delete = models.DO_NOTHING)
    date = models.DateField()
    debit_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING)
    credit_account = models.ForeignKey(related_name='+',to = AccountAccount, on_delete = models.DO_NOTHING)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    adjustment_type = models.CharField(max_length=255)
    tax_report_line = models.ForeignKey(related_name='+',to = AccountTaxReportLine, on_delete = models.DO_NOTHING)
    company_currency = models.ForeignKey(related_name='+',to = ResCurrency, on_delete = models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_adjustments_wizard'


class TeamFavoriteUserRel(models.Model):
    team = models.OneToOneField(CrmTeam, on_delete = models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_favorite_user_rel'
        unique_together = (('team', 'user'),)


class UomCategory(models.Model):
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_category'


class UomUom(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(related_name='+',to = UomCategory, on_delete = models.DO_NOTHING)
    factor = models.DecimalField(max_digits=65535, decimal_places=65535)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535)
    active = models.BooleanField(blank=True, null=True)
    uom_type = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    timesheet_widget = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_uom'


class UtmCampaign(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING)
    stage = models.ForeignKey(related_name='+',to = 'UtmStage', on_delete = models.DO_NOTHING)
    is_auto_campaign = models.BooleanField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(related_name='+',to = ResCompany, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_campaign'


class UtmMedium(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_medium'


class UtmSource(models.Model):
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_source'


class UtmStage(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_stage'


class UtmTag(models.Model):
    name = models.CharField(unique=True, max_length=255)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_tag'


class UtmTagRel(models.Model):
    tag = models.OneToOneField(UtmCampaign, on_delete = models.DO_NOTHING, primary_key=True)
    campaign = models.ForeignKey(related_name='+',to = UtmTag, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'utm_tag_rel'
        unique_together = (('tag', 'campaign'),)


class ValidateAccountMove(models.Model):
    force_post = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validate_account_move'


class WebEditorConverterTest(models.Model):
    char = models.CharField(max_length=255, blank=True, null=True)
    integer = models.IntegerField(blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    numeric = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    many2one = models.ForeignKey(related_name='+',to = 'WebEditorConverterTestSub', on_delete = models.DO_NOTHING, db_column='many2one', blank=True, null=True)
    binary = models.BinaryField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    selection_str = models.CharField(max_length=255, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test'


class WebEditorConverterTestSub(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test_sub'


class WebTourTour(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_tour_tour'


class WizardIrModelMenuCreate(models.Model):
    menu = models.ForeignKey(related_name='+',to = IrUiMenu, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(related_name='+',to = ResUsers, on_delete = models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_ir_model_menu_create'

