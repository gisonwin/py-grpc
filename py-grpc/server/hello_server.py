import grpc
from concurrent import futures
import random
import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloResponse(message='Hello {msg},age= {age}'.format(msg=request.name, age=request.age))

    def GetDeptUser(self,request,context):
        dept_id = request.dept_id
        dept_name = request.dept_name
        uid_list = request.uid_list
        if dept_id <=0 or dept_name == '' or len(uid_list) <=0 :
            return helloworld_pb2.GetDeptUserResponse()
        print('dept_id is {0},dept_name is {1}'.format(dept_id,dept_name))
        user_list =[]
        user_map={}
        for id_ in uid_list:
            uid = id_+random.randint(0,1000)
            letters = 'qwertyuiopasdfghjklzxcvbnm'
            name="".join(random.sample(letters,10))
            user = helloworld_pb2.BasicUser()
            user.id= uid
            user.name= name
            user_list.append(user)
            user_map[uid] = user

        return helloworld_pb2.GetDeptUserResponse(user_list= user_list,user_map=user_map)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    print('gRPC server start on port 50054')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
