---
UID: NS.D3D12UMDDI.D3D12DDI_VIEW_INSTANCING_DESC
title: D3D12DDI_VIEW_INSTANCING_DESC
author: windows-driver-content
description: View instancing description.
old-location: display\d3d12ddi-view-instancing-desc.htm
old-project: display
ms.assetid: 4d942de6-d829-499c-80cf-3cff8266aee4
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: D3D12DDI_VIEW_INSTANCING_DESC, D3D12DDI_VIEW_INSTANCING_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_VIEW_INSTANCING_DESC
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
---

# D3D12DDI_VIEW_INSTANCING_DESC structure



## -description
View instancing description.



## -syntax

````
typedef struct _D3D12DDI_VIEW_INSTANCING_DESC {
  UINT                                     ViewInstanceCount;
  const D3D12DDI_VIEW_INSTANCE_LOCATION *  pViewInstanceLocations;
  D3D12DDI_VIEW_INSTANCING_FLAGS           Flags;
} D3D12DDI_VIEW_INSTANCING_DESC, D3D12DDI_VIEW_INSTANCING_DESC;
````


## -struct-fields

### -field ViewInstanceCount

View instance count.


### -field pViewInstanceLocations

View instance locations.


### -field Flags

Flags.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>