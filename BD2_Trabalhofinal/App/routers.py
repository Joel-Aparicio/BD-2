class MultiDBRouter:
    def db_for_read(self, model, **hints):
        """Define qual banco de dados usar para leitura."""
        if model._meta.app_label == 'BD2_Trabalhofinal.App': #Nome app
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        """Define qual banco de dados usar para escrita."""
        if model._meta.app_label == 'BD2_Trabalhofinal.App':  #Nome app
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Permite relações entre objetos de bancos diferentes."""
        db_list = ('default', 'mongodb')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Define em qual banco de dados as migrações podem ser executadas."""
        if app_label == 'BD2_Trabalhofinal.App': #Nome app
            return db == 'mongodb'
        return db == 'default'
