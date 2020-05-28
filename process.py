import numpy as np

class Simulation:
    def __init__(self, v, D, a, b, t0, t1, initial_condition, dt, dx=0.5):
        # Initialize variables
        # ===============================================================
        # alpha
        self.alpha = (D*dt)/(dx**2)
        # beta
        self.beta = (v*dt)/dx

        self.Nx = int(((b-a)//dx)+1)
        self.Nt = int(((t1-t0)//dt)+1)

        # Mesh in space
        self.x = np.linspace(a, b, self.Nx+1)
        self.dx = self.x[1]-self.x[0]

        # Mesh in time
        self.t = np.linspace(t0, t1, self.Nt+1)
        self.dt = self.t[1]-self.t[0]

        # Concentration as C
        self.C = np.empty((self.Nt+1, self.Nx+1))
        # Initial condition: C(x,0) = initial_condition
        self.C[0,:] = initial_condition
        # Boundary condition: C(0,t) = 1
        self.C[:,0] = 1
        # ===============================================================
        # Simulate
        self.idx_t = 0
        for n in self.t:
            if self.idx_t+1 == len(self.t):
                break
            self.idx_x = 1
            for j in self.x:
                # boundary condition, Cx(inf,t) = 0 -> C_{j+1}^n = C_{j}^n
                if self.idx_x+1 == len(self.x):
                    self.C[self.idx_t+1, self.idx_x] = self.FTBSCS(self.C, self.idx_t, self.idx_x, self.alpha, self.beta, bound=True)
                    break
                self.C[self.idx_t+1, self.idx_x] = self.FTBSCS(self.C, self.idx_t, self.idx_x, self.alpha, self.beta)

                self.idx_x += 1
            self.idx_t += 1
        # ===============================================================
        self.simulationResult = {
            'C':self.C,
            'x':self.x,
            't':self.t,
            'v':v,
            'D':D
            }

    def FTBSCS(self, C, idx_t, idx_x, alpha, beta, bound=False):
        if bound == True:
            return (alpha+beta)*C[idx_t, idx_x-1] + (1-2*alpha-beta)*C[idx_t, idx_x] + (alpha)*C[idx_t, idx_x]

        return (alpha+beta)*C[idx_t, idx_x-1] + (1-2*alpha-beta)*C[idx_t, idx_x] + (alpha)*C[idx_t, idx_x+1]
