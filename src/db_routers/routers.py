#Database-router configuration file

# class AdminRouter:
#     """
#     A router to control all database operations on models in the
#     auth and contenttypes applications.
#     """
#     route_app_labels = {'admin'}

#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read auth and contenttypes models go to auth_db.
#         """
#         if model._meta.app_label in self.route_app_labels:
#             return 'default', 'music_db', 'podcast_db', 'radio_db'
#         return None

#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write auth and contenttypes models go to auth_db.
#         """
#         if model._meta.app_label in self.route_app_labels:
#             return 'default', 'music_db', 'podcast_db', 'radio_db'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Allow relations if a model in the auth or contenttypes apps is
#         involved.
#         """
#         if (
#             obj1._meta.app_label in self.route_app_labels or
#             obj2._meta.app_label in self.route_app_labels
#         ):
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Make sure the auth and contenttypes apps only appear in the
#         'auth_db' database.
#         """
#         if app_label in self.route_app_labels:
#             return db == 'default', 'music_db', 'podcast_db', 'radio_db'
#         return None

# class MainRouter:
#     """
#     A router to control all database operations on models in the
#     auth and contenttypes applications.
#     """
#     route_app_labels = {'admin', 'sessions'}

#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read auth and contenttypes models go to auth_db.
#         """
#         if model._meta.app_label in self.route_app_labels:
#             return 'music_db', 'podcast_db', 'radio_db'
#         return None

#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write auth and contenttypes models go to auth_db.
#         """
#         if model._meta.app_label in self.route_app_labels:
#             return 'music_db', 'podcast_db', 'radio_db'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Allow relations if a model in the auth or contenttypes apps is
#         involved.
#         """
#         if (
#             obj1._meta.app_label in self.route_app_labels or
#             obj2._meta.app_label in self.route_app_labels
#         ):
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Make sure the auth and contenttypes apps only appear in the
#         'auth_db' database.
#         """
#         if app_label in self.route_app_labels:
#             return db == 'music_db', 'podcast_db', 'radio_db'
#         return None'

class AdminRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'admin', 'contenttypes', 'auth', 'sessions'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'all_other'
        return None
    
    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'all_other'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'all_other'
        return None


class MusicRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'admin', 'contenttypes', 'auth', 'sessions', 'music'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'music_db'
        return None
    
    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'music_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'music_db'
        return None

class PodcastRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'admin', 'contenttypes', 'auth', 'sessions', 'podcast'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'podcast_db'
        return None
    
    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'podcast_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'podcast_db'
        return None

class RadioRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'admin', 'contenttypes', 'auth', 'sessions', 'radio'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'radio_db'
        return None
    
    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'radio_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'radio_db'
        return None