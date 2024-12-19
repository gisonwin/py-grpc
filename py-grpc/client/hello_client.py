import grpc
import helloworld_pb2, helloworld_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50054')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='World', age=39))
    print('Greeter client received ：' + response.message)
    response = stub.GetDeptUser(helloworld_pb2.GetDeptUserRequest(dept_id=1, dept_name='GiSonWin', uid_list=[1, 2, 3]))
    print(response.user_list)
    print("*" * 20)
    print(response.user_map)


if __name__ == '__main__':
    run()
