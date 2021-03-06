##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RGoplot(RPackage):
    """Implementation of multilayered visualizations for enhanced graphical
       representation of functional analysis data. It combines and integrates
       omics data derived from expression and functional annotation enrichment
       analyses. Its plotting functions have been developed with an
       hierarchical structure in mind: starting from a general overview to
       identify the most enriched categories (modified bar plot, bubble plot)
       to a more detailed one displaying different types of relevant
       information for the molecules in a given set of categories
       (circle plot, chord plot, cluster plot, Venn diagram, heatmap)."""

    homepage = "https://github.com/wencke/wencke.github.io/issues"
    url      = "https://cran.r-project.org/src/contrib/GOplot_1.0.2.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/GOplot"

    version('1.0.2', sha256='3ddaa2b6d1297ad6daad30d18af708adf43d86e8804b1b92fa29dfbf26d80df9')

    depends_on('r@3.2.3:', type=('build', 'run'))
    depends_on('r-ggplot2@2.0.0:', type=('build', 'run'))
    depends_on('r-ggdendro@0.1-17:', type=('build', 'run'))
    depends_on('r-gridextra@2.0.0:', type=('build', 'run'))
    depends_on('r-rcolorbrewer@1.1.2:', type=('build', 'run'))
