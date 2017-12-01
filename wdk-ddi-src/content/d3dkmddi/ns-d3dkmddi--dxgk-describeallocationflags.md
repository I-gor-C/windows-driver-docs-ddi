---
UID: NS.d3dkmddi._DXGK_DESCRIBEALLOCATIONFLAGS
title: DXGK_DESCRIBEALLOCATIONFLAGS
author: windows-driver-content
description: Used in the DXGKARG_DESCRIBEALLOCATION.Flags member to describe whether an existing allocation is being queried for its display mode.
old-location: display\dxgk_describeallocationflags.htm
old-project: display
ms.assetid: f5cab74a-19ce-45d1-9c6f-461a98c4506c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_DESCRIBEALLOCATIONFLAGS, DXGK_DESCRIBEALLOCATIONFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DESCRIBEALLOCATIONFLAGS
req.alt-loc: D3dkmddi.h
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

# DXGK_DESCRIBEALLOCATIONFLAGS structure



## -description
<p>Used in the <a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-describeallocation.md">DXGKARG_DESCRIBEALLOCATION</a>.<b>Flags</b> member to describe whether an existing allocation is being queried for its display mode.</p>


## -syntax

````
typedef struct _DXGK_DESCRIBEALLOCATIONFLAGS {
  union {
    struct {
      UINT CheckDisplayMode  :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  };
} DXGK_DESCRIBEALLOCATIONFLAGS;
````


## -struct-fields
<dl>

### -field <b>CheckDisplayMode</b>

<dd>
<p>[in] This member is reserved.</p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>[in] This member is reserved and should be set to zero. </p>
<p>Setting this member to zero is equivalent to setting the remaining 31 bits (0xFFFFFFFE) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>[in] A member in the union that <b>DXGK_DESCRIBEALLOCATIONFLAGS</b> contains that can hold a 32-bit value that identifies the type of allocation.</p>
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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-describeallocation.md">DXGKARG_DESCRIBEALLOCATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_DESCRIBEALLOCATIONFLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
