---
UID: NS.d3dumddi._D3DDDICB_SETDISPLAYMODE
title: D3DDDICB_SETDISPLAYMODE
author: windows-driver-content
description: The D3DDDICB_SETDISPLAYMODE structure describes the primary allocation that is used to scan out to the display.
old-location: display\d3dddicb_setdisplaymode.htm
old-project: display
ms.assetid: d2f6d53b-2dd7-46ed-8d1e-dea264da4046
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_SETDISPLAYMODE, D3DDDICB_SETDISPLAYMODE
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
req.alt-api: D3DDDICB_SETDISPLAYMODE
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

# D3DDDICB_SETDISPLAYMODE structure



## -description
<p>The D3DDDICB_SETDISPLAYMODE structure describes the primary allocation that is used to scan out to the display. </p>


## -syntax

````
typedef struct _D3DDDICB_SETDISPLAYMODE {
  D3DKMT_HANDLE hPrimaryAllocation;
  UINT          PrivateDriverFormatAttribute;
} D3DDDICB_SETDISPLAYMODE;
````


## -struct-fields
<dl>

### -field <b>hPrimaryAllocation</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents the kernel-mode handle to the primary allocation for scanning out. The Microsoft Direct3D runtime's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-allocatecb.md">pfnAllocateCb</a> function returns this handle. </p>
</dd>

### -field <b>PrivateDriverFormatAttribute</b>

<dd>
<p>[out] A private format attribute that the user-mode display driver should use to convert the current primary surface if the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdisplaymodecb.md">pfnSetDisplayModeCb</a> callback function returned D3DDDIERR_INCOMPATIBLEPRIVATEFORMAT. </p>
</dd>
</dl>

## -remarks
<p>The user-mode display driver can set the <b>hPrimaryAllocation</b> member in the call to <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdisplaymodecb.md">pfnSetDisplayModeCb</a> to scan out any allocation. However, the allocation must be marked as a primary (that is, the user-mode display driver must have set the <b>Primary</b> bit-field flag in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544364">D3DDDI_ALLOCATIONINFO</a> structure in a call to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-allocatecb.md">pfnAllocateCb</a> function to create the allocation).</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544364">D3DDDI_ALLOCATIONINFO</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-allocatecb.md">pfnAllocateCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdisplaymodecb.md">pfnSetDisplayModeCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_SETDISPLAYMODE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
