#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import CorrMatmul as correct
import matmul as student


class Testmatmul(unittest.TestCase):
    def test0_None(self):
        matrix1 = [[1,2,3],
                [4 ,5,6],
                [7 ,8,9],
                [10,11,12]]
        matrix2 = [[9,8,7],
                [6,5,4],
                [3,2,1],
                [1,2,3]]    
        rep = _("Votre fonction a retourné None pour {} et {} comme argument. Cela implique probablement qu'il manque un return dans votre code.")
        try:
            student_ans = student.matmul(matrix1, matrix2)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {} et {}".format(type(e), e, matrix1, matrix2))
        self.assertIsNotNone(student_ans, rep.format(matrix1, matrix2))

    def test1_matmul_0(self):
        matrix1 = [[1,5,3],
                [4 ,5,5],
                [7 ,3,9]]
        matrix2 = [[3,2,7],
                [1,6,4],
                [3,2,1]]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} et {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.matmul(matrix1, matrix2)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {} et {}".format(type(e), e, matrix1, matrix2))
        correct_ans = correct.matmul(matrix1, matrix2)
        self.assertEqual(student_ans, correct_ans,
                        rep.format(student_ans, matrix1, matrix2, correct_ans))

    def test1_matmul_pos(self):
        matrix1 = [[1,2,3],
                [4 ,5,6],
                [7 ,8,9]]
        matrix2 = [[9,8,7],
                [6,5,4],
                [3,2,1]]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} et {} comme argument positif alors que la réponse attendue est {}")
        try:
            student_ans = student.matmul(matrix1, matrix2)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {} et {}".format(type(e), e, matrix1, matrix2))
        correct_ans = correct.matmul(matrix1, matrix2)
        self.assertEqual(student_ans, correct_ans,
                            rep.format(student_ans, matrix1, matrix2, correct_ans))

if __name__ == '__main__':
    unittest.main()