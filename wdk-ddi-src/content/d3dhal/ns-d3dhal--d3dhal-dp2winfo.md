---
UID: NS.d3dhal._D3DHAL_DP2WINFO
title: D3DHAL_DP2WINFO
author: windows-driver-content
description: The D3DHAL_DP2WINFO structure is used to inform the driver of the w-range to be used for w-buffering.
old-location: display\d3dhal_dp2winfo.htm
old-project: display
ms.assetid: da4cdaff-4418-4b88-bf47-5a1567e940e1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2WINFO, D3DHAL_DP2WINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DHAL_DP2WINFO
req.alt-loc: d3dhal.h
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

# D3DHAL_DP2WINFO structure



## -description
<p>The D3DHAL_DP2WINFO structure is used to inform the driver of the w-range to be used for w-buffering.</p>


## -syntax

````
typedef struct _D3DHAL_DP2WINFO {
  D3DVALUE dvWNear;
  D3DVALUE dvWFar;
} D3DHAL_DP2WINFO, *LPD3DHAL_DP2WINFO;
````


## -struct-fields
<dl>

### -field <b>dvWNear</b>

<dd></dd>

### -field <b>dvWFar</b>

<dd>
<p>Specify the near and far limit of the w-buffer, respectively. These members can be any valid floating-point values.</p>
</dd>
</dl>

## -remarks
<p>The <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> callback parses a D3DHAL_DP2WINFO structure from the command buffer and updates the driver's scaling parameters for w-buffering when <a href="..\d3dhal\ns-d3dhal--d3dhal-dp2command.md">D3DHAL_DP2COMMAND</a> is set to D3DDP2OP_WINFO.</p>

<p>One D3DHAL_DP2WINFO structure follows the D3DHAL_DP2COMMAND structure in the command buffer.</p>

<p>The driver should update the w-buffer portion of its internal rendering context with the w-ranges specified in this structure. The driver can use this information to scale the w-buffer.</p>

<p>Video adapters that do not support this feature should ignore and skip over these instructions and continue processing the rest of the command buffer.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>D3DDP2OP_WINFO</dt>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-dp2command.md">D3DHAL_DP2COMMAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2WINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
