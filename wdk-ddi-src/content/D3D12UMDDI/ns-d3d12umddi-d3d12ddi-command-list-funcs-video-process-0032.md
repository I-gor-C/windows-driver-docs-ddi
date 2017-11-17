---
UID: NS.d3d12umddi.D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032
title: D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032
author: windows-driver-content
description: The command list functions for video processing.
old-location: display\d3d12ddi-command-list-funcs-video-process-0032.htm
ms.assetid: c49f79cc-6ceb-4379-94ac-983b897d198b
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032
req.alt-loc: d3d12umddi.h
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
ms.keywords: D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032, D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032
req.iface: 
---

# D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032 structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The command list functions for video processing.</p>


## -syntax

````
typedef struct _D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032 {
  PFND3D12DDI_CLOSECOMMANDLIST                  pfnCloseCommandList;
  PFND3D12DDI_RESETCOMMANDLIST                  pfnResetCommandList;
  PFND3D12DDI_DISCARD_RESOURCE_0003             pfnDiscardResource;
  PFND3D12DDI_SET_MARKER                        pfnSetMarker;
  PFND3D12DDI_SET_PREDICATION                   pfnSetPredication;
  PFND3D12DDI_BEGIN_END_QUERY_0003              pfnBeginQuery;
  PFND3D12DDI_BEGIN_END_QUERY_0003              pfnEndQuery;
  PFND3D12DDI_RESOLVE_QUERY_DATA                pfnResolveQueryData;
  PFND3D12DDI_RESOURCEBARRIER_0022              pfnResourceBarrier;
  PFND3D12DDI_VIDEO_PROCESS_FRAME_0032          pfnProcessFrame;
  PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030  pfnSetProtectedResourceSession;
  PFND3D12DDI_WRITEBUFFERIMMEDIATE_0032         pfnWriteBufferImmediate;
} D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032, D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032;
````


## -struct-fields
<dl>

### -field <b>pfnCloseCommandList</b>

<dd>
<p>Close command list.</p>
</dd>

### -field <b>pfnResetCommandList</b>

<dd>
<p>Reset command list.</p>
</dd>

### -field <b>pfnDiscardResource</b>

<dd>
<p>Discard resource.</p>
</dd>

### -field <b>pfnSetMarker</b>

<dd>
<p>Set marker.</p>
</dd>

### -field <b>pfnSetPredication</b>

<dd>
<p>Set predication.</p>
</dd>

### -field <b>pfnBeginQuery</b>

<dd>
<p>Begin query.</p>
</dd>

### -field <b>pfnEndQuery</b>

<dd>
<p>End query.</p>
</dd>

### -field <b>pfnResolveQueryData</b>

<dd>
<p>Resolve query data.</p>
</dd>

### -field <b>pfnResourceBarrier</b>

<dd>
<p>Resource barrier.</p>
</dd>

### -field <b>pfnProcessFrame</b>

<dd>
<p>Decode frame.</p>
</dd>

### -field <b>pfnSetProtectedResourceSession</b>

<dd>
<p>Set protected resource session.</p>
</dd>

### -field <b>pfnWriteBufferImmediate</b>

<dd>
<p>Write buffer immediate.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>