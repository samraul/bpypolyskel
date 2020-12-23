import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-4.438845157623291, -11.465906143188477, 0.0)),
    Vector((47.00826644897461, -31.503215789794922, 0.0)),
    Vector((48.900245666503906, -31.948476791381836, 0.0)),
    Vector((51.30160140991211, -32.282413482666016, 0.0)),
    Vector((54.06679153442383, -32.17106628417969, 0.0)),
    Vector((56.83197784423828, -31.72576141357422, 0.0)),
    Vector((59.30609130859375, -31.057819366455078, 0.0)),
    Vector((60.106536865234375, -30.723852157592773, 0.0)),
    Vector((55.23095703125, -19.480634689331055, 0.0)),
    Vector((54.6488151550293, -19.703279495239258, 0.0)),
    Vector((53.04792022705078, -20.03725242614746, 0.0)),
    Vector((51.956398010253906, -20.037263870239258, 0.0)),
    Vector((50.28273010253906, -19.703319549560547, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-4.438845157623291, -11.465906143188477, 11.763288497924805)),
    Vector((47.00826644897461, -31.503215789794922, 11.763288497924805)),
    Vector((48.900245666503906, -31.948476791381836, 11.763288497924805)),
    Vector((51.30160140991211, -32.282413482666016, 11.763288497924805)),
    Vector((54.06679153442383, -32.17106628417969, 11.763288497924805)),
    Vector((56.83197784423828, -31.72576141357422, 11.763288497924805)),
    Vector((59.30609130859375, -31.057819366455078, 11.763288497924805)),
    Vector((60.106536865234375, -30.723852157592773, 11.763288497924805)),
    Vector((55.23095703125, -19.480634689331055, 11.763288497924805)),
    Vector((54.6488151550293, -19.703279495239258, 11.763288497924805)),
    Vector((53.04792022705078, -20.03725242614746, 11.763288497924805)),
    Vector((51.956398010253906, -20.037263870239258, 11.763288497924805)),
    Vector((50.28273010253906, -19.703319549560547, 11.763288497924805)),
    Vector((0.0, 0.0, 11.763288497924805))
]
unitVectors = [
    Vector((0.9318204522132874, -0.36291977763175964, 0.0)),
    Vector((0.9734069108963013, -0.22908292710781097, 0.0)),
    Vector((0.9904689192771912, -0.13773632049560547, 0.0)),
    Vector((0.9991902709007263, 0.04023486003279686, 0.0)),
    Vector((0.9872799515724182, 0.15899130702018738, 0.0)),
    Vector((0.9654358625411987, 0.2606409192085266, 0.0)),
    Vector((0.9228932857513428, 0.38505566120147705, 0.0)),
    Vector((-0.3978491723537445, 0.9174508452415466, 0.0)),
    Vector((-0.9340190291404724, -0.3572230339050293, 0.0)),
    Vector((-0.9789250493049622, -0.20421981811523438, 0.0)),
    Vector((-1.0, -1.0484524864295963e-05, 0.0)),
    Vector((-0.9806695580482483, 0.1956714540719986, 0.0)),
    Vector((-0.93107008934021, 0.36484038829803467, 0.0)),
    Vector((-0.36102449893951416, -0.9325563311576843, 0.0))
]
holesInfo = None
firstVertIndex = 14
numPolygonVerts = 14
faces = []


@pytest.mark.dependency()
@pytest.mark.timeout(10)
def test_polygonize():
    global faces
    faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)


@pytest.mark.dependency(depends=["test_polygonize"])
def test_numVertsInFace():
    for face in faces:
        assert len(face) >= 3


@pytest.mark.dependency(depends=["test_polygonize"])
def test_duplication():
    for face in faces:
        assert len(face) == len(set(face))