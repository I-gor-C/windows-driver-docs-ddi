---
UID: NS.iddcx.IDDCX_MOVEREGION~r1
title: IDDCX_MOVEREGION
author: windows-driver-content
description: Gives information about the current move region.
old-location: display\iddcx_moveregion.htm
old-project: display
ms.assetid: 28974c00-9225-4458-a198-beb4538e3a45
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_MOVEREGION,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_MOVEREGION
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDDCX_MOVEREGION structure



## -description
<p>
                 Gives information about the current move region.</p>


## -syntax

````
typedef struct IDDCX_MOVEREGION {
  UINT  Size;
  POINT SourcePoint;
  RECT  DestRect;
} IDDCX_MOVEREGION, *IDDCX_MOVEREGION;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>
                     Total size of the structure.
                 </p>
</dd>

### -field SourcePoint

<dd>
<p>
                     The location within the surface of the top left of the source rect. The source rect size is the same as the
    destination rect size.
                 </p>
</dd>

### -field DestRect

<dd>
<p>
                     Defines the destination rect of the move.
                 </p>
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>