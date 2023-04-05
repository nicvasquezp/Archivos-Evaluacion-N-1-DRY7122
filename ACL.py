ACL = int(input("Cual es el numero IPV4 ACL:" ))

if ACL >= 1 and ACL <= 99:
	print("Esta es una ACL IPV4 de manera Estandar.")

elif ACL >= 100 and ACL <= 199:
	print("Esta es una ACL IPV4 de manera Extendida.")

else:
	print("Esta ACL IPV4 no corresponde ni a Estandar ni Extendida.")
