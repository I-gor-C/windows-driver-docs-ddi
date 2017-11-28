---
UID: NS.d3dumddi._D3DDDICB_DEALLOCATE2
title: D3DDDICB_DEALLOCATE2
author: windows-driver-content
description: The D3DDDICB_DEALLOCATE2 structure describes parameters for releasing allocations with pfnDeallocate2Cb.
old-location: display\d3dddicb_deallocate2.htm
old-project: display
ms.assetid: C859CB06-3F71-4F6D-9949-0E9AE75CEC20
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_DEALLOCATE2, D3DDDICB_DEALLOCATE2
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
req.alt-api: D3DDDICB_DEALLOCATE2
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

# D3DDDICB_DEALLOCATE2 structure



## -description
<p>The <b>D3DDDICB_DEALLOCATE2</b> structure describes parameters for releasing allocations with <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-deallocate2cb.md">pfnDeallocate2Cb</a>
</p>


## -syntax

````
typedef struct _D3DDDICB_DEALLOCATE2 {
  HANDLE                           hResource;
  UINT                             NumAllocations;
  const D3DKMT_HANDLE              *HandleList;
  D3DDDICB_DESTROYALLOCATION2FLAGS Flags;
} D3DDDICB_DEALLOCATE2;
````


## -struct-fields
<dl>

### -field <b>hResource</b>

<dd>
<p>[in] A handle to a resource whose associated allocations must be released. If the user-mode display driver uses the array that is specified by <b>HandleList</b> to specify the allocations to release, it sets <b>hResource</b> to <b>NULL</b>.</p>
</dd>

### -field <b>NumAllocations</b>

<dd>
<p>[in] The number of allocations in the <b>HandleList</b> array. If the user-mode display driver sets the handle in the <b>hResource</b> member to non-<b>NULL</b>, <b>NumAllocations</b> is ignored by the Direct3D runtime.</p>
</dd>

### -field <b>HandleList</b>

<dd>
<p>[in] An array of <b>D3DKMT_HANDLE</b> data types that represent kernel-mode handles to the allocations. The Direct3D runtime's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-allocatecb.md">pfnAllocateCb</a> function returns these handles. Therefore, the user-mode display driver uses these handles to release the allocations.</p>
<p>If the user-mode display driver sets the handle in the <b>hResource</b> member to non-<b>NULL</b>, <b>HandleList</b> is ignored by the Direct3D runtime. </p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-deallocate2cb.md">pfnDeallocate2Cb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906318">D3DDDICB_DESTROYALLOCATION2FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_DEALLOCATE2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
