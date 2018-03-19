---
UID: NE:strmini.STREAM_DEBUG_LEVEL
title: STREAM_DEBUG_LEVEL
author: windows-driver-content
description: The STREAM_DEBUG_LEVEL enumeration lists incrementally increasing levels of debugger output.
old-location: stream\stream_debug_level.htm
old-project: stream
ms.assetid: 42d70c1f-5cce-4097-849d-a5aa05b669b5
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: DebugLevelError, DebugLevelFatal, DebugLevelInfo, DebugLevelMaximum, DebugLevelTrace, DebugLevelVerbose, DebugLevelWarning, STREAM_DEBUG_LEVEL, STREAM_DEBUG_LEVEL enumeration [Streaming Media Devices], ks-struct_9820cc1d-0d8b-43a8-b1a2-bca3f8a23d22.xml, stream.stream_debug_level, strmini/DebugLevelError, strmini/DebugLevelFatal, strmini/DebugLevelInfo, strmini/DebugLevelMaximum, strmini/DebugLevelTrace, strmini/DebugLevelVerbose, strmini/DebugLevelWarning, strmini/STREAM_DEBUG_LEVEL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: strmini.h
req.include-header: Strmini.h
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
-	strmini.h
api_name:
-	STREAM_DEBUG_LEVEL
product: Windows
targetos: Windows
req.typenames: STREAM_DEBUG_LEVEL
req.product: Windows 10 or later.
---

# STREAM_DEBUG_LEVEL Enumeration
The STREAM_DEBUG_LEVEL enumeration lists incrementally increasing levels of debugger output.

## Syntax
````
typedef enum  { 
  DebugLevelFatal    = 0,
  DebugLevelError    = 1,
  DebugLevelWarning  = 2,
  DebugLevelInfo     = 3,
  DebugLevelTrace    = 4,
  DebugLevelVerbose  = 5,
  DebugLevelMaximum  = 6
} STREAM_DEBUG_LEVEL;
````

## Constants

<table>
            
                <tr>
                    <td>DebugLevelFatal</td>
                    <td>Display only information about nonrecoverable system failure.</td>
                </tr>
            
                <tr>
                    <td>DebugLevelError</td>
                    <td>Display information about serious but recoverable error.</td>
                </tr>
            
                <tr>
                    <td>DebugLevelWarning</td>
                    <td>Display warnings</td>
                </tr>
            
                <tr>
                    <td>DebugLevelInfo</td>
                    <td>Display status information. System must remain responsive.</td>
                </tr>
            
                <tr>
                    <td>DebugLevelTrace</td>
                    <td>Display trace information. System need not remain responsive</td>
                </tr>
            
                <tr>
                    <td>DebugLevelVerbose</td>
                    <td>Display verbose trace information. System need not remain responsive.</td>
                </tr>
            
                <tr>
                    <td>DebugLevelMaximum</td>
                    <td>Display maximum information.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | strmini.h (include Strmini.h) |

## See Also

<a href="..\strmini\nf-strmini-streamclassdebugprint.md">StreamClassDebugPrint</a>