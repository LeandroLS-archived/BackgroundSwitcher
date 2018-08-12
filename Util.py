def api_esta_funcionando(response):
    if(response.status_code == 200):
        return True
    else:
        return False