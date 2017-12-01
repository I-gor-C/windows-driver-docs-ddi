---
UID: NC.d3dumddi.PFND3DDDI_CREATEEXTENSIONDEVICE
title: PFND3DDDI_CREATEEXTENSIONDEVICE
author: windows-driver-content
description: The CreateExtensionDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) extension device.
old-location: display\createextensiondevice.htm
old-project: display
ms.assetid: 7e6dbb70-2e74-4ddb-a504-2c8145af99d9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CreateExtensionDevice
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

# PFND3DDDI_CREATEEXTENSIONDEVICE callback



## -description
<p>The <b>CreateExtensionDevice</b> function creates a Microsoft DirectX Video Acceleration (DirectX VA) extension device. </p>


## -prototype

````
PFND3DDDI_CREATEEXTENSIONDEVICE CreateExtensionDevice;

__checkReturn HRESULT APIENTRY CreateExtensionDevice(
  _In_    HANDLE                          hDevice,
  _Inout_ D3DDDIARG_CREATEEXTENSIONDEVICE *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in, out]

<dd>
<p> A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-createextensiondevice.md">D3DDDIARG_CREATEEXTENSIONDEVICE</a> structure. On input, this structure contains information that the driver can use. On output, the driver specifies information in the structure that the Microsoft Direct3D runtime can use.</p>
</dd>
</dl>

## -returns
<p><b>CreateExtensionDevice</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The extension device is successfully created.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createextensiondevice.md">CreateExtensionDevice</a> could not allocate the required memory for it to complete.</p>

<p> </p>

## -remarks


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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-createextensiondevice.md">D3DDDIARG_CREATEEXTENSIONDEVICE</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroyextensiondevice.md">DestroyExtensionDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_CREATEEXTENSIONDEVICE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
