from flask_restful import Resource, reqparse
from models.staze import *

_staze_reqparse = reqparse.RequestParser()
_staze_reqparse.add_argument("vrh_id", type=int)
_staze_reqparse.add_argument("link_gpx_traga", type=str)
_staze_reqparse.add_argument("naziv",type=str)
_staze_reqparse.add_argument("opis",type=str)

class Staze(Resource):
    def post(self, baza):
        data= _staze_reqparse.parse_args()
        vrh_id=data["vrh_id"]
        link_gpx_traga=data["link_gpx_traga"]
        naziv=data["naziv"]
        opis=data["opis"]
        if baza == "postgres":
            resp=post_staze_pg(vrh_id,link_gpx_traga,naziv, opis)
        elif baza == "mongo":
            pass
        else:
            return {"status":400, "message":"Bad Request"}, 400   
        return resp, 201
    
class Staza(Resource):
    def put(self, baza, id):
        data= _staze_reqparse.parse_args()
        vrh_id=data["vrh_id"]
        link_gpx_traga=data["link_gpx_traga"]
        naziv=data["naziv"]
        opis=data["opis"]
        if baza == "postgres":
            resp=put_staze_pg(id, vrh_id,link_gpx_traga,naziv, opis)
        elif baza == "mongo":
            pass
        else:
            return {"status":400, "message":"Bad Request"}, 400   
        return resp, 201


    def delete(self, baza , id):
        if baza == "postgres":
            resp=del_staze_pg(id)
        elif baza == "mongo":
            pass
        else:
            return {"status":400, "message":"Bad Request"}, 400   
        return resp, 200
