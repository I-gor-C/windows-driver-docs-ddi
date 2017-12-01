---
UID: NS.d3dumddi._D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE
title: D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE
author: windows-driver-content
description: The D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE structure describes the stream state of the video processor to change and the data that is used to change the state.
old-location: display\d3dddiarg_dxvahd_setvideoprocessstreamstate.htm
old-project: display
ms.assetid: f1f99725-4110-49b4-9149-1f6d03faeb0e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE, D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE
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

# D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE structure



## -description
<p>The D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE structure describes the stream state of the video processor to change and the data that is used to change the state. </p>


## -syntax

````
typedef struct _D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE {
  HANDLE                 hVideoProcessor;
  UINT                   StreamNumber;
  DXVAHDDDI_STREAM_STATE State;
  UINT                   DataSize;
  const VOID             *pData;
} D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE;
````


## -struct-fields
<dl>

### -field <b>hVideoProcessor</b>

<dd>
<p>[in] A handle to the video processor whose stream state is changed.</p>
</dd>

### -field <b>StreamNumber</b>

<dd>
<p>[in] A zero-based stream index number. This number must be less than the number that the driver set in the <b>MaxStreamStates</b> member of the <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-vpdevcaps.md">DXVAHDDDI_VPDEVCAPS</a> structure. </p>
</dd>

### -field <b>State</b>

<dd>
<p>[in] A <a href="..\d3dumddi\ne-d3dumddi--dxvahdddi-stream-state.md">DXVAHDDDI_STREAM_STATE</a>-typed value that indicates the stream state to modify.</p>
</dd>

### -field <b>DataSize</b>

<dd>
<p>[in] The size, in bytes, of the data that is used to change the stream state.</p>
</dd>

### -field <b>pData</b>

<dd>
<p>[in] A pointer to the data that is used to change the stream state. For more information about the types of data that <b>pData</b> can point to, see the values of the <a href="..\d3dumddi\ne-d3dumddi--dxvahdddi-stream-state.md">DXVAHDDDI_STREAM_STATE</a> enumeration. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE is supported beginning with the Windows 7 operating system.</p>
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
<a href="..\d3dumddi\ne-d3dumddi--dxvahdddi-stream-state.md">DXVAHDDDI_STREAM_STATE</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-vpdevcaps.md">DXVAHDDDI_VPDEVCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-setvideoprocessstreamstate.md">SetVideoProcessStreamState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
