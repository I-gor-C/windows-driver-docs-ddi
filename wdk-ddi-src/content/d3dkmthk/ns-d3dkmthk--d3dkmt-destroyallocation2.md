---
UID: NS.d3dkmthk._D3DKMT_DESTROYALLOCATION2
title: D3DKMT_DESTROYALLOCATION2
author: windows-driver-content
description: The D3DKMT_DESTROYALLOCATION2 structure describes parameters for releasing allocations with D3DKMTDestroyAllocation2.
old-location: display\d3dkmt_destroyallocation2.htm
old-project: display
ms.assetid: A51C5F98-5979-436A-9E7E-EA54A1469940
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_DESTROYALLOCATION2, D3DKMT_DESTROYALLOCATION2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_DESTROYALLOCATION2
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

# D3DKMT_DESTROYALLOCATION2 structure



## -description
<p>The <b>D3DKMT_DESTROYALLOCATION2</b> structure describes parameters for releasing allocations with <a href="https://msdn.microsoft.com/library/windows/hardware/dn906772">D3DKMTDestroyAllocation2</a>.</p>


## -syntax

````
typedef struct _D3DKMT_DESTROYALLOCATION2 {
  D3DKMT_HANDLE                    hDevice;
  D3DKMT_HANDLE                    hResource;
  const D3DKMT_HANDLE              *phAllocationList;
  UINT                             AllocationCount;
  D3DDDICB_DESTROYALLOCATION2FLAGS Flags;
} D3DKMT_DESTROYALLOCATION2;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A <b>D3DKMT_HANDLE</b> data type that represents a kernel-mode handle to the device that the resource, allocations, or both are associated with.</p>
</dd>

### -field <b>hResource</b>

<dd>
<p>[in] A <b>D3DKMT_HANDLE</b> data type that represents a kernel-mode handle to the resource that is associated with the allocations when releasing a resource. If a resource handle is specified, all of the allocations that are associated with it are automatically released.</p>
</dd>

### -field <b>phAllocationList</b>

<dd>
<p>[in] An array of <b>D3DKMT_HANDLE</b> data types that represent kernel-mode handles to the allocations. If any allocation in the list is associated with a resource, all of the allocations in the list must also be associated with the same resource. If the OpenGL installable client driver sets the handle in the <b>hResource</b> member to a non-<b>NULL</b> value, the installable client driver must set <b>phAllocationList</b> to <b>NULL</b>.</p>
</dd>

### -field <b>AllocationCount</b>

<dd>
<p>[in] The number of allocations in the array that <b>phAllocationList</b> specifies. If the OpenGL installable client driver sets the handle in the <b>hResource</b> member to a non-<b>NULL</b> value, the <b>AllocationCount</b> member is ignored by the OpenGL runtime.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/dn906318">D3DDDICB_DESTROYALLOCATION2FLAGS</a> structure that contains additional details about the operation.</p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906772">D3DKMTDestroyAllocation2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906318">D3DDDICB_DESTROYALLOCATION2FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_DESTROYALLOCATION2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
