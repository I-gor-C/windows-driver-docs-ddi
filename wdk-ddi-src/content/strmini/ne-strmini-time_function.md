---
UID: NE:strmini.TIME_FUNCTION
title: TIME_FUNCTION
author: windows-driver-content
description: "."
old-location: stream\time_function.htm
old-project: stream
ms.assetid: 9335B3FB-B46B-404C-BCF9-F4E2F7A4C216
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: TIME_FUNCTION, stream.time_function, strmini/TIME_GET_STREAM_TIME, TIME_GET_STREAM_TIME, strmini/TIME_SET_ONBOARD_CLOCK, TIME_READ_ONBOARD_CLOCK, strmini/TIME_FUNCTION, TIME_FUNCTION enumeration [Streaming Media Devices], TIME_SET_ONBOARD_CLOCK, strmini/TIME_READ_ONBOARD_CLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: strmini.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Strmini.h
apiname:
-	TIME_FUNCTION
product: Windows
targetos: Windows
req.typenames: TIME_FUNCTION
req.product: Windows 10 or later.
---

# TIME_FUNCTION Enumeration


## Syntax
````
typedef enum  { 
  TIME_GET_STREAM_TIME,
  TIME_READ_ONBOARD_CLOCK,
  TIME_SET_ONBOARD_CLOCK
} TIME_FUNCTION;
````

## Constants

<table>
            
                <tr>
                    <td>TIME_GET_STREAM_TIME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>TIME_READ_ONBOARD_CLOCK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>TIME_SET_ONBOARD_CLOCK</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | strmini.h |