import os
import pandas as pd


def control_head(kx, ky, kz):
    return '''##########
# Physical model settings
#
  xc               pw-lda
  charge           0.0
  spin             none
  relativistic     atomic_zora scalar

##########
# SCF convergence settings
#
  occupation_type     gaussian 0.01
  mixer               pulay
    n_max_pulay                    10
    # charge_mix_param               0.2
    # ini_linear_mixing              10
    # ini_linear_mix_param           0.05
    # preconditioner kerker          1.5
    # precondition_max_l             0
    # preconditioner turnoff charge  1e-4
    # preconditioner turnoff sum_ev  1e-1
  sc_accuracy_rho     1.000e-05
  sc_accuracy_eev     1.000e-03
  sc_accuracy_etot    1.000e-06
  sc_accuracy_forces  1.000e-04
  sc_iter_limit       100

##########
# For periodic boundary conditions
#
  k_grid   {} {} {}
  k_offset 0 0 0

##########
# For relaxation
#
  relax_geometry bfgs 1.000e-02
  relax_unit_cell     full

##########
# Non-standard declarations
#
  override_illconditioning true
  energy_tolerance         2.000e-04

##########
# Output
#
  output hirshfeld
  output mulliken
  output zero_multipoles true

'''.format(kx, ky, kz)


control_head_222 = control_head(2, 2, 2)
control_head_122 = control_head(4, 2, 2)
control_head_212 = control_head(2, 4, 2)
control_head_221 = control_head(2, 2, 4)

control_La = '''################################################################################
#
#  FHI-aims code project
# Volker Blum, Fritz Haber Institute Berlin, 2009
#
#  Suggested "tight" defaults for La atom (to be pasted into control.in file)
#
################################################################################
  species          La
#     global species definitions
    nucleus        57
    mass           138.90547
#
    l_hartree      6
#
    cut_pot        4.0  2.0  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    65  7.0
    radial_multiplier  2
    angular_grids specified
      division   0.1164  110
      division   0.8770  194
      division   0.9952  302
      division   1.1042  434
#      division   1.1747  590
#      division   1.2496  770
#      division   4.2775  974
#      outer_grid  974
      outer_grid  434
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   1.
    valence      4  f   0.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   0.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.2, 2.6, 3.25, 4.00, 5.00 Ang
#
################################################################################
#  Necessary addition to minimal basis
     ionic 4 f auto  
#  "First tier" - improvements: -389.32 meV to -10.38 meV
     hydro 4 d 4.6     
     hydro 4 f 6.2     
     hydro 5 g 10      
     hydro 2 p 1.5     
     hydro 4 s 4.1     
#  "Second tier" - improvements: -30.19 meV to -0.51 meV
     hydro 6 h 13.6
     hydro 4 f 5
     hydro 5 d 4.6
     hydro 5 g 9
     hydro 6 d 11.2
     hydro 4 p 4.3
     hydro 5 s 5.4  
#  "Third tier" - max. impr. -1.72 meV, min. impr. -0.23 meV
#     hydro 6 h 12.4
#     hydro 5 g 6
#     hydro 5 g 28.4
#     hydro 4 f 12.4
#     hydro 4 d 7
#     hydro 5 p 8.4
#     hydro 3 s 2.3
#  Further functions - impr. -0.22 meV and below
#     hydro 5 f 10.8
#     hydro 5 g 15.6
'''

control_Si = '''################################################################################
#
#  FHI-aims code project
#  Volker Blum, Fritz Haber Institute Berlin, 2009
#
#  Suggested "tight" defaults for Si atom (to be pasted into control.in file)
#
#  Revised Jan 04, 2011, following tests (SiC) done by Lydia Nemec: 
#     d and g functions of tier 2 now enabled by default.
#
################################################################################
  species        Si
#     global species definitions
    nucleus             14
    mass                28.0855
#
    l_hartree           6
#
    cut_pot             4.0          2.0  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         42 7.0
    radial_multiplier   2
    angular_grids       specified
      division   0.4121   50
      division   0.7665  110
      division   1.0603  194
      division   1.2846  302
      division   1.4125  434
#      division   1.4810  590
#      division   1.5529  770
#      division   1.6284  974
#      division   2.6016 1202
#      outer_grid   974
      outer_grid  434
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      3  s   2.
    valence      3  p   2.
#     ion occupancy
    ion_occ      3  s   1.
    ion_occ      3  p   1.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.75 A, 2.0 A, 2.25 A, 2.75 A, 3.75 A
#
################################################################################
#  "First tier" - improvements: -571.96 meV to -37.03 meV
     hydro 3 d 4.2
     hydro 2 p 1.4
     hydro 4 f 6.2
     ionic 3 s auto
#  "Second tier" - improvements: -16.76 meV to -3.03 meV
     hydro 3 d 9
     hydro 5 g 9.4
     hydro 4 p 4
     hydro 1 s 0.65
#  "Third tier" - improvements: -3.89 meV to -0.60 meV
#     ionic 3 d auto
#     hydro 3 s 2.6
#     hydro 4 f 8.4
#     hydro 3 d 3.4
#     hydro 3 p 7.8
#  "Fourth tier" - improvements: -0.33 meV to -0.11 meV
#     hydro 2 p 1.6
#     hydro 5 g 10.8
#     hydro 5 f 11.2
#     hydro 3 d 1
#     hydro 4 s 4.5
#  Further basis functions that fell out of the optimization - noise
#  level... < -0.08 meV
#     hydro 4 d 6.6
#     hydro 5 g 16.4
#     hydro 4 d 9
################################################################################
#
# For methods that use the localized form of the "resolution of identity" for
# the two-electron Coulomb operator (RI_method LVL), particularly Hartree-Fock and
# hybrid density functional calculations, the highest accuracy can be obtained by
# uncommenting the line beginning with "for_aux"  below, thus adding an extra g radial
# function to the construction of the product basis set for the expansion.
# See Ref. New J. Phys. 17, 093020 (2015) for more information, particularly Figs. 1 and 6.
#
################################################################################
#
# for_aux hydro 5 g 6.0
'''

control_Hf = '''################################################################################
#
#  FHI-aims code project
# Volker Blum, Fritz Haber Institute Berlin, 2009
#
#  Suggested "tight" defaults for Hf atom (to be pasted into control.in file)
#
################################################################################
  species          Hf
#     global species definitions
    nucleus        72
    mass           178.49
#
    l_hartree      6
#
    cut_pot        4.0  2.0  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    71  7.0
    radial_multiplier  2
    angular_grids specified
      division   0.3723   50
      division   0.7995  110
      division   1.2133  194
      division   1.4586  302
      division   1.6594  434
#      division   1.9508  590
#      division   2.1708  770
#      division   2.4268  974
#      division   3.3577 1202
#      outer_grid  974
      outer_grid  434
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   2.
    valence      4  f  14.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   1.
    ion_occ      4  f  14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.975, 2.49, 3.25, 4.50 AA
#
################################################################################
#
#  "First tier" - improvements: -322.32 meV to -24.16 meV
     hydro 4 f 6
     hydro 3 d 6
     ionic 6 p auto
     hydro 5 g 10.8
     hydro 4 s 4.7  
#  "Second tier" - improvements: -29.31 meV to -1.14 meV
     hydro 5 f 9.6
     ionic 5 d auto
     hydro 6 h 15.2
     hydro 3 p 2.3
     hydro 4 d 6.6
     hydro 3 s 2.1 
#  "Third tier" - max. impr. -1.11 meV, min. impr. - meV
#     hydro 5 f 6.6
#     hydro 5 g 11.2
#     hydro 6 h 17.6
#     hydro 3 p 3
#     hydro 5 g 38.8
#     hydro 4 d 4.9
#     hydro 1 s 0.5 
#  "Fourth tier" - max. impr. -0.31 meV, min. impr. -0.11 meV
#     hydro 5 p 12
#     hydro 5 f 14
#     hydro 5 f 20.8
#     hydro 4 s 12.4
#     hydro 5 d 19.2
#     hydro 6 h 22
#  Further functions: -0.14 meV and below.
#     hydro 5 p 8.6
#     hydro 4 s 6
#     hydro 6 d 9.8
#     hydro 5 f 19.6
'''

control_O = '''################################################################################
#
#  FHI-aims code project
# Volker Blum, Fritz Haber Institute Berlin, 2009
#
#  Suggested "tight" defaults for O atom (to be pasted into control.in file)
#
################################################################################
  species        O
#     global species definitions
    nucleus             8
    mass                15.9994
#
    l_hartree           6
#
    cut_pot             4.0  2.0  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         36 7.0
    radial_multiplier   2
     angular_grids specified
      division   0.1817   50
      division   0.3417  110
      division   0.4949  194
      division   0.6251  302
      division   0.8014  434
#      division   0.8507  590
#      division   0.8762  770
#      division   0.9023  974
#      division   1.2339 1202
#      outer_grid 974
      outer_grid  434
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      2  s   2.
    valence      2  p   4.
#     ion occupancy
    ion_occ      2  s   1.
    ion_occ      2  p   3.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.0 A, 1.208 A, 1.5 A, 2.0 A, 3.0 A
#
################################################################################
#  "First tier" - improvements: -699.05 meV to -159.38 meV
     hydro 2 p 1.8
     hydro 3 d 7.6
     hydro 3 s 6.4
#  "Second tier" - improvements: -49.91 meV to -5.39 meV
     hydro 4 f 11.6
     hydro 3 p 6.2
     hydro 3 d 5.6
     hydro 5 g 17.6
     hydro 1 s 0.75
#  "Third tier" - improvements: -2.83 meV to -0.50 meV
#     ionic 2 p auto
#     hydro 4 f 10.8
#     hydro 4 d 4.7
#     hydro 2 s 6.8
#  "Fourth tier" - improvements: -0.40 meV to -0.12 meV
#     hydro 3 p 5
#     hydro 3 s 3.3
#     hydro 5 g 15.6
#     hydro 4 f 17.6
#     hydro 4 d 14
# Further basis functions - -0.08 meV and below
#     hydro 3 s 2.1
#     hydro 4 d 11.6
#     hydro 3 p 16
#     hydro 2 s 17.2
################################################################################
#
# For methods that use the localized form of the "resolution of identity" for
# the two-electron Coulomb operator (RI_method LVL), particularly Hartree-Fock and
# hybrid density functional calculations, the highest accuracy can be obtained by
# uncommenting the line beginning with "for_aux"  below, thus adding an extra g radial
# function to the construction of the product basis set for the expansion.
# See Ref. New J. Phys. 17, 093020 (2015) for more information, particularly Figs. 1 and 6.
#
################################################################################
#
# for_aux hydro 5 g 6.0
'''

control_head_dict = {
    '122': control_head_122,
    '212': control_head_212,
    '221': control_head_221,
    '222': control_head_222,
}
control_species_dict = {
    'La': control_La,
    'Si': control_Si,
    'Hf': control_Hf,
    'O': control_O,
}
species_order = ['Hf', 'O', 'La', 'Si']

df = pd.read_csv('data.csv')

def write_control(x):
    directory = x['directory']
    sc = str(x['supercell'])
    chem_formula = x['chemical formula']

    content = [control_head_dict[sc]]
    [content.append(control_species_dict[i]) for i in species_order if i in chem_formula]
    content = ''.join(content)
    with open(os.path.join(directory, 'control.in'), 'w+') as f:
        f.write(content)

df.apply(write_control, axis=1)
