---
UID: NS.61883._BUS_GENERATION_NODE
title: BUS_GENERATION_NODE
author: windows-driver-content
description: The BUS_GENERATION_NODE structure is used in conjunction with the Av61883_GetUnitInfo request to retrieve bus characteristics.
old-location: ieee\bus_generation_node.htm
ms.assetid: 8db151ca-6358-41b0-a96a-e69b9d6c2c95
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 61883.h
req.include-header: 61883.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BUS_GENERATION_NODE
req.alt-loc: 61883.h
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
ms.keywords: BUS_GENERATION_NODE, BUS_GENERATION_NODE, *PBUS_GENERATION_NODE
---

# BUS_GENERATION_NODE structure



## -description
<p>The BUS_GENERATION_NODE structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536983">Av61883_GetUnitInfo</a> request to retrieve bus characteristics. </p>


## -syntax

````
typedef struct _BUS_GENERATION_NODE {
  ULONG        GenerationCount;
  NODE_ADDRESS LocalNodeAddress;
  NODE_ADDRESS DeviceNodeAddress;
} BUS_GENERATION_NODE, *PBUS_GENERATION_NODE;
````


## -struct-fields
<dl>

### -field <b>GenerationCount</b>

<dd>
<p>The current bus generation count.</p>
</dd>

### -field <b>LocalNodeAddress</b>

<dd>
<p>The current node address of the local node.</p>
</dd>

### -field <b>DeviceNodeAddress</b>

<dd>
<p>The current node address of the device.</p>
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
<dt>61883.h (include 61883.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536983">Av61883_GetUnitInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20BUS_GENERATION_NODE structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
