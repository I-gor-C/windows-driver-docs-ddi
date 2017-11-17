---
UID: NS.d3d10umddi.D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW
title: D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW
author: windows-driver-content
description: Describes the video processor's output view.
old-location: display\d3d11_1ddiarg_createvideoprocessoroutputview.htm
ms.assetid: 3545AE6F-3D9E-4C3B-8C22-B823A18CC700
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW
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
ms.keywords: D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW, D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW
req.iface: 
---

# D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW structure



## -description
<p>Describes the video processor's output view.</p>


## -syntax

````
typedef struct _D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW {
  D3D10DDI_HRESOURCE             hDrvResource;
  D3D11_1DDI_HVIDEOPROCESSORENUM hDrvVideoProcessorEnum;
  UINT                           MipSlice;
  UINT                           FirstArraySlice;
  UINT                           ArraySize;
} D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW, *PD3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW;
````


## -struct-fields
<dl>

### -field <b>hDrvResource</b>

<dd>
<p>A handle to the video decoder output resource.</p>
</dd>

### -field <b>hDrvVideoProcessorEnum</b>

<dd>
<p>A handle to the video processor enumeration.</p>
</dd>

### -field <b>MipSlice</b>

<dd>
<p>The identifier of the MIP-map slice.</p>
</dd>

### -field <b>FirstArraySlice</b>

<dd>
<p>The identifier of the first array slice.</p>
</dd>

### -field <b>ArraySize</b>

<dd>
<p>The number of array slices for the texture.</p>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406318">D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
