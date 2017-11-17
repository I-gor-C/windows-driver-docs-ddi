---
UID: NS.d3dkmthk._D3DKMT_CREATESTANDARDALLOCATION
title: D3DKMT_CREATESTANDARDALLOCATION
author: windows-driver-content
description: Used to create a standard allocation.
old-location: display\d3dkmt-createstandardallocation.htm
ms.assetid: 7698ab93-68af-479d-97a4-c45ac84b0710
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_CREATESTANDARDALLOCATION
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
ms.keywords: D3DKMT_CREATESTANDARDALLOCATION, D3DKMT_CREATESTANDARDALLOCATION
req.iface: 
---

# D3DKMT_CREATESTANDARDALLOCATION structure



## -description
<p>Used to create a standard allocation.</p>


## -syntax

````
typedef struct _D3DKMT_CREATESTANDARDALLOCATION {
  D3DKMT_STANDARDALLOCATIONTYPE        Type;
  union {
    D3DKMT_STANDARDALLOCATION_EXISTINGHEAP ExistingHeapData;
  };
  D3DKMT_CREATESTANDARDALLOCATIONFLAGS Flags;
} D3DKMT_CREATESTANDARDALLOCATION;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The type of the standard allocation.</p>
</dd>

### -field <b>ExistingHeapData</b>

<dd>
<p>Holds information on the existing heap.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Holds the flags needed to create a standard allocation.</p>
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