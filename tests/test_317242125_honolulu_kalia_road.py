import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-8.682127952575684, 14.126445770263672, 0.0)),
    Vector((-12.333395004272461, 11.755342483520508, 0.0)),
    Vector((-15.694221496582031, 8.983489990234375, 0.0)),
    Vector((-18.712743759155273, 5.8554158210754395, 0.0)),
    Vector((-21.347469329833984, 2.393383026123047, 0.0)),
    Vector((-23.577651977539062, -1.3469488620758057, 0.0)),
    Vector((-25.361801147460938, -5.321052074432373, 0.0)),
    Vector((-26.689542770385742, -9.4732666015625, 0.0)),
    Vector((-27.529756546020508, -13.736802101135254, 0.0)),
    Vector((-27.8720703125, -18.078262329101562, 0.0)),
    Vector((-27.71648406982422, -22.43085479736328, 0.0)),
    Vector((-27.0733699798584, -26.738920211791992, 0.0)),
    Vector((-25.93235206604004, -30.935665130615234, 0.0)),
    Vector((-24.324552536010742, -34.98769760131836, 0.0)),
    Vector((-22.270715713500977, -38.81709289550781, 0.0)),
    Vector((-19.781211853027344, -42.401580810546875, 0.0)),
    Vector((-6.254883766174316, -31.692657470703125, 0.0)),
    Vector((-7.603364944458008, -29.499662399291992, 0.0)),
    Vector((-8.692523002624512, -27.173086166381836, 0.0)),
    Vector((-9.511982917785645, -24.724056243896484, 0.0)),
    Vector((-10.041001319885254, -22.208234786987305, 0.0)),
    Vector((-10.269204139709473, -19.647886276245117, 0.0)),
    Vector((-10.217338562011719, -17.065275192260742, 0.0)),
    Vector((-9.864657402038574, -14.516058921813965, 0.0)),
    Vector((-9.22153377532959, -12.022501945495605, 0.0)),
    Vector((-8.298341751098633, -9.629134178161621, 0.0)),
    Vector((-7.105454444885254, -7.347084999084473, 0.0)),
    Vector((-5.6532440185546875, -5.209751129150391, 0.0)),
    Vector((-3.972829818725586, -3.261660575866699, 0.0)),
    Vector((-2.0849573612213135, -1.5139449834823608, 0.0)),
    Vector((0.0, 0.0, 3.5)),
    Vector((-8.682127952575684, 14.126445770263672, 3.5)),
    Vector((-12.333395004272461, 11.755342483520508, 3.5)),
    Vector((-15.694221496582031, 8.983489990234375, 3.5)),
    Vector((-18.712743759155273, 5.8554158210754395, 3.5)),
    Vector((-21.347469329833984, 2.393383026123047, 3.5)),
    Vector((-23.577651977539062, -1.3469488620758057, 3.5)),
    Vector((-25.361801147460938, -5.321052074432373, 3.5)),
    Vector((-26.689542770385742, -9.4732666015625, 3.5)),
    Vector((-27.529756546020508, -13.736802101135254, 3.5)),
    Vector((-27.8720703125, -18.078262329101562, 3.5)),
    Vector((-27.71648406982422, -22.43085479736328, 3.5)),
    Vector((-27.0733699798584, -26.738920211791992, 3.5)),
    Vector((-25.93235206604004, -30.935665130615234, 3.5)),
    Vector((-24.324552536010742, -34.98769760131836, 3.5)),
    Vector((-22.270715713500977, -38.81709289550781, 3.5)),
    Vector((-19.781211853027344, -42.401580810546875, 3.5)),
    Vector((-6.254883766174316, -31.692657470703125, 3.5)),
    Vector((-7.603364944458008, -29.499662399291992, 3.5)),
    Vector((-8.692523002624512, -27.173086166381836, 3.5)),
    Vector((-9.511982917785645, -24.724056243896484, 3.5)),
    Vector((-10.041001319885254, -22.208234786987305, 3.5)),
    Vector((-10.269204139709473, -19.647886276245117, 3.5)),
    Vector((-10.217338562011719, -17.065275192260742, 3.5)),
    Vector((-9.864657402038574, -14.516058921813965, 3.5)),
    Vector((-9.22153377532959, -12.022501945495605, 3.5)),
    Vector((-8.298341751098633, -9.629134178161621, 3.5)),
    Vector((-7.105454444885254, -7.347084999084473, 3.5)),
    Vector((-5.6532440185546875, -5.209751129150391, 3.5)),
    Vector((-3.972829818725586, -3.261660575866699, 3.5)),
    Vector((-2.0849573612213135, -1.5139449834823608, 3.5))
]
unitVectors = [
    Vector((-0.5236131548881531, 0.8519561886787415, 0.0)),
    Vector((-0.8386765718460083, -0.5446297526359558, 0.0)),
    Vector((-0.7714667320251465, -0.6362696886062622, 0.0)),
    Vector((-0.694393515586853, -0.7195953130722046, 0.0)),
    Vector((-0.6056048274040222, -0.7957655787467957, 0.0)),
    Vector((-0.5121271014213562, -0.8589096069335938, 0.0)),
    Vector((-0.409563273191452, -0.9122817516326904, 0.0)),
    Vector((-0.30457448959350586, -0.9524884819984436, 0.0)),
    Vector((-0.19335095584392548, -0.9811297059059143, 0.0)),
    Vector((-0.07860364764928818, -0.9969059228897095, 0.0)),
    Vector((0.03572283312678337, -0.9993616938591003, 0.0)),
    Vector((0.14764533936977386, -0.9890403151512146, 0.0)),
    Vector((0.26235783100128174, -0.9649707078933716, 0.0)),
    Vector((0.3688158392906189, -0.929502546787262, 0.0)),
    Vector((0.4726460874080658, -0.8812524080276489, 0.0)),
    Vector((0.5704385042190552, -0.8213403224945068, 0.0)),
    Vector((0.784029483795166, 0.6207236051559448, 0.0)),
    Vector((-0.5238003730773926, 0.8518410921096802, 0.0)),
    Vector((-0.4239791929721832, 0.9056719541549683, 0.0)),
    Vector((-0.31731370091438293, 0.9483206272125244, 0.0)),
    Vector((-0.20577649772167206, 0.9785990715026855, 0.0)),
    Vector((-0.08877766132354736, 0.9960514903068542, 0.0)),
    Vector((0.020078564062714577, 0.9997984170913696, 0.0)),
    Vector((0.1370435357093811, 0.9905650019645691, 0.0)),
    Vector((0.24974150955677032, 0.9683125615119934, 0.0)),
    Vector((0.35988426208496094, 0.9329969882965088, 0.0)),
    Vector((0.46325358748435974, 0.8862258195877075, 0.0)),
    Vector((0.5619986057281494, 0.8271381855010986, 0.0)),
    Vector((0.6531683206558228, 0.7572126984596252, 0.0)),
    Vector((0.7338216304779053, 0.6793422102928162, 0.0)),
    Vector((0.8091766238212585, 0.5875654220581055, 0.0))
]
holesInfo = None
firstVertIndex = 31
numPolygonVerts = 31
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