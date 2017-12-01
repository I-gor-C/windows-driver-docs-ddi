---
UID: NE.d3dkmdt._D3DKMDT_VIDEO_SIGNAL_STANDARD
title: D3DKMDT_VIDEO_SIGNAL_STANDARD
author: windows-driver-content
description: The D3DKMDT_VIDEO_SIGNAL_STANDARD enumeration contains constants that represent video signal standards.
old-location: display\d3dkmdt_video_signal_standard.htm
old-project: display
ms.assetid: bb129e02-ae01-4bbc-a81f-809f1a27060c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_VIDEO_SIGNAL_STANDARD
req.alt-loc: d3dkmdt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# D3DKMDT_VIDEO_SIGNAL_STANDARD enumeration



## -description
<p>The D3DKMDT_VIDEO_SIGNAL_STANDARD enumeration contains constants that represent video signal standards.</p>


## -syntax

````
typedef enum _D3DKMDT_VIDEO_SIGNAL_STANDARD { 
  D3DKMDT_VSS_UNINITIALIZED  = 0,
  D3DKMDT_VSS_VESA_DMT       = 1,
  D3DKMDT_VSS_VESA_GTF       = 2,
  D3DKMDT_VSS_VESA_CVT       = 3,
  D3DKMDT_VSS_IBM            = 4,
  D3DKMDT_VSS_APPLE          = 5,
  D3DKMDT_VSS_NTSC_M         = 6,
  D3DKMDT_VSS_NTSC_J         = 7,
  D3DKMDT_VSS_NTSC_443       = 8,
  D3DKMDT_VSS_PAL_B          = 9,
  D3DKMDT_VSS_PAL_B1         = 10,
  D3DKMDT_VSS_PAL_G          = 11,
  D3DKMDT_VSS_PAL_H          = 12,
  D3DKMDT_VSS_PAL_I          = 13,
  D3DKMDT_VSS_PAL_D          = 14,
  D3DKMDT_VSS_PAL_N          = 15,
  D3DKMDT_VSS_PAL_NC         = 16,
  D3DKMDT_VSS_SECAM_B        = 17,
  D3DKMDT_VSS_SECAM_D        = 18,
  D3DKMDT_VSS_SECAM_G        = 19,
  D3DKMDT_VSS_SECAM_H        = 20,
  D3DKMDT_VSS_SECAM_K        = 21,
  D3DKMDT_VSS_SECAM_K1       = 22,
  D3DKMDT_VSS_SECAM_L        = 23,
  D3DKMDT_VSS_SECAM_L1       = 24,
  D3DKMDT_VSS_EIA_861        = 25,
  D3DKMDT_VSS_EIA_861A       = 26,
  D3DKMDT_VSS_EIA_861B       = 27,
  D3DKMDT_VSS_PAL_K          = 28,
  D3DKMDT_VSS_PAL_K1         = 29,
  D3DKMDT_VSS_PAL_L          = 30,
  D3DKMDT_VSS_PAL_M          = 31,
  D3DKMDT_VSS_OTHER          = 255
} D3DKMDT_VIDEO_SIGNAL_STANDARD;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_VSS_UNINITIALIZED"></a><a id="d3dkmdt_vss_uninitialized"></a><b>D3DKMDT_VSS_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_VIDEO_SIGNAL_STANDARD has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_VSS_VESA_DMT"></a><a id="d3dkmdt_vss_vesa_dmt"></a><b>D3DKMDT_VSS_VESA_DMT</b>

<dd>
<p>Represents the Video Electronics Standards Association (VESA) Display Monitor Timing (DMT) standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_VESA_GTF"></a><a id="d3dkmdt_vss_vesa_gtf"></a><b>D3DKMDT_VSS_VESA_GTF</b>

<dd>
<p>Represents the VESA Generalized Timing Formula (GTF) standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_VESA_CVT"></a><a id="d3dkmdt_vss_vesa_cvt"></a><b>D3DKMDT_VSS_VESA_CVT</b>

<dd>
<p>Represents the VESA Coordinated Video Timing (CVT) standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_IBM"></a><a id="d3dkmdt_vss_ibm"></a><b>D3DKMDT_VSS_IBM</b>

<dd>
<p>Represents the IBM standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_APPLE"></a><a id="d3dkmdt_vss_apple"></a><b>D3DKMDT_VSS_APPLE</b>

<dd>
<p>Represents the Apple standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_NTSC_M"></a><a id="d3dkmdt_vss_ntsc_m"></a><b>D3DKMDT_VSS_NTSC_M</b>

<dd>
<p>Represents the National Television Standards Committee (NTSC) standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_NTSC_J"></a><a id="d3dkmdt_vss_ntsc_j"></a><b>D3DKMDT_VSS_NTSC_J</b>

<dd>
<p>Represents the NTSC standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_NTSC_443"></a><a id="d3dkmdt_vss_ntsc_443"></a><b>D3DKMDT_VSS_NTSC_443</b>

<dd>
<p>Represents the NTSC standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_B"></a><a id="d3dkmdt_vss_pal_b"></a><b>D3DKMDT_VSS_PAL_B</b>

<dd>
<p>Represents the Phase Alteration Line (PAL) standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_B1"></a><a id="d3dkmdt_vss_pal_b1"></a><b>D3DKMDT_VSS_PAL_B1</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_G"></a><a id="d3dkmdt_vss_pal_g"></a><b>D3DKMDT_VSS_PAL_G</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_H"></a><a id="d3dkmdt_vss_pal_h"></a><b>D3DKMDT_VSS_PAL_H</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_I"></a><a id="d3dkmdt_vss_pal_i"></a><b>D3DKMDT_VSS_PAL_I</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_D"></a><a id="d3dkmdt_vss_pal_d"></a><b>D3DKMDT_VSS_PAL_D</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_N"></a><a id="d3dkmdt_vss_pal_n"></a><b>D3DKMDT_VSS_PAL_N</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_NC"></a><a id="d3dkmdt_vss_pal_nc"></a><b>D3DKMDT_VSS_PAL_NC</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_SECAM_B"></a><a id="d3dkmdt_vss_secam_b"></a><b>D3DKMDT_VSS_SECAM_B</b>

<dd>
<p>Represents the Systeme Electronic Pour Couleur Avec Memoire (SECAM) standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_SECAM_D"></a><a id="d3dkmdt_vss_secam_d"></a><b>D3DKMDT_VSS_SECAM_D</b>

<dd>
<p>Represents the SECAM standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_SECAM_G"></a><a id="d3dkmdt_vss_secam_g"></a><b>D3DKMDT_VSS_SECAM_G</b>

<dd>
<p>Represents the SECAM standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_SECAM_H"></a><a id="d3dkmdt_vss_secam_h"></a><b>D3DKMDT_VSS_SECAM_H</b>

<dd>
<p>Represents the SECAM standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_SECAM_K"></a><a id="d3dkmdt_vss_secam_k"></a><b>D3DKMDT_VSS_SECAM_K</b>

<dd>
<p>Represents the SECAM standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_SECAM_K1"></a><a id="d3dkmdt_vss_secam_k1"></a><b>D3DKMDT_VSS_SECAM_K1</b>

<dd>
<p>Represents the SECAM standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_SECAM_L"></a><a id="d3dkmdt_vss_secam_l"></a><b>D3DKMDT_VSS_SECAM_L</b>

<dd>
<p>Represents the SECAM standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_SECAM_L1"></a><a id="d3dkmdt_vss_secam_l1"></a><b>D3DKMDT_VSS_SECAM_L1</b>

<dd>
<p>Represents the SECAM standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_EIA_861"></a><a id="d3dkmdt_vss_eia_861"></a><b>D3DKMDT_VSS_EIA_861</b>

<dd>
<p>Represents the Electronics Industries Association (EIA) standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_EIA_861A"></a><a id="d3dkmdt_vss_eia_861a"></a><b>D3DKMDT_VSS_EIA_861A</b>

<dd>
<p>Represents the EIA standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_EIA_861B"></a><a id="d3dkmdt_vss_eia_861b"></a><b>D3DKMDT_VSS_EIA_861B</b>

<dd>
<p>Represents the EIA standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_K"></a><a id="d3dkmdt_vss_pal_k"></a><b>D3DKMDT_VSS_PAL_K</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_K1"></a><a id="d3dkmdt_vss_pal_k1"></a><b>D3DKMDT_VSS_PAL_K1</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_L"></a><a id="d3dkmdt_vss_pal_l"></a><b>D3DKMDT_VSS_PAL_L</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_PAL_M"></a><a id="d3dkmdt_vss_pal_m"></a><b>D3DKMDT_VSS_PAL_M</b>

<dd>
<p>Represents the PAL standard.</p>
</dd>

### -field <a id="D3DKMDT_VSS_OTHER"></a><a id="d3dkmdt_vss_other"></a><b>D3DKMDT_VSS_OTHER</b>

<dd>
<p>Represents any video standard other than those represented by the previous constants in this enumeration.</p>
</dd>
</dl>

## -remarks
<p>The <b>SignalInfo</b> member of the <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-target-mode.md">D3DKMDT_VIDPN_TARGET_MODE</a> structure is a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-video-signal-info.md">D3DKMDT_VIDEO_SIGNAL_MODE</a> structure.</p>

<p>The <b>VideoStandard</b> member of the D3DKMDT_VIDEO_SIGNAL_MODE structure is a D3DKMDT_VIDEO_SIGNAL_STANDARD value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.vidpn_target_mode_set_interface">VidPn Target Mode Set Interface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_VIDEO_SIGNAL_STANDARD enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
