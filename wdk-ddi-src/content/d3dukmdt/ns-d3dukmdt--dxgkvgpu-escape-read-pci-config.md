---
UID: NS.d3dukmdt._DXGKVGPU_ESCAPE_READ_PCI_CONFIG
title: DXGKVGPU_ESCAPE_READ_PCI_CONFIG
author: windows-driver-content
description: A structure used to read the PCI config for an escape.
old-location: display\dxgkvgpu_escape_read_pci_config.htm
old-project: display
ms.assetid: B6F4207F-B55A-4B36-883D-291E351742CA
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKVGPU_ESCAPE_READ_PCI_CONFIG, DXGKVGPU_ESCAPE_READ_PCI_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: TBD
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKVGPU_ESCAPE_READ_PCI_CONFIG
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

# DXGKVGPU_ESCAPE_READ_PCI_CONFIG structure



## -description
<p>A structure used to read the PCI config for an escape.</p>


## -syntax

````
typedef struct _DXGKVGPU_ESCAPE_READ_PCI_CONFIG {
  DXGKVGPU_ESCAPE_HEAD Header;
  UINT                 Offset;
  UINT                 Size;
} DXGKVGPU_ESCAPE_READ_PCI_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The escape header being processed.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>Offset in bytes in the PCI config space.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Size in bytes to read.</p>
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
<dt>D3dukmdt.h (include TBD)</dt>
</dl>
</td>
</tr>
</table>