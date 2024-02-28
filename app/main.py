from managers import ActorManager

db_path = 'cinema.db'
manager = ActorManager(db_path)

actor_id = manager.create('John', 'Doe')
print(f"Actor with ID {actor_id} created")

actors = manager.all()
for actor in actors:
    print(f"{actor.id}: {actor.first_name} {actor.last_name}")

manager.update(actor_id, first_name='Jane', last_name='Doe')
print("Actor updated")

manager.delete(actor_id)
print("Actor deleted")
