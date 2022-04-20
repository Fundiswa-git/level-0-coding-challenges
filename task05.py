def area(s1,s2,s3)
s_perimeter=1/2*(s1+s2+s3)
s_perimeter_m_s1=s_perimeter-s1

s_perimeter_m_s2=s_perimeter-s2
s_perimeter_m_s3=s_perimeter-s3

area=(s_perimeter)*(s_perimeter_m_s1)*(s_perimeter_m_s2)*(s_perimeter_m_s3)

return sqrt(area)

print(area(1,2,3))
