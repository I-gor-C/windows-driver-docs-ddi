---
UID : NE:ksproxy.FRAMING_PROP
title : FRAMING_PROP
author : windows-driver-content
description : .
old-location : stream\framing_prop.htm
old-project : stream
ms.assetid : EE68F14D-F76D-4D98-99FB-BD3FB93B669A
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : stream.framing_prop, FRAMING_PROP enumeration [Streaming Media Devices], ksproxy/FramingProp_Old, FramingProp_Ex, ksproxy/FramingProp_Uninitialized, FramingProp_None, FramingProp_Uninitialized, FRAMING_PROP, ksproxy/FRAMING_PROP, FramingProp_Old, ksproxy/FramingProp_Ex, *PFRAMING_PROP, ksproxy/FramingProp_None
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ksproxy.h
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
req.typenames : FRAMING_PROP
---

# FRAMING_PROP Enumeration


## Syntax
````
typedef enum  { 
  FramingProp_Uninitialized,
  FramingProp_None,
  FramingProp_Old,
  FramingProp_Ex
} FRAMING_PROP;
````

## Constants

<table>

<tr>
<td>FramingProp_Ex</td>
<td></td>
</tr>

<tr>
<td>FramingProp_None</td>
<td></td>
</tr>

<tr>
<td>FramingProp_Old</td>
<td></td>
</tr>

<tr>
<td>FramingProp_Uninitialized</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h |