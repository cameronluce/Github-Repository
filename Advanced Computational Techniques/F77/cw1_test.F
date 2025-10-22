program CW1
integer i, j, k
real*8  a(512,512,512)
open(unit=6, file=’output.txt’, status=’unknown’)
do j = 1, 512
  do i = 1, 512
do k = 1, 512
      a(i,j,k) = 100 * dexp(pi/2).
      write(6,*) a(i,j,k)
enddo enddo
enddo
close(unit=6)
end