---
UID: NS.ksmedia.PKSPROPERTY_VIDEOCOMPRESSION_S
title: PKSPROPERTY_VIDEOCOMPRESSION_S
author: windows-driver-content
description: The KSPROPERTY_VIDEOCOMPRESSION_S structure describes a single KSPROPERTY_VIDEOCOMPRESSION_Xxx property of a specified stream.
old-location: stream\ksproperty_videocompression_s.htm
ms.assetid: 0fc80a67-de81-4cdf-8c38-bbf78c62d017
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
req.alt-api: KSPROPERTY_VIDEOCOMPRESSION_S
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
ms.keywords: PKSPROPERTY_VIDEOCOMPRESSION_S, KSPROPERTY_VIDEOCOMPRESSION_S, *PKSPROPERTY_VIDEOCOMPRESSION_S
req.iface: 
---

# PKSPROPERTY_VIDEOCOMPRESSION_S structure



## -description
<p>The KSPROPERTY_VIDEOCOMPRESSION_S structure describes a single KSPROPERTY_VIDEOCOMPRESSION_Xxx property of a specified stream. </p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  ULONG      StreamIndex;
  LONG       Value;
} KSPROPERTY_VIDEOCOMPRESSION_S, *PKSPROPERTY_VIDEOCOMPRESSION_S;
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

### -field <b>Value</b>

<dd>
<p>Specifies the value of a request. For Set requests, the minidriver must set the property specified in <b>Property</b> to this value. For Get requests, the minidriver must return the value of the property specified in <b>Property</b>.</p>
</dd>
</dl>

## -remarks
<p>All KSPROPERTY_VIDEOCOMPRESSION properties that use this structure are read/write.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567813">PROPSETID_VIDCAP_VIDEOCOMPRESSION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565986">KSPROPERTY_VIDEOCOMPRESSION_KEYFRAME_RATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566009">KSPROPERTY_VIDEOCOMPRESSION_PFRAMES_PER_KEYFRAME</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566015">KSPROPERTY_VIDEOCOMPRESSION_QUALITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566004">KSPROPERTY_VIDEOCOMPRESSION_OVERRIDE_KEYFRAME</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565991">KSPROPERTY_VIDEOCOMPRESSION_OVERRIDE_FRAME_SIZE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566019">KSPROPERTY_VIDEOCOMPRESSION_WINDOWSIZE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_VIDEOCOMPRESSION_S structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
