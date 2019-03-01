!**********************************************************************
! ext_mod.f90
! Copyright (C) 2018 - 2019 Scott Schoeller (sschoellerSTEM)
!
! This file is part of PhySciCalc
! PhySciCalc is free software: you can redistribute it and/or modify
! it under the terms of the GNU General Public License as published by
! the Free Software Foundation, either version 3 of the License, or
! (at your option) any later version.
! PhySciCalc is distributed in the hope that it will be useful,
! but WITHOUT ANY WARRANTY; without even the implied warranty of
! MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
! GNU General Public License for more details.
! You should have received a copy of the GNU General Public License
! along with PhySciCalc.  If not, see <https://www.gnu.org/licenses/>.
!**********************************************************************
MODULE ext_mod

implicit none
! constants section
real, parameter :: c = 299792458 ! speed of light, in m/s

contains

function gmol(grams, MW) ! g->mol conversions
  real :: gmol
  
  real :: MW ! molecular weight
  real :: grams ! grams of material
  real :: result ! result of calculation

  result = grams/MW
  write (*,*) result
end function gmol

function ke(kg, v) ! KE = 0.5*kg*v^2
  real :: ke

  real :: kg ! mass of object in kg
  real :: v ! velocity in m/s
  real :: result ! result of calculation

  result = 0.5*kg*(v**2)
  write (*,*) result
end function ke

function re(kg) ! E = kg*c^2
  real :: re

  real :: kg ! mass of object in kg
  real :: result ! result of calculation

  result = kg*(c**2)
  write (*,*) result
end function re

END MODULE ext_mod
