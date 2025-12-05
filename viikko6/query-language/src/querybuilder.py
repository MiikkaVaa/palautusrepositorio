from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, matchers=None):
        if matchers is None:
            self._matchers = []
        else:
            self._matchers = matchers

    def build(self):
        if not self._matchers:
            return All()
        if len(self._matchers) == 1:
            return self._matchers[0]
        return And(*self._matchers)

    def plays_in(self, team):
        return QueryBuilder(self._matchers + [PlaysIn(team)])

    def hasAtLeast(self, value, attr):
        return QueryBuilder(self._matchers + [HasAtLeast(value, attr)])
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(self._matchers + [HasFewerThan(value, attr)])
    
    def one_of(self, *builders):
        or_matchers = [builder.build() for builder in builders]
        return QueryBuilder(self._matchers + [Or(*or_matchers)])