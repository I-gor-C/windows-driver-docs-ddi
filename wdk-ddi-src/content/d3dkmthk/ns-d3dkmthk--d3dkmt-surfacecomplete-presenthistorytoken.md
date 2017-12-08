---
UID: NS.d3dkmthk._D3DKMT_SURFACECOMPLETE_PRESENTHISTORYTOKEN
title: D3DKMT_SURFACECOMPLETE_PRESENTHISTORYTOKEN
author: windows-driver-content
description: A structure used to present the history token for a surface.
old-location: display\d3dkmt_surfacecomplete_presenthistorytoken.htm
old-project: display
ms.assetid: AF58684E-3516-48F9-B771-63701C00645F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_SURFACECOMPLETE_PRESENTHISTORYTOKEN, D3DKMT_SURFACECOMPLETE_PRESENTHISTORYTOKEN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_SURFACECOMPLETE_PRESENTHISTORYTOKEN
req.alt-loc: d3dkmthk.h
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

# D3DKMT_SURFACECOMPLETE_PRESENTHISTORYTOKEN structure



## -description
<p>A structure used to present the history token for a surface.</p>


## -syntax

````
typedef struct _D3DKMT_SURFACECOMPLETE_PRESENTHISTORYTOKEN {
  ULONG64 hLogicalSurface;
} D3DKMT_SURFACECOMPLETE_PRESENTHISTORYTOKEN;
````


## -struct-fields
<dl>

### -field hLogicalSurface

<dd>
<p>The logical surface that the token is being presented for.</p>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>