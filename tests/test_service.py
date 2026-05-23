import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")

if SRC not in sys.path:
    sys.path.insert(0, SRC)

from service.sgflow_service import SGFlowService


class TestService(unittest.TestCase):
    def test_metricas_nao_limitam_em_dez(self):
        service = SGFlowService()

        for i in range(12):
            service.cadastrar_caminhao(f"ABC{i:04d}", "Ana", "Carga", "SP", 50, [])

        self.assertEqual(len(service.metricas), 12)

    def test_resumo_performance_tem_totais(self):
        service = SGFlowService()
        service.cadastrar_caminhao("ABC1D23", "Ana", "Carga", "SP", 50, [])

        resumo = service.resumo_performance()

        self.assertIn("tempo_total", resumo)
        self.assertIn("volume_total", resumo)
        self.assertIn("memoria_total", resumo)
        self.assertIn("memoria_media_mb", resumo)

    def test_descarga_sem_carga_bloqueia(self):
        service = SGFlowService()
        sucesso, mensagem = service.cadastrar_caminhao("QES4521", "Pedro", "Descarga", "Manaus", 100, [])
        self.assertFalse(sucesso)

    def test_exportar_metricas_txt(self):
        service = SGFlowService()
        service.cadastrar_caminhao("ABC1D23", "Ana", "Carga", "SP", 50, [])
        texto = service.exportar_metricas_txt()

        self.assertIn("SGFLOW - Relatório de Performance", texto)
        self.assertIn("Memória média", texto)


if __name__ == "__main__":
    unittest.main()
