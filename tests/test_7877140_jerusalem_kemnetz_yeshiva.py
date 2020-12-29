import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-13.019206047058105, -19.091283798217773, 0.0)),
    Vector((6.765076160430908, -32.583213806152344, 0.0)),
    Vector((9.168331146240234, -29.065515518188477, 0.0)),
    Vector((18.724599838256836, -35.577693939208984, 0.0)),
    Vector((10.956600189208984, -46.9656867980957, 0.0)),
    Vector((-0.7758553624153137, -38.961822509765625, 0.0)),
    Vector((-2.176180124282837, -41.010101318359375, 0.0)),
    Vector((-18.724590301513672, -29.722286224365234, 0.0)),
    Vector((-27.467182159423828, -42.54627227783203, 0.0)),
    Vector((64.32071685791016, -105.15219116210938, 0.0)),
    Vector((92.84739685058594, -63.32923889160156, 0.0)),
    Vector((0.0, 0.0, 11.657144546508789)),
    Vector((-13.019206047058105, -19.091283798217773, 11.657144546508789)),
    Vector((6.765076160430908, -32.583213806152344, 11.657144546508789)),
    Vector((9.168331146240234, -29.065515518188477, 11.657144546508789)),
    Vector((18.724599838256836, -35.577693939208984, 11.657144546508789)),
    Vector((10.956600189208984, -46.9656867980957, 11.657144546508789)),
    Vector((-0.7758553624153137, -38.961822509765625, 11.657144546508789)),
    Vector((-2.176180124282837, -41.010101318359375, 11.657144546508789)),
    Vector((-18.724590301513672, -29.722286224365234, 11.657144546508789)),
    Vector((-27.467182159423828, -42.54627227783203, 11.657144546508789)),
    Vector((64.32071685791016, -105.15219116210938, 11.657144546508789)),
    Vector((92.84739685058594, -63.32923889160156, 11.657144546508789)),
    Vector((78.03045654296875, -68.5836410522461, 0.0)),
    Vector((63.75291442871094, -89.51180267333984, 0.0)),
    Vector((55.70098114013672, -84.0238037109375, 0.0)),
    Vector((62.049720764160156, -74.72858428955078, 0.0)),
    Vector((58.01902770996094, -71.97901916503906, 0.0)),
    Vector((65.95730590820312, -60.34608459472656, 0.0)),
    Vector((78.03045654296875, -68.5836410522461, 11.657144546508789)),
    Vector((63.75291442871094, -89.51180267333984, 11.657144546508789)),
    Vector((55.70098114013672, -84.0238037109375, 11.657144546508789)),
    Vector((62.049720764160156, -74.72858428955078, 11.657144546508789)),
    Vector((58.01902770996094, -71.97901916503906, 11.657144546508789)),
    Vector((65.95730590820312, -60.34608459472656, 11.657144546508789)),
    Vector((57.29984664916992, -55.236572265625, 0.0)),
    Vector((44.15768051147461, -75.06263732910156, 0.0)),
    Vector((34.468894958496094, -68.62841033935547, 0.0)),
    Vector((47.6110725402832, -48.8134880065918, 0.0)),
    Vector((57.29984664916992, -55.236572265625, 11.657144546508789)),
    Vector((44.15768051147461, -75.06263732910156, 11.657144546508789)),
    Vector((34.468894958496094, -68.62841033935547, 11.657144546508789)),
    Vector((47.6110725402832, -48.8134880065918, 11.657144546508789))
]
unitVectors = [
    Vector((-0.563408374786377, -0.8261785507202148, 0.0)),
    Vector((0.8261759281158447, -0.5634122490882874, 0.0)),
    Vector((0.5641096234321594, 0.8256999254226685, 0.0)),
    Vector((0.8263666033744812, -0.563132643699646, 0.0)),
    Vector((-0.5635080933570862, -0.8261105418205261, 0.0)),
    Vector((-0.8260810971260071, 0.5635513663291931, 0.0)),
    Vector((-0.5643739104270935, -0.8255192637443542, 0.0)),
    Vector((-0.826115608215332, 0.563500702381134, 0.0)),
    Vector((-0.5632913112640381, -0.8262583613395691, 0.0)),
    Vector((0.8261299133300781, -0.5634797215461731, 0.0)),
    Vector((0.5634855628013611, 0.8261258602142334, 0.0)),
    Vector((-0.8261271715164185, 0.5634838342666626, 0.0)),
    Vector((-0.5635615587234497, -0.8260740041732788, 0.0)),
    Vector((-0.8263207077980042, 0.5631997585296631, 0.0)),
    Vector((0.5640091896057129, 0.8257685303688049, 0.0)),
    Vector((-0.8260970711708069, 0.5635278224945068, 0.0)),
    Vector((0.5636630654335022, 0.8260047435760498, 0.0)),
    Vector((0.8260405659675598, -0.5636106133460999, 0.0)),
    Vector((-0.5525092482566833, -0.8335067629814148, 0.0)),
    Vector((-0.8330395817756653, 0.553213357925415, 0.0)),
    Vector((0.5527254343032837, 0.8333634734153748, 0.0)),
    Vector((0.8334807753562927, -0.5525484681129456, 0.0))
]
holesInfo = [
    (30, 6),
    (40, 4)
]
firstVertIndex = 12
numPolygonVerts = 12
faces = []

bpypolyskel.debugOutputs["skeleton"] = 1


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


@pytest.mark.dependency(depends=["test_polygonize"])
def test_edgeCrossing():
    assert not bpypolyskel.checkEdgeCrossing(bpypolyskel.debugOutputs["skeleton"])