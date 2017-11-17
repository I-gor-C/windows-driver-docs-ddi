---
UID: NS.d3dkmddi._DXGKARG_CLOSEALLOCATION
title: DXGKARG_CLOSEALLOCATION
author: windows-driver-content
description: The DXGKARG_CLOSEALLOCATION structure describes allocations that the display miniport driver should close.
old-location: display\dxgkarg_closeallocation.htm
ms.assetid: ccd65750-b4d0-4955-9fd4-9546709c2390
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_CLOSEALLOCATION
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
ms.keywords: DXGKARG_CLOSEALLOCATION, DXGKARG_CLOSEALLOCATION
req.iface: 
---

# DXGKARG_CLOSEALLOCATION structure



## -description
<p>The DXGKARG_CLOSEALLOCATION structure describes allocations that the display miniport driver should close.</p>


## -syntax

````
typedef struct _DXGKARG_CLOSEALLOCATION {
  UINT         NumAllocations;
  const HANDLE *pOpenHandleList;
} DXGKARG_CLOSEALLOCATION;
````


## -struct-fields
<dl>

### -field <b>NumAllocations</b>

<dd>
<p>[in] The number of elements in the array that <b>pOpenHandleList</b> specifies.</p>
</dd>

### -field <b>pOpenHandleList</b>

<dd>
<p>[in] An array of handles to device-specific allocations to close.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/f9c195d7-debe-495e-a355-e176d06884f8">DxgkDdiCloseAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_CLOSEALLOCATION structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
