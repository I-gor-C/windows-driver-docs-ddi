---
UID : NE:ks.KSPROPERTY_GM
title : KSPROPERTY_GM
author : windows-driver-content
description : "."
old-location : stream\ksproperty_gm.htm
old-project : stream
ms.assetid : 723A64D3-30E0-4B8C-8CAB-3D7B685860F3
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ks/KSPROPERTY_GM, KSPROPERTY_GM_TIMESTAMP_CLOCK, KSPROPERTY_GM_GRAPHMANAGER, KSPROPERTY_GM_RATEMATCH, KSPROPERTY_GM_RENDER_CLOCK, ks/KSPROPERTY_GM_RENDER_CLOCK, KSPROPERTY_GM, ks/KSPROPERTY_GM_GRAPHMANAGER, ks/KSPROPERTY_GM_TIMESTAMP_CLOCK, KSPROPERTY_GM enumeration [Streaming Media Devices], stream.ksproperty_gm, ks/KSPROPERTY_GM_RATEMATCH
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ks.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : KSPROPERTY_GM
---

# KSPROPERTY_GM Enumeration


## Syntax
````
typedef enum  { 
  KSPROPERTY_GM_GRAPHMANAGER,
  KSPROPERTY_GM_TIMESTAMP_CLOCK,
  KSPROPERTY_GM_RATEMATCH,
  KSPROPERTY_GM_RENDER_CLOCK
} KSPROPERTY_GM;
````

## Constants

<table>

<tr>
<td>KSPROPERTY_GM_GRAPHMANAGER</td>
<td>Not supported.</td>
</tr>

<tr>
<td>KSPROPERTY_GM_RATEMATCH</td>
<td>Not supported.</td>
</tr>

<tr>
<td>KSPROPERTY_GM_RENDER_CLOCK</td>
<td>Not supported.</td>
</tr>

<tr>
<td>KSPROPERTY_GM_TIMESTAMP_CLOCK</td>
<td>Not supported.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h |