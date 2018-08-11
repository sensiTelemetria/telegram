class Info ():
    nomeCliente= None
    numeroTags= 0
    nomeEmpresa= None
    telefoneContato= None
    email = None
    contato = None
    site = None

    def __init__(self,nomeCliente,numeroTags,nomeEmpresa,telefoneContato,email,contato, site):
        self.nomeCliente = nomeCliente
        self.numeroTags = numeroTags
        self.nomeEmpresa = nomeEmpresa
        self.telefoneContato = telefoneContato
        self.email = email
        self.contato = contato
        self.site = site


    def get_info(self):
        msg = "\nAqui estão as informações do sistema, como pedido! \n\n"
        msg = msg + "*->* Nome do cliente: *" +  self.nomeCliente + "*\n\n"
        msg = msg + "*->* Numero de Tags: *" +  str(self.numeroTags) + "*\n\n"
        msg = msg + "*->* Nome da empresa fornecedora do sistema: *" +  self.nomeEmpresa + "*\n\n"
        msg = msg + "*->* Telefone para contato: *" +  self.telefoneContato + "*\n\n"
        msg = msg + "*->* email para contato: *" +  self.email + "*\n\n"
        msg = msg + "*->* Para saber mais sobre a empresa que fui criada: " + self.site + "\n\n"
        msg = msg + "*->* Contato Telegram de empresa: " + self.contato + "\n\n"
        msg = msg + "\nPrecisando, é só digitar *Sensi*!"
        return  msg