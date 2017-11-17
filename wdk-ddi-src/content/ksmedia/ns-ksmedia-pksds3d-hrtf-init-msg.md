---
UID: NS.ksmedia.PKSDS3D_HRTF_INIT_MSG
title: PKSDS3D_HRTF_INIT_MSG
author: windows-driver-content
description: The KSDS3D_HRTF_INIT_MSG structure specifies the parameter settings to use to initialize the head-relative transfer function (HRTF).
old-location: audio\ksds3d_hrtf_init_msg.htm
ms.assetid: 8e25a1e2-24b1-418c-b1eb-884bdbad63b3
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSDS3D_HRTF_INIT_MSG
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
ms.keywords: PKSDS3D_HRTF_INIT_MSG, KSDS3D_HRTF_INIT_MSG, *PKSDS3D_HRTF_INIT_MSG
req.iface: 
---

# PKSDS3D_HRTF_INIT_MSG structure



## -description
<p>The KSDS3D_HRTF_INIT_MSG structure specifies the parameter settings to use to initialize the head-relative transfer function (HRTF).</p>


## -syntax

````
typedef struct {
  ULONG                      Size;
  KSDS3D_HRTF_FILTER_QUALITY Quality;
  FLOAT                      SampleRate;
  ULONG                      MaxFilterSize;
  ULONG                      FilterTransientMuteLength;
  ULONG                      FilterOverlapBufferLength;
  ULONG                      OutputOverlapBufferLength;
  ULONG                      Reserved;
} KSDS3D_HRTF_INIT_MSG, *PKSDS3D_HRTF_INIT_MSG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size in bytes of the structure.</p>
</dd>

### -field <b>Quality</b>

<dd>
<p>Specifies the HRTF filter quality level. Set this parameter to one of the following KSDS3D_HRTF_FILTER_QUALITY enumeration values:</p>
<ul>
<li>
<p>LIGHT_FILTER selects an efficient algorithm that produces a good quality effect.</p>
</li>
<li>
<p>FULL_FILTER selects an algorithm that produces a high-quality effect but requires more processing time.</p>
</li>
</ul>
</dd>

### -field <b>SampleRate</b>

<dd>
<p>Specifies the sample rate, in samples per second (hertz), at which each channel should be played. For example, a value of 22,050 specifies a sample rate of 22.05 kHz.</p>
</dd>

### -field <b>MaxFilterSize</b>

<dd>
<p>Specifies the maximum filter size in bytes. If the filter is in direct form, the maximum size is the order of the filter (numerator and denominator have equal order). If the filter is in cascade form, the maximum size is the maximum number of biquadratic coefficients.</p>
</dd>

### -field <b>FilterTransientMuteLength</b>

<dd>
<p>Specifies how long to delay cross-fading to the new filter in order to avoid introducing the new filter's initial transient signal into the output signal. The delay is specified as a number of initial samples produced by the new filter. During this time, the output comes from the old filters only.</p>
</dd>

### -field <b>FilterOverlapBufferLength</b>

<dd>
<p>Specifies the total number of samples over which to mute and cross-fade the filter outputs.</p>
</dd>

### -field <b>OutputOverlapBufferLength</b>

<dd>
<p>Specifies the number of samples over which to cross-fade the output channels after a transition across azimuth angle zero. This member is used when cross-fading of the output channels is enabled by the <b>CrossFadeOutput</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff537108">KSDS3D_HRTF_PARAMS_MSG</a>.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Set to zero.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537355">KSPROPERTY_HRTF3D_INITIALIZE</a> property.</p>

<p>The <b>Quality</b> values FULL_FILTER and LIGHT_FILTER correspond to the GUID_DS3DALG_HRTF_FULL and GUID_DS3DALG_HRTF_LIGHT settings that are described in the Microsoft Windows SDK documentation.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff537482">KSPROPSETID_Hrtf3d</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537108">KSDS3D_HRTF_PARAMS_MSG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537355">KSPROPERTY_HRTF3D_INITIALIZE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537482">KSPROPSETID_Hrtf3d</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSDS3D_HRTF_INIT_MSG structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
