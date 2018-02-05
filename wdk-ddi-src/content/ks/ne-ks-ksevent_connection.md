---
UID : NE:ks.KSEVENT_CONNECTION
title : KSEVENT_CONNECTION
author : windows-driver-content
description : "."
old-location : stream\ksevent_connection.htm
old-project : stream
ms.assetid : E85946B3-90B6-41CA-9F69-47B33AE8D851
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ks/KSEVENT_CONNECTION_PRIORITY, KSEVENT_CONNECTION_POSITIONUPDATE, KSEVENT_CONNECTION_PRIORITY, KSEVENT_CONNECTION_ENDOFSTREAM, ks/KSEVENT_CONNECTION_DATADISCONTINUITY, KSEVENT_CONNECTION, stream.ksevent_connection, ks/KSEVENT_CONNECTION_POSITIONUPDATE, KSEVENT_CONNECTION_DATADISCONTINUITY, ks/KSEVENT_CONNECTION_TIMEDISCONTINUITY, KSEVENT_CONNECTION enumeration [Streaming Media Devices], ks/KSEVENT_CONNECTION_ENDOFSTREAM, ks/KSEVENT_CONNECTION, KSEVENT_CONNECTION_TIMEDISCONTINUITY
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
req.typenames : KSEVENT_CONNECTION
---

# KSEVENT_CONNECTION Enumeration


## Syntax
````
typedef enum  { 
  KSEVENT_CONNECTION_POSITIONUPDATE,
  KSEVENT_CONNECTION_DATADISCONTINUITY,
  KSEVENT_CONNECTION_TIMEDISCONTINUITY,
  KSEVENT_CONNECTION_PRIORITY,
  KSEVENT_CONNECTION_ENDOFSTREAM
} KSEVENT_CONNECTION;
````

## Constants

<table>

<tr>
<td>KSEVENT_CONNECTION_DATADISCONTINUITY</td>
<td></td>
</tr>

<tr>
<td>KSEVENT_CONNECTION_ENDOFSTREAM</td>
<td></td>
</tr>

<tr>
<td>KSEVENT_CONNECTION_POSITIONUPDATE</td>
<td></td>
</tr>

<tr>
<td>KSEVENT_CONNECTION_PRIORITY</td>
<td></td>
</tr>

<tr>
<td>KSEVENT_CONNECTION_TIMEDISCONTINUITY</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h |