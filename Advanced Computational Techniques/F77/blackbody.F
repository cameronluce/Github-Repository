      program blackbody
      integer i
      real*8 nu, dnu, temp, b_nu
      temp = 5000.
      nu = 1.
      dnu = 0.1

      open(unit=1,file='bb.dat',status='unknown')

      do i = 1,1000

        b_nu = bby(nu,temp)
        write(1,*) nu, b_nu
        nu = nu + dnu

      enddo
 
      close(1)

      end

      function bby(nu,temp)

      real*8 h, clight, k_b, nu, temp

      clight = 3.0d8
      k_b = 1.3806d-23
      h = 6.62d-34

      bby = (2 * h * nu**3./clight**2.)
     ./(dexp(h*nu/(k_b*temp)) - 1.)

      return
      end
