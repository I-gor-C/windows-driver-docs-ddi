---
UID: NE.ksmedia.KS_AnalogVideoStandard
title: KS_AnalogVideoStandard
author: windows-driver-content
description: The KS_AnalogVideoStandard enumeration defines various analog video standards that are used worldwide.
old-location: stream\ks_analogvideostandard.htm
ms.assetid: 33efef2f-0734-416e-9f89-394a3dd344b8
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_AnalogVideoStandard
req.alt-loc: ksmedia.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
req.iface: 
---

# KS_AnalogVideoStandard enumeration



## -description
<p>The KS_AnalogVideoStandard enumeration defines various analog video standards that are used worldwide.</p>


## -syntax

````
typedef enum  { 
  KS_AnalogVideo_None         = 0x00000000,
  KS_AnalogVideo_NTSC_M       = 0x00000001,
  KS_AnalogVideo_NTSC_M_J     = 0x00000002,
  KS_AnalogVideo_NTSC_433     = 0x00000004,
  KS_AnalogVideo_PAL_B        = 0x00000010,
  KS_AnalogVideo_PAL_D        = 0x00000020,
  KS_AnalogVideo_PAL_G        = 0x00000040,
  KS_AnalogVideo_PAL_H        = 0x00000080,
  KS_AnalogVideo_PAL_I        = 0x00000100,
  KS_AnalogVideo_PAL_M        = 0x00000200,
  KS_AnalogVideo_PAL_N        = 0x00000400,
  KS_AnalogVideo_PAL_60       = 0x00000800,
  KS_AnalogVideo_SECAM_B      = 0x00001000,
  KS_AnalogVideo_SECAM_D      = 0x00002000,
  KS_AnalogVideo_SECAM_G      = 0x00004000,
  KS_AnalogVideo_SECAM_H      = 0x00008000,
  KS_AnalogVideo_SECAM_K      = 0x00010000,
  KS_AnalogVideo_SECAM_K1     = 0x00020000,
  KS_AnalogVideo_SECAM_L      = 0x00040000,
  KS_AnalogVideo_SECAM_L1     = 0x00080000,
  KS_AnalogVideo_PAL_N_COMBO  = 0x00100000
} KS_AnalogVideoStandard;
````


## -enum-fields
<dl>

### -field <a id="KS_AnalogVideo_None"></a><a id="ks_analogvideo_none"></a><a id="KS_ANALOGVIDEO_NONE"></a><b>KS_AnalogVideo_None</b>

<dd>
<p>Specifies a digital sensor.</p>
</dd>

### -field <a id="KS_AnalogVideo_NTSC_M"></a><a id="ks_analogvideo_ntsc_m"></a><a id="KS_ANALOGVIDEO_NTSC_M"></a><b>KS_AnalogVideo_NTSC_M</b>

<dd>
<p>Specifies the National Television Standards Committee (NTSC) "M" standard, at 7.5 IRE for black.</p>
</dd>

### -field <a id="KS_AnalogVideo_NTSC_M_J"></a><a id="ks_analogvideo_ntsc_m_j"></a><a id="KS_ANALOGVIDEO_NTSC_M_J"></a><b>KS_AnalogVideo_NTSC_M_J</b>

<dd>
<p>Specifies the NTSC "M" standard that is used in Japan, at 0 IRE for black.</p>
</dd>

### -field <a id="KS_AnalogVideo_NTSC_433"></a><a id="ks_analogvideo_ntsc_433"></a><a id="KS_ANALOGVIDEO_NTSC_433"></a><b>KS_AnalogVideo_NTSC_433</b>

<dd>
<p>Specifies the NTSC 433 standard</p>
</dd>

### -field <a id="KS_AnalogVideo_PAL_B"></a><a id="ks_analogvideo_pal_b"></a><a id="KS_ANALOGVIDEO_PAL_B"></a><b>KS_AnalogVideo_PAL_B</b>

<dd>
<p>Specifies the Phase Alteration Line (PAL) "B" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_PAL_D"></a><a id="ks_analogvideo_pal_d"></a><a id="KS_ANALOGVIDEO_PAL_D"></a><b>KS_AnalogVideo_PAL_D</b>

<dd>
<p>Specifies the PAL "D" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_PAL_G"></a><a id="ks_analogvideo_pal_g"></a><a id="KS_ANALOGVIDEO_PAL_G"></a><b>KS_AnalogVideo_PAL_G</b>

<dd>
<p>Specifies the PAL "G" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_PAL_H"></a><a id="ks_analogvideo_pal_h"></a><a id="KS_ANALOGVIDEO_PAL_H"></a><b>KS_AnalogVideo_PAL_H</b>

<dd>
<p>Specifies the PAL "H" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_PAL_I"></a><a id="ks_analogvideo_pal_i"></a><a id="KS_ANALOGVIDEO_PAL_I"></a><b>KS_AnalogVideo_PAL_I</b>

<dd>
<p>Specifies the PAL "I" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_PAL_M"></a><a id="ks_analogvideo_pal_m"></a><a id="KS_ANALOGVIDEO_PAL_M"></a><b>KS_AnalogVideo_PAL_M</b>

<dd>
<p>Specifies the PAL "M" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_PAL_N"></a><a id="ks_analogvideo_pal_n"></a><a id="KS_ANALOGVIDEO_PAL_N"></a><b>KS_AnalogVideo_PAL_N</b>

<dd>
<p>Specifies the PAL "N" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_PAL_60"></a><a id="ks_analogvideo_pal_60"></a><a id="KS_ANALOGVIDEO_PAL_60"></a><b>KS_AnalogVideo_PAL_60</b>

<dd>
<p>Specifies the PAL-60 standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_SECAM_B"></a><a id="ks_analogvideo_secam_b"></a><a id="KS_ANALOGVIDEO_SECAM_B"></a><b>KS_AnalogVideo_SECAM_B</b>

<dd>
<p>Specifies the Systeme Electronic Pour Couleur Avec Memoire (SECAM) "B" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_SECAM_D"></a><a id="ks_analogvideo_secam_d"></a><a id="KS_ANALOGVIDEO_SECAM_D"></a><b>KS_AnalogVideo_SECAM_D</b>

<dd>
<p>Specifies the SECAM "D" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_SECAM_G"></a><a id="ks_analogvideo_secam_g"></a><a id="KS_ANALOGVIDEO_SECAM_G"></a><b>KS_AnalogVideo_SECAM_G</b>

<dd>
<p>Specifies the SECAM "G" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_SECAM_H"></a><a id="ks_analogvideo_secam_h"></a><a id="KS_ANALOGVIDEO_SECAM_H"></a><b>KS_AnalogVideo_SECAM_H</b>

<dd>
<p>Specifies the SECAM "H" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_SECAM_K"></a><a id="ks_analogvideo_secam_k"></a><a id="KS_ANALOGVIDEO_SECAM_K"></a><b>KS_AnalogVideo_SECAM_K</b>

<dd>
<p>Specifies the SECAM "K" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_SECAM_K1"></a><a id="ks_analogvideo_secam_k1"></a><a id="KS_ANALOGVIDEO_SECAM_K1"></a><b>KS_AnalogVideo_SECAM_K1</b>

<dd>
<p>Specifies the SECAM "K1" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_SECAM_L"></a><a id="ks_analogvideo_secam_l"></a><a id="KS_ANALOGVIDEO_SECAM_L"></a><b>KS_AnalogVideo_SECAM_L</b>

<dd>
<p>Specifies the SECAM "L" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_SECAM_L1"></a><a id="ks_analogvideo_secam_l1"></a><a id="KS_ANALOGVIDEO_SECAM_L1"></a><b>KS_AnalogVideo_SECAM_L1</b>

<dd>
<p>Specifies the SECAM "L1" standard.</p>
</dd>

### -field <a id="KS_AnalogVideo_PAL_N_COMBO"></a><a id="ks_analogvideo_pal_n_combo"></a><a id="KS_ANALOGVIDEO_PAL_N_COMBO"></a><b>KS_AnalogVideo_PAL_N_COMBO</b>

<dd>
<p>Specifies the combination PAL "N" standard (Argentina).</p>
</dd>
</dl>

## -remarks
<p>You can combine the values in the KS_AnalogVideoStandard enumeration with a bitwise OR  indicate support for multiple analog video standards.</p>

<p>You can combine the values in the KS_AnalogVideoStandard enumeration with a bitwise OR  indicate support for multiple analog video standards.</p>

<p>You can combine the values in the KS_AnalogVideoStandard enumeration with a bitwise OR  indicate support for multiple analog video standards.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567691">KS_TVTUNER_CHANGE_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567692">KS_VBIINFOHEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567706">KS_VIDEO_STREAM_CONFIG_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565872">KSPROPERTY_TUNER_MODE_CAPS_S</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565918">KSPROPERTY_TUNER_STANDARD_S</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566047">KSPROPERTY_VIDEODECODER_CAPS_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_AnalogVideoStandard enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
