---
UID: NS.ks.PKSRATE_CAPABILITY
title: PKSRATE_CAPABILITY
author: windows-driver-content
description: The client uses the KSRATE_CAPABILITY structure in a KSPROPERTY_STREAM_RATECAPABILITY property request.
old-location: stream\ksrate_capability.htm
ms.assetid: 70866a87-0ebd-4230-9958-ace18116fa23
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSRATE_CAPABILITY
req.alt-loc: ks.h
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
ms.keywords: PKSRATE_CAPABILITY, KSRATE_CAPABILITY, *PKSRATE_CAPABILITY
req.iface: 
---

# PKSRATE_CAPABILITY structure



## -description
<p>The client uses the KSRATE_CAPABILITY structure in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565756">KSPROPERTY_STREAM_RATECAPABILITY</a> property request.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  KSRATE     Rate;
} KSRATE_CAPABILITY, *PKSRATE_CAPABILITY;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> that specifies the property identifier.</p>
</dd>

### -field <b>Rate</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff566752">KSRATE</a> that specifies the requested rate.</p>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>