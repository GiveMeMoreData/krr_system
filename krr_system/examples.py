from krr_system.domain import TimeDomainDescription, Fluent

example1 = TimeDomainDescription()
example1.initially(alive=True)
example1.causes("load", [Fluent(loaded= True), Fluent(jammed=False)])
example1.releases("load", Fluent(hidden=False))
example1.causes("jam", Fluent(jammed=True), conditions=Fluent(loaded=True))
example1.causes("shoot", Fluent(alive=False), conditions=[Fluent(loaded=True), Fluent(hidden=False), Fluent(jammed=False)])
example1.causes("shoot", [Fluent(loaded=False), Fluent(jammed=False)])
example1.duration("load", 2)
example1.duration("jam", 1)
example1.duration("shoot", 1)


example2 = TimeDomainDescription()
example2.initially(alive=True)
example2.causes("load", [Fluent(loaded= True), Fluent(jammed=False)])
example2.releases("load", Fluent(hidden=False))
example2.causes("jam", Fluent(jammed=True), conditions=Fluent(loaded=True))
example2.causes("shoot", Fluent(alive=False), conditions=[Fluent(loaded=True), Fluent(hidden=False), Fluent(jammed=False)])
example2.causes("shoot", [Fluent(loaded=False), Fluent(jammed=False)])
example2.duration("load", 2)
example2.duration("jam", 1)
example2.duration("shoot", 1)

example3 = TimeDomainDescription()
example3.initially(inspired=True, painted=False)
example3.causes("paint", [Fluent(painted=True), Fluent(inspired=False)])
example3.impossible("paint", conditions=Fluent(inspired=False))
example3.causes("pay", Fluent(painted=False))
example3.impossible("pay", conditions=Fluent(painted=False))
example3.releases("pay", Fluent(inspired=False))
example3.duration("paint", 2)
example3.duration("pay", 1)