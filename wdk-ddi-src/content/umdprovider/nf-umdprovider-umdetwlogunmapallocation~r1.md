---
UID: NF.umdprovider.UMDEtwLogUnmapAllocation~r1
title: UMDEtwLogUnmapAllocation
author: windows-driver-content
description: Indicates that a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) memory allocation, or a portion of the allocation, is no longer being used. Call this function whether or not the allocation is being destroyed.
old-location: display\umdetwlogunmapallocation.htm
old-project: display
ms.assetid: 36c204fb-638d-44d2-8379-a5bd79e4167a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: UMDEtwLogUnmapAllocation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: umdprovider.h
req.include-header: Umdprovider.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UMDEtwLogUnmapAllocation
req.alt-loc: umdprovider.h
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
req.product: Windows 10 or later.
---

# UMDEtwLogUnmapAllocation function



## -description
<p>Indicates that a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) memory allocation, or a portion of the allocation, is no longer being used. Call this function whether or not the allocation is being destroyed.</p>


## -syntax

````
void UMDEtwLogUnmapAllocation(
   ULONGLONG                  hD3DAllocation,
   ULONGLONG                  hDxgAllocation,
   ULONGLONG                  Offset,
   ULONGLONG                  Size,
   UMDETW_ALLOCATION_USAGE    Usage,
   UMDETW_ALLOCATION_SEMANTIC Semantic
);
````


## -parameters
<dl>

### -param hD3DAllocation 

<dd>
<p>A handle to the Direct3D allocation.</p>
<p> For Direct3D 10 user-mode drivers, the handle will be the value of the <i>hResource</i> parameter of the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a> function. For Direct3D 9 user-mode drivers, the handle will be the value of the <i>pResource</i> parameter that the driver returns in the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a> function.</p>
<p>The driver can set this value to <b>NULL</b> if it uses allocations internally.</p>
</dd>

### -param hDxgAllocation 

<dd>
<p>A handle to the DirectX graphics kernel subsystem (Dxgkrnl.sys) allocation that the Direct3D allocation is mapped to.</p>
</dd>

### -param Offset 

<dd>
<p>The starting address, in bytes, of the Direct3D allocation within the Dxgkrnl allocation.</p>
</dd>

### -param Size 

<dd>
<p>The size, in bytes, of the Direct3D allocation within the Dxgkrnl allocation.</p>
</dd>

### -param Usage 

<dd>
<p>A <a href="..\umdprovider\ns-umdprovider--umdetw-allocation-usage.md">UMDETW_ALLOCATION_USAGE</a> structure that indicates the reason for this mapping.</p>
</dd>

### -param Semantic 

<dd>
<p>If the allocation is used internally by the user-mode driver, this is a <a href="..\umdprovider\ne-umdprovider--umdetw-allocation-semantic.md">UMDETW_ALLOCATION_SEMANTIC</a> structure that indicates what the allocation is used for.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>When called, this function logs an event that describes which API resource the allocation is, or was, being used for. If no API resource was associated with the allocation, the function logs an event that describes the purpose that the driver indicated for this allocation.</p>

<p>The user-mode display driver must completely account for the video memory it allocates, so it must call this function to log an event every time the allocation changes.</p>

<p>The driver should pass the same parameters values to <b>UMDEtwLogUnmapAllocation</b> as it did to <a href="..\umdprovider\nf-umdprovider-umdetwlogmapallocation.md">UMDEtwLogMapAllocation</a>.</p>

<p><b>UMDEtwLogUnmapAllocation</b> is defined inline in Umdprovider.h as:</p>

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Umdprovider.h (include Umdprovider.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a>
</dt>
<dt>
<a href="..\umdprovider\ne-umdprovider--umdetw-allocation-semantic.md">UMDETW_ALLOCATION_SEMANTIC</a>
</dt>
<dt>
<a href="..\umdprovider\ns-umdprovider--umdetw-allocation-usage.md">UMDETW_ALLOCATION_USAGE</a>
</dt>
<dt>
<a href="..\umdprovider\nf-umdprovider-umdetwlogmapallocation.md">UMDEtwLogMapAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20UMDEtwLogUnmapAllocation function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
