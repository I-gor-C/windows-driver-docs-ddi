---
UID: NC.d3dumddi.PFND3DDDI_DXVAHD_SETVIDEOPROCESSBLTSTATE
title: PFND3DDDI_DXVAHD_SETVIDEOPROCESSBLTSTATE
author: windows-driver-content
description: The SetVideoProcessBltState function sets the state of a bit-block transfer (bitblt) for a video processor.
old-location: display\setvideoprocessbltstate.htm
old-project: display
ms.assetid: 6796372c-279d-427c-a2a4-9b7c99494f53
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: SetVideoProcessBltState is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetVideoProcessBltState
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

# PFND3DDDI_DXVAHD_SETVIDEOPROCESSBLTSTATE callback



## -description
<p>The <i>SetVideoProcessBltState</i> function sets the state of a bit-block transfer (bitblt) for a video processor. </p>


## -prototype

````
PFND3DDDI_DXVAHD_SETVIDEOPROCESSBLTSTATE SetVideoProcessBltState;

__checkReturn HRESULT APIENTRY SetVideoProcessBltState(
  _In_       HANDLE                                   hDevice,
  _In_ const D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE *pData
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
<p> A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-dxvahd-setvideoprocessbltstate.md">D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE</a> structure that describes how to change the bitblt state. </p>
</dd>
</dl>

## -returns
<p><i>SetVideoProcessBltState</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The bitblt state is successfully set. </p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><i>SetVideoProcessBltState</i> could not allocate the required memory for it to complete.</p>

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
<p>SetVideoProcessBltState is supported beginning with the Windows 7 operating system.</p>
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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-dxvahd-setvideoprocessbltstate.md">D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_DXVAHD_SETVIDEOPROCESSBLTSTATE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
