import numpy as np


# Simpson's 1 / 3 rule to calculate the no. of free electrons(nfree) in the material
def nfree(oddSum, evenSum, firstValue, lastValue, energyInterval):
    """This function calculates the no. of free electrons of the material by taking the following inputs.

    Args:
        oddSum (float): summation of energy of odd numbered DOS

        evenSum (float): summation of energy of even numbered DOS

        firstValue (float): first value of the energy in the considered range of DOS

        lastValue (float): last value of the energy in the considered range of DOS

        energyInterval (float): interval of energy

    Returns:
        float: gives the value of nfree
    """
    nfree = (energyInterval / 3) * (
        firstValue + (4 * oddSum) + (2 * evenSum) + lastValue
    )
    return round(nfree, 4)


# Function to calculate the metalic population of the material
def metPop(nfree, volm):
    """Calculates the metallic population of the material

    Args:
        nfree (float): no. of free electrons in the material

        volm (float): optimized volume of the cell

    Returns:
        float: gives the metallic population
    """
    return round(nfree / volm, 4)


# Function to calculate the bond volume
def bondVolm(volm, typesBond, bondsVar):
    """Calcultes the fractional bond volume of the different types of bond

    Args:
        volm (float): optimized volume of the cell

        typesBond (int): types of bond present in the material

        bondsVar (array): bond variables such as bondlength, no. of bonds, mullikan population of different types of bond
        is stored in an array of m * n matrix form where m is the no. of rows corresponding to bond types and each row having n
        no. of columns corresponding to the bond variables of each type of bond

    Returns:
        list: contains the fractional bond volume of each type of bond
    """
    bondLengthCubed = []
    bondDensity = []

    for i in range(typesBond):
        bondlencube = bondsVar[i][0] ** 3
        bondLengthCubed.append(bondlencube)
        bondens = bondsVar[i][1] / volm
        bondDensity.append(bondens)

    totalbondensity = np.multiply(
        np.array(bondLengthCubed), np.array(bondDensity)
    ).tolist()

    bondVolume = []

    for i in range(typesBond):
        bondvol = bondLengthCubed[i] / sum(totalbondensity)
        bondVolume.append(bondvol)

    roundedBondvolm = np.around(bondVolume, 4).tolist()

    return roundedBondvolm


def bondHardness(bondsvar, metallicpop, bondvolm, typesbond):
    """Calculates the fractional hardness of the individual bond types present
    in the material

    Args:
        bondsvar (array): bond variables such as bondlength, no. of bonds, mullikan population of different types of bond
        is stored in an array of m * n matrix form where m is the no. of rows corresponding to bond types and each row having n
        no. of columns corresponding to the bond variables of each type of bond

        metallicpop (float): the metallic population of the material

        bondvolm (list): the fractional bond volume of each type of bond

        typesbond (int): types of bond present in the material

    Returns:
        list: contains the fractional bond hardness of each type of bond in GPa unit
    """
    bondhard = []

    for i in range(typesbond):
        bonhardness = 740 * (bondsvar[i][2] - metallicpop) * (bondvolm[i]) ** (-5 / 3)
        bondhard.append(bonhardness)
    roundedbondhard = np.around(bondhard, 4).tolist()
    return roundedbondhard


def totolhardness(bondhardness, typesbond, bondsvar):
    """Calculates the total bond hardness of the material

    Args:
        bondhardness (list): fractional bond hardness of each type of bond

        typesbond (int): types of bond present in the material

        bondsvar (array): bond variables such as bondlength, no. of bonds, mullikan population of different types of bond
        is stored in an array of m * n matrix form where m is the no. of rows corresponding to bond types and each row having n
        no. of columns corresponding to the bond variables of each type of bond

    Returns:
        float: gives the total bond hardness of the material in GPa unit
    """
    totalbonds = 0
    hardness = 1
    for i in range(typesbond):
        totalbonds += bondsvar[i][1]
        hardness *= bondhardness[i] ** bondsvar[i][1]

    totalbondhardness = round(hardness ** (1 / totalbonds), 4)

    return totalbondhardness


# main function to call
def main():
    """The main function takes all the inputs and store them in suitable formats.These are then used to calculate the required
    values for the final result of the total bon hardness.
    The inputs are given as arguments to various functions defined above to calculate the necessary values which are stored and printed
    as the ouptut for the user.
    """
    firstValue = float(
        input("Enter the Value of Energy for the First Density of State: ")
    )
    lastValue = float(
        input("Enter the Value of Energy for the Last Density of State: ")
    )
    evenSum = float(
        input("Enter the Summation of Energy of Even Numbered Density of States: ")
    )
    oddSum = float(
        input("Enter the Summation of Energy of Odd numbered Density of States: ")
    )
    energyInterval = float(input("Enter the energy interval: "))

    volm = float(input("Enter the Optimized Volume of the Cell: "))

    typesBond = int(input("Enter the no. of Types of Bond for the Material: "))

    bondsVar = np.empty([typesBond, 3])
    for i in range(typesBond):
        du = float(input("Enter the Bondlength of Type-" + str(i + 1) + " Bond: "))
        nu = float(input("Enter the Total no. bonds of Type-" + str(i + 1) + ": "))
        pu = float(
            input("Enter the Mullikan Population of Type-" + str(i + 1) + " Bonds: ")
        )
        bondsVar[i] = [du, nu, pu]

    nfreeValue = nfree(oddSum, evenSum, firstValue, lastValue, energyInterval)
    pmubar = metPop(nfreeValue, volm)
    volmofbonds = bondVolm(volm, typesBond, bondsVar)
    hardnessofbonds = bondHardness(bondsVar, pmubar, volmofbonds, typesBond)
    totalbondhardness = totolhardness(hardnessofbonds, typesBond, bondsVar)

    print("The no. of Free Electrons is", nfreeValue)
    print("The Metallic Population is", pmubar)
    print("The volume of bonds are: ", volmofbonds)
    print("The Hardness of Bonds are (in GPa): ", hardnessofbonds)
    print("Total Bond Hardness of the Compound is: ", totalbondhardness)


main()
