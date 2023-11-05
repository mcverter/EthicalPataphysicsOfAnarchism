from RadicalEmpiricism.src.word_analysis.db.db import commit_all

class DatabasePopulator:
    def log(self, message, counter):
        print(message, '. Counter is ', counter)

    def commit(self):
        commit_all()