from geom2d.point import Point


class AffineTransform:
    def __init__(self, sx=1, sy=1, tx=0, ty=0, shx=0, shy=0):
        self.sx = sx
        self.sy = sy
        self.tx = tx
        self.ty = ty
        self.shx = shx
        self.shy = shy

    def apply_to_point(self, point: Point):
        return Point(
            (self.sx * point.x) + (self.shx * point.y) + self.tx,
            (self.shy * point.x) + (self.sy * point.y) + self.ty
        )
