---
UID: NS.D3DKMTHK._D3DKMT_OUTPUTDUPL_METADATA
title: _D3DKMT_OUTPUTDUPL_METADATA
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outputdupl_metadata.htm
old-project: display
ms.assetid: abf4f00a-05bb-48f6-989e-f1b453fb0708
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_OUTPUTDUPL_METADATA, D3DKMT_OUTPUTDUPL_METADATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OUTPUTDUPL_METADATA
req.alt-loc: D3dkmthk.h
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
---

# _D3DKMT_OUTPUTDUPL_METADATA structure



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef struct _D3DKMT_OUTPUTDUPL_METADATA {
  D3DKMT_HANDLE                  hAdapter;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  D3DKMT_OUTPUTDUPL_METADATATYPE Type;
  UINT                           BufferSizeSupplied;
  PVOID                          pBuffer;
  UINT                           BufferSizeRequired;
} D3DKMT_OUTPUTDUPL_METADATA;
````


## -struct-fields

### -field hAdapter


### -field VidPnSourceId


### -field Type


### -field BufferSizeSupplied


### -field pBuffer


### -field BufferSizeRequired


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>