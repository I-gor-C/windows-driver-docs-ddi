---
UID: NE.d3dkmthk._D3DKMT_PNP_KEY_TYPE
title: D3DKMT_PNP_KEY_TYPE
author: windows-driver-content
description: An enum that indicates the type of PNP key.
old-location: display\d3dkmt_pnp_key_type.htm
ms.assetid: 48B173D5-56C3-4611-BC55-CB7A25D05352
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_PNP_KEY_TYPE
req.alt-loc: d3dkmthk.h
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
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
req.iface: 
---

# D3DKMT_PNP_KEY_TYPE enumeration



## -description
<p>An enum that indicates the type of PNP key. </p>


## -syntax

````
typedef enum _D3DKMT_PNP_KEY_TYPE { 
  D3DKMT_PNP_KEY_HARDWARE  = 1,
  D3DKMT_PNP_KEY_SOFTWARE  = 2
} D3DKMT_PNP_KEY_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMT_PNP_KEY_HARDWARE"></a><a id="d3dkmt_pnp_key_hardware"></a><b>D3DKMT_PNP_KEY_HARDWARE</b>

<dd>
<p>Indicates that the key is a hardware key..</p>
</dd>

### -field <a id="D3DKMT_PNP_KEY_SOFTWARE"></a><a id="d3dkmt_pnp_key_software"></a><b>D3DKMT_PNP_KEY_SOFTWARE</b>

<dd>
<p>Indicates that the key is a software key.</p>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>