from .modulo_menu_arquivo import MenuArquivo as p
from .modulo_menu_ferramenta import MenuFerramenta as f

class MenuInicial():
    def adicionar(self):
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("&Arquivo")
        mp = [
            p.menu_arquivo_sair(self)
        ]

        # p.menu_django(self), p.menu_service(self), p.menu_radio(self),
        #       p.menu_arquivo(self),p.menu_cheat(self), p.menu_evolucao(self),
        #       p.menu_zzz(self), p.menu_tela(self), p.menu_pclima(self),
        for _ in range(len(mp)): mp[_]

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("&Ferramenta")
        mf = [
            f.menu_ferramenta_service(self)
        ]

        # p.menu_django(self), p.menu_service(self), p.menu_radio(self),
        #       p.menu_arquivo(self),p.menu_cheat(self), p.menu_evolucao(self),
        #       p.menu_zzz(self), p.menu_tela(self), p.menu_pclima(self),
        for _ in range(len(mf)): mf[_]
