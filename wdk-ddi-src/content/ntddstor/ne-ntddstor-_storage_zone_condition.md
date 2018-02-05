---
UID : NE:ntddstor._STORAGE_ZONE_CONDITION
title : "_STORAGE_ZONE_CONDITION"
author : windows-driver-content
description : Note  This structure is for internal use only and should not be called from your code. .
old-location : storage\storage_zone_condition.htm
old-project : storage
ms.assetid : 57FF3890-6B37-45EB-BB02-22B2ADDFAA90
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : ntddstor/ZoneConditionReadOnly, _STORAGE_ZONE_CONDITION, ntddstor/ZoneConditionFull, ntddstor/ZoneConditionEmpty, ntddstor/STORAGE_ZONE_CONDITION, ntddstor/PSTORAGE_ZONE_CONDITION, ZoneConditionConventional, ntddstor/ZoneConditionClosed, storage.storage_zone_condition, ZoneConditionEmpty, ZoneConditionImplicitlyOpened, ntddstor/ZoneConditionConventional, ntddstor/ZoneConditionExplicitlyOpened, PSTORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION, STORAGE_ZONE_CONDITION enumeration [Storage Devices], ZoneConditionFull, PSTORAGE_ZONE_CONDITION enumeration pointer [Storage Devices], ntddstor/ZoneConditionImplicitlyOpened, ZoneConditionClosed, ntddstor/ZoneConditionOffline, ZoneConditionOffline, ZoneConditionReadOnly, STORAGE_ZONE_CONDITION, ZoneConditionExplicitlyOpened
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddstor.h
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
req.typenames : STORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION
---

# _STORAGE_ZONE_CONDITION Enumeration
<div class="alert"><b>Note</b>  This  structure is for internal use only and should not be called from your code.</div>
<div> </div>

## Syntax
````
typedef enum _STORAGE_ZONE_CONDITION { 
  ZoneConditionConventional      = 0x00,
  ZoneConditionEmpty             = 0x01,
  ZoneConditionImplicitlyOpened  = 0x02,
  ZoneConditionExplicitlyOpened  = 0x03,
  ZoneConditionClosed            = 0x04,
  ZoneConditionReadOnly          = 0x0D,
  ZoneConditionFull              = 0x0E,
  ZoneConditionOffline           = 0x0F
} STORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION;
````

## Constants

<table>

<tr>
<td>ZoneConditionClosed</td>
<td>N/A</td>
</tr>

<tr>
<td>ZoneConditionConventional</td>
<td>N/A</td>
</tr>

<tr>
<td>ZoneConditionEmpty</td>
<td>N/A</td>
</tr>

<tr>
<td>ZoneConditionExplicitlyOpened</td>
<td>N/A</td>
</tr>

<tr>
<td>ZoneConditionFull</td>
<td>N/A</td>
</tr>

<tr>
<td>ZoneConditionImplicitlyOpened</td>
<td>N/A</td>
</tr>

<tr>
<td>ZoneConditionOffline</td>
<td>N/A</td>
</tr>

<tr>
<td>ZoneConditionReadOnly</td>
<td>N/A</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddstor.h |