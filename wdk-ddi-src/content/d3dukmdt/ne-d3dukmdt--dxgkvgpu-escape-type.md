---
UID: NE.d3dukmdt._DXGKVGPU_ESCAPE_TYPE
title: DXGKVGPU_ESCAPE_TYPE
author: windows-driver-content
description: An enum that holds information about the escape type.
old-location: display\dxgkvgpu_escape_type.htm
old-project: display
ms.assetid: F7081B59-DB24-4BFE-B1BD-3BE228804AB2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dukmdt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKVGPU_ESCAPE_TYPE
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
req.iface: 
---

# DXGKVGPU_ESCAPE_TYPE enumeration



## -description
<p>An enum that holds information about the escape type.</p>


## -syntax

````
typedef enum _DXGKVGPU_ESCAPE_TYPE { 
  DXGKVGPU_ESCAPE_TYPE_READ_PCI_CONFIG  = 0,
  DXGKVGPU_ESCAPE_TYPE_GET_VGPU_TYPE    = 4
} DXGKVGPU_ESCAPE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DXGKVGPU_ESCAPE_TYPE_READ_PCI_CONFIG"></a><a id="dxgkvgpu_escape_type_read_pci_config"></a><b>DXGKVGPU_ESCAPE_TYPE_READ_PCI_CONFIG</b>

<dd>
<p>Indicates the PCI config of the escape type.</p>
</dd>

### -field <a id="DXGKVGPU_ESCAPE_TYPE_GET_VGPU_TYPE"></a><a id="dxgkvgpu_escape_type_get_vgpu_type"></a><b>DXGKVGPU_ESCAPE_TYPE_GET_VGPU_TYPE</b>

<dd>
<p>Indicates the VGPU type of the escape.</p>
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