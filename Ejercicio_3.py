def num_carac(palabra):
    
    recuento={}
    for caracteristica in palabra:
        if caracteristica in recuento:
            recuento[caracteristica]+=1
            
        else:
            recuento[caracteristica]=1
    return recuento

palabra ="Mazana"
recuento= num_carac(palabra)
print(recuento)