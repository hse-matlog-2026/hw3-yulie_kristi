# This file is part of the materials accompanying the book
# "Mathematical Logic through Python" by Gonczarowski and Nisan,
# Cambridge University Press. Book site: www.LogicThruPython.org
# (c) Yannai A. Gonczarowski and Noam Nisan, 2017-2022
# File name: propositions/operators.py

"""Syntactic conversion of propositional formulas to use only specific sets of
operators."""

from propositions.syntax import *
from propositions.semantics import *

def to_not_and_or(formula: Formula) -> Formula:
    sub = {'T': Formula.parse('(p|~p)'), 'F': Formula.parse('(p&~p)'), '->': Formula.parse('(~p|q)'), '+': Formula.parse('((p|q)&~(p&q))'), '<->': Formula.parse('((~p|q)&(~q|p))'), '-&': Formula.parse('~(p&q)'), '-|': Formula.parse('~(p|q)')
    }
    return formula.substitute_operators(sub)

def to_not_and(formula: Formula) -> Formula:
    sub = {
        'T': Formula.parse('~(p&~p)'),
        'F': Formula.parse('(p&~p)'),
        '|': Formula.parse('~(~p&~q)'),
        '->': Formula.parse('~(p&~q)'),
        '+': Formula.parse('(~(p&q)&~(~p&~q))'),
        '<->': Formula.parse('(~(p&~q)&~(q&~p))'),
        '-&': Formula.parse('~(p&q)'),
        '-|': Formula.parse('(~p&~q)')
    }
    return formula.substitute_operators(sub)
    
def to_nand(formula: Formula) -> Formula:
    sub = {
        'T': Formula.parse('(p-&(p-&p))'),
        'F': Formula.parse('((p-&(p-&p))-&(p-&(p-&p)))'),
        '~': Formula.parse('(p-&p)'),
        '&': Formula.parse('((p-&q)-&(p-&q))'),
        '|': Formula.parse('((p-&p)-&(q-&q))'),
        '->': Formula.parse('(p-&(q-&q))'),
        '+': Formula.parse('((p-&(p-&q))-&(q-&(p-&q)))'),
        '<->': Formula.parse('(((p-&p)-&(q-&q))-&(p-&q))'),
        '-|': Formula.parse('(((p-&p)-&(q-&q))-&((p-&p)-&(q-&q)))')
    }
    return formula.substitute_operators(sub)

def to_implies_not(formula: Formula) -> Formula:
    sub = {
        'T': Formula.parse('(p->p)'),
        'F': Formula.parse('~(p->p)'),
        '&': Formula.parse('~(p->~q)'),
        '|': Formula.parse('(~p->q)'),
        '+': Formula.parse('((p->q)->~(q->p))'),
        '<->': Formula.parse('~((p->q)->~(q->p))'),
        '-&': Formula.parse('(p->~q)'),
        '-|': Formula.parse('~(~p->q)')
    }
    return formula.substitute_operators(sub)

def to_implies_false(formula: Formula) -> Formula:
    sub = {
        'T': Formula.parse('(F->F)'),
        '~': Formula.parse('(p->F)'),
        '|': Formula.parse('((p->F)->q)'),
        '&': Formula.parse('((p->(q->F))->F)'),
        '<->': Formula.parse('(((p->q)->((q->p)->F))->F)'),
        '+': Formula.parse('((((p->q)->((q->p)->F))->F)->F)'),
        '-&': Formula.parse('(((p->(q->F))->F)->F)'),
        '-|': Formula.parse('(((p->F)->q)->F)')
    }
    return formula.substitute_operators(sub)
