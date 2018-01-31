---
UID : NE:pointofservicedriverinterface._MsrTrackIds
title : "_MsrTrackIds"
author : windows-driver-content
description : Defines the constants that represent the magnetic stripe reader (MSR) tracks.
old-location : pos\msrtrackids.htm
old-project : pos
ms.assetid : 9366722a-c545-411d-a59f-63edfb0cd68e
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : pointofservicedriverinterface/MsrTrackIds_None, pointofservicedriverinterface/MsrTrackIds_Track2, _MsrTrackIds, MsrTrackIds_Track4, MsrTrackIds enumeration, MsrTrackIds_Track3, MsrTrackIds_Track1, pointofservicedriverinterface/MsrTrackIds_Track3, MsrTrackIds_Track2, MsrTrackIds_None, pointofservicedriverinterface/MsrTrackIds_Track4, pos.msrtrackids, MsrTrackIds, pointofservicedriverinterface/MsrTrackIds, pointofservicedriverinterface/MsrTrackIds_Track1
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : pointofservicedriverinterface.h
req.include-header : Pointofservicedriverinterface.h
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
req.irql : Called at PASSIVE_LEVEL.
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : MsrTrackIds
---

# _MsrTrackIds Enumeration
Defines the constants that represent the magnetic stripe reader (MSR) tracks.

## Syntax
````
typedef enum _MsrTrackIds { 
  MsrTrackIds_None    = 0x0,
  MsrTrackIds_Track1  = 0x1,
  MsrTrackIds_Track2  = 0x2,
  MsrTrackIds_Track3  = 0x3,
  MsrTrackIds_Track4  = 0x4
} MsrTrackIds;
````

## Constants

<table>

<tr>
<td>MsrTrackIds_None</td>
<td></td>
</tr>

<tr>
<td>MsrTrackIds_Track1</td>
<td></td>
</tr>

<tr>
<td>MsrTrackIds_Track2</td>
<td></td>
</tr>

<tr>
<td>MsrTrackIds_Track3</td>
<td></td>
</tr>

<tr>
<td>MsrTrackIds_Track4</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |