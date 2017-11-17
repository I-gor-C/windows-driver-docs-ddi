---
UID: NS.d3d12umddi.D3D12DDICB_ALLOCATE_0022
title: D3D12DDICB_ALLOCATE_0022
author: windows-driver-content
description: Specifies information for use in an allocation callback function.
old-location: display\d3d12ddicb_allocate_0022.htm
ms.assetid: C39262BA-D1CE-4634-974A-ACCE8D321830
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDICB_ALLOCATE_0022
req.alt-loc: D3d12umddi.h
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
ms.keywords: D3D12DDICB_ALLOCATE_0022, D3D12DDICB_ALLOCATE_0022
req.iface: 
---

# D3D12DDICB_ALLOCATE_0022 structure



## -description
<p>Specifies information for use in an allocation callback function. </p>


## -syntax

````
typedef struct D3D12DDICB_ALLOCATE_0022 {
  const VOID                    *pPrivateDriverData;
  UINT                          PrivateDriverDataSize;
  HANDLE                        hResource;
  D3DKMT_HANDLE                 hKMResource;
  UINT                          NumAllocations;
  D3D12DDI_ALLOCATION_INFO_0022 *pAllocationInfo;
} D3D12DDICB_ALLOCATE_0022;
````


## -struct-fields
<dl>

### -field <b>pPrivateDriverData</b>

<dd>
<p>A pointer to a buffer that contains optional private driver data.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>Size of the private driver data.</p>
</dd>

### -field <b>hResource</b>

<dd>
<p>The handle of a resource. </p>
</dd>

### -field <b>hKMResource</b>

<dd>
<p>A handle of a kernel resource. </p>
</dd>

### -field <b>NumAllocations</b>

<dd>
<p>The number of allocations.</p>
</dd>

### -field <b>pAllocationInfo</b>

<dd>
<p>Allocation as a <a href="https://msdn.microsoft.com/A600C402-EB77-4C44-8349-96DAF11B807C">D3D12DDI_ALLOCATION_INFO_0022</a> structure. </p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/A600C402-EB77-4C44-8349-96DAF11B807C">D3D12DDI_ALLOCATION_INFO_0022</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D12DDICB_ALLOCATE_0022 structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
