Name:		kokoro-voice-em_alex
Version:	1.0
Release:	1
Summary:	Spanish male Kokoro voice em_alex
URL:		https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Provides:	kokoro-voice
Provides:	kokoro-voice-es
Requires:	kokoro-model >= 1.0

%sourcelist
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/voices/em_alex.pt

%description
%{summary}.
Uses the shared checkpoint in kokoro-model.
Pronunciation uses espeak-ng.
Select it with: kokoro -m em_alex

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -c -m 644 %{S:0} %{buildroot}%{_datadir}/kokoro/voices/em_alex.pt

%files
%{_datadir}/kokoro/voices/em_alex.pt
