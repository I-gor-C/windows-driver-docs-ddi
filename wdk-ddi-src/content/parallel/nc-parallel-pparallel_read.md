---
UID : NC:parallel.PPARALLEL_READ
title : PPARALLEL_READ
author : windows-driver-content
description : The PPARALLEL_READ-typed callback routine reads data from a parallel device. The system-supplied bus driver for parallel ports supplies this routine.
old-location : parports\pparallel_read.htm
old-project : parports
ms.assetid : a478fd0d-3fbe-4cd9-aaf9-67b74b607770
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : RegisterOpRegionHandler
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : parallel.h
req.include-header : Parallel.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PPARALLEL_READ
req.alt-loc : parallel.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*LPRILGBATOKEN, RILGBATOKEN"
---


# PPARALLEL_READ callback function
The PPARALLEL_READ-typed callback routine reads data from a parallel device. The system-supplied bus driver for parallel ports supplies this routine.

## Syntax

```
PPARALLEL_READ PparallelRead;

NTSTATUS PparallelRead(
  PVOID Context,
  PVOID Buffer,
  ULONG NumBytesToRead,
  PULONG NumBytesRead,
  UCHAR Channel
)
{...}
```

## Parameters

`Context`

Pointer to the device extension of a parallel device's physical device object (<a href="wdkgloss.p#wdkgloss.pdo#wdkgloss.pdo"><i>PDO</i></a>).

`Buffer`

Pointer to a read buffer that the caller allocates.

`NumBytesToRead`

Specifies the number of bytes to read. Must less than or equal to the number of bytes in the caller-allocated read buffer.

`NumBytesRead`

Specifies the number of bytes that were actually read from the parallel device and saved in the caller-allocated read buffer.

`Channel`

Not used.


## Return Value

<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The requested data was successfully transferred from the device.
<dl>
<dt><b>STATUS_<i>Xxx</i></b></dt>
</dl>An internal operation resulted in an NTSTATUS error.

## Remarks

To obtain a pointer to the system-supplied PPARALLEL_READ callback, a kernel-mode driver uses an <a href="..\parallel\ni-parallel-ioctl_internal_parclass_connect.md">IOCTL_INTERNAL_PARCLASS_CONNECT</a> request, which returns a <a href="..\parallel\ns-parallel-_parclass_information.md">PARCLASS_INFORMATION</a> structure. The <b>ParallelRead</b> member of the PARCLASS_INFORMATION structure is a pointer to this callback.

A client can only use this routine if it has a lock on a parallel port. A client obtains a lock on a parallel port by using an <a href="..\parallel\ni-parallel-ioctl_internal_lock_port.md">IOCTL_INTERNAL_LOCK_PORT</a> request.

The PPARALLEL_READ callback runs in the caller's thread at the IRQL of the caller.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | parallel.h (include Parallel.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\parallel\ni-parallel-ioctl_internal_lock_port.md">IOCTL_INTERNAL_LOCK_PORT</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pparallel_write.md">PPARALLEL_WRITE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PPARALLEL_READ function pointer%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>