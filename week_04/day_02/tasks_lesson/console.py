import pdb
from models.task import Task
from models.user import User
import repositories.task_repository as task_repository
import repositories.user_repository as user_repository


# task_repository.delete_all()

# task_1 = Task("Walk the dog", "Jack Jarvis", 60)
# print(task_1.__dict__)
# task_repository.save(task_1)
# task_2 = Task('Feed Cat', 'Victor McDade', 5)
# task_repository.save(task_2)
# res = task_repository.select_all()
# for task in res:
#     print(task.__dict__)
# found_task = task_repository.select(1)
# task_1.mark_complete()
# task_repository.update(task_1)

user_1 = User('David', 'Strain')
user_2 = User('Kyle', 'Law')
user_repository.save(user_1)
user_repository.save(user_2)
# res = user_repository.select_all()
# for user in res:
#     print(user.__dict__)
# print(res)
# found_user = user_repository.select(10)
# print(found_user.__dict__)
# user_repository.delete_all()

task = Task('Walk Dog', user_2, 60)
task_repository.save(task)

pdb.set_trace()