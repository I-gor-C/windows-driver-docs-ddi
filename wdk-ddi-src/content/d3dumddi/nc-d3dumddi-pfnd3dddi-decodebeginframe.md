---
UID: NC.d3dumddi.PFND3DDDI_DECODEBEGINFRAME
title: PFND3DDDI_DECODEBEGINFRAME
author: windows-driver-content
description: The DecodeBeginFrame function notifies the user-mode display driver that decoding can begin on the specified Microsoft DirectX Video Accelerator (VA) decode device.
old-location: display\decodebeginframe.htm
old-project: display
ms.assetid: 3e6153aa-7b21-429d-8908-1ff3a4d25e17
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
req.alt-api: DecodeBeginFrame
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

# PFND3DDDI_DECODEBEGINFRAME callback



## -description
<p>The <b>DecodeBeginFrame</b> function notifies the user-mode display driver that decoding can begin on the specified Microsoft DirectX Video Accelerator (VA) decode device.</p>


## -prototype

````
PFND3DDDI_DECODEBEGINFRAME DecodeBeginFrame;

__checkReturn HRESULT APIENTRY DecodeBeginFrame(
  _In_ HANDLE                     hDevice,
  _In_ D3DDDIARG_DECODEBEGINFRAME *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p> A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-decodebeginframe.md">D3DDDIARG_DECODEBEGINFRAME</a> structure that describes information for the DirectX VA decoder to start decoding a frame.</p>
</dd>
</dl>

## -returns
<p><b>DecodeBeginFrame</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>Decoding successfully began.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodebeginframe.md">DecodeBeginFrame</a> could not allocate the required memory for it to complete.</p>

<p> </p>

## -remarks
<p>The <b>DecodeBeginFrame</b> function notifies the user-mode display driver that its <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodeexecute.md">DecodeExecute</a> function can be called on the specified decode device.</p>

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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-decodebeginframe.md">D3DDDIARG_DECODEBEGINFRAME</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicefuncs.md">D3DDDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodeexecute.md">DecodeExecute</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_DECODEBEGINFRAME callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
