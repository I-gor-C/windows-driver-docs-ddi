---
UID: NE:ks.KSDEGRADE_STANDARD
title: KSDEGRADE_STANDARD
author: windows-driver-content
description: The KSDEGRADE_STANDARD enumeration lists different types of degradation.
old-location: stream\ksdegrade_standard.htm
old-project: stream
ms.assetid: 5790ce0e-13f8-4700-8b25-a5375dd83758
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KSDEGRADE_STANDARD, KSDEGRADE_STANDARD enumeration [Streaming Media Devices], KSDEGRADE_STANDARD_COMPUTATION, KSDEGRADE_STANDARD_QUALITY, KSDEGRADE_STANDARD_SAMPLE, KSDEGRADE_STANDARD_SKIP, ks-struct_933ec08b-6ad6-47dc-8092-357d6bbe1c72.xml, ks/KSDEGRADE_STANDARD, ks/KSDEGRADE_STANDARD_COMPUTATION, ks/KSDEGRADE_STANDARD_QUALITY, ks/KSDEGRADE_STANDARD_SAMPLE, ks/KSDEGRADE_STANDARD_SKIP, stream.ksdegrade_standard
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: Ks.h
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
-	ks.h
api_name:
-	KSDEGRADE_STANDARD
product:
- Windows
targetos: Windows
req.typenames: KSDEGRADE_STANDARD
---

# KSDEGRADE_STANDARD Enumeration
The KSDEGRADE_STANDARD enumeration lists different types of degradation.

## Syntax
```
typedef enum KSDEGRADE_STANDARD {
  KSDEGRADE_STANDARD_SAMPLE       ,
  KSDEGRADE_STANDARD_QUALITY      ,
  KSDEGRADE_STANDARD_COMPUTATION  ,
  KSDEGRADE_STANDARD_SKIP
} ;
```

## Constants

<table>
            
                <tr>
                    <td>KSDEGRADE_STANDARD_SAMPLE</td>
                    <td>Specifies sample degradation.</td>
                </tr>
            
                <tr>
                    <td>KSDEGRADE_STANDARD_QUALITY</td>
                    <td>Specifies quality degradation.</td>
                </tr>
            
                <tr>
                    <td>KSDEGRADE_STANDARD_COMPUTATION</td>
                    <td>Specifies computation degradation.</td>
                </tr>
            
                <tr>
                    <td>KSDEGRADE_STANDARD_SKIP</td>
                    <td>Requests to skip ahead a specified delta in the data stream.</td>
                </tr>
</table>

## Remarks

For more information, see <a href="https://msdn.microsoft.com/359e6e12-903f-4037-8f35-b090ce41f770">Quality Management</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561671">KSDEGRADE</a>