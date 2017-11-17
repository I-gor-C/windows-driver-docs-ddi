---
UID: NS.ksmedia._tagKSTOPOLOGY_ENDPOINTIDPAIR
title: tagKSTOPOLOGY_ENDPOINTIDPAIR
author: windows-driver-content
description: The KSTOPOLOGY_ENDPOINTIDPAIR structure specifies the render and capture endpoint IDs to use for the KSPROPERTY_TELEPHONY_ENDPOINTIDPAIR property.
old-location: audio\kstopology_endpointidpair.htm
ms.assetid: 556B56A6-1EF4-406B-A9FB-901C0CF24BC0
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10,Windows 10 Mobile
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSTOPOLOGY_ENDPOINTIDPAIR
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
ms.keywords: tagKSTOPOLOGY_ENDPOINTIDPAIR, KSTOPOLOGY_ENDPOINTIDPAIR, *PKSTOPOLOGY_ENDPOINTIDPAIR
req.iface: 
---

# tagKSTOPOLOGY_ENDPOINTIDPAIR structure



## -description
<p>The <b>KSTOPOLOGY_ENDPOINTIDPAIR</b> structure specifies the render and capture endpoint IDs to use for the <a href="https://msdn.microsoft.com/library/windows/hardware/mt169874">KSPROPERTY_TELEPHONY_ENDPOINTIDPAIR</a> property.</p>


## -syntax

````
typedef struct _tagKSTOPOLOGY_ENDPOINTIDPAIR {
  KSTOPOLOGY_ENDPOINTID RenderEndpoint;
  KSTOPOLOGY_ENDPOINTID CaptureEndpoint;
} KSTOPOLOGY_ENDPOINTIDPAIR, *PKSTOPOLOGY_ENDPOINTIDPAIR;
````


## -struct-fields
<dl>

### -field <b>RenderEndpoint</b>

<dd>
<p>Specifies the render endpoint ID.</p>
</dd>

### -field <b>CaptureEndpoint</b>

<dd>
<p>Specifies the capture endpoint ID. </p>
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
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Client</p>
</th>
<td width="70%">
<p>Windows 10 Mobile</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt169886">KSTOPOLOGY_ENDPOINTID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSTOPOLOGY_ENDPOINTIDPAIR structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
