%define debug_package	%{nil}
%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1
%define Werror_cflags -Wformat
# TODO: ask for appdata.xml upstream -DONE on ven 11 set 2015, 20.17.47, CEST Symbianflo
%define _appdatadir %{_datadir}/appdata

%define major 1
%define majorquicktime 1.6.0
%define majormpeg3 1.5.0

%define libguicast %mklibname guicast %{major}
%define libmpeg3hv %mklibname mpeg3hv %{majormpeg3}
%define libquicktimehv %mklibname quicktimehv %{majorquicktime}

%define devlibguicast %mklibname -d guicast %{major}
%define devlibmpeg3hv %mklibname -d mpeg3hv %{majormpeg3}
%define devlibquicktimehv %mklibname -d quicktimehv %{majorquicktime}

%define oname CinelerraCV
%define distsuffix plf
%define snap 20110903

Summary:	Non-Linear Video Editing Suite
Name:		cinelerra-cv
Version:	2.3
#Release:	1.git%{snap}.1
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Video
Url:		http://cinelerra-cv.org
# git clone git://git.cinelerra-cv.org/CinelerraCV.git cinelerra-cv
Source0:	http://cinelerra-cv.org/releases/%{oname}-%{version}.tar.xz
Patch1:         cinelerracv-2.3-no-buildtime.patch

BuildRequires:	imagemagick
BuildRequires:	libtool
BuildRequires:	nasm
BuildRequires:	texinfo
BuildRequires:	yasm
BuildRequires:	a52dec-devel
BuildRequires:	jpeg-devel
BuildRequires:	lame-devel
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	libmp4v2-devel
BuildRequires:	xvid-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(esound)
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(IlmBase)
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libdv)
BuildRequires:	pkgconfig(libiec61883)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(mjpegtools)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(x264)
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(libdc1394-2)
BuildRequires:	pkgconfig(dirac)
BuildRequires:	pkgconfig(schroedinger-1.0)
BuildRequires:	libnut-devel
BuildRequires:	gsm-devel
BuildRequires:	docbook2x
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xft)
#BuildRequires:	appstream-util
BuildRequires:	gcc-c++, gcc, gcc-cpp

Requires:	%{libguicast} = %{EVRD}
Requires:	%{libmpeg3hv} = %{EVRD}
Requires:	%{libquicktimehv} = %{EVRD}
Requires:	mjpegtools >= 1.6.3

Obsoletes:      cinelerra < %{EVRD}
Provides:	cinelerra = %{EVRD}

%description
If you want to make movies, you want the compositing and editing that
the big boys use, you want the efficiency of an embedded UNIX operating
system combined with the power of a general purpose PC, or you just want
to defy the establishment, the time has come to download Cinelerra.

This version is based on the "Community" tree found at
http://cinelerra-cv.org.

This package is in restricted because MP3 encoder and video codecs are
covered by software patents.

%files -f %{name}.lang
%doc NEWS ChangeLog COPYING LICENSE TODO
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png
%{_datadir}/pixmaps/%{name}.xpm
#%%{_appdatadir}/%{name}.appdata.xml
#----------------------------------------------------------------------------
%package	%{libguicast}
Summary:        Toolkit library (cinelerra's internal)
Group:          System/Libraries
Provides:	%{_lib}guicast1 = %{EVRD}

%description	%{libguicast}
Is a toolkit library mainly used by HeroineVirtual's software.

%files		%{libguicast}
%doc NEWS ChangeLog COPYING LICENSE TODO
%{_libdir}/libguicast.so.*

#----------------------------------------------------------------------------
%package	%{libmpeg3hv}
Summary:        Advanced editing and manipulation of MPEG streams
Group:          System/Libraries
Provides:	%{_lib}mpeg3hv%{majormpeg3} = %{EVRD}

%description	%{libmpeg3hv}
Libmpeg3 supports advanced editing and manipulation of MPEG streams. MPEG
is normally a last mile format but with libmpeg3 you can edit it like a
first mile solution.

%files		%{libmpeg3hv}
%doc NEWS ChangeLog COPYING LICENSE TODO
%{_libdir}/libmpeg3hv*.so.*

#----------------------------------------------------------------------------
%package	%{libquicktimehv}
Summary:        Quicktime 4 Linux Cinelerra internal library
Group:          System/Libraries
Provides:       %{libquicktimehv}-cv = %{EVRD}
Provides:	%{_lib}quicktimehv%{majorquicktime} = %{EVRD}

%description	%{libquicktimehv}
Quicktime 4 Linux was the first convenient way to read and write
uncompressed Quicktime movies on Linux. Today Quicktime 4 Linux is intended
for content creation and uncompressed movies. These usually arise during
the production phase and not the consumer phase of a movie. It has
improvements in colormodel support, bit depth, accuracy, reliability, and
codecs, while not stressing economy.


%files		%{libquicktimehv}
%doc NEWS ChangeLog COPYING LICENSE TODO
%{_libdir}/libquicktimehv*.so.*
#----------------------------------------------------------------------------
%package	%{devlibguicast}
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{libguicast} = %{EVRD}
Provides:	%{name}-%{_lib}guicast-devel = %{EVRD}


%description	%{devlibguicast}
Toolkit library (cinelerra's internal).

%files		%{devlibguicast}
%doc NEWS ChangeLog COPYING LICENSE TODO
%{_libdir}/libguicast.so
#----------------------------------------------------------------------------
%package	%{devlibmpeg3hv}
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{libmpeg3hv} = %{EVRD}
Provides:	%{name}-%{_lib}mpeg3hv-devel = %{EVRD}


%description	%{devlibmpeg3hv}
Advanced editing and manipulation of MPEG streams.

%files		%{devlibmpeg3hv}
%doc NEWS ChangeLog COPYING LICENSE TODO
%dir %{_includedir}/mpeg3
%{_includedir}/mpeg3/libmpeg3.h
%{_includedir}/mpeg3/mpeg3private.h
%{_libdir}/libmpeg3hv.so
#----------------------------------------------------------------------------
%package	%{devlibquicktimehv}
Summary:        Development files for %{name}
Group:          Development/Other
Conflicts:      pkgconfig(libquicktime)
Requires:       %{libquicktimehv} = %{EVRD}
Provides:	%{name}-%{_lib}quicktimehv-devel = %{EVRD}


%description	%{devlibquicktimehv}
Quicktime 4 Linux Cinelerra internal library.

%files		%{devlibquicktimehv}
%doc NEWS ChangeLog COPYING LICENSE TODO
%dir %{_includedir}/quicktime
%{_includedir}/quicktime/qtprivate.h
%{_includedir}/quicktime/quicktime.h
%{_libdir}/libquicktimehv.so

#----------------------------------------------------------------------------
%prep
%setup -qn %{oname}-%{version}
%patch1 -p1


%build
export CC=gcc
export CXX=g++

./autogen.sh
export CXXFLAGS="%{optflags} $(pkg-config --cflags freetype2) -D__STDC_CONSTANT_MACROS"
export CFLAGS="%{optflags} -fPIC"
%configure2_5x \
	--enable-freetype2 \
	--disable-rpath \
	--enable-alsa \
	--with-plugindir="%{_libdir}/%{name}" \
	--enable-alsa \
	--enable-opengl
	
%make

%install
%makeinstall_std

mkdir -p %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
convert image/cinelerra-cv.xpm -resize 48x48 %{buildroot}%{_liconsdir}/%{name}.png
convert image/cinelerra-cv.xpm -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert image/cinelerra-cv.xpm -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png

rm -f %{buildroot}%{_datadir}/applications/cinelerra.desktop
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Cinelerra
Comment=Non-Linear Video Editor
Exec=cinelerra
Icon=%{name}
Terminal=false
Type=Application
Categories=AudioVideo;Video;AudioVideoEditing;X-MandrivaLinux-Multimedia-Video;
EOF


#mkdir -p %{buildroot}%{_appdatadir}
#cp -R  *.appdata.xml %{buildroot}%{_appdatadir}/*.appdata.xml
#appstream-util validate-relax --nonet %{buildroot}%{_appdatadir}/*.xml

rm -rf %{buildroot}%{_libdir}/vhook


%find_lang %{name}