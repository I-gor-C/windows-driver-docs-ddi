---
UID: NE:pointofservicedriverinterface._MsrTrackErrorType
title: "_MsrTrackErrorType"
author: windows-driver-content
description: This enumeration defines the kinds of magnetic stripe reader track errors.
old-location: pos\msrtrackerrortype.htm
old-project: pos
ms.assetid: 2abd9341-527f-43af-baa2-622b759b47cd
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: MsrTrackErrorType_EndSentinelError, MsrTrackErrorType_StartSentinelError, MsrTrackErrorType_ParityError, pointofservicedriverinterface/MsrTrackErrorType_Unknown, pos.msrtrackerrortype, pointofservicedriverinterface/MsrTrackErrorType_None, pointofservicedriverinterface/MsrTrackErrorType_ParityError, MsrTrackErrorType_None, pointofservicedriverinterface/MsrTrackErrorType_LrcError, MsrTrackErrorType, MsrTrackErrorType_LrcError, pointofservicedriverinterface/MsrTrackErrorType_EndSentinelError, _MsrTrackErrorType, pointofservicedriverinterface/MsrTrackErrorType, pointofservicedriverinterface/MsrTrackErrorType_StartSentinelError, MsrTrackErrorType_Unknown, MsrTrackErrorType enumeration
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	pointofservicedriverinterface.h
apiname:
-	MsrTrackErrorType
product: Windows
targetos: Windows
req.typenames: MsrTrackErrorType
---

# _MsrTrackErrorType Enumeration
This enumeration defines the kinds of magnetic stripe reader track errors.

## Syntax
````
typedef enum _MsrTrackErrorType { 
  MsrTrackErrorType_Unknown             = -1,
  MsrTrackErrorType_None                = 0,
  MsrTrackErrorType_StartSentinelError  = 1,
  MsrTrackErrorType_EndSentinelError    = 2,
  MsrTrackErrorType_ParityError         = 3,
  MsrTrackErrorType_LrcError            = 4
} MsrTrackErrorType;
````

## Constants

<table>
            
                <tr>
                    <td>MsrTrackErrorType_EndSentinelError</td>
                    <td>An end sentinel error.</td>
                </tr>
            
                <tr>
                    <td>MsrTrackErrorType_LrcError</td>
                    <td>A Longitudinal Redundancy Check (LRC) or checksum error.</td>
                </tr>
            
                <tr>
                    <td>MsrTrackErrorType_None</td>
                    <td>No error occurred.</td>
                </tr>
            
                <tr>
                    <td>MsrTrackErrorType_ParityError</td>
                    <td>A parity error.</td>
                </tr>
            
                <tr>
                    <td>MsrTrackErrorType_StartSentinelError</td>
                    <td>A start sentinel error.</td>
                </tr>
            
                <tr>
                    <td>MsrTrackErrorType_Unknown</td>
                    <td>An unspecified error.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |