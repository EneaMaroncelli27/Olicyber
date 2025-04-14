from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

N = 22714782753220015042573603265764327669650408033887636001879315184259375362820403603936005525717891771936636443451884119703671427781729492224095091855683005507053963590222220410804649184763035006811331809382943132022500027644637621163477965898393682291084319795270435040869951140803612012610686322537800900791300826066574059761090027917447672155092101024934115081690160104897792167626579027888190943470746383568651182247114083165294856136382262206643466869528191984416012578579746005217713198188905067819779002232496897304974008305258471888110945562966313488702125793402335565466499907920044056450331308275860705662078
e = 65537
flag_enc = '388244a02eb9e2c2c06bcbc932422e0d181156ea4e08710b6987aad4f16e55e137b45ed9776b6baaffad78006db8131526e0c941b759e4493f38a697caba8d1a8e81300baa86d7b0a63b542e661b3bda502f6c09bf5636dbf567c21a3f3b10dcf9054ed4c485755df1d6d2f4a05814281eea0f4cb43d4e623a92c62473e2a2315e29e46ac31ff37e2a8feddba8f6d11a31aa7941d7edef3087582e43f2faa83a0555a598c1248568d8a268d993c8b47e8cc7c76d9ce95df1933d6b32fa331c1fcb154ebd65681945c958d8f0f10c015a478cc03fa4e31c1b5a4c55dc3da7b9c9ee5e0f24481b81a75af306dc9b766913c234f03673e9dc1cf35eb7f338d12e1f'

print(iroot(N, 2))

p = 11357391376610007521286801632882163834825204016943818000939657592129687681410201801968002762858945885968318221725942059851835713890864746112047545927841502753526981795111110205402324592381517503405665904691471566011250013822318810581738982949196841145542159897635217520434975570401806006305343161268900450395650413033287029880545013958723836077546050512467057540845080052448896083813289513944095471735373191784325591123557041582647428068191131103321733434764095992208006289289873002608856599094452533909889501116248448652487004152629235944055472781483156744351062896701167782733249953960022028225165654137930352831039
q = 2

phi = (p-1)*(q-1)
d = pow(e, -1, phi)

plaintext = pow(int(flag_enc, 16), d, N)
print(long_to_bytes(plaintext))