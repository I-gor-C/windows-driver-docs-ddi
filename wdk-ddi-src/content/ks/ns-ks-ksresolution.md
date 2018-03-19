---
UID: NS:ks.KSRESOLUTION
title: KSRESOLUTION
author: windows-driver-content
description: The KSRESOLUTION structure specifies granularity and error of a kernel streaming clock.
old-location: stream\ksresolution.htm
old-project: stream
ms.assetid: fbd6222c-6d54-4e2a-aa5b-8051f0838886
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKSRESOLUTION, KSRESOLUTION, KSRESOLUTION structure [Streaming Media Devices], PKSRESOLUTION, PKSRESOLUTION structure pointer [Streaming Media Devices], ks-struct_eb48cf83-0b80-4955-89a4-0b363497bef5.xml, ks/KSRESOLUTION, ks/PKSRESOLUTION, stream.ksresolution"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
-	KSRESOLUTION
product: Windows
targetos: Windows
req.typenames: KSRESOLUTION, *PKSRESOLUTION
---

# KSRESOLUTION structure
The KSRESOLUTION structure specifies granularity and error of a kernel streaming clock.

## Syntax
````
typedef struct {
  LONGLONG Granularity;
  LONGLONG Error;
} KSRESOLUTION, *PKSRESOLUTION;
````

## Members


`Granularity`

Specifies the increment granularity of the clock in 100-nanosecond units, where 1 is the best.

`Error`

Specifies the +/- notification error of the clock in 100-nanosecond units, where 0 is the best, meaning the event notification granularity is as good as the increment granularity.

## Remarks
Vendors can supply a structure of type KSRESOLUTION in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565092">KSPROPERTY_CLOCK_RESOLUTION</a> property request.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff565092">KSPROPERTY_CLOCK_RESOLUTION</a>