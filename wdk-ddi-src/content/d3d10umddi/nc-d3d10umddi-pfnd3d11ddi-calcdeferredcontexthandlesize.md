---
UID: NC.d3d10umddi.PFND3D11DDI_CALCDEFERREDCONTEXTHANDLESIZE
title: PFND3D11DDI_CALCDEFERREDCONTEXTHANDLESIZE
author: windows-driver-content
description: The CalcDeferredContextHandleSize function queries for the amount of storage space that the driver requires to satisfy deferred context handles to the given immediate context object.
old-location: display\calcdeferredcontexthandlesize.htm
old-project: display
ms.assetid: d26c26ef-be8e-434a-b3d3-623ed539c541
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CalcDeferredContextHandleSize is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CalcDeferredContextHandleSize
req.alt-loc: d3d10umddi.h
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

# PFND3D11DDI_CALCDEFERREDCONTEXTHANDLESIZE callback



## -description
<p>The <b>CalcDeferredContextHandleSize</b> function queries for the amount of storage space that the driver requires to satisfy deferred context handles to the given immediate context object. </p>


## -prototype

````
PFND3D11DDI_CALCDEFERREDCONTEXTHANDLESIZE CalcDeferredContextHandleSize;

SIZE_T APIENTRY CalcDeferredContextHandleSize(
  _In_ D3D10DDI_HDEVICE    hDevice,
  _In_ D3D11DDI_HANDLETYPE HandleType,
  _In_ VOID                *pICObject
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>HandleType</i> [in]

<dd>
<p> A <a href="https://msdn.microsoft.com/library/windows/hardware/ff542152">D3D11DDI_HANDLETYPE</a>-typed value that indicates the type of deferred context handle to determine the size of the memory region for. </p>
</dd>

### -param <i>pICObject</i> [in]

<dd>
<p> A pointer to the object for the immediate context.</p>
</dd>
</dl>

## -returns
<p><b>CalcDeferredContextHandleSize</b> returns the size of the storage space that the driver requires for the deferred context handles to the object that <b>pICObject</b> points to.</p>

## -remarks
<p>The driver is only required to implement <b>CalcDeferredContextHandleSize</b> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability that can be returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure from a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a> function.</p>

<p>The Direct3D runtime does not call the <b>CalcDeferredContextHandleSize</b> function from function tables for the deferred context. The runtime calls <b>CalcDeferredContextHandleSize</b> from the function table for the immediate context.</p>

<p>For more information about how <b>CalcDeferredContextHandleSize</b> is used, see <a href="https://msdn.microsoft.com/1b3e5c29-9b9e-4c10-8fe0-706255c8fd91">Using Context-Local DDI Handles</a>. </p>

<p>The driver is only required to implement <b>CalcDeferredContextHandleSize</b> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability that can be returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure from a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a> function.</p>

<p>The Direct3D runtime does not call the <b>CalcDeferredContextHandleSize</b> function from function tables for the deferred context. The runtime calls <b>CalcDeferredContextHandleSize</b> from the function table for the immediate context.</p>

<p>For more information about how <b>CalcDeferredContextHandleSize</b> is used, see <a href="https://msdn.microsoft.com/1b3e5c29-9b9e-4c10-8fe0-706255c8fd91">Using Context-Local DDI Handles</a>. </p>

## -requirements
<table>
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
<p>Version</p>
</th>
<td width="70%">
<p>CalcDeferredContextHandleSize is supported beginning with the Windows 7 operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542152">D3D11DDI_HANDLETYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_CALCDEFERREDCONTEXTHANDLESIZE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
