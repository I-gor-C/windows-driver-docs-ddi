---
UID: NS.d3d10umddi.D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW
title: D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW
author: windows-driver-content
description: Describes the video processor's input view.
old-location: display\d3d11_1ddiarg_createvideoprocessorinputview.htm
old-project: display
ms.assetid: 73F8F146-A38B-4890-867D-862361455AD4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW, D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW
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

# D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW structure



## -description
<p>Describes the video processor's input view.</p>


## -syntax

````
typedef struct _D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW {
  D3D10DDI_HRESOURCE             hDrvResource;
  D3D11_1DDI_HVIDEOPROCESSORENUM hDrvVideoProcessorEnum;
  UINT                           FourCC;
  UINT                           MipSlice;
  UINT                           FirstArraySlice;
  UINT                           ArraySize;
} D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW, *PD3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW;
````


## -struct-fields
<dl>

### -field <b>hDrvResource</b>

<dd>
<p>A handle to the video decoder input resource.</p>
</dd>

### -field <b>hDrvVideoProcessorEnum</b>

<dd>
<p>A handle to the video processor enumeration.</p>
</dd>

### -field <b>FourCC</b>

<dd>
<p>A FOURCC code that the application uses to override the surface format. A value of zero indicates that the application will not override the resource format.</p>
<p>For example, if a new video standard emerges that requires a new substream format, the application can create an equivelant surface using a standard format and then specify a FOURCC code when it creates a view to indicate that the data is laid out according to the new video standard.</p>
<p>For more information about FOURCC codes, see <a href="http://go.microsoft.com/fwlink/p/?linkid=231686">Video FOURCCs</a>.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406320">D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
