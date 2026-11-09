#!/usr/bin/env python3
"""Tests de la semilla: la cabeza de miu-v14 es un commit del workflow.

Cada test reproduce un numero del README con los datos leidos por API
de GitHub el 2026-11-09 (Jaime393/miu-v14). Solo stdlib.
"""

import unittest

from cabeza_workflow_repro import (
    AUTO_MD,
    COMMITS,
    WORKFLOW,
    check_cabeza,
    check_rafaga,
    check_serie,
    check_sin_v30,
    check_v31,
    check_workflow_escribe_la_cabeza,
)


class TestSerie(unittest.TestCase):
    def test_trece_commits_un_dia(self):
        self.assertEqual(len(COMMITS), 13)
        self.assertEqual(
            {c[1][:10] for c in COMMITS}, {"2026-08-23"})

    def test_arco_22_min_52_s(self):
        # 16:24:04Z -> 16:46:56Z = 1372 s.
        self.assertIn("22 min 52 s", check_serie())

    def test_dos_rafagas(self):
        self.assertIn("2 commits en 4 s", check_rafaga())
        self.assertIn("11 en 16 s", check_rafaga())
        self.assertIn("22 min 32 s", check_rafaga())


class TestV31(unittest.TestCase):
    def test_diez_commits_un_archivo_cada_uno(self):
        v31 = [c for c in COMMITS if c[3].startswith("v31 completa")]
        self.assertEqual(len(v31), 10)
        self.assertIn("huecos 0-1 s", check_v31())

    def test_sin_v30(self):
        self.assertIn("v30 ausente", check_sin_v30())


class TestCabeza(unittest.TestCase):
    def test_cabeza_es_miu_tejedor(self):
        self.assertIn("0198a9d1", check_cabeza())
        self.assertIn("miu-tejedor", check_cabeza())

    def test_workflow_produce_la_cabeza(self):
        # Cada linea del guion que la cabeza reproduce.
        self.assertIn('echo "# MIU 16/16" > AUTO.md', WORKFLOW)
        self.assertIn('git config user.name "miu-tejedor"', WORKFLOW)
        self.assertIn('git config user.email "miu@local"', WORKFLOW)
        self.assertIn('git commit -m "MIU Auto"', WORKFLOW)
        self.assertIn("git push origin main", WORKFLOW)
        self.assertIn("8 s antes", check_workflow_escribe_la_cabeza())

    def test_auto_md_doce_bytes(self):
        self.assertEqual(AUTO_MD, "# MIU 16/16\n")
        self.assertEqual(len(AUTO_MD.encode("utf-8")), 12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
