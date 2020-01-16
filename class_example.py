


class Protein:
    """
    doctring.
    """

    def __init__(self, fname):
        """
        Parameters
        ----------
        fname : str
            The path to the protein pdb file.
        """
        return

    def get_residue_coords(self, resnum):
        """
        Return XYZ coords for all atoms of the ``resnum``.
        Numpy (N, 3) where N is the number of atoms of the residue
        in ``resnum`` position.
        """
        return

    def slice_pdb(self, start, stop):
        """
        Slice the PDB file from residue ``start`` to residue ``stop``
        where stop is INCLUSIVE

        Returns
        -------
        np.ndarray of shape (N, 15) of dtype=str
            where N is the number of atoms that compose the residue
            range.
        """
        return

    def get_backbone(self):
        """
        Get the backbone data of the PDB.

        Returns
        -------
        np.ndarray of shape (N, 15) of dtype=str
            where N is the number of residues * 4.
        """
        print('sending you my backbone')
        return

    def save_pdb(self, fname):
        """
        save the pdb information back to a pdb file.
        
        Parameters
        ----------
        fname : str
            The path to the protein pdb file.
        """
        return
