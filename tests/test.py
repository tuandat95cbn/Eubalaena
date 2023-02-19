import xarray as xr
from euba.build import builder
depth = [0.494, 541.1]
L_lat= 2
L_lng= 2
time=["2019-05-16"]

longitude=[L_lng]
latitude=[L_lng]

ds = xr.Dataset({
        "thetao": (("time", "depth", "latitude", "longitude"),[[[[29.716087 ]],[[ 6.8198795]]]]),
        "so": (("time", "depth", "latitude", "longitude"),[[[[34.282967]],[[34.60036 ]]]]),
    },
    coords={
        "longitude": longitude,
        "latitude": latitude,
        "time": time,
        "depth": depth,
    },
)

#def test_formula_sig(t,s,z):
#    return a+b*t+c*t**2+d*t**3+e*(s-35)+f*z+g*z**2+h*t*(s-35)+j*t*z**3
    #return d*t**3+e*(s-35)
print(round(builder.MacKenzie(29.72, 34.28, 0.494),2))
print(round(1544.050014987869,2))
assert round(builder.MacKenzie(29.72, 34.28, 0.494))  == round(1544.050014987869)
assert round(builder.MacKenzie_uncertainty(29.72, 34.28, 0.494,0.97, 0.293))  == round(2.3158740881855167)

#print(test_formula_sig(6.82, 34.6, 541.1))
#  def test_formula_deviation(t,s,z,dt,ds):
    #  return (b+2*c*t+3*d*t**2+h*(s-35)+j*z**3)*dt+(e+h*t)*ds
#  print(test_formula_deviation(29.72, 34.28, 0.494,0.97, 0.293))
#  print(test_formula_deviation(6.82, 34.6, 541.1,0.48,0.082))
#  (SS, std_SS) = build_sound_velocity_dataset(ds)
#  assert round(SS.sel(longitude=[L_lng],latitude=[L_lng],depth=[0.5], time=["2019-05-16"] ,method="nearest").load().values[0][0][0][0]) == round(test_formula_sig(29.72, 34.28, 0.494))
#  assert round(SS.sel(longitude=[L_lng],latitude=[L_lng],depth=[500], time=["2019-05-16"] ,method="nearest").load().values[0][0][0][0]) == round(test_formula_sig(6.82, 34.6, 541.1))
#  assert round(std_SS.sel(longitude=[L_lng],latitude=[L_lng],depth=[0.5], time=["2019-05-16"] ,method="nearest").load().values[0][0][0][0],2) == round(test_formula_deviation(29.72, 34.28, 0.494,0.97, 0.293),2)
#  assert round(std_SS.sel(longitude=[L_lng],latitude=[L_lng],depth=[500], time=["2019-05-16"] ,method="nearest").load().values[0][0][0][0],2) == round(test_formula_deviation(6.82, 34.6, 541.1,0.48,0.082),2)
