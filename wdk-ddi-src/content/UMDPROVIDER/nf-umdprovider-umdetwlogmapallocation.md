---
UID: NF.umdprovider.UMDEtwLogMapAllocation
title: UMDEtwLogMapAllocation
author: windows-driver-content
description: Describes how a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) memory allocation, or a portion of the allocation, is being used.
old-location: display\umdetwlogmapallocation.htm
ms.assetid: 60456f6a-3de7-46ae-b486-f53041ce1508
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: umdprovider.h
req.include-header: Umdprovider.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UMDEtwLogMapAllocation
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
ms.keywords: UMDEtwLogMapAllocation
req.iface: 
req.product: Windows 10 or later.
---

# UMDEtwLogMapAllocation function



## -description
<p>Describes how a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) memory allocation, or a portion of the allocation, is being used.</p>


## -syntax

````
void UMDEtwLogMapAllocation(
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

### -param <i>hD3DAllocation</i> 

<dd>
<p>A handle to the Direct3D allocation.</p>
<p> For Direct3D 10 user-mode drivers, the handle will be the value of the <i>hResource</i> parameter of the <a href="https://msdn.microsoft.com/c21839f0-8302-49f9-a2b4-4009fbd2d88c">CreateResource(D3D10)</a> function. For Direct3D 9 user-mode drivers, the handle will be the value of the <i>pResource</i> parameter that the driver returns in the <a href="https://msdn.microsoft.com/5b74c989-1a62-4415-a19a-dd0ba2fcff83">CreateResource</a> function.</p>
<p>The driver can set this value to <b>NULL</b> if it uses allocations internally.</p>
</dd>

### -param <i>hDxgAllocation</i> 

<dd>
<p>A handle to the DirectX graphics kernel subsystem (Dxgkrnl.sys) allocation that the Direct3D allocation is mapped to.</p>
</dd>

### -param <i>Offset</i> 

<dd>
<p>The starting address, in bytes, of the Direct3D allocation within the Dxgkrnl allocation.</p>
</dd>

### -param <i>Size</i> 

<dd>
<p>The size, in bytes, of the Direct3D allocation within the Dxgkrnl allocation.</p>
</dd>

### -param <i>Usage</i> 

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/jj542442">UMDETW_ALLOCATION_USAGE</a> structure that indicates the reason for this mapping.</p>
</dd>

### -param <i>Semantic</i> 

<dd>
<p>If the allocation is used internally by the user-mode driver, this is a <a href="https://msdn.microsoft.com/library/windows/hardware/jj542441">UMDETW_ALLOCATION_SEMANTIC</a> structure that indicates what the allocation is used for.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>The user-mode display driver must completely account for the video memory it allocates, so it must call this function to log an event every time the allocation changes.</p>

<p>Examples of when to call this function are:</p>

<p><b>UMDEtwLogMapAllocation</b> is defined inline in Umdprovider.h as:</p>

<p>The user-mode display driver must completely account for the video memory it allocates, so it must call this function to log an event every time the allocation changes.</p>

<p>Examples of when to call this function are:</p>

<p><b>UMDEtwLogMapAllocation</b> is defined inline in Umdprovider.h as:</p>

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
<a href="https://msdn.microsoft.com/5b74c989-1a62-4415-a19a-dd0ba2fcff83">CreateResource</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c21839f0-8302-49f9-a2b4-4009fbd2d88c">CreateResource(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj542441">UMDETW_ALLOCATION_SEMANTIC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj542442">UMDETW_ALLOCATION_USAGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20UMDEtwLogMapAllocation function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
