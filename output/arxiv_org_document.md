# Arxiv Org Document

*Converted from PDF on 2025-07-06 18:24:50*


## Page 1

TAUP-287908 WIS/03/10-Feb-DPPA hep-th/yymmnnn Non-Perturbative Field Theory-
From two dimensional conformal field theory to QCD in four dimensions
### Yitzhak Frishman
Department of Particle Physics and Astrophysics The Weizmann Institute of Science Rehovot 76100, Israel
Jacob Sonnenschein School of Physics and Astronomy
The Raymond and Beverly Sackler Faculty of Exact Sciences
Tel Aviv University, Ramat Aviv 69978, Israel
### Abstract
This note is based on the summary of our book entitled “Non-perturbative field theory-
from two dimensional conformal field theory to QCD in four dimensions”, published
recently by Cambridge University Press. It includes 436 pages.
The book provides a detailed description of the tool box of non-perturbative tech-
niques, presents applications of them to simplified systems, mainly of gauge dynamics in
two dimensions, and examines the lessons one can learn from those systems about four dimensional QCD and hadron physics.
In particular the book deals with conformal invariance, integrability, bosonization,
large N, solitons in two dimensions and monopoles and instantons in four dimensions,
confinement versus screening and finally the hadronic spectrum and scattering.
We also attach the table of contents and the list of references of the book.
We would be grateful for any comments or suggestions related to the
material in the book. These may be incorporated in a possible future edition. They may be sent via the e-mails below. 0102 yaM 01 ]ht-peh[ 2v9584.4001:viXra

## Page 2

yitzhak.frishman@weizmann.ac.il cobi@post.tau.ac.il 2

## Page 3

1 General
Relativistic Quantum Field Theory has been very successful in describing strong, electro-
magnetic and weak interactions, in the region of small couplings by using perturbation
theory, within the framework of the Standard Model.
However, the region of strong coupling, like the hadronic spectrum and various scat-
tering phenomena of hadrons within QCD, is still largely unsolved.
A large variety of methods have been used to address this question, including QCD
sum rules, lattice gauge simulations, light cone quantization, low energy effective La-
grangians like the Skyrme model and chiral Lagrangians, large N approximation, tech-
niquesofconformalinvariance,integrablemodelapproach,supersymmetricmodels,string
theory approach etc. In spite of this major effort the gap between the phenomenology
and the basic theory has been only partially bridged, and the problem is still open.
The goals of this book are to provide a detailed description of the tool box of non-
perturbative techniques, to apply them on simplified systems, mainly of gauge dynamics
in two dimensions, and to examine the lessons one can learn from those systems about
four dimensional QCD and hadron physics.
The study of two dimensional models in order to improve the understanding of four
dimensionalphysicalsystemswasfoundtobefruitful. Thiscanbeachievedfollowingtwo
differentapproaches. Inthefirstoneappliesnon-perturbativemethodsonthesimplertwo
dimensional model, extract the physical behavior and extrapolate it to four dimensions.
The second is based on gaining insight on the methods by first applying them first in
two dimensions, then apply the analogous methods on the four dimensional system and
deduce certain physical properties of it.
This follows two directions, one is the utilization of non-perturbative methods on
simpler setups and the second is extracting the physical behavior of hadrons in one space dimension.
Obviously, physics in two dimensions is simpler than that of the real world since the
underlying manifold is simpler and since the number of degrees of freedom of each field
is smaller. There are some additional simplifying features in two dimensional physics.
In one space dimension there is no rotation symmetry and no angular momentum. The
light cone is disconnected and is composed of left moving and right moving branches.
Therefore, massless particles are either on one branch or the other. These two properties
are the basic building blocks of the idea of transmutation between systems of different
statistics. Also, the ultra-violet behavior is more convergent in two dimensions, making
for instance QCD a superconvergent theory. 2
In this summary note we go over several notions, concepts and methods with an
emphasis on the comparison between the two and four dimensional worlds and on what
one can deduce about the latter from the former. In particular we deal with conformal 1

## Page 4

invariance, integrability, bosonization, large N, solitons in two dimensions and monopoles
and instantons in four dimensions, confinement versus screening, and finally the hadronic
spectrum and scattering. We end this note with an brief outlook which includes several
comments on (i) further progress in the application of the methods discussed in the
book, (ii) applications to other domains and developments in gauge dynamics due to
other methods. The table of content of the book and the bibliography of the book are added as appendices. 2 Conformal Invariance
From the onset there is a very dramatic difference between conformal invariance in two
and four dimensions. The former is characterized by an infinite dimensional algebra, the
Virasoro algebra, whereas the latter is associated with the finite dimensional algebra of
SO(4,2). This basic difference stems from the fact that whereas the conformal transfor-
mations in four dimensions are global, in two dimensions the parameters of conformal
transformations are holomorphic functions (or anti-holomorphic). Nevertheless there are
several features of conformal invariance which are common to the two cases. We will now
compare various aspects of conformal invariance in two and four dimensions.
- The notion of a primary field and correspondingly a highest weight state is used
both in two dimensional conformal field theories as well as for the four dimensional
collinear algebra. 1 It is expressed for the former as
L [φ(0)|0 >] = h[|φ(0)|0 >] L [φ(0)|0 >] = 0, n > 0 (1) 0 n and for the latter
L [Φ(0)|0 >] = j[|Φ(0)|0 >] L [Φ(0)|0 >] = 0, (2) 0 −
The difference is of course the infinite set of annihilation operators L versus the n
single annihilation operator L in four dimensions. −
- The COPE, the conformal operator product expansion, has a compact form in two dimensional CFT
Ø (z,z¯)Ø (w,w¯) ∼ (cid:88) C (z −w)h k −hi−hj(z¯−w¯)h¯ k −h¯ i−h¯ jØ (w,w¯) (3) i j ijk k k
1 Define the lightcone coordinate x via xµ = x nµ + x nµ + xµ where nµn = nµn = − − + + − T + +µ − −µ
0 nµn = 1. The collinear group which is an SL(2,R) group, is defined by the following three + −µ
transformations x →x +a , x →ax and x → x− where a˜µ =anµ − − − − − − 1+2a˜x− 2

## Page 5

where C are the product coefficients while in four dimensions it reads ijk A(x)B(0) = (cid:88) ∞ C (cid:18) 1 (cid:19)1/2(tA+tB−tn) xn − +s1+s2−sA−sB n x2 B(j −j +j ,j −j +j ) n=0 A B n B A n (cid:90) 1
× duu(jA−jB+jn−1)(1−u)(jB−jA+jn−1)Oj1,j2(ux ) (4) n − 0
where the definitions of the various quantities are in Chapter 17 of the book. Again
there is a striking difference between the simple formula in two dimensions and the complicated one in four dimensions.
- As an example let’s compare the OPE of two currents. As is described in Chapter
3, the expression in two dimensions reads kδab fabJc(w) Ja(z)Jb(w) = +i c +finite terms (5) (z −w)2 (z −w)
for any non-abelian group, and in particular for the abelian case the second term
on the RHS is missing. For comparison the OPE of the transverse components of
the electromagnetic currents given in Chapter 17 takes the form JT(x)JT(0) ∼ (cid:80)∞ C (cid:16) 1 (cid:17)(6−tn)/2
```
(−ix )n+1 Γ(2jn) (cid:82)1du[u(1−u)]jn−1Q1,1(ux ) n=0 n x2 − Γ(jn)Γ(jn) 0 n − (6)
```
- The conformal Ward identity associated with the dilatation operator in four di- mensions N
```
(cid:88) (l +γ(g∗)+x ∂ ) < Tφ(x )...φ(x ) >= 0 (7) φ i i 1 N i
```
where l is the canonical dimension and γ(g∗) is the anomalous dimension, seems φ
very similar to the one in two dimensions (cid:88)
```
(z ∂ +h ) < 0|φ (z ,z¯ )...φ (z ,z¯ )|0 >= 0 (8) i i i 1 1 1 n n n i
```
In both cases one has to determine the full quantum conformal dimensions of the
various operators. However, as is shown in Chapter 2, in certain CFT models,
like the unitary minimal models, there are powerful tools based on unitarity which
enable us to determine exactly the dimensions h of all the primary operators and i
hence all the operators of the model. On the other hand, it is a non-trivial task 3

## Page 6

to determine the anomalous dimensions in other models in two dimension, and of
course of four dimensional operators. In certain supersymmetric theories there are
operators whose dimension is protected 2, but generically one has to use pertur-
bative calculations to determine the anomalous dimensions of gauge theories to a given order in the coupling constant.
Using the Ward identity one can extract the form of the two point function of
operators of spin s in four dimensions. It is given by
```
(cid:34) (cid:35)l +γ(g∗)(cid:32) (cid:33)s 1 φ (x −x )
```
```
< φ(x )φ(x ) >= N (g∗)(µ∗)−2γ(g∗) 1 2 + (9) 1 2 2 (x −x )2 (x −x ) 1 2 1 2 −
```
The corresponding two point function in two dimensions, which depends only on
the conformal dimension of the operator h, reads c 2
G (z ,z¯ ,z ,z¯ ) ≡< 0|φ (z ,z¯ )φ (z ,z¯ )|0 >= (10)
2 1 1 2 2 1 1 1 1 2 2 (z 1 −z 2 )2h1(z¯ 1 −z¯ 2 )2h¯ 1
- As for higher point functions, it is shown in Chapter 2 that one can use the local
Ward identities together with Virasoro null vectors to write down a partial differ-
ential equations that determine the correlators. The result for a four point function
was later used to determine the four point function of the Ising model.
- Two dimensional conformal field theories are further invariant under affine Lie
algebra transformations, and as is shown in Chapter 3 those can be combined with
null vectors to derive the so called Knizhnik-Zamolodchikov equations, which can
beusedtosolveforthefour-pointfunctionoftheSU(N)WZWmodel(seeChapter
4). This type of differential equations that fully determine correlation functions are
obviously absent in four dimensional interacting conformal field theories. 3 Integrability
Integrability is discussed in Chapter 5 in the context of two dimensional models and
in Chapter 18 in four dimensional gauge theories. For systems with a finite number of
degrees of freedom, like spin chain models, there is a finite number of conserved charges,
equal of course to the number of degrees of freedom. For integrable field theories there is
an infinite countable number of conserved charges. Furthermore, the scattering processes
of those models always involve a conservation of the number of particles.
2Ofcoursebesidestheusualoperatorswithnoanomalousdimensions,likeconservedcurrents,energy- momentum tensor, and the like 4

## Page 7

Spin chain Planar High energy N = 4 SYM scattering in QCD Cyclic Single trace Reggeized guons spin chain operator in t-channel Spin Field operator SL(2) spin at a site Number of Number of Number of sites operators gluons Hamiltonian Anomalous dilatation H
BFKL operator Energy Anomalous dimension ∼ 1logA λ logs eigenvalue g−2δD evolution dilatation the total rapidity time variable logs
Zero momentum U = 1 Cyclicity constraint
Table 1: spin chain structure of the two dimensional model and the four dimensional
gauge systems of N = 4 SYM and of high-energy behavior of scattering amplitudes in QCD.
In two dimensions we have encountered continuous integrable models like the sine-
Gordon model as well as discretized ones like the XXX spin chain model. The integrable
sectorsofgaugedynamicalsystemsarebasedonidentifyinganexactmapbetweencertain
properties of the systems and a spin chain structure. In two dimensions the spin chain
models follow from a discretization of the space coordinate, by placing a spin variable on
each site that can take several values and imposing periodicity. In the four dimensional
```
N = 4 super YM theory the spin chain corresponds to a trace of field operators and in
```
the process of high-energy scattering it is a “chain” of reggeized gluons exchanged in the
t-channel of a scattering process. A summary of the comparison among the basic two
dimensional spin chain, the “spin chains” associated with the planar N = 4 SYM, and
the high energy scattering in QCD, is given in table 1. . A powerful method to solve
all these spin chain models is the use of the algebraic Bethe ansatz. This is discussed in
details for the the XXX model in Chapter 5. The solutions of the energy eigenvalues 1/2
needed for the high energy scattering process was based on generalizing this method to
the case of spin s Heisenberg model and for the N = 4 to the case of an SO(6) invariance.
There is one conceptual difference between the spin chains of the two dimensional
models and those associated with the N = 4 SYM in four dimensions. In the former
the models are non conformal, involving a scale, and hence also with particles and an S- 5
| Spin chain | Planar
N = 4 SYM | High energy
scattering in QCD |
| --- | --- | --- |
| Cyclic
spin chain | Single trace
operator | Reggeized guons
in t-channel |
| Spin
at a site | Field operator | SL(2) spin |
| Number of
sites | Number of
operators | Number of
gluons |
| Hamiltonian | Anomalous dilatation
operator | H
BFKL |
| Energy
eigenvalue | Anomalous dimension
g−2δD | ∼ 1logA
λ logs |
| evolution
time | dilatation
variable | the total rapidity
logs |
| Zero momentum U = 1 | Cyclicity constraint |  |


## Page 8

matrix. Theintegrablesectorsoffourdimensionalgaugetheories, however, areconformal invariant.
The study of integrable models in two dimensions is quite mature, whereas the ap-
plication of integrability to four dimensional systems is at an infant stage. The concepts
of multi-local charges and of quantum groups, discussed in Chapter 5, have been applied
only slightly to gauge dynamical systems in four dimensions. 4 Bosonization
Bosonization is the formulation of fermionic systems in terms of bosonic variables and
fermionization is just the opposite process. The detailed discussion is in Chapter 6. The
study of bosonized physical systems offers several advantages:
```
(1) It is usually easier to deal with commuting fields rather than anti-commuting ones.
```
```
(2) In certain examples, like the Thirring model, the fermionic strong coupling regime
```
turns into the weak coupling one in its bosonic version, the Sine-Gordon model.
```
(3) The non-abelian bosonization, especially in the product scheme, offers a separation
```
between colored and flavored degrees of freedom, which is very convenient for analyzing the low lying spectrum.
```
(4) Baryons composed of N quarks are a many-body problem in the fermion language, C
```
while simple solitons in the boson language.
```
(5) One loop fermionic computations involving the currents turn into tree level consider-
```
ation in the bosonized version. The best known example of the latter are the chiral (or axial) anomalies.
In four dimensions, spin is obviously non-trivial and one cannot constitute generically
a bosonization equivalence. However, in certain circumstances a four dimensional system
can be described approximately by fields that depend only on the time and the radial
direction. In those cases one can apply the bosonization technique. Examples of such sce-
narios are monopole induced proton decay, and fractional charges induced on monopoles
by light fermions. In these cases the relevant degrees of freedom are in an s-wave and
hence taken to depend only on the time and the radial direction. This enables one to use
the corresponding bosonized field. There is a slight difference with two dimensions, as
the radial coordinate goes from zero to infinity, so ”half” a line. Appropriate boundary
conditions enable to use a reflection, so to extend to a full line. 5 Topological field configurations
- The topological charges in any dimensions are conserved regardless of the equations
of motion of the corresponding systems. In two dimensions it is very easy to write 6

## Page 9

down a current which is conserved without the use of the equations of motion.
This is referred to as a topological conservation. Consider a scalar field φ or its
non-ablelian analog which is expressed in terms of a group element g ∈ G of a non-
abelian group G, then the following currents are abelian and non-abelian conserved currents
```
J = (cid:15) ∂νφ J = (cid:15) g−1∂νg (11) µ µν µ µν
```
Recall that for a system that admits, for instance in abelian case, also a current
```
J = ∂ φ that is conserved upon the use of the equations of motion, one can then µ µ
```
replace the two currents with left and right conserved currents J = ∂ φ or J = ∂φ ± ± ¯ ¯
and J = ∂φ using complex coordinates. The charge associated with the topological conserved current is given by (cid:90)
```
Q = dxφ(cid:48) = [φ(t,+∞)−φ(t,−∞)] ≡ φ −φ (12) top + −
```
where the space dimension is taken to be R. For a compactified space dimension,
namely an S1 this charge vanishes, except for cases where the field is actually an
angle variable, in which case the charge is 2π. The latter appears in the case of
U(1) gauge theory in two dimensions, where there is a winding number.
- Obviouslyonecannothavesuchtopologicallyconservedcurrentsandchargesinfour
dimensions. However, for theories that are invariant under a non-abelian group,
one can construct also in four dimensions a topological current and charge, like for
the cases of Skyrmions, magnetic monopoles and instantons. For the Skyrmions the topological current is given by i(cid:15)µνρσ Jµ = Tr[L L L ] (13) skyre 24π2 ν ρ σ where L = U†∂ U with U ∈ SU(N ) µ µ f
- The topological charges, for compact spaces, are the winding numbers of the corre-
sponding topological configurations. For a compact one space dimension, we have
the map of S1 → S1 related to the homotopy group π (S1). In two space dimen- 1
sions, the windings are associated with the map S → SG/H, as for the magnetic 2 2
monopoles. For three space dimensions, it is S3 → S3 for the Skyrmions at N = 2, f
and the non-abelian instantons for the gauge group SU(2). The topological data
of the various models is summarized in table 2.
- AccordingtoDerrick’stheorem,foratheoryofascalarfieldwithanordinarykinetic
term with two derivatives, and any local potential at D ≥ 2, the only non-singular
time-independent solutions of finite energy are the vacua. However, as is described 7

## Page 10

Table 2: Topological classical field configurations in two and four dimensions classical dim. map topological field current soliton two (cid:15)µν∂ φ ν
baryon two S1 → S1 (cid:15)µνTr[g−1∂ g]; g ∈ U(N ) ν f
Skyrmion four S3 → S3 i(cid:15)µνρσTr[L L L ] 24π2 ν ρ σ
monopole four S2 → S2 1 (cid:15) (cid:15)abc∂νΦ ˆa∂ρΦ ˆb∂σΦ ˆc space G/H 8π µνρσ
instanton four S3 → S3 i(cid:15)µνρσTr[A ∂ A + 2A A A ] s g 16π2 ν ρ σ 3 ν ρ σ
in Chapters 20-22, there are solitons in the form of Skyrmions and monopoles and
instantons. Those configurations bypass Derrick’s theorem by introducing higher
derivative terms or including non-abelian gauge fields.
- As is emphasized in Chapter 20, the extraction of the baryonic properties in the
Skyrme model is very similar to the one for baryons in the bosonized theory in two
dimensions. Unlikethelatterwhichisexactinthestrongcouplinglimit, onecannot
derive the former starting from the underlying theory. Another major difference
between the two models is of course the existence of angular momentum only in the four dimensional case.
- A non-trivial task associated with topological configurations is the construction of
configurations that carry multipole topological charge, for instance a multi-baryon
statebothofthebosonizedQCD aswellasoftheSkyrmemodel, amulti-monopole 2
solution and a multi-intanton solution. For the two dimensional baryons (see Chap-
ter 13) the construction is a straightforward generalization of the the configura-
tion of baryon number one. For the multi-monopoles solutions the book describes
Nahm’s construction, and for the multi-intantons the ADHM construction. These
constructions, which are in fact related, are much more complicated than that for the two dimensional muti-baryons.
- A very important phenomenon that occurs in both two and four dimensions is the
strong-weak duality, and the duality between a soliton and an elementary field.
In two dimensions we have encountered this duality in the relation between the
Thirring model and the sine-Gordon model, where the coupling of the latter β is
related to that of the former g as (Chapter 6) β2 1 = (14) 4π 1+ g π
This also relates the elementary fermion field of the Thirring model with the soliton
of the sine-Gordon model. In particular for g = 0 corresponding to β2 = 4π, the 8
| classical
field | dim. | map | topological
current |
| --- | --- | --- | --- |
| soliton | two |  | (cid:15)µν∂ φ
ν |
| baryon | two | S1 → S1 | (cid:15)µνTr[g−1∂ g]; g ∈ U(N )
ν f |
| Skyrmion | four | S3 → S3 | i(cid:15)µνρσTr[L L L ]
24π2 ν ρ σ |
| monopole | four | S2 → S2
space G/H | 1 (cid:15) (cid:15)abc∂νΦ ˆa∂ρΦ ˆb∂σΦ ˆc
8π µνρσ |
| instanton | four | S3 → S3
s g | i(cid:15)µνρσTr[A ∂ A + 2A A A ]
16π2 ν ρ σ 3 ν ρ σ |


## Page 11

ThirringmodeldescribesafreeDiracfermion,whilethesolitonofthecorresponding
sine-Gordon theory is the same fermion in its bosonization disguise. An analog
in four dimensions is the Olive-Montonen duality discussed in Chapter 21, which
relates the electric charge e with the magnetic one e = 4π, where the former is M e
carried by the elementary states W± and the latter by the magnetic monopoles. 6 Confinement versus screening
The naive intuition tells us that dynamical quarks in the fundamental representation
can screen external sources in the fundamental representation, dynamical adjoint quarks
can screen adjoint sources, but that dynamical adjoint cannot screen fundamentals. It
turns out that in two dimensions this is not the case, and massless adjoint quarks can
screen an external source in the fundamental representation. Moreover any massless
dynamical field will necessarily be in the screening phase. The argument is that in all
cases considered in the book we have found that the string tension is proportional to the mass of the dynamical quarks σ ∼ mg (15)
where m is the mass of the quark and g is the gauge coupling, and hence for the massless
case it vanishes. This is shown in Chapter 14 based on performing a chiral rotation
that enables us to eliminate the external sources and compute the string tension as the
difference between the Hamiltonian of the system with the external sources and the one without them namely σ =< H > − < H > (16) 0
It seems as if the situation in two dimensions is very different than in four dimensions.
From the onset there is a dramatic difference between two and four dimensions relating to
the concept of confining theory. In two dimensions both the coulomb (abelian) potential
and the non-abelian one are linear with the separation distance L whereas obviously the
coulomb potential between two particles behaves like 1/L while the confining one is linear
with L. However, that does not explain the difference between two and four dimensions,
it merely means that in two dimensions the coulomb and confining potentials behave in
the same manner. The determination of the string tension in two dimensions cannot be
repeated in four dimensions. The reason is that in the latter case the anomaly is not
linear in the gauge fields and thus one cannot use the chiral rotation to eliminate the
externalquarkanti-quarkpair. Thatdoesnotimplythatthesituationinfourdimensions
differs from the two dimensional one, it just means that one has to use different methods
to compute the string tension in four dimensions. 9

## Page 12

What are the four dimensional systems that might resemble the two dimensional case
of dynamical adjoint matter and external fundamental quarks? A system with external
quarks in the fundamental representation in the context of pure YM theory seems a
possible analog since the dynamical fields, the gluons, are in the adjoint representation,
though they are vector fields and not fermions. An alternative is the N = 1 SYM where
inadditiontothegluonstherearealsogluinoswhicharemajoranafermionsintheadjoint
representation. Both these cases should correspond to the massless adjoint case in two
dimensions. The latter admits a screening behavior whereas the four dimensional models
seem to be in the confining phase. This statement is supported by several different types
of calculations in particular for the non supersymmetric case this behavior is found in lattice simulations.
At this point we cannot provide a satisfactory intuitive explanation why the behavior
in two and four dimensions is so different. There is also no simple picture of how the
massless adjoint dynamical quarks in two dimensions are able to screen external charges in the fundamental representation.
It is worth mentioning that there is ample evidence that four dimensional hadronic
physics is well described by a string theory. This is based for instance on realizing that
mesons and baryons in nature admit Regge trajectory behavior which is an indication of
a stringy nature. Any string theory is by definition a two dimensional theory and hence a
verybasicrelationbetweenfourdimensionalhadronphysicsandtwodimensionalphysics.
In addition to the ordinary string tension which relates to the potential between a
quark and anti-quark in the fundamental representation, one defines the k string that
connects a set of k quarks with a set of k anti-quarks. This object has been examined
in four dimensional YM as well as four dimensional N = 1 SYM. These two cases
seem to be the analog of the two dimensional QCD theory with adjoint quarks and
with external quarks in a representation that is characterized by k boxes in the Young
tableau description. In Chapter 14 we present an expression for the string tension as
a function of the representation of the external and dynamical quarks and in particular
for dynamical adjoint fermions and external quarks in the k representation. If there
is any correspondence between the four dimensional adjoint matter field and the two
dimensional adjoint quarks it must be with massive adjoint quarks since for the massless
case, as was mentioned above, the two dimensional string tension vanishes whereas the
four dimensional one does not. Thus one may consider a correspondence for a softly
broken N = 1 case where the gluinos are massive.
In two dimensions for the pure YM case we found that the string tension behaves like
σ ∼ g2k2 while a Wilson line calculation yields σ ∼ g2C (R), where C (R) is the second ext 2 2
Casimir operator in the R representation of the external quarks. For the QCD case of 10

## Page 13

general k external charges and adjoint dynamical quarks we found πk σ2d ∼ sin2( ) (17) k N
whereas in four dimensions it is believed that for general k, the string tension either
follows a Casimir law or a sinusoidal rule k(N −k) πk σcas ∼ σsin ∼ sin( ) (18) k N k N
As expected all these expressions are invariant under k → N −k which corresponds
for antisymmetric representations replacing a quark with an anti-quark.
7 Hadronic phenomenology of two dimensions versus four dimensions
QCD was addressed first in the fermionic formulation in the seminal work ’t Hooft 2
where the mesonic spectrum in the large N limit was determined. In the book we have C
presented three additional approaches to the hadronic spectra in two dimensions:(i) the
currentization method for massless quarks for the entire plane of N and N ,(ii) the C f
DLCQ approach to extract the mesonic spectrum for the case of fundamental as well
as adjoint quarks and finally (iii) the bosonized formulation in the strong coupling limit
to determine the baryonic spectrum. As for the four dimensional hadronic spectrum
we described in the book the use of the large N planar limit and the analysis of the C
baryonic world using the Skyrme model. It is worth mentioning again that whereas in
the four dimensional case the Skyrme approach is only an approximated model derived
by an “educational guess”, in two dimension the action in the strong coupling regime is exact. 7.1 Mesons
As was just mentioned the two dimensional mesonic spectrum was extracted using the
large N approximation in the fermionic formulation for N = 1 (’t Hooft model), also C f
by using the currentization for massless quarks and the DLCQ approach that can be
applied for both the cases of quarks in the fundamental representation and the adjoint
representation. For the particular region of N >> N and m = 0, the fermionic large N C f c
and the currentization treatments yielded identical results. In fact this result is achieved
also using the DLCQ method for adjoint fermions upon a truncation to a single parton
and replacing g2 with 2g2 (see Chapter 12). For massive fundamental quarks the DLCQ 11

## Page 14

results match very nicely those of lattice simulations and the large N calculations, as c
can be seen from figures 12.1 and 12.2 in the book.
### Inallthesemethodsthecorrespondingequationsdonotadmitexactanalyticsolutions
for the whole range of parameters and thus one has to resort to numerical solutions,
however, incertaindomainsonecandeterminetheanalyticbehaviorofthewavefunctions and masses.
The spectrum of mesons in two dimensions is characterized by the dependence of
the meson masses M on the gauge coupling g, the number of colors N , the number mes c
of flavors N , the quark mass m , and the excitation number n. In four dimensional f q
QCD the meson spectra depend on the same parameters apart from the fact that Λ
# QCD
the QCD scale is replacing the two dimensional gauge coupling. The following lines
summarize the properties of the spectrum:
- The highly excited states n >> 1, where n is the excitation number, are character- ized by M2 ∼ πg2N n (19) mes c
This seems to fit the behaviors of mesons in nature. This behavior is referred to as
a Regge trajectory and it follows easily from a bosonic string model of the meson.
Following this analogy, the role of the string tension in two dimensional model is
played by g2N . This seems to be in contradiction with the statement that the c string tension is proportional to m g. q
It is very difficult to derive the Regge trajectory behavior from direct calculations in four dimensional QCD.
- The opposite limit of low lying states and in particular the ground state can be
deduced in the limit of large quark masses, namely m >> g and small quark q
masses g >> m . For the ground state in the former limit we find q M0 ∼ = m +m (20) mes 1 2
where m are the masses of the quark and anti-quark. In the opposite limit of i m << g q (cid:115) π g2N (M0 )2 ∼ = c (m +m ) (21) mes 3 π 1 2
For the special case of massless quarks we find a massless meson. This is very
reminiscent of the four dimensional picture. For the massless case this should 12

## Page 15

compare with the massless pions and for small masses this is similar to the pseudo- Goldstone boson relation where ¯ < ψψ > m2 ∼ (m +m ) (22) π f2 1 2 π
- The ’t Hooft model cannot be used to explore the dependence on N the number f
of flavors. This can be done from the ’t Hooft like equations derived in Chapter
## 11. It was found out that for the first massive state there is a linear dependence of the meson mass squared on N f M2 ∼ N (23) mes f
We are not aware of a similar behavior of the mesons in four dimensions.
- The ’t Hooft model provides the solution of the meson spectrum in the planar limit
in two dimensions. The planar, namely large N limit, in four dimensions is too c
complicated to be similarly solved. As explained in Chapter 19 one can extract
the scaling dependence in N of certain hadronic properties like the mass the size c
and scattering amplitude, but the full determination of the hadronic spectrum
and scattering is still unresolved. A tremendous progress has been made in the
understanding of the supersymmetric theory of N = 4 partly by demonstrating
that certain sectors of it can be described by integrable spin chain models (see Chapter 18).
- As is demonstrated in Chapter 12 the DLCQ method has been found very effec-
tive to address the spectrum of mesons of two dimensional QCD. This raises the
question of whether one can use the DLCQ method to handle the spectrum of four
dimensional QCD. This task is clearly much more difficult. En route to the extrac-
tion of the hadronic spectrum of QCD an easier system has been analyzed. It is 4
that of the collinear QCD (see Chapter 17) where in the Hamiltonian of the system
one drops off all interaction terms that depend on the transverse momenta. In this
effective two dimensional setup the transverse degrees of freedom of the gluon are
retained in the form of two scalar fields. This system which was not described in
the book has actually been solved and complete bound and continuum spectrum
were extracted as well as the Fock space wavefunctions. 7.2 Baryons
Chapter 13 of the book describes the spectrum of baryons in multiflavor two dimensional
QCD in the strong coupling limit mq → 0. The four dimensional baryonic spectrum is ec 13

## Page 16

Table 3: Scaling of Baryon masses with N in two and four dimensions C two dimensions four dimensions Classical baryon mass N N
C C Quantum correction N0 N−1
# C C
discussed in the large N limit in Chapter 19 and using the Skyrme model approach in C
Chapter20. Wewouldlikenowtocomparethesespectraandtoinvestigatethepossibility
of predicting four dimensional baryonic properties from the simpler two dimensional
model. In the former case the mass is a function of the QCD scale Λ , the number of
# QCD
colors N and the number of flavors N , and in the latter it is a function of e ,N and C f c C
N . Thus it seems that the dimensionful gauge coupling in two dimensions is the analog f of Λ in four dimensions.
# QCD
- In two dimensions, in the strong coupling limit, the mass of the baryon was found to be
```
(cid:115) 2N √ (cid:115) (cid:18) π (cid:19)3 (cid:34) (N −1) (cid:35) E = 4m C +m 2 C −N2 F (24) π N 2 C 2N
```
C F where the classical mass m is given by √ e N m = [N C cm q ( c√ F )∆C]1+ 1 ∆C (25) 2π N2−1
with ∆ = C . Due to the fact that in two dimensions there is no spin, the C NC(NC+NF)
structure of the spectrum with respect to the flavor group is obviously different in
two and four dimensions. For instance the lowest allowed state for N = N = 3 C f
is in two dimensions the totally symmetric representation 10, where as it is the
mixed representation 8 in four dimensions.
- Let us discuss now the scaling with N in the large N limit. In two dimensions the
# C C
classical term behaves like N , while the quantum correction like 1. The classical C
result is in accordance with the result, derived when the large N expansion is ap-
plied to the baryonic system (Chapter 19), and with the Skyrmion result (Chapter
20). However, whereas in two dimensions the quantum correction behaves like N0 c
namely suppressed by a factor of 1 , in four dimensions it behaves like 1 namely
### Nc Nc
a suppression of 1 . This is summarized in table 3. N2 c
- In terms of the dependence on the number of flavors, it is interesting to note that
both in two dimensions and in four dimensions, the contribution to the mass due to
the quantum fluctuations is proportional to the second Casimir operator associated
with the representation of the baryonic state under the SU(N ) flavor group 3. f 3compare (24) with (68) of Chapter 20 14
|  | two dimensions | four dimensions |
| --- | --- | --- |
| Classical baryon mass | N
C | N
C |
| Quantum correction | N0
C | N−1
C |


## Page 17

Table 4: flavor content of two dimensional and four dimensional baryons two dimensions four dimensions state value state value (cid:104)u¯u(cid:105) ∆+ 1 p 2 2 5 (cid:68) d ¯ d (cid:69) ∆+ 1 p 11 3 30 (cid:104)s¯s(cid:105) ∆+ 1 p 7 6 30 (cid:104)s¯s(cid:105) ∆++ 1 ∆ 7 6 24 (cid:104)s¯s(cid:105) Ω− 5 24
- Another property of the baryonic spectrum that can be compared between the two
and four dimensional cases is the flavor content of the various states. In Chapter
13 we presented the u¯u,d ¯ d and s¯s content for the ∆+ and ∆++ states. Recall that
in the two dimensional model for N = N = 3 we do not have a state in the 8 C f
representation but only in the 10 so strictly speaking there is no exact analog of
the proton. Instead we take the charge =+1 ∆+ as the two dimensional analog of
the proton. In the Skyrme model one can compute in a similar manner the flavor
content of the four dimensional baryons. The two and four dimensional states compare as is summarized in table 4. 8 Outlook
We can imagine future developments associated with the topics covered in the book in
three different directions: Further progress in the application of the methods discussed
in the book to unravel the mysteries of gauge dynamics in nature, applications of the
methods in other domains of physics not related to four dimensional gauge theories and
improving our understanding of the strong interaction and hadron physics due to other
non-perturbative techniques that were not discussed in the book. Let us now briefly
fantasize on hypothetical developments in those three avenues.
8.1 Further progress in the application of the methods dis- cussed in the book
- A lesson that follows from the book is that the exploration of physical systems on
one space dimension is both simpler to handle and sheds light on the real world so
there are plenty of other unresolved questions that could be explored first in two
dimensions. This includes exploration of the full standard model and the physics
beyond the standard model including supersymmetry and its dynamical breaking, 15
|  | two dimensions
state value | four dimensions
state value |
| --- | --- | --- |
| (cid:104)u¯u(cid:105) | ∆+ 1
2 | p 2
5 |
| (cid:68)¯ (cid:69)
dd | ∆+ 1
3 | p 11
30 |
| (cid:104)s¯s(cid:105) | ∆+ 1
6 | p 7
30 |
| (cid:104)s¯s(cid:105) | ∆++ 1
6 | ∆ 7
24 |
| (cid:104)s¯s(cid:105) |  | Ω− 5
24 |


## Page 18

large extra dimensions, compositeness etc.
- There has been a tremendous development in recent years in applying methods of
integrable models and in particular of spin chains, like the thermal Bethe ansatz,
to N = 4 SYM theory, namely, in the context of supersymmetric conformal gauge
theory. We have no doubt that there will be further development in computing the
anomalous dimensions of gauge invariant operators and correlators.
- Moreover, one can identify in a similar manner to N = 4 SYM theory a spin
chain structure in gauge theories which are confining and with less or even no
supersymmetries. In that case the spin chain Hamiltonian would not correspond
to the dilatation operator but rather be associated with the excitation energies of hadrons.
- It is plausible that the full role of magnetic monopoles and of instantons has not
yet been revealed. They have already had several reincarnations and there may
be more. For instance there was recently a proposal to describe baryons as in-
stantons which are solitons of a five dimensional flavor gauge theory in curved five dimensions. 8.2 Applications to other domains
- A very important application of two dimensional conformal symmetry has been to
superstring theories. A great part of the developments in supserstring theories is
attributed to the infinite dimensional conformal symmetry algebra. In fact it went
in both directions and certain progress in understanding the structure of conformal
invariance has emerged from the research of string theories. A similar symbiotic
evolution took place with regard to the affine Lie algebras.
- String theories and in particular the string theory on AdS ×S5 have recently been 5
analyzed using the tools of integrable models like mapping to spin chains, using the
Behte ansatz equations, identifying a set of infinitely many conserved charges and using structure of Yangian symmetry.
- Spin chain models have been suggested to describe systems of “real” spins in con-
densed matter physics. As is discussed in this book the application of the cor-
responding tools to field theory systems has been quite fruitful. The opposite
direction will presumably also take place and the use of properties of integrability
that were understood in field theories will shed new light on certain condensed matter systems. 16

## Page 19

- The application of conformal invariance to condensed matter systems at criticality
has a long history. There has been recently an intensive effort to further develop
the understanding of systems like various superconductors, fractional Hall effect
and other systems using modern conformal symmetry techniques.
8.3 Developments in gauge dynamics due to other methods
- An extremely important framework for analyzing gauge theories has been super-
symmetry. Regardless of whether it is realized in nature or not it is evident that
there are more tools to handle supersymmetric gauge theories and hence they are
much better understood than non supersymmetric ones. One can gain novel in-
sight into non supersymmetric theories by introducing supersymmetry breaking
terms to well understood supersymmetric models. For instance one can start with
the Seiberg-Witten solution of N = 2 where the structure of vacua is known and
extract confinement behavior in N = 1 and non supersymmetric theories.
- Abreakthroughintheunderstandingofgaugetheoriesinthestrongcouplingregime
took place with the discovery by Maldacena of the AdS/CFT holographic duality
```
[160]. ThestronglycoupledN = 4inthelargeN limitandlarge’tHooftparameter c
```
λ is mapped into a weakly curved supergravity background. Thousands of research
papers that followed develop this map in many different directions and in particular
also in relation to the pure YM theory and QCD in four dimensions. There is very
little doubt that further exploration of the duality will shed new light on QCD and on hadron physics.
- String theory had been born as a possible theory of hadron physics. It then un-
derwent a phase transition into a candidate of the theory of quantum gravity and
even a unifying theory of everything. In recent years, mainly due to the AdS/CFT
duality there is a renaissance of the idea that hadrons at low energies should be
described as strings. This presumably combined with the duality seems to be a
useful tool that will improve our understanding of gauge dynamics.
- The computations of scattering amplitudes in gauge theories has been boosted in
recent years due to various developments including the use of techniques based on
twistors, on a novel T-duality in the context of the Ads/CFT duality and on a
conjectured duality between Wilson lines and scattering amplitudes. One does not
need a wild imagination to foresee a further progress in the industry of computing scattering amplitudes. 17

## Page 20

To summarize, non-perturbative methods have always been very important tools in ex-
ploringthephysicalworld. Wehavenodoubtthattheywillcontinuetobeaveryessential
ingredient in future developments of science in general and physics in particular. 18

## Page 21

9 The list of references of the book
### References
```
[1] E. Abdalla and M. C. B. Abdalla, “Updating QCD in two-dimensions,” Phys. Rept. 265, 253 (1996) [arXiv:hep-th/9503002].
```
```
[2] E. Abdalla, M. C. B. Abdalla and K. D. Rothe, “Nonperturbative methods in two-
```
dimensional quantum field theory,” Singapore: World Scientific (2001) 832 p
```
[3] A. Abrashkin, Y. Frishman and J. Sonnenschein, “The spectrum of states with one
```
current acting on the adjoint vacuum of Nucl. Phys. B 703, 320 (2004) [arXiv:hep- th/0405165].
```
[4] C. Adam, “Charge screening and confinement in the massive Schwinger model,”
```
Phys. Lett. B 394, 161 (1997) [arXiv:hep-th/9609155].
```
[5] G. S. Adkins, C. R. Nappi and E. Witten, “Static Properties Of Nucleons In The
```
Skyrme Model,” Nucl. Phys. B 228, 552 (1983).
```
[6] S. L. Adler, J. C. Collins and A. Duncan, “Energy momentum tensor trace anomaly
```
in spin 1/2 quantum electrodynamics” Phys. Rev. D 15, 1712 (1977).
```
[7] I. Affleck, “On the realization of chiral symmetry in (1+1)-dimensions,” Nucl. Phys. B 265, 448 (1986).
```
```
[8] O. Aharony, O. Ganor, J. Sonnenschein and S. Yankielowicz, “On the twisted G/H
```
topological models,” Nucl. Phys. B 399, 560 (1993) [arXiv:hep-th/9208040].
```
[9] O. Aharony, O. Ganor, J. Sonnenschein, S. Yankielowicz and N. Sochen, “Physical
```
states in G/G models and 2-d gravity,” Nucl. Phys. B 399, 527 (1993) [arXiv:hep- th/9204095].
```
[10] O. Aharony, S. S. Gubser, J. M. Maldacena, H. Ooguri and Y. Oz, “Large N
```
field theories, string theory and gravity,” Phys. Rept. 323, 183 (2000) [arXiv:hep- th/9905111].
```
[11] A. Y. Alekseev and V. Schomerus, “D-branes in the WZW model,” Phys. Rev. D
```
60, 061901 (1999) [arXiv:hep-th/9812193].
```
[12] D. Altschuler, K. Bardakci and E. Rabinovici, ”A construction of the c < 1 modular
```
invariant partition function,” Commun. Math. Phys. 118, 241 (1988). 19

## Page 22

```
[13] L. Alvarez-Gaume, G. Sierra and C. Gomez, ”Topics in conformal field theory,”
```
Contribution to the Knizhnik Memorial Volume, L. Brink, et al., World Scientific.
In *Brink, L. (ed.) et al.: Physics and mathematics of strings* 16-184 (1989)
```
[14] F. Antonuccio and S. Dalley, “Glueballs from (1+1)-dimensional gauge theories
```
with transverse degrees of freedom,” Nucl. Phys. B 461, 275 (1996) [arXiv:hep- ph/9506456].
```
[15] A. Armoni, Y. Frishman and J. Sonnenschein, “The string tension in massive
```
QCD(2),” Phys. Rev. Lett. 80, 430 (1998) [arXiv:hep-th/9709097].
```
[16] A.Armoni,Y.FrishmanandJ.Sonnenschein,“Thestringtensionintwodimensional
```
gauge theories,” Int. J. Mod. Phys. A 14, 2475 (1999) [arXiv:hep-th/9903153].
```
[17] A. Armoni, Y. Frishman and J. Sonnenschein, “Massless QCD(2) from current con-
```
stituents,” Nucl. Phys. B 596, 459 (2001) [arXiv:hep-th/0011043].
```
[18] A. Armoni and J. Sonnenschein, “Mesonic spectra of bosonized QCD in two-
```
dimensions models,” Nucl. Phys. B 457, 81 (1995) [arXiv:hep-th/9508006].
```
[19] M.F.AtiyahandN.J.Hitchin, “Thegeometryanddynamicsofmagneticmonopole.
```
M.B. Porter lectures” PRINCETON, USA: UNIV. PR. (1988) 133p
```
[20] M. F. Atiyah, N. J. Hitchin, V. G. Drinfeld and Yu. I. Manin, “Construction of
```
instantons,” Phys. Lett. A 65, 185 (1978).
```
[21] F.A.Bais,“Tobeornottobe? Magneticmonopolesinnon-Abeliangaugetheories,” arXiv:hep-th/0407197.
```
```
[22] A. P. Balachandran, V. P. Nair, N. Panchapakesan and S. G. Rajeev, “Low Mass
```
Solitons From Fractional Charges In QCD,” Phys. Rev. D 28, 2830 (1983).
```
[23] I. I. Balitsky and L. N. Lipatov, “The Pomeranchuk Singularity In Quantum Chro-
```
modynamics,” Sov. J. Nucl. Phys. 28, 822 (1978) [Yad. Fiz. 28, 1597 (1978)].
```
[24] V. Baluni, “The Bose form of two-dimensional Quantum Chromodynamics,” Phys. Lett. B 90, 407 (1980).
```
```
[25] T. Banks, ”Lectures on conformal field theory,” Presented at the Theoretical Ad-
```
vanced Studies Institute, St. John’s College, Santa Fe, N.Mex., Jul 5 - Aug 1, 1987. Published in Santa Fe: TASI 87:572
```
[26] T. I. Banks and C. M. Bender, “Anharmonic oscillator with polynomial self-
```
interaction,” J. Math. Phys. 13, 1320 (1972). 20

## Page 23

```
[27] K. Bardakci and M. B. Halpern, “New dual quark models,” Phys. Rev. D 3, 2493 (1971).
```
```
[28] A. Bassetto, G. Nardelli and R. Soldati, “Yang-Mills theories in algebraic nonco-
```
variant gauges: Canonical quantization and renormalization,” Singapore, Singapore: World Scientific (1991) 227 p
```
[29] R.J. Baxter, “Exactly Solved Models in Statistical Mechanics,” Academic press 1989
```
```
[30] K. Becker, M. Becker and J. H. Schwarz, “String theory and M-theory: A modern
```
introduction,” Cambridge, UK: Cambridge Univ. Pr. (2007) 739 p
```
[31] N. Beisert, “The dilatation operator of N = 4 super Yang-Mills theory and Phys.
```
Rept. 405, 1 (2005) [arXiv:hep-th/0407277].
```
[32] A. A. Belavin, A. M. Polyakov, A. S. Shvarts and Yu. S. Tyupkin, “Pseudoparticle
```
solutions of the Yang-Mills equations,” Phys. Lett. B 59, 85 (1975).
```
[33] A. A. Belavin, A. M. Polyakov and A. B. Zamolodchikov, “Infinite conformal sym-
```
metry in two-dimensional quantum field theory,” Nucl. Phys. B 241, 333 (1984).
```
[34] A. V. Belitsky, V. M. Braun, A. S. Gorsky and G. P. Korchemsky, “Integrability in
```
QCD and beyond,” Int. J. Mod. Phys. A 19, 4715 (2004) [arXiv:hep-th/0407232].
```
[35] D. E. Berenstein, J. M. Maldacena and H. S. Nastase, “Strings in flat space and
```
pp waves from N = 4 super Yang Mills,” JHEP 0204, 013 (2002) [arXiv:hep- th/0202021].
```
[36] M. Bernstein and J. Sonnenschein, “A comment on the quantizaiton of the chiral
```
bosons” Phys. Rev. Lett. 60, 1772 (1988).
```
[37] J. D. Bjorken and S. D. Drell, “Relativistic Quantum Field Theory” New York: McGraw-Hill 1965, ISBN 0-07-005494-0
```
```
[38] G. Bhanot, K. Demeterfi and I. R. Klebanov, “(1+1)-dimensional large N QCD
```
coupled to adjoint fermions,” Phys. Rev. D 48, 4980 (1993) [arXiv:hep-th/9307111].
```
[39] D. Bernard and A. Leclair, “Quantum group symmetries and nonlocal currents in
```
2-D QFT,” Commun. Math. Phys. 142, 99 (1991).
```
[40] K. M. Bitar and S. J. Chang, “Vacuum Tunneling Of Gauge Theory In Minkowski Space,” Phys. Rev. D 17, 486 (1978). 21
```

## Page 24

```
[41] E. B. Bogomolny, “Stability Of Classical Solutions,” Sov. J. Nucl. Phys. 24, 449 (1976) [Yad. Fiz. 24, 861 (1976)].
```
```
[42] V. M. Braun, S. E. Derkachov, G. P. Korchemsky and A. N. Manashov, “Baryon
```
distribution amplitudes in QCD,” Nucl. Phys. B 553, 355 (1999) [arXiv:hep- ph/9902375].
```
[43] V. M. Braun, G. P. Korchemsky and D. Mueller, “The uses of conformal symmetry
```
in QCD,” Prog. Part. Nucl. Phys. 51, 311 (2003) [arXiv:hep-ph/0306057].
```
[44] E. Brezin and J. L. Gervais, “Nonperturbative Aspects In Quantum Field Theory.
```
Proceedings Of Les Houches Winter Advanced Study Institute, March 1978,” Phys. Rept. 49, 91 (1979).
```
[45] E.Brezin,C.Itzykson, J.Zinn-JustinandJ.B.Zuber,“Remarksabouttheexistence
```
of nonlocal charges in two-dimensional models,” Phys. Lett. B 82, 442 (1979).
```
[46] E. Brezin and S. R. Wadia, “The Large N expansion in quantum field theory and
```
statistical physics: From spin systems to two-dimensional gravity,” Singapore, Sin- gapore: World Scientific (1993) 1130 p
```
[47] S. J. Brodsky, “Gauge theories on the light-front,” Braz. J. Phys. 34, 157 (2004) [arXiv:hep-th/0302121].
```
```
[48] S. J. Brodsky, H. C. Pauli and S. S. Pinsky, “Quantum chromodynamics and
```
other field theories on the light cone,” Phys. Rept. 301, 299 (1998) [arXiv:hep- ph/9705477].
```
[49] S. J. Brodsky, Y. Frishman, G. P. Lepage and C. T. Sachrajda, “Hadronic Wave
```
Functions At Short Distances And The Operator Product Expansion,” Phys. Lett. B 91, 239 (1980).
```
[50] S. J. Brodsky, Y. Frishman and G. P. Lepage, “On The Application Of Conformal
```
Symmetry To Quantum Field Theory,” Phys. Lett. B 167, 347 (1986).
```
[51] S. J. Brodsky, P. Damgaard, Y. Frishman and G. P. Lepage, “Conformal Symmetry:
```
Exclusive Processes Beyond Leading Order,” Phys. Rev. D 33, 1881 (1986).
```
[52] R. C. Brower, W. L. Spence and J. H. Weis, “Effects Of Confinement On Analyticity
```
In Two-Dimensional QCD,” Phys. Rev. D 18, 499 (1978).
```
[53] G. E. Brown, ‘Selected papers, with commentary, of Tony Hilton Royle Skyrme,”
```
Singapore, Singapore: World Scientific (1994) 438 p. (World Scientific series in 20th century physics, 3) 22

## Page 25

```
[54] R. N. Cahn, ”Semisimple Lie algebras and their representations,” Menlo Park, Usa:
```
Benjamin/cummings (1984) 158 P. (Frontiers In Physics, 59)
```
[55] C. G. . Callan, “Broken Scale Invariance In Scalar Field Theory,” Phys. Rev. D 2, 1541 (1970).
```
```
[56] C. G. Callan, N. Coote and D. J. Gross, “Two-Dimensional Yang-Mills Theory: A
```
Model Of Quark Confinement,” Phys. Rev. D 13, 1649 (1976).
```
[57] C. G. . Callan, R. F. Dashen and D. J. Gross, “Toward a theory of the strong
```
interactions,” Phys. Rev. D 17, 2717 (1978).
```
[58] J. L. Cardy, “Boundary conditions, fusion rules and the Verlinde formula,” Nucl. Phys. B 324, 581 (1989).
```
```
[59] J.L.Cardy, ”Conformalinvarianceandstatisticalmechanics,”Les Houches Summer School 1988:0169-246
```
```
[60] A. Casher, H. Neuberger and S. Nussinov, “Chromoelectric Flux Tube Model Of
```
Particle Production,” Phys. Rev. D 20, 179 (1979).
```
[61] A. Chodos, “Simple connection between conservation laws in the Korteweg-De Vries
```
and sine-Gordon systems,” Phys. Rev. D 21, 2818 (1980).
```
[62] E. Cohen, Y. Frishman and D. Gepner, “Bosonization of two-dimensional QCD with flavor,” Phys. Lett. B 121, 180 (1983).
```
```
[63] S. R. Coleman, “Quantum sine-Gordon equation as the massive Thirring model,” Phys. Rev. D 11, 2088 (1975).
```
```
[64] S. R. Coleman, “More about the massive Schwinger model,” Annals Phys. 101, 239 (1976).
```
```
[65] S. R. Coleman, “The uses of instantons,” Subnucl. Ser. 15, 805 (1979).
```
```
[66] S. Coleman, “ Aspects of symmetry”, selected Erice lectures of Sidney Coleman, Cambridge Univ. Press 1985.
```
```
[67] S. R. Coleman, “The Magnetic Monopole Fifty Years Later,” In the “unity of fun-
```
damental interactions” ed A. Zichichi ( Plenum New York 1983)
```
[68] S. R. Coleman, R. Jackiw and L. Susskind, “Charge Shielding And Quark Confine-
```
ment In The Massive Schwinger Model,” Annals Phys. 93, 267 (1975). 23

## Page 26

```
[69] S. Cordes, G. W. Moore and S. Ramgoolam, “Large N 2-D Yang-Mills theory
```
and topological string theory,” Commun. Math. Phys. 185, 543 (1997) [arXiv:hep- th/9402107].
```
[70] E. Corrigan, D. B. Fairlie, S. Templeton and P. Goddard, “A Green’s Function For
```
The General Selfdual Gauge Field,” Nucl. Phys. B 140, 31 (1978).
```
[71] E. Corrigan and P. Goddard, “Construction Of Instanton And Monopole Solutions
```
And Reciprocity,” Annals Phys. 154, 253 (1984).
```
[72] S. Dalley and I. R. Klebanov, “String spectrum of (1+1)-dimensional large N QCD
```
with adjoint matter,” Phys. Rev. D 47, 2517 (1993) [arXiv:hep-th/9209049].
```
[73] R. F. Dashen and Y. Frishman, “Four fermion interactions and scale invariance,” Phys. Rev. D 11, 2781 (1975).
```
```
[74] R.F.Dashen, B.HasslacherandA.Neveu, “Nonperturbativemethodsandextended
```
hadron models in field theory. 2. Two-dimensional models and extended hadrons,” Phys. Rev. D 10, 4130 (1974).
```
[75] G. Date, Y. Frishman and J. Sonnenschein, ”The spectrum of multiflavor QCD in
```
two-dimensions’” Nucl. Phys. B 283, 365 (1987).
```
[76] G. F. Dell-Antonio, Y. Frishman and D. Zwanziger, “Thirring model in terms of
```
```
currents: Solution and light cone expansions,” Phys. Rev. D 6, 988 (1972).
```
```
[77] P. Di Francesco, P. Mathieu, D. Senechal “Conformal field theory”, Series:Graduate
```
Texts in Contemporary Physics, Springer-Verlag 1997.
```
[78] P. A. M. Dirac, “Theory Of Magnetic Monopoles,” In *Coral Gables 1976, Proceed-
```
ings, New Pathways In High-energy Physics, Vol.I*, New York 1976, 1-14
```
[79] F. M. Dittes and A. V. Radyushkin, “Two Loop Contribution To The Evolution Of
```
The Pion Wave Function,” Phys. Lett. B 134, 359 (1984); M. H. Sarmadi, Phys.
Lett. B 143, 471 (1984); S. V. Mikhailov and A. V. Radyushkin, Nucl. Phys. B 254,
89 (1985); G. R. Katz, Phys. Rev. D 31, 652 (1985).
```
[80] N. Dorey, T. J. Hollowood, V. V. Khoze, M. P. Mattis and S. Vandoren, “Multi-
```
instanton calculus and the AdS/CFT correspondence in N = 4 Nucl. Phys. B 552, 88 (1999) [arXiv:hep-th/9901128]. [81] 24

## Page 27

```
[81] N. Dorey, T. J. Hollowood, V. V. Khoze and M. P. Mattis, “The calculus of many
```
instantons,” Phys. Rept. 371, 231 (2002) [arXiv:hep-th/0206063].
```
[82] M. R. Douglas, K. Li and M. Staudacher, “Generalized two-dimensional QCD,”
```
Nucl. Phys. B 420, 118 (1994) [arXiv:hep-th/9401062]. [83]
```
[83] A. V. Efremov and A. V. Radyushkin, “Factorization And Asymptotical Behavior
```
Of Pion Form-Factor In QCD,” Phys. Lett. B 94, 245 (1980).
```
[84] T. Eguchi and H. Ooguri, “Chiral bosonization on a Riemann surface,” Phys. Lett. B 187, 127 (1987).
```
```
[85] S. Elitzur and G. Sarkissian, “D-branes on a gauged WZW model,” Nucl. Phys. B 625, 166 (2002) [arXiv:hep-th/0108142].
```
```
[86] J.R.Ellis, Y.Frishman, A.HananyandM.Karliner, “Quarksolitonsasconstituents
```
of hadrons,” Nucl. Phys. B 382, 189 (1992) [arXiv:hep-ph/9204212].
```
[87] J. R. Ellis, Y. Frishman and M. Karliner, “Meson baryon scattering in QCD(2) for
```
any coupling,” Phys. Lett. B 566 (2003) 201 [arXiv:hep-ph/0305292].
```
[88] L. D. Faddeev, “How Algebraic Bethe Ansatz works for integrable model,” arXiv:hep-th/9605187.
```
```
[89] B.L. Feigin and D.B. Fuchs “Skew symmetric differential operators on the line and
```
Verma modules over the Virasoro algebra” Funct. Anal. Prilozhen 16 (1982) 47.
```
[90] S. Ferrara, A. F. Grillo and R. Gatto, “Improved light cone expansion,” Phys. Lett.
```
B 36, 124 (1971) [Phys. Lett. B 38, 188 (1972)].
```
[91] D. Finkelstein and J. Rubinstein, “Connection between spin, statistics, and kinks,” J. Math. Phys. 9, 1762 (1968).
```
```
[92] R. Floreanini and R. Jackiw, “Selfdual fields as charge density solitons,” Phys. Rev. Lett. 59, 1873 (1987).
```
```
[93] D. Friedan, “Introduction To Polyakov’s string theory,” Published in Les Houches Summer School 1982:0839.
```
```
[94] D. Friedan, E. J. Martinec and S. H. Shenker, “Conformal invariance, supersymme-
```
try and string theory,” Nucl. Phys. B 271, 93 (1986). 25

## Page 28

```
[95] D. Friedan, Z. a. Qiu and S. H. Shenker, “Conformal invariance, unitarity and two-
```
dimensional critical exponents,” Phys. Rev. Lett. 52, 1575 (1984).
```
[96] Y. Frishman, A. Hanany and J. Sonnenschein, “Subtleties in QCD theory in two-
```
dimensions,” Nucl. Phys. B 429, 75 (1994) [arXiv:hep-th/9401046].
```
[97] Y. Frishman and M. Karliner, “Baryon wave functions and strangeness content in
```
QCD in two-dimensions,” Nucl. Phys. B 344 (1990) 393.
```
[98] Y. Frishman and M. Karliner, “Scattering and resonances in QCD(2),” Phys. Lett.
```
B 541 (2002) 273 [Erratum-ibid. B 562 (2003) 367] [arXiv:hep-ph/0206001].
```
[99] Y. Frishman and J. Sonnenschein, ”Bosonization of colored-flavored fermions and
```
QCD in two-dimenstions,” Nucl. Phys. B 294, 801 (1987).
```
[100] Y. Frishman and J. Sonnenschein, ”Gauging of chiral bosonized actions’” Nucl. Phys. B 301, 346 (1988).
```
```
[101] Y. Frishman and J. Sonnenschein, “Bosonization and QCD in two-dimensions,”
```
Phys. Rept. 223, 309 (1993) [arXiv:hep-th/9207017].
```
[102] Y. Frishman and W. J. Zakrzewski, “Multibaryons in QCD in two-dimensions,” Nucl. Phys. B 328, 375 (1989).
```
```
[103] Y. Frishman and W. J. Zakrzewski, ”Explicit expressions for masses and bindings
```
of multibaryons in QCD**2” Nucl. Phys. B 331, 781 (1990).
```
[104] S. Fubini, A. J. Hanson and R. Jackiw, “New approach to field theory,” Phys. Rev. D 7, 1732 (1973).
```
```
[105] O. Ganor, J. Sonnenschein and S. Yankielowicz, “The string theory approach to
```
generalized 2-d Yang-Mills theory,” Nucl. Phys. B 434, 139 (1995) [arXiv:hep- th/9407114].
```
[106] E. G. Gimon, L. A. Pando Zayas, J. Sonnenschein and M. J. Strassler, “A soluble
```
string theory of hadrons,” JHEP 0305, 039 (2003) [arXiv:hep-th/0212061].
```
[107] D. Gepner, “Nonabelian bosonization and multiflavor QED and QCD in two-
```
dimensions,” Nucl. Phys. B 252, 481 (1985).
```
[108] D. Gepner and E. Witten, “String theory on group manifolds,” Nucl. Phys. B 278, 493 (1986). 26
```

## Page 29

```
[109] P. H. Ginsparg, ”Applied conformal field theory,” Published in Les Houches Sum-
```
mer School 1988:1-168, arXiv:hep-th/9108028.
```
[110] P. Goddard, A. Kent and D. I. Olive, “Virasoro algebras and coset space models,” Phys. Lett. B 152 (1985) 88.
```
```
[111] P. Goddard and D. I. Olive, “Kac-Moody and Virasoro algebras in relation to
```
quantum physics,” Int. J. Mod. Phys. A 1, 303 (1986).
```
[112] D. Gonzales and A. N. Redlich, “The low-energy effective dynamics of two-
```
dimensional gauge theories,” Nucl. Phys. B 256, 621 (1985).
```
[113] M. B. Green, J. H. Schwarz and E. Witten, “Superstring theory. vol. 2: Loop
```
amplitudes, anomalies and phenomenology,” Cambridge, Uk: Univ. Pr. (1987) 596
P. (Cambridge Monographs On Mathematical Physics)
```
[114] C. Gomez, G. Sierra and M. Ruiz-Altaba, “Quantum groups in two-dimensional
```
physics,” Cambridge, UK: Univ. Pr. (1996) 457 p
```
[115] D. J. Gross, “Two-dimensional QCD as a string theory,” Nucl. Phys. B 400, 161 (1993) [arXiv:hep-th/9212149].
```
```
[116] D. J. Gross, I. R. Klebanov, A. V. Matytsin and A. V. Smilga, “Screening vs.
```
Confinement in 1+1 Dimensions,” Nucl. Phys. B 461, 109 (1996) [arXiv:hep- th/9511104].
```
[117] D. J. Gross and A. Neveu, “Dynamical symmetry breaking in asymptotically free
```
field theories,” Phys. Rev. D 10, 3235 (1974).
```
[118] D. J. Gross and W. Taylor, “Two-dimensional QCD is a string theory,” Nucl. Phys.
```
B 400, 181 (1993) [arXiv:hep-th/9301068].
```
[119] D. J. Gross and W. Taylor, “Twists and Wilson loops in the string theory of two-
```
dimensional QCD,” Nucl. Phys. B 403, 395 (1993) [arXiv:hep-th/9303046].
```
[120] I. G. Halliday, E. Rabinovici, A. Schwimmer and M. S. Chanowitz, “Quantization
```
of anomalous two-dimensional models,” Nucl. Phys. B 268, 413 (1986).
```
[121] M. B. Halpern, “Quantum solitons which are SU(N) fermions,” Phys. Rev. D 12, 1684 (1975).
```
```
[122] G. ’t Hooft, ”A plannar diagram theory for strong interactions,” Nucl. Phys. B 72, 461 (1974). 27
```

## Page 30

```
[123] G. ’t Hooft, “ Magnetic monopoles in unified gauge theories” Nucl. Phys. B 79, 276 (1974).
```
```
[124] G. ’t Hooft, “A two-dimensional model for mesons,” Nucl. Phys. B 75, 461 (1974).
```
```
[125] G. ’t Hooft, “Computation of the quantum effects due to a four-dimensional pseu-
```
doparticle,” Phys. Rev. D 14, 3432 (1976) [Erratum-ibid. D 18, 2199 (1978)].
```
[126] P. Horava, “Topological strings and QCD in two-dimensions,” hep-th/9311156,
```
talk given at NATO Advanced Research Workshop on New Developments in String
Theory, Conformal Models and Topological Field Theory, Cargese, France, 12-21 May 1993.
```
[127] K. Hornbostel, “The application of light cone quantization to quantum chromody-
```
namics in (1+1)-dimensions,” Ph.D. thesis, SLAC-R-333, Dec 1988
```
[128] K. Hornbostel, S. J. Brodsky and H. C. Pauli, “Light cone quantized QCD in
```
```
(1+1)-dimensions,” Phys. Rev. D 41, 3814 (1990).
```
```
[129] C. Imbimbo and A. Schwimmer, ”The Lagrangian formulation of chiral scalars,” Phys. Lett. B 193, 455 (1987).
```
```
[130] C. Itzykson and J. B. Zuber, “Quantum Field Theory,” New York, Usa: Mcgraw-
```
hill (1980) 705 P.(International Series In Pure and Applied Physics)
```
[131] R. Jackiw and C. Rebbi, “Vacuum periodicity in a Yang-Mills quantum theory,” Phys. Rev. Lett. 37, 172 (1976).
```
```
[132] R. Jackiw, C. Nohl and C. Rebbi, “Conformal properties of pseudoparticle config-
```
urations,” Phys. Rev. D 15, 1642 (1977).
```
[133] A. D. Jackson and M. Rho, “Baryons As Chiral Solitons,” Phys. Rev. Lett. 51, 751 (1983).
```
```
[134] B. Julia and A. Zee, “Poles With Both Magnetic And Electric Charges In Non-
```
abelian Gauge Theory,” Phys. Rev. D 11, 2227 (1975).
```
[135] N. Ishibashi, “The boundary and crosscap states in conformal field theories,” Mod. Phys. Lett. A 4, 251 (1989).
```
```
[136] V. G. Kac, “Simple graded algebras of finite growth,” Funct. Anal. Appl. 1, 328 (1967). 28
```

## Page 31

```
[137] L. P. Kadanoff, “Correlators along the line of two dimensional Ising model” Phys. Rev. 188, 859 (1969).
```
```
[138] M. Kaku, “Strings, conformal fields, and M-theory,” New York, USA: Springer (2000) 531 p
```
```
[139] V. A. Kazakov, “Wilson loop average for an arbitrary contour in two-dimensional
```
U(N) gauge theory,” Nucl. Phys. B 179, 283 (1981).
```
[140] S. V. Ketov, “Conformal field theory,” Singapore, Singapore: World Scientific (1995) 486 p
```
```
[141] V. V. Khoze, M. P. Mattis and M. J. Slater, “The instanton hunter’s guide to
```
supersymmetric SU(N) gauge theory,” Nucl. Phys. B 536, 69 (1998) [arXiv:hep- th/9804009].
```
[142] E. Kiritsis, “String theory in a nutshell,” Princeton, USA: Univ. Pr. (2007) 588 p
```
```
[143] V. G. Knizhnik and A. B. Zamolodchikov, “Current algebra and Wess-Zumino
```
model in two dimensions,” Nucl. Phys. B 247, 83 (1984).
```
[144] W.KrauthandM.Staudacher, “Non-integrabilityoftwo-dimensionalQCD,”Phys.
```
Lett. B 388, 808 (1996) [arXiv:hep-th/9608122].
```
[145] E. A. Kuraev, L. N. Lipatov and V. S. Fadin, “The Pomeranchuk Singularity In
```
Nonabelian Gauge Theories,” Sov. Phys. JETP 45, 199 (1977) [Zh. Eksp. Teor. Fiz.
72, 377 (1977)]. “Multi - Reggeon Processes In The Yang-Mills Theory,” Sov. Phys.
JETP 44, 443 (1976) [Zh. Eksp. Teor. Fiz. 71, 840 (1976)].
```
[146] D. Kutasov, ”Duality off the critical point in two-dimentional systems with non-
```
abelian symmetries,” Phys. Lett. B 233, 369 (1989).
```
[147] D. Kutasov, “Two-dimensional QCD coupled to adjoint matter and string theory,”
```
Nucl. Phys. B 414, 33 (1994) [arXiv:hep-th/9306013].
```
[148] D. Kutasov and A. Schwimmer, “Universality in two-dimensional gauge theory,”
```
Nucl. Phys. B 442, 447 (1995) [arXiv:hep-th/9501024].
```
[149] T. D. Lee and Y. Pang, “Nontopological solitons,” Phys. Rept. 221, 251 (1992).
```
```
[150] G. P. Lepage and S. J. Brodsky, “Exclusive Processes In Quantum Chromodynam-
```
```
ics: Evolution Equations For Hadronic Wave Functions And The Form-Factors Of Mesons,” Phys. Lett. B 87, 359 (1979). 29
```

## Page 32

```
[151] L.N.Lipatov,“Thecreationofquantumchromodynamicsandtheeffectiveenergy,”
```
Bologna, Italy: Univ. Bologna (1998) 367 p
```
[152] J. H. Lowenstein and J. A. Swieca, “Quantum electrodynamics in two-dimensions,” Annals Phys. 68 (1971) 172.
```
```
[153] M. Luscher, “Quantum nonlocal charges and absence of particle production in the
```
two-dimensional nonlinear Sigma model,” Nucl. Phys. B 135, 1 (1978).
```
[154] D. Lust and S. Theisen, “Lectures on string theory,” Lect. Notes Phys. 346, 1 (1989).
```
```
[155] A. Maciocia, “Metrics on the moduli spaces of instantons over Euclidean four
```
space,” Commun. Math. Phys. 135, 467 (1991).
```
[156] G. Mack and A. Salam, “Finite component field representations of the conformal group,” Annals Phys. 53, 174 (1969).
```
```
[157] V. G. Makhankov, Y. P. Rybakov and V. I. Sanyuk, “The Skyrme model: Fun-
```
damentals, methods, applications,” Berlin, Germany: Springer (1993) 265 p.
```
(Springer series in nuclear and particle physics)
```
```
[158] J. M. Maldacena, “The large N limit of superconformal field theories and super-
```
gravity,” Adv. Theor. Math. Phys. 2, 231 (1998) [Int. J. Theor. Phys. 38, 1113 (1999)] [arXiv:hep-th/9711200].
```
[159] S. Mandelstam, “Soliton operators for the quantized sine-Gordon equation,” Phys. Rev. D 11, 3026 (1975).
```
```
[160] A. V. Manohar, “Large N QCD,” arXiv:hep-ph/9802419, Published in *Les
```
Houches 1997, Probing the standard model of particle interactions, Pt. 2* 1091- 1169.
```
[161] A. A. Migdal, “Recursion equations in gauge field theories,” Sov. Phys. JETP 42,
```
413 (1975) [Zh. Eksp. Teor. Fiz. 69, 810 (1975)].
```
[162] J. A. Minahan and K. Zarembo, “The Bethe-ansatz for N = 4 super Yang-Mills,”
```
JHEP 0303, 013 (2003) [arXiv:hep-th/0212208].
```
[163] C. Montonen and D. I. Olive, “Magnetic Monopoles As Gauge Particles?,” Phys. Lett. B 72, 117 (1977).
```
```
[164] R. V. Moody, “Lie algebras associated with generalized Cartan matrices,” Bull. Am. Math. Soc. 73, 217 (1967). 30
```

## Page 33

```
[165] M. Moshe and J. Zinn-Justin, “Quantum field theory in the large N limit: A
```
review,” Phys. Rept. 385, 69 (2003) [arXiv:hep-th/0306133].
```
[166] D. Mueller, “Constraints for anomalous dimensions of local light cone operators in
```
phi**3 in six-dimensions theory,” Z. Phys. C 49, 293 (1991); Phys. Rev. D 49, 2525 (1994).
```
[167] W. Nahm, “A Simple Formalism For The Bps Monopole,” Phys. Lett. B 90, 413 (1980).
```
```
[168] N. K. Nielsen, “Gauge Invariance And Broken Conformal Symmetry,” Nucl. Phys. B 97, 527 (1975).
```
```
[169] N. K. Nielsen, “The Energy Momentum Tensor In A Nonabelian Quark Gluon Theory,” Nucl. Phys. B 120, 212 (1977).
```
```
[170] S. P. Novikov, “Multivalued functions and functionals, An analogue to Morse the- ory” Sov. Math. Dock. 24 , 222 (1981)
```
```
[171] T. Ohrndorf, “Constraints From Conformal Covariance On The Mixing Of Opera-
```
tors Of Lowest Twist,” Nucl. Phys. B 198, 26 (1982).
```
[172] R. D. Peccei and H. R. Quinn, “Constraints Imposed By CP Conservation In The
```
Presence Of Instantons,” Phys. Rev. D 16, 1791 (1977).
```
[173] M. E. Peskin and D. V. Schroeder, “An Introduction To Quantum Field Theory,”
```
Reading, USA: Addison-Wesley (1995) 842 p
```
[174] J. Polchinski, “String theory. Vol. 2: Superstring theory and beyond,” Cambridge, UK: Univ. Pr. (1998) 531 p
```
```
[175] A. M. Polyakov, “Particle spectrum in quantum field theory,” JETP Lett. 20, 194
```
```
(1974) [Pisma Zh. Eksp. Teor. Fiz. 20, 430 (1974)].
```
```
[176] A. M. Polyakov, “Hidden symmetry of the two-dimensional chiral fields,” Phys. Lett. B 72, 224 (1977).
```
```
[177] A. M. Polyakov, “Quantum geometry of bosonic strings,” Phys. Lett. B 103, 207 (1981).
```
```
[178] A. M. Polyakov, ”Gauge fields and strings”, Chur, Switzerland: Harwood (1987)
```
301 p. (Contemporary concepts in Physics, 3) 31

## Page 34

```
[179] A. M. Polyakov and P. B. Wiegmann, “Goldstone fields in two-dimensions with
```
multivalued actions,” Phys. Lett. B 141, 223 (1984).
```
[180] M. K. Prasad and C. M. Sommerfield, “An Exact Classical Solution For The ’T
```
Hooft Monopole And The Julia-Zee Dyon,” Phys. Rev. Lett. 35, 760 (1975).
```
[181] E. Rabinovici, A. Schwimmer and S. Yankielowicz, “Quantization in the presence
```
of Wess-Zumino terms,” Nucl. Phys. B 248, 523 (1984).
```
[182] R. Rajaraman, “An introduction to solitons and instantons in quantum field the-
```
ory,” Amsterdam, Netherlands: North-holland (1982) 409p
```
[183] C. Rebbi and G. Soliani, “ Solitons and particles,” World Scientific 1984.
```
```
[184] B. E. Rusakov, “Loop averages and partition functions in U(N) gauge theory on
```
two-dimensional manifolds,” Mod. Phys. Lett. A 5, 693 (1990).
```
[185] T. Schafer and E. V. Shuryak, “Instantons in QCD,” Rev. Mod. Phys. 70, 323 (1998) [arXiv:hep-ph/9610451].
```
```
[186] J. Schechter and H. Weigel, “The Skyrme model for baryons,” arXiv:hep- ph/9907554.
```
```
[187] T. D. Schultz, D. C. Mattis and E. H. Lieb, “Two-dimensional Ising model as a
```
soluble problem of many fermions,” Rev. Mod. Phys. 36, 856 (1964).
```
[188] M. A. Shifman, “Instantons in gauge theories,” Singapore, Singapore: World Sci- entific (1994) 488 p
```
```
[189] E. V. Shuryak, “The Role Of Instantons In Quantum Chromodynamics. 1. Physical Vacuum,” Nucl. Phys. B 203, 93 (1982).
```
```
[190] J. S. Schwinger, “Gauge Invariance And Mass. 2,” Phys. Rev. 128, 2425 (1962).
```
```
[191] N. Seiberg and E. Witten, “Monopoles, duality and chiral symmetry breaking in
```
```
N=2 supersymmetric QCD,” Nucl. Phys. B 431, 484 (1994) [arXiv:hep-th/9408099].
```
```
[192] N. Seiberg and E. Witten, “Monopole Condensation, And Confinement In N=2
```
Supersymmetric Yang-Mills Theory,” Nucl. Phys. B 426, 19 (1994) [Erratum-ibid.
B 430, 485 (1994)] [arXiv:hep-th/9407087].
```
[193] Y. M. Shnir, “Magnetic Monopoles,” Berlin, Germany: Springer (2005) 532 p
```
```
[194] W. Siegel, “Manifest Lorentz invariance sometimes requires nonlinearity,” Nucl. Phys. B 238, 307 (1984). 32
```

## Page 35

```
[195] T. H. R. Skyrme, “A Nonlinear theory of strong interactions,” Proc. Roy. Soc. Lond. A 247, 260 (1958).
```
```
[196] T. H. R. Skyrme, “Particle states of a quantized meson field,” Proc. Roy. Soc. Lond. A 262, 237 (1961).
```
```
[197] T. H. R. Skyrme, “A Unified Field Theory Of Mesons And Baryons,” Nucl. Phys. 31, 556 (1962).
```
```
[198] Smirnov, F. A. “Form factors in completely integrable models of quantum field
```
theory,” Adv.Ser.Math.Phys.14:1-208,1992.
```
[199] J. Sonnenschein, ”Chiral bosons’” Nucl. Phys. B 309, 752 (1988).
```
```
[200] M. Spiegelglas and S. Yankielowicz, “G/G Topological Field Theories By Cosetting
```
G(K),” Nucl. Phys. B 393, 301 (1993) [arXiv:hep-th/9201036].
```
[201] P.J.Steinhardt, “BaryonsandBaryoniuminQCDintwo-dimensions,” Nucl.Phys. B 176, 100 (1980).
```
```
[202] M. Stone, “Bosonization,” Singapore: World Scientific (1994) 539 p
```
```
[203] H. Sugawara, “A Field theory of currents,” Phys. Rev. 170, 1659 (1968).
```
```
[204] K. Symanzik, “Small Distance Behavior In Field Theory And Power Counting,” Commun. Math. Phys. 18, 227 (1970
```
```
[205] W. E. Thirring, “A soluble relativistic field theory,” Annals Phys. 3, 91 (1958).
```
```
[206] C. B. Thorn, “Computing The Kac Determinant Using Dual Model Techniques
```
And More About The No - Ghost Theorem,” Nucl. Phys. B 248, 551 (1984).
```
[207] S.B Treiman, R. Jackiw and D. Gross “Current algebra and its applications” (
```
Princeton, University Press, New Jersey, 1972)
```
[208] A. I. Vainshtein, V. I. Zakharov, V. A. Novikov and M. A. Shifman, “ABC of
```
instantons,” Sov. Phys. Usp. 25, 195 (1982) [Usp. Fiz. Nauk 136, 553 (1982)].
```
[209] S. Vandoren and P. van Nieuwenhuizen, “Lectures on instantons,” arXiv:0802.1862 [hep-th].
```
```
[210] E. P. Verlinde, “Fusion rules and modular transformations in 2d conformal field theory,” Nucl. Phys. B 300, 360 (1988). 33
```

## Page 36

```
[211] E. P. Verlinde and H. L. Verlinde, “Chiral bosonization, determinants and the
```
string partition function,” Nucl. Phys. B 288, 357 (1987).
```
[212] M.S.Virasoro, “Subsidiaryconditionsandghostsindualresonancemodels,” Phys. Rev. D 1, 2933 (1970).
```
```
[213] M. Wakimoto, “Fock representations of the affine Lie algebra A1(1),” Commun. Math. Phys. 104, 605 (1986).
```
```
[214] E. J. Weinberg and P. Yi, “Magnetic monopole dynamics, supersymmetry, and
```
duality,” Phys. Rept. 438, 65 (2007) [arXiv:hep-th/0609055].
```
[215] S. Weinberg, “The Quantum theory of fields. Vol. 1: Foundations,” Cambridge, UK: Univ. Pr. (1995) 609 p
```
```
[216] G. Veneziano, “U(1) Without Instantons,” Nucl. Phys. B 159, 213 (1979).
```
```
[217] J. Wess and B. Zumino, “Consequences of anomalous Ward identities,” Phys. Lett. B 37, 95 (1971).
```
```
[218] F. Wilczek, “Inequivalent embeddings of SU(2) and instanton interactions,” Phys. Lett. B 65, 160
```
```
[219] K. G. Wilson, “Nonlagrangian models of current algebra,” Phys. Rev. 179, 1499 (1969).
```
```
[220] E. Witten, “Some exact multipseudoparticle solutions of classical Yang-Mills the- ory,” Phys. Rev. Lett. 38, 121 (1977).
```
```
[221] E. Witten, “Instantons, the Quark model, and the 1/N expansion,” Nucl. Phys. B 149, 285 (1979).
```
```
[222] E. Witten, “Baryons in the 1/N expansion,” Nucl. Phys. B 160, 57 (1979).
```
```
[223] E. Witten, “Large N chiral dynamics,” Annals Phys. 128, 363 (1980).
```
```
[224] E. Witten, “Nonabelian bosonization in two dimensions,” Commun. Math. Phys. 92, 455 (1984).
```
```
[225] E. Witten, “Global aspects of current algebra,” Nucl. Phys. B 223, 422 (1983).
```
```
[226] E. Witten, “Current algebra, baryons, and Quark confinement,” Nucl. Phys. B 223, 433 (1983). 34
```

## Page 37

```
[227] E. Witten, “On Holomorphic factorization of WZW and coset models,” Commun. Math. Phys. 144, 189 (1992).
```
```
[228] E. Witten, “Two-dimensional gauge theories revisited,” J. Geom. Phys. 9, 303 (1992) [arXiv:hep-th/9204083].
```
```
[229] C. N. Yang and R. L. Mills, “Conservation of isotopic spin and isotopic gauge invariance,” Phys. Rev. 96, 191 (1954).
```
```
[230] C. N. Yang, “Some exact results for the many body problems in one dimension
```
with repulsive delta function interaction,” Phys. Rev. Lett. 19, 1312 (1967).
```
[231] I. Zahed and G. E. Brown, “The Skyrme Model,” Phys. Rept. 142, 1 (1986).
```
```
[232] A. B. Zamolodchikov, “Renormalization group and perturbation theory near fixed
```
points in two-dimensional field theory,” Sov. J. Nucl. Phys. 46, 1090 (1987) [Yad. Fiz. 46, 1819 (1987)].
```
[233] A. B. Zamolodchikov, “Exact solutions of conformal field theory in two-dimensions
```
and critical phenomena,” Rev. Math. Phys. 1, 197 (1990).
```
[234] A. B. Zamolodchikov, ” Thermodynamic Bethe Anzatz in relativistic models, scal-
```
ing three state Potts and Lee-Yang models,” Nucl. Phys. B 342, 695 (1990).
```
[235] A. B. Zamolodchikov and A. B. Zamolodchikov, “Factorized S-matrices in two di-
```
mensions as the exact solutions of certain relativistic quantum field models,” Annals Phys. 120, 253 (1979).
```
[236] A. B. Zamolodchikov, A. B. Zamolodchikov and I. M. . Khalatnikov, ”Physics
```
Reviews, Vol. 10, pt. 4: Condormal field theory and critical phenomena in two-
dimensional systems,” London, UK: Harwood (1989) 269-433. (Soviet scientific re- views, Section A, 10.4)
```
[237] B. Zwiebach, “A first course in string theory,” Cambridge, UK: Univ. Pr. (2004) 558 p 35
```

## Page 38

10 Appendix A- The table of content of the book 36

## Page 39

37

## Page 40

38

## Page 41

39

## Page 42

40

## Page 43

41

## Page 44

42