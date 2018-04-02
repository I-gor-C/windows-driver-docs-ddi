---
UID: NS:ks.KSDISPATCH_TABLE
title: KSDISPATCH_TABLE
author: windows-driver-content
description: The KSDISPATCH_TABLE structure contains pointers to minidriver implemented IRP dispatch routines.
old-location: stream\ksdispatch_table.htm
old-project: stream
ms.assetid: baa45ce7-3dcd-4383-99f2-aeb664a03190
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKSDISPATCH_TABLE, KSDISPATCH_TABLE, KSDISPATCH_TABLE structure [Streaming Media Devices], PKSDISPATCH_TABLE, PKSDISPATCH_TABLE structure pointer [Streaming Media Devices], ks-struct_c1daf962-90e2-495e-9531-c23716ee9d68.xml, ks/KSDISPATCH_TABLE, ks/PKSDISPATCH_TABLE, stream.ksdispatch_table"
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
-	KSDISPATCH_TABLE
product: Windows
targetos: Windows
req.typenames: KSDISPATCH_TABLE, *PKSDISPATCH_TABLE
---

# KSDISPATCH_TABLE structure
The KSDISPATCH_TABLE structure contains pointers to minidriver implemented IRP dispatch routines.

## Syntax
```
typedef struct KSDISPATCH_TABLE {
  PDRIVER_DISPATCH        DeviceIoControl;
  PDRIVER_DISPATCH        Read;
  PDRIVER_DISPATCH        Write;
  PDRIVER_DISPATCH        Flush;
  PDRIVER_DISPATCH        Close;
  PDRIVER_DISPATCH        QuerySecurity;
  PDRIVER_DISPATCH        SetSecurity;
  PFAST_IO_DEVICE_CONTROL FastDeviceIoControl;
  PFAST_IO_READ           FastRead;
  PFAST_IO_WRITE          FastWrite;
} *PKSDISPATCH_TABLE, KSDISPATCH_TABLE;
```

## Members


`DeviceIoControl`

Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a> IRPs to.

`Read`

Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> IRPs to.

`Write`

Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a> IRPs to.

`Flush`

Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff549235">IRP_MJ_FLUSH_BUFFERS</a> IRPs to.

`Close`

Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> IRPs to.

`QuerySecurity`

Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff549298">IRP_MJ_QUERY_SECURITY</a> IRPs to.

`SetSecurity`

Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff549407">IRP_MJ_SET_SECURITY</a> IRPs to.

`FastDeviceIoControl`

Specifies the minidriver's routine to dispatch fast device I/O control requests to.

`FastRead`

Specifies the minidriver's routine to dispatch fast read requests to.

`FastWrite`

Specifies the minidriver's routine to dispatch fast write requests to.

## Remarks
A pointer to a dispatch table is contained in the opaque object header that is the first element of data pointed to by the file object's <b>FsContext</b> field.

For more information about minidriver implemented IRP dispatch routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566840">KsSetMajorFunctionHandler</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566840">KsSetMajorFunctionHandler</a>