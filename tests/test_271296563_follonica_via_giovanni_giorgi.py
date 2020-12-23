import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-1.1574395895004272, -5.031641006469727, 0.0)),
    Vector((8.656346321105957, -7.369344711303711, 0.0)),
    Vector((9.83008098602295, -2.2709105014801025, 0.0)),
    Vector((7.808637619018555, -1.8033713102340698, 0.0)),
    Vector((8.599278450012207, 1.6252700090408325, 0.0)),
    Vector((7.792331695556641, 1.8145121335983276, 0.0)),
    Vector((8.64002799987793, 5.476924419403076, 0.0)),
    Vector((10.08275032043457, 5.154099941253662, 0.0)),
    Vector((10.94675350189209, 5.287684440612793, 0.0)),
    Vector((11.704792976379395, 5.688436031341553, 0.0)),
    Vector((12.259057998657227, 6.345221996307373, 0.0)),
    Vector((12.511735916137695, 7.168986797332764, 0.0)),
    Vector((12.438375473022461, 8.0150146484375, 0.0)),
    Vector((12.03897762298584, 8.77198600769043, 0.0)),
    Vector((11.3868989944458, 9.3731107711792, 0.0)),
    Vector((3.7005374431610107, 11.243269920349121, 0.0)),
    Vector((1.051476001739502, -0.2449028044939041, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-1.1574395895004272, -5.031641006469727, 1.0)),
    Vector((8.656346321105957, -7.369344711303711, 1.0)),
    Vector((9.83008098602295, -2.2709105014801025, 1.0)),
    Vector((7.808637619018555, -1.8033713102340698, 1.0)),
    Vector((8.599278450012207, 1.6252700090408325, 1.0)),
    Vector((7.792331695556641, 1.8145121335983276, 1.0)),
    Vector((8.64002799987793, 5.476924419403076, 1.0)),
    Vector((10.08275032043457, 5.154099941253662, 1.0)),
    Vector((10.94675350189209, 5.287684440612793, 1.0)),
    Vector((11.704792976379395, 5.688436031341553, 1.0)),
    Vector((12.259057998657227, 6.345221996307373, 1.0)),
    Vector((12.511735916137695, 7.168986797332764, 1.0)),
    Vector((12.438375473022461, 8.0150146484375, 1.0)),
    Vector((12.03897762298584, 8.77198600769043, 1.0)),
    Vector((11.3868989944458, 9.3731107711792, 1.0)),
    Vector((3.7005374431610107, 11.243269920349121, 1.0)),
    Vector((1.051476001739502, -0.2449028044939041, 1.0)),
    Vector((0.0, 0.0, 1.0))
]
unitVectors = [
    Vector((0.9727818965911865, -0.23172259330749512, 0.0)),
    Vector((0.22434641420841217, 0.9745094180107117, 0.0)),
    Vector((-0.9742799997329712, 0.22534100711345673, 0.0)),
    Vector((0.2247018963098526, 0.9744275808334351, 0.0)),
    Vector((-0.973585844039917, 0.22832168638706207, 0.0)),
    Vector((0.22549699246883392, 0.9742438793182373, 0.0)),
    Vector((0.9758680462837219, -0.21836087107658386, 0.0)),
    Vector((0.9882577657699585, 0.15279564261436462, 0.0)),
    Vector((0.8840595483779907, 0.46737444400787354, 0.0)),
    Vector((0.644940197467804, 0.7642330527305603, 0.0)),
    Vector((0.29325011372566223, 0.9560357332229614, 0.0)),
    Vector((-0.08638745546340942, 0.9962616562843323, 0.0)),
    Vector((-0.4666537046432495, 0.8844401240348816, 0.0)),
    Vector((-0.7352494597434998, 0.6777966022491455, 0.0)),
    Vector((-0.9716529250144958, 0.2364116758108139, 0.0)),
    Vector((-0.22469398379325867, -0.9744293689727783, 0.0)),
    Vector((-0.9739316701889038, 0.22684170305728912, 0.0)),
    Vector((-0.2241775244474411, -0.97454833984375, 0.0))
]
holesInfo = None
firstVertIndex = 18
numPolygonVerts = 18
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