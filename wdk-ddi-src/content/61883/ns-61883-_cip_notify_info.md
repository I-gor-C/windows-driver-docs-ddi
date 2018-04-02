---
UID: NS:61883._CIP_NOTIFY_INFO
title: "_CIP_NOTIFY_INFO"
author: windows-driver-content
description: The CIP_NOTIFY_INFO structure contains information about the frame.
old-location: ieee\cip_notify_info.htm
old-project: IEEE
ms.assetid: 60b0d44b-0178-43ce-a1ad-7f5825bed3ba
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PCIP_NOTIFY_INFO, 61883/CIP_NOTIFY_INFO, 61883/PCIP_NOTIFY_INFO, 61883_structures_383bc74c-1168-4478-8284-b2724f9ec654.xml, CIP_NOTIFY_INFO, CIP_NOTIFY_INFO structure [Buses], IEEE.cip_notify_info, PCIP_NOTIFY_INFO, PCIP_NOTIFY_INFO structure pointer [Buses], _CIP_NOTIFY_INFO"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 61883.h
req.include-header: 61883.h
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
-	61883.h
api_name:
-	CIP_NOTIFY_INFO
product: Windows
targetos: Windows
req.typenames: CIP_NOTIFY_INFO, *PCIP_NOTIFY_INFO
---

# _CIP_NOTIFY_INFO structure
The CIP_NOTIFY_INFO structure contains information about the frame.

## Syntax
```
typedef struct _CIP_NOTIFY_INFO {
  HANDLE     hConnect;
  PVOID      Context;
  PCIP_FRAME Frame;
} *PCIP_NOTIFY_INFO, CIP_NOTIFY_INFO;
```

## Members


`hConnect`

A handle to the connection.

`Context`

Points to the context provided by the caller at <b>NotifyContext</b> in the input CIP_FRAME structure.

`Frame`

Points to the completed frame.

## Remarks
The IEC-61883 protocol driver allocates and initializes this structure from the input CIP_FRAME structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | 61883.h (include 61883.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537045">CIP_FRAME</a>