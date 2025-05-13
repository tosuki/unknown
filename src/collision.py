class Collision:
    def check_collision(ctx, entity_a, entity_b):
        ax, ay = ctx.get_position(entity_a.x, entity_a.y)
        bx, by = ctx.get_position(entity_b.x, entity_b.y)

        # AABB collision detection
        if (ax < bx + entity_b.width and ax + entity_a.width > bx and
            ay < by + entity_b.height and ay + entity_a.height > by):
            return True

        return False
