---
UID: NS.d3dumddi._D3DDDICB_RECLAIMALLOCATIONS
title: D3DDDICB_RECLAIMALLOCATIONS
author: windows-driver-content
description: Describes video memory resources that are to be reclaimed and that the user-mode display driver previously offered for reuse. Used with the pfnReclaimAllocationsCb function.
old-location: display\d3dddicb_reclaimallocations.htm
ms.assetid: 61c8fdbf-b003-4caa-af13-ba6f1e22400c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_RECLAIMALLOCATIONS
req.alt-loc: D3dumddi.h
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
ms.keywords: D3DDDICB_RECLAIMALLOCATIONS, D3DDDICB_RECLAIMALLOCATIONS
req.iface: 
---

# D3DDDICB_RECLAIMALLOCATIONS structure



## -description
<p>Describes video memory resources that are to be reclaimed and that the user-mode display driver  previously offered  for reuse. Used with the  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451695">pfnReclaimAllocationsCb</a> function.</p>


## -syntax

````
typedef struct _D3DDDICB_RECLAIMALLOCATIONS {
  const HANDLE        *pResources;
  const D3DKMT_HANDLE *HandleList;
  BOOL                *pDiscarded;
  UINT                NumAllocations;
} D3DDDICB_RECLAIMALLOCATIONS;
````


## -struct-fields
<dl>

### -field <b>pResources</b>

<dd>
<p>[in] A pointer to an array of handles to the resources that are to be reclaimed.</p>
<p>If <b>pResources</b> is not <b>NULL</b>, the <b>HandleList</b> member must be <b>NULL</b>.</p>
<div class="alert"><b>Note</b>  If resources were created with the <b>D3D10_DDI_BIND_PRESENT</b> flag value set in <i>pCreateResource</i>-&gt;<b>BindFlags</b>, the driver must not use the <b>pResources</b> member to reclaim by resource handles. Instead, the driver must reclaim the resources by using allocation handles specified by <b>HandleList</b>.</div>
<div> </div>
</dd>

### -field <b>HandleList</b>

<dd>
<p>[in] An array of D3DKMT_HANDLE data types that represent kernel-mode handles to the allocations that are to be reclaimed.</p>
<p>If <b>HandleList</b> is not <b>NULL</b>, the <b>pResources</b> member must be <b>NULL</b>.</p>
</dd>

### -field <b>pDiscarded</b>

<dd>
<p>[out] An  array of Boolean values that specify whether each resource or allocation was discarded.</p>
<p>Each Boolean value in this array corresponds to a resource at the same index location in the arrays pointed to by <b>pResources</b> or   <b>HandleList.</b></p>
<p>The DirectX graphics kernel subsystem sets each Boolean value to <b>TRUE</b> if the correponding resource was discarded, or to <b>FALSE</b> if not.</p>
<p>The value of <b>pDiscarded</b> can be <b>NULL</b>. If the driver sets it to <b>NULL</b>, the content of the resource or allocation can be assumed to be lost. If the driver does not need the content of the resource or allocation, setting <b>pDiscarded</b> to <b>NULL</b> might improve performance.</p>
</dd>

### -field <b>NumAllocations</b>

<dd>
<p>[in] The number of items in the <b>pResources</b>, <b>HandleList</b>, or  <b>pDiscarded</b> members, whichever is not <b>NULL</b>.</p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/2dff9d2e-c497-422f-824b-a7101904fd67">CreateResource(D3D11)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541697">D3D10DDIARG_CREATERESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451695">pfnReclaimAllocationsCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_RECLAIMALLOCATIONS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
