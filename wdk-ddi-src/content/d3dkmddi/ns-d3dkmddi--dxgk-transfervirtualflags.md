---
UID: NS.d3dkmddi._DXGK_TRANSFERVIRTUALFLAGS
title: DXGK_TRANSFERVIRTUALFLAGS
author: windows-driver-content
description: DXGK_TRANSFERVIRTUALFLAGS is used as part of an allocation transfer operation.
old-location: display\dxgk_transfervirtualflags.htm
old-project: display
ms.assetid: E5323A30-5BBE-4084-9F99-91FBDD680C12
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_TRANSFERVIRTUALFLAGS, DXGK_TRANSFERVIRTUALFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_TRANSFERVIRTUALFLAGS
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_TRANSFERVIRTUALFLAGS structure



## -description
<p><b>DXGK_TRANSFERVIRTUALFLAGS</b> is used as part of an allocation transfer operation.</p>


## -syntax

````
typedef struct _DXGK_TRANSFERVIRTUALFLAGS {
  union {
    struct {
      UINT Src64KBPages  :1;
      UINT Dst64KBPages  :1;
      UINT Reserved  :30;
    };
    UINT   Flags;
  };
} DXGK_TRANSFERVIRTUALFLAGS;
````


## -struct-fields
<dl>

### -field <b>Src64KBPages</b>

<dd>
<p>When set, the source page tables are mapped to  64KB pages.</p>
</dd>

### -field <b>Dst64KBPages</b>

<dd>
<p>When set, the destination page tables are mapped to  64KB pages.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The consolidated value of the structure flags.</p>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>