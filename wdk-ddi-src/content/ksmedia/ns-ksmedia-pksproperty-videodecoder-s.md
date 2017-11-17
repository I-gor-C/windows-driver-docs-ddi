---
UID: NS.ksmedia.PKSPROPERTY_VIDEODECODER_S
title: PKSPROPERTY_VIDEODECODER_S
author: windows-driver-content
description: The KSPROPERTY_VIDEODECODER_S structure describes property settings in the PROPSETID_VIDCAP_VIDEODECODER property set.
old-location: stream\ksproperty_videodecoder_s.htm
ms.assetid: 9444835d-0290-49e7-8f49-a1506ce282cd
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
req.alt-api: KSPROPERTY_VIDEODECODER_S
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
ms.keywords: PKSPROPERTY_VIDEODECODER_S, KSPROPERTY_VIDEODECODER_S, *PKSPROPERTY_VIDEODECODER_S
req.iface: 
---

# PKSPROPERTY_VIDEODECODER_S structure



## -description
<p>The KSPROPERTY_VIDEODECODER_S structure describes property settings in the PROPSETID_VIDCAP_VIDEODECODER property set.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  ULONG      Value;
} KSPROPERTY_VIDEODECODER_S, *PKSPROPERTY_VIDEODECODER_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>Specifies the value of a request. For Set requests, the minidriver should set the property specified in <b>Property</b> to this value. For Get requests, the minidriver should return the value of the property specified in <b>Property</b>.</p>
</dd>
</dl>

## -remarks
<p>The KSPROPERTY_VIDEODECODER_S structure is shared among the KSPROPERTY_VIDEODECODER_STANDARD, KSPROPERTY_VIDEODECODER_OUTPUT_ENABLE, and KSPROPERTY_VIDEODECODER_VCR_TIMING properties within the property set. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566058">KSPROPERTY_VIDEODECODER_STANDARD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566051">KSPROPERTY_VIDEODECODER_OUTPUT_ENABLE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566062">KSPROPERTY_VIDEODECODER_VCR_TIMING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_VIDEODECODER_S structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
