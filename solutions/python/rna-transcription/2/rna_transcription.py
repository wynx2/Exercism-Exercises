"""Module that transcribes DNA to RNA"""
def to_rna(dna_strand):
    """Function to transcribe DNA to RNA"""
    dna_Strand_1 = dna_strand.replace("A","U")
    dna_Strand_2 = dna_Strand_1.replace("T","A")
    rna_list = list(dna_Strand_2)

    for character_index in range(len(rna_list)):
        if rna_list[character_index] == "G":
            rna_list[character_index] = "C"
        elif rna_list[character_index] == "C":
            rna_list[character_index] = "G"

    return "".join(rna_list)