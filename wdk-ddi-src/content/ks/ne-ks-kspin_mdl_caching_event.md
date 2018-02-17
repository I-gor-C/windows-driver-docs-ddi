---
UID: NE:ks.KSPIN_MDL_CACHING_EVENT
title: KSPIN_MDL_CACHING_EVENT
author: windows-driver-content
description: This enumeration is used internally by the operating system.
old-location: stream\kspin_mdl_caching_event.htm
old-project: stream
ms.assetid: 74A7C2C8-F12B-4753-8E1F-C425B0B56788
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: ks/KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE, KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT, KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE, KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT, KSPIN_MDL_CACHING_EVENT, ks/KSPIN_MDL_CACHING_EVENT, ks/KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT, stream.kspin_mdl_caching_event, KSPIN_MDL_CACHING_NOTIFY_CLEANUP, ks/KSPIN_MDL_CACHING_NOTIFY_CLEANUP, ks/KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT, KSPIN_MDL_CACHING_EVENT enumeration [Streaming Media Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
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
-	ks.h
apiname:
-	KSPIN_MDL_CACHING_EVENT
product: Windows
targetos: Windows
req.typenames: KSPIN_MDL_CACHING_EVENT
---

# KSPIN_MDL_CACHING_EVENT Enumeration
This enumeration is used internally by the operating system.

## Syntax
````
typedef enum  { 
  KSPIN_MDL_CACHING_NOTIFY_CLEANUP,
  KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT,
  KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT,
  KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE
} KSPIN_MDL_CACHING_EVENT;
````

## Constants

<table>
            
                <tr>
                    <td>KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE</td>
                    <td>This value is used internally by the operating system.</td>
                </tr>
            
                <tr>
                    <td>KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT</td>
                    <td>This value is used internally by the operating system.</td>
                </tr>
            
                <tr>
                    <td>KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT</td>
                    <td>This value is used internally by the operating system.</td>
                </tr>
            
                <tr>
                    <td>KSPIN_MDL_CACHING_NOTIFY_CLEANUP</td>
                    <td>This value is used internally by the operating system.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h |