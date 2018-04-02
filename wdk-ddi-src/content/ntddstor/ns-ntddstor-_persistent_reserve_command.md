---
UID: NS:ntddstor._PERSISTENT_RESERVE_COMMAND
title: "_PERSISTENT_RESERVE_COMMAND"
author: windows-driver-content
description: The PERSISTENT_RESERVE_COMMAND structure is used together with the IOCTL_STORAGE_PERSISTENT_RESERVE_IN and IOCTL_STORAGE_PERSISTENT_RESERVE_OUT requests to obtain and control information about persistent reservations and reservation keys that are active within a device server.
old-location: storage\persistent_reserve_command.htm
old-project: storage
ms.assetid: c7debd93-0fcd-43c5-a950-8154b62175bf
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PPERSISTENT_RESERVE_COMMAND, PERSISTENT_RESERVE_COMMAND, PERSISTENT_RESERVE_COMMAND structure [Storage Devices], PPERSISTENT_RESERVE_COMMAND, PPERSISTENT_RESERVE_COMMAND structure pointer [Storage Devices], _PERSISTENT_RESERVE_COMMAND, ntddstor/PERSISTENT_RESERVE_COMMAND, ntddstor/PPERSISTENT_RESERVE_COMMAND, storage.persistent_reserve_command, structs-general_4fe3d6f6-6e9f-41f5-915c-2636707f429c.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
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
-	ntddstor.h
api_name:
-	PERSISTENT_RESERVE_COMMAND
product: Windows
targetos: Windows
req.typenames: PERSISTENT_RESERVE_COMMAND, *PPERSISTENT_RESERVE_COMMAND
---

# _PERSISTENT_RESERVE_COMMAND structure
The PERSISTENT_RESERVE_COMMAND structure is used together with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560582">IOCTL_STORAGE_PERSISTENT_RESERVE_IN</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff560586">IOCTL_STORAGE_PERSISTENT_RESERVE_OUT</a> requests to obtain and control information about persistent reservations and reservation keys that are active within a device server.

## Syntax
```
typedef struct _PERSISTENT_RESERVE_COMMAND {
  ULONG Version;
  ULONG Size;
  union {
    struct {
      UCHAR  : 5 ServiceAction;
      UCHAR  : 3 Reserved1;
      USHORT     AllocationLength;
    } PR_IN;
    struct {
      UCHAR  : 5 ServiceAction;
      UCHAR  : 3 Reserved1;
      UCHAR  : 4 Type;
      UCHAR  : 4 Scope;
      UCHAR      ParameterList[0];
    } PR_OUT;
  } DUMMYUNIONNAME;
} PERSISTENT_RESERVE_COMMAND, *PPERSISTENT_RESERVE_COMMAND;
```

## Members


`Version`

The version of this structure.

`Size`

The size of this structure.

`DUMMYUNIONNAME`



## Remarks
The behavior of the storage device when a SCSI Persistent Reserve In command or a SCSI Persistent Reserve Out command is received is described in the <a href="http://go.microsoft.com/fwlink/p/?linkid=153142">SCSI Primary Commands - 2 (SPC-2)</a> specification.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddstor.h (include Ntddstor.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560582">IOCTL_STORAGE_PERSISTENT_RESERVE_IN</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560586">IOCTL_STORAGE_PERSISTENT_RESERVE_OUT</a>