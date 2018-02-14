---
UID: NE:pointofservicedriverinterface._MsrErrorReportingType
title: "_MsrErrorReportingType"
author: windows-driver-content
description: This enumeration defines the constants that indicate the error reporting type for the magnetic stripe reader (MSR).
old-location: pos\msrerrorreportingtype.htm
old-project: pos
ms.assetid: 86b0845b-28fc-47d3-add8-dd3e8b8f631c
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: pointofservicedriverinterface/MsrErrorReportingType, pointofservicedriverinterface/MsrErrorReportingType_CardLevel, pointofservicedriverinterface/MsrErrorReportingType_TrackLevel, MsrErrorReportingType enumeration, pos.msrerrorreportingtype, _MsrErrorReportingType, MsrErrorReportingType, MsrErrorReportingType_CardLevel, MsrErrorReportingType_TrackLevel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pointofservicedriverinterface.h
req.include-header: Pointofservicedriverinterface.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	pointofservicedriverinterface.h
apiname:
-	MsrErrorReportingType
product: Windows
targetos: Windows
req.typenames: MsrErrorReportingType
---

# _MsrErrorReportingType Enumeration
This enumeration defines the constants that indicate the error reporting type for the magnetic stripe reader (MSR).

## Syntax
````
typedef enum _MsrErrorReportingType { 
  MsrErrorReportingType_CardLevel   = ,
  MsrErrorReportingType_TrackLevel
} MsrErrorReportingType;
````

## Constants

<table>
            
                <tr>
                    <td>MsrErrorReportingType_CardLevel</td>
                    <td>Reports errors at the card level.</td>
                </tr>
            
                <tr>
                    <td>MsrErrorReportingType_TrackLevel</td>
                    <td>Reports errors at the track level.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |