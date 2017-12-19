---
UID: NS.NTDDRILAPITYPES.RILTERMINALCAPABILITYINFO
title: RILTERMINALCAPABILITYINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilterminalcapabilityinfo.htm
old-project: NetVista
ms.assetid: e6ad67bf-cd16-469e-af49-6a640a4319c0
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILTERMINALCAPABILITYINFO, RILTERMINALCAPABILITYINFO, LPRILTERMINALCAPABILITYINFO, *LPRILTERMINALCAPABILITYINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILTERMINALCAPABILITYINFO
req.alt-loc: ntddrilapitypes.h
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
---

# RILTERMINALCAPABILITYINFO structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILTERMINALCAPABILITYINFO {
  DWORD      dwSize;
  BYTE [256] bData;
} RILTERMINALCAPABILITYINFO, RILTERMINALCAPABILITYINFO;
````


## -struct-fields

### -field dwSize


### -field bData


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>