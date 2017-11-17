---
UID: NS.d3dumddi._D3DDDICB_LOCK2
title: D3DDDICB_LOCK2
author: windows-driver-content
description: D3DDDICB_LOCK2 describes parameters for locking an allocation.
old-location: display\d3dddicb_lock2.htm
ms.assetid: 71E2E98D-4C97-4C04-A379-88C2A7CC8428
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_LOCK2
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
ms.keywords: D3DDDICB_LOCK2, D3DDDICB_LOCK2
req.iface: 
---

# D3DDDICB_LOCK2 structure



## -description
<p><b>D3DDDICB_LOCK2</b> describes parameters for locking an allocation.</p>


## -syntax

````
typedef struct _D3DDDICB_LOCK2 {
  D3DKMT_HANDLE       hAllocation;
  D3DDDICB_LOCK2FLAGS Flags;
  PVOID               pData;
} D3DDDICB_LOCK2;
````


## -struct-fields
<dl>

### -field <b>hAllocation</b>

<dd>
<p>[in] A driver specified <b>D3DKMT_HANDLE</b> to the allocation to lock.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A set of flags to pass to the <a href="https://msdn.microsoft.com/033FF321-2617-4AAF-8445-10800411F0B5">Lock2</a> kernel function which will determine how the allocation is locked. See <a href="https://msdn.microsoft.com/library/windows/hardware/dn894602">D3DDDICB_LOCK2FLAGS</a> for details.</p>
</dd>

### -field <b>pData</b>

<dd>
<p>[out] A CPU virtual address pointing a valid memory location pointing to the CPU backing store or the GPU frame buffer.</p>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/033FF321-2617-4AAF-8445-10800411F0B5">Lock2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894602">D3DDDICB_LOCK2FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_LOCK2 structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
