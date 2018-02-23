---
UID: NS:iddcx.IDARG_IN_QUERY_HWCURSOR
title: IDARG_IN_QUERY_HWCURSOR
author: windows-driver-content
description: Gives information about the cursor associated with the monitor.
old-location: display\idarg_in_query_hwcursor.htm
old-project: display
ms.assetid: 293364D0-0614-4780-B5E5-1115F084A8C6
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: PIDARG_IN_QUERY_HWCURSOR, display.idarg_in_query_hwcursor, iddcx/IDARG_IN_QUERY_HWCURSOR, PIDARG_IN_QUERY_HWCURSOR structure pointer [Display Devices], iddcx/PIDARG_IN_QUERY_HWCURSOR, IDARG_IN_QUERY_HWCURSOR structure [Display Devices], IDARG_IN_QUERY_HWCURSOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
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
-	iddcx.h
apiname:
-	IDARG_IN_QUERY_HWCURSOR
product: Windows
targetos: Windows
req.typenames: 
---

# IDARG_IN_QUERY_HWCURSOR structure
Gives information about the cursor associated with the monitor.

## Syntax
````
typedef struct _IDARG_IN_QUERY_HWCURSOR {
  IDDCX_MONITOR_DESCRIPTION                                   MonitorDescription;
  UINT                                                        TargetModeBufferInputCount;
  _Field_size_(TargetModeBufferInputCount) IDDCX_TARGET_MODE* pTargetModes;
} IDARG_IN_QUERY_HWCURSOR, *PIDARG_IN_QUERY_HWCURSOR;
````

## Members


`LastShapeId`



`pShapeBuffer`



`ShapeBufferSizeInBytes`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | iddcx.h |