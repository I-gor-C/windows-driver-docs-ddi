---
UID: NS.d3dumddi._D3DDDICB_QUERYRESIDENCY
title: D3DDDICB_QUERYRESIDENCY
author: windows-driver-content
description: The D3DDDICB_QUERYRESIDENCY structure describes the residency status of a resource or list of allocations.
old-location: display\d3dddicb_queryresidency.htm
old-project: display
ms.assetid: 43dafaea-06cd-49bb-99ab-99708b1a93cb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_QUERYRESIDENCY, D3DDDICB_QUERYRESIDENCY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_QUERYRESIDENCY
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

# D3DDDICB_QUERYRESIDENCY structure



## -description
<p>The D3DDDICB_QUERYRESIDENCY structure describes the residency status of a resource or list of allocations. </p>


## -syntax

````
typedef struct _D3DDDICB_QUERYRESIDENCY {
  HANDLE                 hResource;
  UINT                   NumAllocations;
  const D3DKMT_HANDLE    *HandleList;
  D3DDDI_RESIDENCYSTATUS *pResidencyStatus;
} D3DDDICB_QUERYRESIDENCY;
````


## -struct-fields
<dl>

### -field hResource

<dd>
<p>[in] A handle to a resource whose residency is queried. If the user-mode display driver uses the array in the <b>HandleList</b> member to query for residency, it sets <b>hResource</b> to <b>NULL</b>.</p>
<p>If <b>hResource</b> is non-<b>NULL</b>, all allocations that belong to the resource are queried, and the result is returned in the first element of the array that <b>pResidencyStatus</b> points to. The residency status of a resource is equal to the lowest residency status of all allocations that belong to the resource.</p>
</dd>

### -field NumAllocations

<dd>
<p>[in] The number of allocations in the <b>HandleList</b> array. If the user-mode display driver sets the handle in the <b>hResource</b> member to non-<b>NULL</b>, it must set <b>NumAllocations</b> to zero.</p>
</dd>

### -field HandleList

<dd>
<p>[in] An array of D3DKMT_HANDLE data types that represent kernel-mode handles to the allocations. The Microsoft Direct3D runtime's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-allocatecb.md">pfnAllocateCb</a> function returns these handles. Therefore, the user-mode display driver uses these handles to query for residency.</p>
<p>If the user-mode display driver sets the handle in the <b>hResource</b> member to non-<b>NULL</b>, it must set <b>HandleList</b> to <b>NULL</b>. </p>
</dd>

### -field pResidencyStatus

<dd>
<p>[out] A pointer to an array of D3DDDI_RESIDENCYSTATUS values. If the <b>hResource</b> member is non-<b>NULL</b>, the array contains a single element and receives one of the following value to indicate the residency status of the resource. If <b>hResource</b> is <b>NULL</b>, the number of elements in the array is specified by the <b>NumAllocations</b> member, and each element receives one of the following values to indicate the residency status of the corresponding allocation in the array that is specified by <b>HandleList</b>. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DDDI_RESIDENCYSTATUS_RESIDENTINGPUMEMORY (1)</p>
</td>
<td>
<p>The resource or list of allocations reside in GPU memory, which is the highest residency status.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDI_RESIDENCYSTATUS_RESIDENTINSHAREDMEMORY (2)</p>
</td>
<td>
<p>The resource or list of allocations reside in shared memory.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDI_RESIDENCYSTATUS_NOTRESIDENT (3)</p>
</td>
<td>
<p>The resource or list of allocations is nonresident, which is the lowest residency status.</p>
</td>
</tr>
</table>
<p> </p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryresidencycb.md">pfnQueryResidencyCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_QUERYRESIDENCY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
