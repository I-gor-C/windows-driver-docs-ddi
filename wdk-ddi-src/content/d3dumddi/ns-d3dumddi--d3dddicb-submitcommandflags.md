---
UID: NS.d3dumddi._D3DDDICB_SUBMITCOMMANDFLAGS
title: D3DDDICB_SUBMITCOMMANDFLAGS
author: windows-driver-content
description: D3DDDICB_SUBMITCOMMANDFLAGS is used to indicate how to process command buffers on contexts that support graphics processing unit (GPU) virtual addressing.
old-location: display\d3dddicb_submitcommandflags.htm
old-project: display
ms.assetid: 415255A8-4D43-4677-B4B3-0425D6D57933
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_SUBMITCOMMANDFLAGS, D3DDDICB_SUBMITCOMMANDFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_SUBMITCOMMANDFLAGS
req.alt-loc: d3dumddi.h
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

# D3DDDICB_SUBMITCOMMANDFLAGS structure



## -description
<p><b>D3DDDICB_SUBMITCOMMANDFLAGS</b> is used to indicate how to process command buffers on contexts that support graphics processing unit (GPU) virtual addressing.</p>


## -syntax

````
typedef struct _D3DDDICB_SUBMITCOMMANDFLAGS {
  union {
    struct {
      UINT NullRendering  :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  };
} D3DDDICB_SUBMITCOMMANDFLAGS;
````


## -struct-fields
<dl>

### -field <b>NullRendering</b>

<dd>
<p>Indicates  whether the associated  command buffers should be processed. When set, the command buffers should not be processed. This flag is set only during performance investigating and debugging to simulate an infinitely fast rendering engine that still must perform the overhead of DMA buffer submission and signaling. <b>NullRendering</b> is never set during typical operations.

</p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit Value member (0x00000001).
</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. </p>
<p>Setting this member to zero is equivalent to setting the remaining 31 bits (0xFFFFFFFE) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>The consolidated value of the bit-field members in this structure.</p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>