---
UID: NE.ksmedia.KSPROPERTY_AUDIOENGINE
title: KSPROPERTY_AUDIOENGINE
author: windows-driver-content
description: The properties contained in the KSPROPSETID_AudioEngine property set are defined by this enumeration and must be supported by a KSNODETYPE_AUDIO_ENGINE node.
old-location: audio\ksproperty_audioengine.htm
ms.assetid: F20C05A3-C8A0-4061-93B9-03FD19D37C82
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_AUDIOENGINE
req.alt-loc: Ksmedia.h
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

# KSPROPERTY_AUDIOENGINE enumeration



## -description
<p>The properties contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450902">KSPROPSETID_AudioEngine</a> property set are defined by this enumeration and must be supported by a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450866">KSNODETYPE_AUDIO_ENGINE</a> node.</p>


## -syntax

````
typedef enum  { 
  KSPROPERTY_AUDIOENGINE_LFXENABLE               = 0,
  KSPROPERTY_AUDIOENGINE_GFXENABLE               = 1,
  KSPROPERTY_AUDIOENGINE_MIXFORMAT               = 2,
  KSPROPERTY_AUDIOENGINE_DEVICEFORMAT            = 4,
  KSPROPERTY_AUDIOENGINE_SUPPORTEDDEVICEFORMATS  = 5,
  KSPROPERTY_AUDIOENGINE_DESCRIPTOR              = 6,
  KSPROPERTY_AUDIOENGINE_BUFFER_SIZE_RANGE       = 7,
  KSPROPERTY_AUDIOENGINE_LOOPBACK_PROTECTION     = 8,
  KSPROPERTY_AUDIOENGINE_VOLUMELEVEL             = 9
} KSPROPERTY_AUDIOENGINE;
````


## -enum-fields
<dl>

### -field <a id="KSPROPERTY_AUDIOENGINE_LFXENABLE"></a><a id="ksproperty_audioengine_lfxenable"></a><b>KSPROPERTY_AUDIOENGINE_LFXENABLE</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450876">KSPROPERTY_AUDIOENGINE_LFXENABLE</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_AUDIOENGINE_GFXENABLE"></a><a id="ksproperty_audioengine_gfxenable"></a><b>KSPROPERTY_AUDIOENGINE_GFXENABLE</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450874">KSPROPERTY_AUDIOENGINE_GFXENABLE</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_AUDIOENGINE_MIXFORMAT"></a><a id="ksproperty_audioengine_mixformat"></a><b>KSPROPERTY_AUDIOENGINE_MIXFORMAT</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450880">KSPROPERTY_AUDIOENGINE_MIXFORMAT</a>   property.</p>
</dd>

### -field <a id="KSPROPERTY_AUDIOENGINE_DEVICEFORMAT"></a><a id="ksproperty_audioengine_deviceformat"></a><b>KSPROPERTY_AUDIOENGINE_DEVICEFORMAT</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450872">KSPROPERTY_AUDIOENGINE_DEVICEFORMAT</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_AUDIOENGINE_SUPPORTEDDEVICEFORMATS"></a><a id="ksproperty_audioengine_supporteddeviceformats"></a><b>KSPROPERTY_AUDIOENGINE_SUPPORTEDDEVICEFORMATS</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450884">KSPROPERTY_AUDIOENGINE_SUPPORTEDDEVICEFORMATS</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_AUDIOENGINE_DESCRIPTOR"></a><a id="ksproperty_audioengine_descriptor"></a><b>KSPROPERTY_AUDIOENGINE_DESCRIPTOR</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450870">KSPROPERTY_AUDIOENGINE_DESCRIPTOR</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_AUDIOENGINE_BUFFER_SIZE_RANGE"></a><a id="ksproperty_audioengine_buffer_size_range"></a><b>KSPROPERTY_AUDIOENGINE_BUFFER_SIZE_RANGE</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450868">KSPROPERTY_AUDIOENGINE_BUFFER_SIZE_RANGE</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_AUDIOENGINE_LOOPBACK_PROTECTION"></a><a id="ksproperty_audioengine_loopback_protection"></a><b>KSPROPERTY_AUDIOENGINE_LOOPBACK_PROTECTION</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450878">KSPROPERTY_AUDIOENGINE_LOOPBACK_PROTECTION</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_AUDIOENGINE_VOLUMELEVEL"></a><a id="ksproperty_audioengine_volumelevel"></a><b>KSPROPERTY_AUDIOENGINE_VOLUMELEVEL</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh831855">KSPROPERTY_AUDIOENGINE_VOLUMELEVEL</a> property.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450866">KSNODETYPE_AUDIO_ENGINE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450902">KSPROPSETID_AudioEngine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSPROPERTY_AUDIOENGINE enumeration%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
