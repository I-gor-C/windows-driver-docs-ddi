---
UID: NE.d3dkmddi._DXGK_DISPLAYPANELORIENTATION
title: DXGK_DISPLAYPANELORIENTATION
author: windows-driver-content
description: Enum used to express the orientation of an integrated panel.
old-location: display\dxgk_displaypanelorientation.htm
ms.assetid: 49758A57-EFCE-4E9C-9BF6-74F6EFD356D9
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DISPLAYPANELORIENTATION
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
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
req.iface: 
---

# DXGK_DISPLAYPANELORIENTATION enumeration



## -description
<p>Enum used to express the orientation of an integrated panel.</p>


## -syntax

````
typedef enum _DXGK_DISPLAYPANELORIENTATION { 
  DXGK_DPO_0    = 0,
  DXGK_DPO_90   = 1,
  DXGK_DPO_180  = 2,
  DXGK_DPO_270  = 3
} DXGK_DISPLAYPANELORIENTATION;
````


## -enum-fields
<dl>

### -field <a id="DXGK_DPO_0"></a><a id="dxgk_dpo_0"></a><b>DXGK_DPO_0</b>

<dd>
<p>Indicates a 0 degree rotation.</p>
</dd>

### -field <a id="DXGK_DPO_90"></a><a id="dxgk_dpo_90"></a><b>DXGK_DPO_90</b>

<dd>
<p>Indicates a 90 degree rotation.</p>
</dd>

### -field <a id="DXGK_DPO_180"></a><a id="dxgk_dpo_180"></a><b>DXGK_DPO_180</b>

<dd>
<p>Indicates a 180 degree rotation.</p>
</dd>

### -field <a id="DXGK_DPO_270"></a><a id="dxgk_dpo_270"></a><b>DXGK_DPO_270</b>

<dd>
<p>Indicates a 270 degree rotation.</p>
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