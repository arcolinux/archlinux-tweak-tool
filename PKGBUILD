# Maintainer: Erik Dubois <erik.dubois@gmail.com>
pkgname=arcolinux-tweak-tool-git
_pkgname=arcolinux-tweak-tool
pkgver=1.1
pkgrel=7
_destname="/"
pkgdesc="arcolinux tweak tool"
arch=('any')
url="https://github.com/arcolinux/${_pkgname}"
license=('Attribution-NonCommercial-ShareAlike 4.0 International Public License')
makedepends=('git')
options=(!strip !emptydirs)
conflicts=()
replaces=(hefftor-skel-app-git hefftor-skelap-git)
source=("${_pkgname}::git+https://github.com/arcolinux/${_pkgname}.git")
sha256sums=('SKIP')
package() {
	install -dm 755 ${pkgdir}${_destname}
	cp -r ${srcdir}/${_pkgname}/usr ${pkgdir}${_destname}
}