---
UID : NE:ks.PKSPIN_COMMUNICATION
title : "*PKSPIN_COMMUNICATION"
author : windows-driver-content
description : .
old-location : stream\kspin_communication.htm
old-project : stream
ms.assetid : DBBEEE9D-82C1-4387-AA6D-C5D86EDB138C
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : "*PKSPIN_COMMUNICATION, *PKSPIN_COMMUNICATION, KSPIN_COMMUNICATION"
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
req.alt-api : KSPIN_COMMUNICATION
req.alt-loc : Ks.h
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
req.typenames : "*PKSPIN_COMMUNICATION, KSPIN_COMMUNICATION"
---

# *PKSPIN_COMMUNICATION Enumeration


## Syntax
````
typedef enum  { 
  KSPIN_COMMUNICATION_NONE,
  KSPIN_COMMUNICATION_SINK,
  KSPIN_COMMUNICATION_SOURCE,
  KSPIN_COMMUNICATION_BOTH,
  KSPIN_COMMUNICATION_BRIDGE
} KSPIN_COMMUNICATION, *PKSPIN_COMMUNICATION;
````

## Constants

<table>

<tr>
<td>KSPIN_COMMUNICATION_BOTH</td>
<td></td>
</tr>

<tr>
<td>KSPIN_COMMUNICATION_BRIDGE</td>
<td></td>
</tr>

<tr>
<td>KSPIN_COMMUNICATION_NONE</td>
<td></td>
</tr>

<tr>
<td>KSPIN_COMMUNICATION_SINK</td>
<td></td>
</tr>

<tr>
<td>KSPIN_COMMUNICATION_SOURCE</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h |