---
UID : NE:ks.KSPROPERTY_STREAMINTERFACE
title : KSPROPERTY_STREAMINTERFACE
author : windows-driver-content
description : .
old-location : stream\ksproperty_streaminterface.htm
old-project : stream
ms.assetid : E771F59E-7F85-40B9-BBA9-D1CC398B12CA
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ks/KSPROPERTY_STREAMINTERFACE, stream.ksproperty_streaminterface, KSPROPERTY_STREAMINTERFACE_HEADERSIZE, KSPROPERTY_STREAMINTERFACE, KSPROPERTY_STREAMINTERFACE enumeration [Streaming Media Devices], ks/KSPROPERTY_STREAMINTERFACE_HEADERSIZE
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
req.typenames : KSPROPERTY_STREAMINTERFACE
---

# KSPROPERTY_STREAMINTERFACE Enumeration


## Syntax
````
typedef enum  { 
  KSPROPERTY_STREAMINTERFACE_HEADERSIZE
} KSPROPERTY_STREAMINTERFACE;
````

## Constants

<table>

<tr>
<td>KSPROPERTY_STREAMINTERFACE_HEADERSIZE</td>
<td>Specify to query a pin for the size of the stream header that this pin uses.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h |