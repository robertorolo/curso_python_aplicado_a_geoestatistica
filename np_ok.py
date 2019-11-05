def dist(p1, p2):
	
	return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def covariance(h):

	return np.exp(-(h/18)**2)

def mat_c(cov):
    cov_shape = cov.shape
    C_shape = (cov_shape[0]+1, cov_shape[1]+1)
    C = np.ones(C_shape)
    C[C_shape[0]-1,C_shape[1]-1] = 0
    C[:-1,:-1] = cov
    
    return C

dist_mat = np.array([[dist((3,10),(3,10)), dist((3,10),(-2,5)), dist((3,10),(4,-5))],
	                 [dist((3,10),(-2,5)), dist((-2,5),(-2,5)), dist((4,-5),(-2,5))],
	                 [dist((4,-5),(3,10)), dist((4,-5),(-2,5)), dist((4,-5),(4,-5))]])

dist_vec = np.array([[dist((3,10),(0,0)), dist((0,0),(-2,5)), dist((0,0),(4,-5))]])

cov_mat = covariance(dist_mat)

cov_vec = covariance(dist_vec)

C = mat_c(cov_mat)

D = np.append(cov_vec, 1)

C_inv = np.linalg.inv(C)

w = C_inv @ D

grade = 53*w[0] + 40*w[1] + 32*w[1]

