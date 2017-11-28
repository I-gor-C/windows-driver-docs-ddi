---
UID: NS.ksmedia.PKSPROPERTY_VIDEOCONTROL_CAPS_S
title: PKSPROPERTY_VIDEOCONTROL_CAPS_S
author: windows-driver-content
description: The KSPROPERTY_VIDEOCONTROL_CAPS_S structure describes the video-control capabilities of a minidriver, such as image flipping or event triggering abilities.
old-location: stream\ksproperty_videocontrol_caps_s.htm
old-project: stream
ms.assetid: e651202a-d0da-4147-9439-6cf0731c4886
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSPROPERTY_VIDEOCONTROL_CAPS_S, KSPROPERTY_VIDEOCONTROL_CAPS_S, *PKSPROPERTY_VIDEOCONTROL_CAPS_S
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_VIDEOCONTROL_CAPS_S
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
req.iface: 
---

# PKSPROPERTY_VIDEOCONTROL_CAPS_S structure



## -description
<p>The KSPROPERTY_VIDEOCONTROL_CAPS_S structure describes the video-control capabilities of a minidriver, such as image flipping or event triggering abilities.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  ULONG      StreamIndex;
  ULONG      VideoControlCaps;
} KSPROPERTY_VIDEOCONTROL_CAPS_S, *PKSPROPERTY_VIDEOCONTROL_CAPS_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>StreamIndex</b>

<dd>
<p>Contains the zero-based index of the stream.</p>
</dd>

### -field <b>VideoControlCaps</b>

<dd>
<p>Indicates the video control capabilities for the specified stream. This member must be set to one or more (logically ORed) values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567696">KS_VideoControlFlags</a> enumeration.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567696">KS_VideoControlFlags</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568120">PROPSETID_VIDCAP_VIDEOCONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566035">KSPROPERTY_VIDEOCONTROL_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566043">KSPROPERTY_VIDEOCONTROL_MODE_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_VIDEOCONTROL_CAPS_S structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
