---
UID: NE.d3dumddi._D3DDDI_DEVICEEXECUTION_STATE
title: D3DDDI_DEVICEEXECUTION_STATE
author: windows-driver-content
description: Indicates the state of the device.
old-location: display\d3dddi_deviceexecution_state.htm
ms.assetid: E81A31B5-E06F-4848-9AC6-8A18E8E97E15
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_DEVICEEXECUTION_STATE
req.alt-loc: D3dumddi.h
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# D3DDDI_DEVICEEXECUTION_STATE enumeration



## -description
<p>Indicates the state of the device.</p>


## -syntax

````
typedef enum _D3DDDI_DEVICEEXECUTION_STATE { 
  D3DDDI_DEVICEEXECUTION_ACTIVE             = 1,
  D3DDDI_DEVICEEXECUTION_RESET              = 2,
  D3DDDI_DEVICEEXECUTION_HUNG               = 3,
  D3DDDI_DEVICEEXECUTION_STOPPED            = 4,
  D3DDDI_DEVICEEXECUTION_ERROR_OUTOFMEMORY  = 5,
  D3DDDI_DEVICEEXECUTION_ERROR_DMAFAULT     = 6
} D3DDDI_DEVICEEXECUTION_STATE;
````


## -enum-fields
<dl>

### -field <a id="D3DDDI_DEVICEEXECUTION_ACTIVE"></a><a id="d3dddi_deviceexecution_active"></a><b>D3DDDI_DEVICEEXECUTION_ACTIVE</b>

<dd>
<p>The device is active.</p>
</dd>

### -field <a id="D3DDDI_DEVICEEXECUTION_RESET"></a><a id="d3dddi_deviceexecution_reset"></a><b>D3DDDI_DEVICEEXECUTION_RESET</b>

<dd>
<p>The device has been reset.</p>
</dd>

### -field <a id="D3DDDI_DEVICEEXECUTION_HUNG"></a><a id="d3dddi_deviceexecution_hung"></a><b>D3DDDI_DEVICEEXECUTION_HUNG</b>

<dd>
<p>The device is still running but has stopped responding (it is "hung").</p>
</dd>

### -field <a id="D3DDDI_DEVICEEXECUTION_STOPPED"></a><a id="d3dddi_deviceexecution_stopped"></a><b>D3DDDI_DEVICEEXECUTION_STOPPED</b>

<dd>
<p>The device has stopped.</p>
</dd>

### -field <a id="D3DDDI_DEVICEEXECUTION_ERROR_OUTOFMEMORY"></a><a id="d3dddi_deviceexecution_error_outofmemory"></a><b>D3DDDI_DEVICEEXECUTION_ERROR_OUTOFMEMORY</b>

<dd>
<p>The device has run out of memory.</p>
</dd>

### -field <a id="D3DDDI_DEVICEEXECUTION_ERROR_DMAFAULT"></a><a id="d3dddi_deviceexecution_error_dmafault"></a><b>D3DDDI_DEVICEEXECUTION_ERROR_DMAFAULT</b>

<dd>
<p>The device has a DMA fault error.</p>
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
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