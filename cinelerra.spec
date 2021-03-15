%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1
%define Werror_cflags -Wformat

%define date 20201031
%define cin cinelerra

%define distsuffix plf

Name:		cinelerra
Version:	5.1.%{date}
Release:	1
Summary:	Non-Linear Video Editing Suite
License:	GPL
Group:		Video
URL:		https://www.cinelerra-gg.org
# git://git.cinelerra-cv.org/CinelerraCV.git#branch=master
Source0:	https://www.cinelerra-gg.org/download/pkgs/src/cin_%{version}-src.tgz
Source1:	cinelerra.rpmlintrc

# from /guicat , must compile partially first
#Source2:	pngtoh

BuildRequires:	libtool
BuildRequires:	pkgconfig(x11)
BuildRequires:	a52dec-devel
BuildRequires:	pkgconfig(esound)
# some headers needed even if not compiled with external ffmpeg
# do not build with 'external ffmpeg' in configure
# latest gits use hevy modified ffmpeg headers
# in order to have a full-optional plugins.Sflo
BuildRequires:	ffmpeg-devel 
BuildRequires:	imagemagick
BuildRequires:	jpeg-devel
BuildRequires:	lame-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libdv)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	libfaac-devel
#BuildRequires:	libfaad2-devel
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(libiec61883)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(mjpegtools)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(theora)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	nasm
BuildRequires:	yasm
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	texinfo
BuildRequires:	pkgconfig(libtiff-4)
#BuildRequires:	pkgconfig(x264)
BuildRequires:	xvid-devel
BuildRequires:	pkgconfig(IlmBase)
#BuildRequires:	libmp4v2-devel
BuildRequires:	pkgconfig(uuid)
BuildRequires:	desktop-file-utils

Requires:	mjpegtools >= 1.6.3
Requires:	ffmpeg

# is plf, no EVRD macro here
Requires:	lib%{name} = %{version}-%{release}

Conflicts:	libmpeg3-progs

%description
If you want to make movies, you want the compositing
and editing that the big boys use, you want the efficiency
of an embedded UNIX operating system combined with the
power of a general purpose PC, or you just want to defy
the establishment, the time has come to download Cinelerra.

This version is based on the "Community" tree found at
http://cinelerra.org.

This package is in restricted because MP3 encoder and
video codecs are covered by software patents.

##################################
%define major		0
%define libname		%mklibname %{name} 

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for %{name}
Provides:	lib%{name} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed by %{name}.

%files -n %{libname}
%doc NEWS ChangeLog TODO
%{_libdir}/%{name}
%{_libdir}/*.so.*

###########################

%prep
%setup -q -n %{name}-5.1

# autoconf will drop it from config.sub. Sflo
# libtool crappy hack
#cp -r %{SOURCE2} pngtoh
#find plugins -name "*.png"  -exec ./pngtoh {} \;


%build
export CC=gcc
export CXX=g++

#export CFLAGS+="%{optflags} -Wwrite-strings -D__STDC_CONSTANT_MACROS"
#export CPPFLAGS="$CFLAGS"
#export LDFLAGS+="$LDFLAGS -Wl,-z,noexecstack"


sh autogen.sh
./configure --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --with-plugindir=%{_libdir}/%{name} \
    --with-buildinfo=git/recompile \
    --enable-opengl \
    --disable-esd 

%make_build

%install
%make_install

rm -rf %{buildroot}/%{_includedir}
rm -rf  %{buildroot}/%{_libdir}/pkgconfig %{buildroot}/%{_libdir}/{*.so,*.la,*.a}
rm -rf %{buildroot}%{_libdir}/vhook

chmod 0644 %{buildroot}%{_libdir}/%{name}/fonts/*

# icons
mkdir -p %{buildroot}/%{_liconsdir}
convert plugins/defaulttheme/data/reel.png -resize 48x48 %{buildroot}/%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}
convert plugins/defaulttheme/data/reel.png -resize 32x32 %{buildroot}/%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_miconsdir}
convert plugins/defaulttheme/data/reel.png -resize 16x16 %{buildroot}/%{_miconsdir}/%{name}.png



rm -f %{buildroot}%{_datadir}/applications/cinelerra-cv.desktop
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Cinelerra
Comment=Non-Linear Video Editor
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=AudioVideo;Video;AudioVideoEditing;X-MandrivaLinux-Multimedia-Video;
EOF

desktop-file-validate %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop

%find_lang %{name}



%files -f %{name}.lang
%doc NEWS ChangeLog TODO
%{_bindir}/%{name}
%{_bindir}/mpeg3cat
%{_bindir}/mpeg3dump
%{_bindir}/mpeg3toc
%{_bindir}/mplexlo
%{_datadir}/applications/*.desktop
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png
%{_datadir}/pixmaps/%{name}.xpm

