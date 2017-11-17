---
UID: NS.d3dkmthk._D3DKMT_UNLOCK
title: D3DKMT_UNLOCK
author: windows-driver-content
description: The D3DKMT_UNLOCK structure describes allocations to unlock.
old-location: display\d3dkmt_unlock.htm
ms.assetid: 397d2ab0-89a0-42a8-a665-ca7e1ed5d8f3
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_UNLOCK
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
ms.keywords: D3DKMT_UNLOCK, D3DKMT_UNLOCK
req.iface: 
---

# D3DKMT_UNLOCK structure



## -description
<p>The D3DKMT_UNLOCK structure describes allocations to unlock. </p>


## -syntax

````
typedef struct _D3DKMT_UNLOCK {
  D3DKMT_HANDLE       hDevice;
  UINT                NumAllocations;
  const D3DKMT_HANDLE *phAllocations;
} D3DKMT_UNLOCK;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the device that the allocation is associated with.</p>
</dd>

### -field <b>NumAllocations</b>

<dd>
<p>[in] The number of allocations in the array that <b>phAllocations</b> specifies. </p>
</dd>

### -field <b>phAllocations</b>

<dd>
<p>[in] An array of D3DKMT_HANDLE data types that represent kernel-mode handles to the allocations to unlock.</p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547233">D3DKMTUnlock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_UNLOCK structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
