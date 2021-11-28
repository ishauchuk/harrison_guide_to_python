names = ['Serg', 'Dasha', 'Alex']
print(names)
print(id(names))
names.sort()
print(names)
print(id(names))
print(names[0], names[1], sep=', ')

personal_my = tuple(['Ihar', 'Shauchuk', 29])
# print(personal_my)
personal_friend_1 = tuple(['Alex', 'Dukvalov', 29])
personal_friend_2 = tuple(['Serg', 'Charnukha', 29])
personal_friend_3 = tuple(['Darie', 'Vasko', 26])

people = []
people.append(personal_my)
people.append(personal_friend_1)
people.append(personal_friend_2)
people.append(personal_friend_3)
print(people)
people.sort()
print(people)

shekspir = """Prince. Rebellious subjects, enemies to peace,
    Profaners of this neighbour-stained steel-
    Will they not hear? What, ho! you men, you beasts,
    That quench the fire of your pernicious rage
    With purple fountains issuing from your veins!
    On pain of torture, from those bloody hands
    Throw your mistempered weapons to the ground
    And hear the sentence of your moved prince.
    Three civil brawls, bred of an airy word
    By thee, old Capulet, and Montague,
    Have thrice disturb'd the quiet of our streets
    And made Verona's ancient citizens
    Cast by their grave beseeming ornaments
    To wield old partisans, in hands as old,
    Cank'red with peace, to part your cank'red hate.
    If ever you disturb our streets again,
    Your lives shall pay the forfeit of the peace.
    For this time all the rest depart away.
    You, Capulet, shall go along with me;
    And, Montague, come you this afternoon,
    To know our farther pleasure in this case,
    To old Freetown, our common judgment place.
    Once more, on pain of death, all men depart.
              Exeunt [all but Montague, his Wife, and Benvolio].
"""

ralph = """
Those who are esteemed umpires of taste are often persons who have
acquired some knowledge of admired pictures or sculptures, and have an
inclination for whatever is elegant; but if you inquire whether they are
beautiful souls, and whether their own acts are like fair pictures, you
learn that they are selfish and sensual. Their cultivation is local, as
if you should rub a log of dry wood in one spot to produce fire, all the
rest remaining cold. Their knowledge of the fine arts is some study of
rules and particulars, or some limited judgment of color or form, which
is exercised for amusement or for show. It is a proof of the shallowness
of the doctrine of beauty as it lies in the minds of our amateurs, that
men seem to have lost the perception of the instant dependence of form
upon soul. There is no doctrine of forms in our philosophy. We were
put into our bodies, as fire is put into a pan to be carried about; but
there is no accurate adjustment between the spirit and the organ, much
less is the latter the germination of the former. So in regard to other
forms, the intellectual men do not believe in any essential dependence
of the material world on thought and volition. Theologians think it a
pretty air-castle to talk of the Spiritual meaning of a ship or a cloud,
of a city or a contract, but they prefer to come again to the solid
ground of historical evidence; and even the poets are contented with a
civil and conformed manner of living, and to write poems from the fancy,
at a safe distance from their own experience. But the highest minds of
the world have never ceased to explore the double meaning, or shall
I say the quadruple or the centuple or much more manifold meaning, of
every sensuous fact; Orpheus, Empedocles, Heraclitus, Plato, Plutarch,
Dante, Swedenborg, and the masters of sculpture, picture, and poetry.
For we are not pans and barrows, nor even porters of the fire and
torch-bearers, but children of the fire, made of it, and only the same
divinity transmuted and at two or three removes, when we know least
about it. And this hidden truth, that the fountains whence all this
river of Time and its creatures floweth are intrinsically ideal and
beautiful, draws us to the consideration of the nature and functions of
the Poet, or the man of Beauty; to the means and materials he uses, and
to the general aspect of the art in the present time.
"""

shekspir_1 = shekspir.lower()
ralph_1 = ralph.lower()

print("Both words are:\n\t", *list(set(shekspir_1.split(' ')) & set(ralph_1.split(' '))), sep=' ')
print("Unique words are:\n\t", *list(set(shekspir_1.split(' ')) ^ set(ralph_1.split(' '))), sep=' ')
print("Unique words are:\n\t", *list(set(ralph_1.split(' ')) ^ set(shekspir_1.split(' '))), sep=' ')
