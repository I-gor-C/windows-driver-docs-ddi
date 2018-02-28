---
UID: NE:pointofservicedriverinterface._MsrCardType
title: "_MsrCardType"
author: windows-driver-content
description: This enumeration defines the kinds of magnetic stripe cards.
old-location: pos\msrcardtype.htm
old-project: pos
ms.assetid: aa7af210-fb5e-49a1-911f-cb1e90c2ac26
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: MsrCardType, MsrCardType enumeration, MsrCardType_Aamva, MsrCardType_Bank, MsrCardType_ExtendedBase, MsrCardType_Unknown, _MsrCardType, pointofservicedriverinterface/MsrCardType, pointofservicedriverinterface/MsrCardType_Aamva, pointofservicedriverinterface/MsrCardType_Bank, pointofservicedriverinterface/MsrCardType_ExtendedBase, pointofservicedriverinterface/MsrCardType_Unknown, pos.msrcardtype
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
req.irql: Called at PASSIVE_LEVEL.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	pointofservicedriverinterface.h
api_name:
-	MsrCardType
product: Windows
targetos: Windows
req.typenames: MsrCardType
---

# _MsrCardType Enumeration
This enumeration defines the kinds of magnetic stripe cards.

## Syntax
````
typedef enum _MsrCardType { 
  MsrCardType_Unknown,
  MsrCardType_Bank,
  MsrCardType_Aamva,
  MsrCardType_ExtendedBase
} MsrCardType;
````

## Constants

<table>
            
                <tr>
                    <td>MsrCardType_Aamva</td>
                    <td>American Association of Motor Vehicle Administrators (AAMVA) card.</td>
                </tr>
            
                <tr>
                    <td>MsrCardType_Bank</td>
                    <td>Bank card.</td>
                </tr>
            
                <tr>
                    <td>MsrCardType_ExtendedBase</td>
                    <td>Vendor-specific card.</td>
                </tr>
            
                <tr>
                    <td>MsrCardType_Unknown</td>
                    <td>Unknown card type.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |