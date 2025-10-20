program test1
integer i, j
real*8 Tc, Tf, conv
conv = 5./9.
do j = 1, 100000
    do i = 1, 100000
    Tc = 100.
    Tf = Tc/conv + 32.
    enddo
enddo
end
