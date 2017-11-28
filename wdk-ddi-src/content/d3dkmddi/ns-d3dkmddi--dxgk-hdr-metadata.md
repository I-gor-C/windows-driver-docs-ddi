---
UID: NS.d3dkmddi._DXGK_HDR_METADATA
title: DXGK_HDR_METADATA
author: windows-driver-content
description: Contains information about the HDR metadata.
old-location: display\dxgk_hdr_metadata.htm
old-project: display
ms.assetid: 15AE3B05-1FD4-4ADB-B92F-9098225A920B
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_HDR_METADATA, DXGK_HDR_METADATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_HDR_METADATA
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_HDR_METADATA structure



## -description
<p>Contains information about the HDR metadata.</p>


## -syntax

````
typedef struct _DXGK_HDR_METADATA {
  D3DDDI_HDR_METADATA_TYPE  Type;
  UINT                      Size;
  VOID                      *pMetaData;
} DXGK_HDR_METADATA;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Indicates the type of the HDR metadata.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Indicates the size of the HDR metadata.</p>
</dd>

### -field <b>pMetaData</b>

<dd>
<p>Pointer to the HDR metadata.</p>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>