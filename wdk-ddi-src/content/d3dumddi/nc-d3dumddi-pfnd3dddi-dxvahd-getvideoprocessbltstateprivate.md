---
UID: NC.d3dumddi.PFND3DDDI_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE
title: PFND3DDDI_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE
author: windows-driver-content
description: The GetVideoProcessBltStatePrivate function retrieves the state data of a private bit-block transfer (bitblt) for a video processor.
old-location: display\getvideoprocessbltstateprivate.htm
old-project: display
ms.assetid: bb4c04cf-0125-47bf-8fc8-88d807e7b6ad
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: GetVideoProcessBltStatePrivate is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetVideoProcessBltStatePrivate
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

# PFND3DDDI_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE callback



## -description
<p>The <i>GetVideoProcessBltStatePrivate</i> function retrieves the state data of a private bit-block transfer (bitblt) for a video processor. </p>


## -prototype

````
PFND3DDDI_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE GetVideoProcessBltStatePrivate;

__checkReturn HRESULT APIENTRY GetVideoProcessBltStatePrivate(
  _In_    HANDLE                                          hDevice,
  _Inout_ D3DDDIARG_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE *pData
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
<p> A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-dxvahd-getvideoprocessbltstateprivate.md">D3DDDIARG_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE</a> structure that describes the private bitblt state data to retrieve. </p>
</dd>
</dl>

## -returns
<p>The <i>GetVideoProcessBltStatePrivate</i> function returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The bitblt state data is successfully retrieved. </p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><i>GetVideoProcessBltStatePrivate</i> could not allocate the required memory for it to complete.</p>

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
<p><i>GetVideoProcessBltStatePrivate</i> is supported beginning with the Windows 7 operating system.</p>
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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-dxvahd-getvideoprocessbltstateprivate.md">D3DDDIARG_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
