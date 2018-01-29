---
UID : NE:ks.KSSTACK_USE
title : KSSTACK_USE
author : windows-driver-content
description : .
old-location : stream\ksstack_use.htm
old-project : stream
ms.assetid : 76B45154-5E81-4515-ADEE-11401FDF4681
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ks/KsStackCopyToNewLocation, stream.ksstack_use, ks/KsStackReuseCurrentLocation, ks/KsStackUseNewLocation, KsStackCopyToNewLocation, KsStackReuseCurrentLocation, KSSTACK_USE, ks/KSSTACK_USE, KSSTACK_USE enumeration [Streaming Media Devices], KsStackUseNewLocation
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
req.typenames : KSSTACK_USE
---

# KSSTACK_USE Enumeration


## Syntax
````
typedef enum  { 
  KsStackCopyToNewLocation,
  KsStackReuseCurrentLocation,
  KsStackUseNewLocation
} KSSTACK_USE;
````

## Constants

<table>

<tr>
<td>KsStackCopyToNewLocation</td>
<td></td>
</tr>

<tr>
<td>KsStackReuseCurrentLocation</td>
<td></td>
</tr>

<tr>
<td>KsStackUseNewLocation</td>
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