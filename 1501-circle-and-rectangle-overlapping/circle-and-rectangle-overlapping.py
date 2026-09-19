class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xClosest = max(x1, min(xCenter, x2))
        yClosest = max(y1, min(yCenter, y2))

        distX = xCenter - xClosest
        distY = yCenter - yClosest

        return (distY ** 2) + (distX ** 2) <= (radius ** 2)