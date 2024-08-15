from ninja import Router

router = Router()

@router.get('/hello')
def hello(request):
    return "hello world"