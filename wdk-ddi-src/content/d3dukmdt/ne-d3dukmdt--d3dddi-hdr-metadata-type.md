---
UID: NE.d3dukmdt._D3DDDI_HDR_METADATA_TYPE
title: D3DDDI_HDR_METADATA_TYPE
author: windows-driver-content
description: Defines the format of HDR metadata.
old-location: display\d3dddi_hdr_metadata_type.htm
ms.assetid: C30C34BF-F67D-4838-B337-9EF0D85B27DA
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dukmdt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_HDR_METADATA_TYPE
req.alt-loc: d3dukmdt.h
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
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
req.iface: 
---

# D3DDDI_HDR_METADATA_TYPE enumeration



## -description
<p>Defines the format of HDR metadata.</p>


## -syntax

````
typedef enum _D3DDDI_HDR_METADATA_TYPE { 
  D3DDDI_HDR_METADATA_TYPE_NONE                 = 0,
  D3DDDI_HDR_METADATA_TYPE_HDR10                = 1
} D3DDDI_HDR_METADATA_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DDDI_HDR_METADATA_TYPE_NONE_______________"></a><a id="d3dddi_hdr_metadata_type_none_______________"></a><b>D3DDDI_HDR_METADATA_TYPE_NONE               </b>

<dd>
<p>No HDR metadata is present.</p>
</dd>

### -field <a id="D3DDDI_HDR_METADATA_TYPE_HDR10"></a><a id="d3dddi_hdr_metadata_type_hdr10"></a><b>D3DDDI_HDR_METADATA_TYPE_HDR10</b>

<dd>
<p>The HDR metadata is defined using the D3DDDI_HDR_METADATA_HDR10 structure.</p>
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
<dt>D3dukmdt.h</dt>
</dl>
</td>
</tr>
</table>