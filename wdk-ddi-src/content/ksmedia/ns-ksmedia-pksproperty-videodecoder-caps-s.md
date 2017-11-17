---
UID: NS.ksmedia.PKSPROPERTY_VIDEODECODER_CAPS_S
title: PKSPROPERTY_VIDEODECODER_CAPS_S
author: windows-driver-content
description: The KSPROPERTY_VIDEODECODER_CAPS_S structure describes the hardware capabilities of the video decoder device.
old-location: stream\ksproperty_videodecoder_caps_s.htm
ms.assetid: af81a053-8c09-411c-a437-21859ea867b2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_VIDEODECODER_CAPS_S
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
ms.keywords: PKSPROPERTY_VIDEODECODER_CAPS_S, KSPROPERTY_VIDEODECODER_CAPS_S, *PKSPROPERTY_VIDEODECODER_CAPS_S
req.iface: 
---

# PKSPROPERTY_VIDEODECODER_CAPS_S structure



## -description
<p>The KSPROPERTY_VIDEODECODER_CAPS_S structure describes the hardware capabilities of the video decoder device.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  ULONG      StandardsSupported;
  ULONG      Capabilities;
  ULONG      SettlingTime;
  ULONG      HSyncPerVSync;
} KSPROPERTY_VIDEODECODER_CAPS_S, *PKSPROPERTY_VIDEODECODER_CAPS_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>StandardsSupported</b>

<dd>
<p>Specifies the video standards supported by the device. This member may be set to one or more (logically ORed) values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567297">KS_AnalogVideoStandard</a> enumeration.</p>
</dd>

### -field <b>Capabilities</b>

<dd>
<p>Specifies video decoder capabilities. This member must be set to zero or one of the values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567697">KS_VIDEODECODER_FLAGS</a> enumeration.</p>
</dd>

### -field <b>SettlingTime</b>

<dd>
<p>Specifies the settling time when changing input video sources. This value is expressed in milliseconds.</p>
</dd>

### -field <b>HSyncPerVSync</b>

<dd>
<p>Specifies the number of horizontal sync pulses the video decoder produces during the vertical sync period. Decoders that follow the ITU_656 should set this value to six.</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567297">KS_AnalogVideoStandard</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567697">KS_VIDEODECODER_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568121">PROPSETID_VIDCAP_VIDEODECODER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566046">KSPROPERTY_VIDEODECODER_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_VIDEODECODER_CAPS_S structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
