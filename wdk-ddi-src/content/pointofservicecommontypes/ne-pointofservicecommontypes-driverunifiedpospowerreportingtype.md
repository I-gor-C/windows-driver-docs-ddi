---
UID: NE:pointofservicecommontypes.DriverUnifiedPosPowerReportingType
title: DriverUnifiedPosPowerReportingType
author: windows-driver-content
description: This enumeration defines the type of power reporting that is supported by the device (for example, advanced, standard, and so on).
old-location: pos\unifiedpospowerreportingtype.htm
old-project: pos
ms.assetid: e0263969-1c6a-4805-a647-d4b9df83ef71
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: Advanced, DriverUnifiedPosPowerReportingType, DriverUnifiedPosPowerReportingType enumeration, Standard, UnknownPowerReportingType, pointofservicecommontypes/Advanced, pointofservicecommontypes/DriverUnifiedPosPowerReportingType, pointofservicecommontypes/Standard, pointofservicecommontypes/UnknownPowerReportingType, pos.unifiedpospowerreportingtype
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pointofservicecommontypes.h
req.include-header: Pointofservicecommontypes.h
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
req.irql: Called at PASSIVE_LEVEL.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	pointofservicecommontypes.h
api_name:
-	DriverUnifiedPosPowerReportingType
product: Windows
targetos: Windows
req.typenames: DriverUnifiedPosPowerReportingType
---

# DriverUnifiedPosPowerReportingType Enumeration
This enumeration defines the type of power reporting that is supported by the device (for example, advanced, standard, and so on).

## Syntax
````
typedef enum _DriverUnifiedPosPowerReportingType { 
  UnknownPowerReportingType  = 0,
  Standard                   = 1,
  Advanced                   = 2
} DriverUnifiedPosPowerReportingType;
````

## Constants

<table>
            
                <tr>
                    <td>Advanced</td>
                    <td>The device supports the advanced power reporting type.</td>
                </tr>
            
                <tr>
                    <td>Standard</td>
                    <td>The device supports the standard power reporting type.</td>
                </tr>
            
                <tr>
                    <td>UnknownPowerReportingType</td>
                    <td>The power reporting type is not known.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicecommontypes.h (include Pointofservicecommontypes.h) |