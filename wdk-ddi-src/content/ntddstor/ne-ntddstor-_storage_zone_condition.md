---
UID: NE:ntddstor._STORAGE_ZONE_CONDITION
title: "_STORAGE_ZONE_CONDITION"
author: windows-driver-content
description: Note  This structure is for internal use only and should not be called from your code. .
old-location: storage\storage_zone_condition.htm
old-project: storage
ms.assetid: 57FF3890-6B37-45EB-BB02-22B2ADDFAA90
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PSTORAGE_ZONE_CONDITION, PSTORAGE_ZONE_CONDITION, PSTORAGE_ZONE_CONDITION enumeration pointer [Storage Devices], STORAGE_ZONE_CONDITION, STORAGE_ZONE_CONDITION enumeration [Storage Devices], ZoneConditionClosed, ZoneConditionConventional, ZoneConditionEmpty, ZoneConditionExplicitlyOpened, ZoneConditionFull, ZoneConditionImplicitlyOpened, ZoneConditionOffline, ZoneConditionReadOnly, _STORAGE_ZONE_CONDITION, ntddstor/PSTORAGE_ZONE_CONDITION, ntddstor/STORAGE_ZONE_CONDITION, ntddstor/ZoneConditionClosed, ntddstor/ZoneConditionConventional, ntddstor/ZoneConditionEmpty, ntddstor/ZoneConditionExplicitlyOpened, ntddstor/ZoneConditionFull, ntddstor/ZoneConditionImplicitlyOpened, ntddstor/ZoneConditionOffline, ntddstor/ZoneConditionReadOnly, storage.storage_zone_condition"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddstor.h
api_name:
-	STORAGE_ZONE_CONDITION
product: Windows
targetos: Windows
req.typenames: STORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION
---

# _STORAGE_ZONE_CONDITION Enumeration
<div class="alert"><b>Note</b>  This  structure is for internal use only and should not be called from your code.</div>
<div> </div>

## Syntax
```
typedef enum _STORAGE_ZONE_CONDITION {
  ZoneConditionConventional      ,
  ZoneConditionEmpty             ,
  ZoneConditionImplicitlyOpened  ,
  ZoneConditionExplicitlyOpened  ,
  ZoneConditionClosed            ,
  ZoneConditionReadOnly          ,
  ZoneConditionFull              ,
  ZoneConditionOffline
} STORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION;
```

## Constants

<table>
            
                <tr>
                    <td>ZoneConditionConventional</td>
                    <td>N/A</td>
                </tr>
            
                <tr>
                    <td>ZoneConditionEmpty</td>
                    <td>N/A</td>
                </tr>
            
                <tr>
                    <td>ZoneConditionImplicitlyOpened</td>
                    <td>N/A</td>
                </tr>
            
                <tr>
                    <td>ZoneConditionExplicitlyOpened</td>
                    <td>N/A</td>
                </tr>
            
                <tr>
                    <td>ZoneConditionClosed</td>
                    <td>N/A</td>
                </tr>
            
                <tr>
                    <td>ZoneConditionReadOnly</td>
                    <td>N/A</td>
                </tr>
            
                <tr>
                    <td>ZoneConditionFull</td>
                    <td>N/A</td>
                </tr>
            
                <tr>
                    <td>ZoneConditionOffline</td>
                    <td>N/A</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddstor.h |