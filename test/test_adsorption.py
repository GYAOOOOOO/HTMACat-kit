from HTMACat.catkit.gen.adsorption import Builder
from HTMACat.catkit.gratoms import *
from rdkit import Chem
from rdkit.Chem import AllChem, rdMolDescriptors
import math
from HTMACat.Extract_info import *
from HTMACat.model.Substrate import Slab
from HTMACat.model.Ads import Adsorption
from HTMACat.model.Species import Sim_Species, Sml_Species
from HTMACat.catkit.gen.adsorption import AdsorptionSites
from HTMACat.model.Structure import Structure
import networkx.algorithms.isomorphism as iso
from ase import Atoms
import pytest


@pytest.fixture
def species():
    species1 = Sml_Species(form="N")
    return [species1]


@pytest.fixture
def ads(species):
    sites = ["1"]
    ads = Adsorption(species=species, sites=sites)
    return ads


def test_set_species(ads):
    species1 = Sml_Species(form="[O]")
    ads.set_species([species1])
    assert ads.species[0].get_formular() == "[O]"


def test_add_species(ads):
    species = "[NH2]"
    species = Sml_Species(form="[NH2]")
    ads.add_species(species)
    assert ads.species[1].get_formular() == "[NH2]"


def test_add_sites(ads):
    sites = "1"
    ads.add_sites(sites)
    assert ads.sites[-1] == "1"


def test_get_sites(ads):
    assert ads.get_sites()[0] == "1"


def test_out_file_name(ads):
    assert ads.out_file_name() == "Pt_100_H3N"


def test_out_print(ads):
    assert ads.out_print() == "N adsorption on Pt (100) substrate"

'''
def test_construct_single_adsorption(ads):
    slab_ads = ads.construct()
    assert len(slab_ads) == 3
    assert np.allclose(
        slab_ads[0].numbers,
        [
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            7,
            1,
            1,
            1,
        ],
    )
    # assert np.allclose(slab_ads[0].positions,   [[ 1.40007143e+00,  1.40007143e+00,  8.00000000e+00],
    #                                             [-1.03582051e-16, -1.47387144e-16,  9.98000000e+00],
    #                                             [ 1.40007143e+00,  1.40007143e+00,  1.19600000e+01],
    #                                             [ 0.00000000e+00,  0.00000000e+00,  1.39400000e+01],
    #                                             [ 1.40007143e+00,  4.20021428e+00,  8.00000000e+00],
    #                                             [-1.03582051e-16,  2.80014285e+00,  9.98000000e+00],
    #                                             [ 1.40007143e+00,  4.20021428e+00,  1.19600000e+01],
    #                                             [ 0.00000000e+00,  2.80014285e+00,  1.39400000e+01],
    #                                             [ 1.40007143e+00,  7.00035713e+00,  8.00000000e+00],
    #                                             [-1.03582051e-16,  5.60028571e+00,  9.98000000e+00],
    #                                             [ 1.40007143e+00,  7.00035713e+00,  1.19600000e+01],
    #                                             [ 0.00000000e+00,  5.60028571e+00,  1.39400000e+01],
    #                                             [ 4.20021428e+00,  1.40007143e+00,  8.00000000e+00],
    #                                             [ 2.80014285e+00, -1.47387144e-16,  9.98000000e+00],
    #                                             [ 4.20021428e+00,  1.40007143e+00,  1.19600000e+01],
    #                                             [ 2.80014285e+00,  0.00000000e+00,  1.39400000e+01],
    #                                             [ 4.20021428e+00,  4.20021428e+00,  8.00000000e+00],
    #                                             [ 2.80014285e+00,  2.80014285e+00,  9.98000000e+00],
    #                                             [ 4.20021428e+00,  4.20021428e+00,  1.19600000e+01],
    #                                             [ 2.80014285e+00,  2.80014285e+00,  1.39400000e+01],
    #                                             [ 4.20021428e+00,  7.00035713e+00,  8.00000000e+00],
    #                                             [ 2.80014285e+00,  5.60028571e+00,  9.98000000e+00],
    #                                             [ 4.20021428e+00,  7.00035713e+00,  1.19600000e+01],
    #                                             [ 2.80014285e+00,  5.60028571e+00,  1.39400000e+01],
    #                                             [ 7.00035713e+00,  1.40007143e+00,  8.00000000e+00],
    #                                             [ 5.60028571e+00, -1.47387144e-16,  9.98000000e+00],
    #                                             [ 7.00035713e+00,  1.40007143e+00,  1.19600000e+01],
    #                                             [ 5.60028571e+00,  0.00000000e+00,  1.39400000e+01],
    #                                             [ 7.00035713e+00,  4.20021428e+00,  8.00000000e+00],
    #                                             [ 5.60028571e+00,  2.80014285e+00,  9.98000000e+00],
    #                                             [ 7.00035713e+00,  4.20021428e+00,  1.19600000e+01],
    #                                             [ 5.60028571e+00,  2.80014285e+00,  1.39400000e+01],
    #                                             [ 7.00035713e+00,  7.00035713e+00,  8.00000000e+00],
    #                                             [ 5.60028571e+00,  5.60028571e+00,  9.98000000e+00],
    #                                             [ 7.00035713e+00,  7.00035713e+00,  1.19600000e+01],
    #                                             [ 5.60028571e+00,  5.60028571e+00,  1.39400000e+01],
    #                                             [-1.57500777e-15, -3.67705866e-15,  1.60100000e+01],
    #                                             [ 9.56643671e-01, -2.33956750e-01,  1.56916423e+01],
    #                                             [-6.47564215e-01, -7.57175539e-01,  1.56911076e+01],
    #                                             [-2.90195569e-01,  9.49032278e-01,  1.56877405e+01]])
'''

@pytest.fixture
def ads2(species):
    sites = ["2"]
    ads = Adsorption(species=species, sites=sites)
    return ads


def test_construct_double_adsorption(ads2):
    slab_ads = ads2.construct()
    assert len(slab_ads) == 4
    assert np.allclose(
        slab_ads[0].numbers,
        [
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            78,
            7,
            1,
            1,
            1,
        ],
    )
    print(slab_ads[0].positions)
    # assert np.allclose(slab_ads[0].positions, [[ 1.40007143e+00,  1.40007143e+00,  8.00000000e+00],
    #                                             [-1.03582051e-16, -1.47387144e-16,  9.98000000e+00],
    #                                             [ 1.40007143e+00,  1.40007143e+00,  1.19600000e+01],
    #                                             [ 0.00000000e+00,  0.00000000e+00,  1.39400000e+01],
    #                                             [ 1.40007143e+00,  4.20021428e+00,  8.00000000e+00],
    #                                             [-1.03582051e-16,  2.80014285e+00,  9.98000000e+00],
    #                                             [ 1.40007143e+00,  4.20021428e+00,  1.19600000e+01],
    #                                             [ 0.00000000e+00,  2.80014285e+00,  1.39400000e+01],
    #                                             [ 1.40007143e+00,  7.00035713e+00,  8.00000000e+00],
    #                                             [-1.03582051e-16,  5.60028571e+00,  9.98000000e+00],
    #                                             [ 1.40007143e+00,  7.00035713e+00,  1.19600000e+01],
    #                                             [ 0.00000000e+00,  5.60028571e+00,  1.39400000e+01],
    #                                             [ 4.20021428e+00,  1.40007143e+00,  8.00000000e+00],
    #                                             [ 2.80014285e+00, -1.47387144e-16,  9.98000000e+00],
    #                                             [ 4.20021428e+00,  1.40007143e+00,  1.19600000e+01],
    #                                             [ 2.80014285e+00,  0.00000000e+00,  1.39400000e+01],
    #                                             [ 4.20021428e+00,  4.20021428e+00,  8.00000000e+00],
    #                                             [ 2.80014285e+00,  2.80014285e+00,  9.98000000e+00],
    #                                             [ 4.20021428e+00,  4.20021428e+00,  1.19600000e+01],
    #                                             [ 2.80014285e+00,  2.80014285e+00,  1.39400000e+01],
    #                                             [ 4.20021428e+00,  7.00035713e+00,  8.00000000e+00],
    #                                             [ 2.80014285e+00,  5.60028571e+00,  9.98000000e+00],
    #                                             [ 4.20021428e+00,  7.00035713e+00,  1.19600000e+01],
    #                                             [ 2.80014285e+00,  5.60028571e+00,  1.39400000e+01],
    #                                             [ 7.00035713e+00,  1.40007143e+00,  8.00000000e+00],
    #                                             [ 5.60028571e+00, -1.47387144e-16,  9.98000000e+00],
    #                                             [ 7.00035713e+00,  1.40007143e+00,  1.19600000e+01],
    #                                             [ 5.60028571e+00,  0.00000000e+00,  1.39400000e+01],
    #                                             [ 7.00035713e+00,  4.20021428e+00,  8.00000000e+00],
    #                                             [ 5.60028571e+00,  2.80014285e+00,  9.98000000e+00],
    #                                             [ 7.00035713e+00,  4.20021428e+00,  1.19600000e+01],
    #                                             [ 5.60028571e+00,  2.80014285e+00,  1.39400000e+01],
    #                                             [ 7.00035713e+00,  7.00035713e+00,  8.00000000e+00],
    #                                             [ 5.60028571e+00,  5.60028571e+00,  9.98000000e+00],
    #                                             [ 7.00035713e+00,  7.00035713e+00,  1.19600000e+01],
    #                                             [ 5.60028571e+00,  5.60028571e+00,  1.39400000e+01],
    #                                             [ 0.00000000e+00,  3.34800069e-01,  1.56146836e+01],
    #                                             [ 0.00000000e+00,  1.06527136e+00,  1.49779948e+01],
    #                                             [-4.30649928e-01,  8.72345002e-01, -8.50538030e-02],
    #                                             [ 9.91341014e-01, -7.45837958e-02, -9.33137801e-02]])
