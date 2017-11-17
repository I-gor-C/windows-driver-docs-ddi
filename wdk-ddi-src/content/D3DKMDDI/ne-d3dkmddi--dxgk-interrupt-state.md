---
UID: NE.d3dkmddi._DXGK_INTERRUPT_STATE
title: DXGK_INTERRUPT_STATE
author: windows-driver-content
description: .
old-location: display\dxgk_interrupt_state.htm
ms.assetid: C72DF96B-5D12-4AC0-8FBB-904E087807DB
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_INTERRUPT_STATE
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

# DXGK_INTERRUPT_STATE enumeration



## -description
<p>Provides additional information for <a href="https://msdn.microsoft.com/0C09CAB1-3DFC-4340-8FF2-99CAF7F13156">DxgkDdi_ControlInterrupt2 </a>when VSYNC is not being utilized.</p>


## -syntax

````
typedef enum _DXGK_INTERRUPT_STATE { 
  DXGK_INTERRUPT_ENABLE      = 0,
  DXGK_INTERRUPT_DISABLE     = 1
} DXGK_INTERRUPT_STATE;
````


## -enum-fields
<dl>

### -field <a id="DXGK_INTERRUPT_ENABLE____"></a><a id="dxgk_interrupt_enable____"></a><b>DXGK_INTERRUPT_ENABLE    </b>

<dd>
<p>Indicates that the interrupt is enabled.</p>
</dd>

### -field <a id="DXGK_INTERRUPT_DISABLE___"></a><a id="dxgk_interrupt_disable___"></a><b>DXGK_INTERRUPT_DISABLE   </b>

<dd>
<p>Indicates that the interrupt is disabled.</p>
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
<p>Available in Windows 10.</p>
</td>
</tr>
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