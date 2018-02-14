---
UID: NC:parallel.PPARALLEL_WRITE
title: PPARALLEL_WRITE
author: windows-driver-content
description: The PPARALLEL_WRITE-typed callback routine writes data to a parallel device. The system-supplied bus driver for parallel ports supplies this routine.
old-location: parports\pparallel_write.htm
old-project: parports
ms.assetid: 4973b1e2-5828-40d1-bb2e-da67a406eafa
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: parports.pparallel_write, PPARALLEL_WRITE function pointer [Parallel Ports], PPARALLEL_WRITE, parallel/PPARALLEL_WRITE, cisspd_c9bcb3ed-ca6a-44d7-8952-f96f76490262.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: parallel.h
req.include-header: Parallel.h
req.target-type: Desktop
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
-	UserDefined
apilocation:
-	parallel.h
apiname:
-	PPARALLEL_WRITE
product: Windows
targetos: Windows
req.typenames: "*LPRILGBATOKEN, RILGBATOKEN"
---


# PPARALLEL_WRITE callback function
The PPARALLEL_WRITE-typed callback routine writes data to a parallel device. The system-supplied bus driver for parallel ports supplies this routine.

## Syntax

```
PPARALLEL_WRITE PparallelWrite;

NTSTATUS PparallelWrite(
  PVOID Context,
  PVOID Buffer,
  ULONG NumBytesToWrite,
  PULONG NumBytesWritten,
  UCHAR Channel
)
{...}
```

## Parameters

`Context`

Pointer to the device extension of a parallel device's physical device object (<a href="https://msdn.microsoft.com/139a10e9-203b-499b-9291-8537eae9189c">PDO</a>).

`Buffer`

Pointer to a caller-allocated write buffer.

`NumBytesToWrite`

Specifies the number of bytes to copy from the write buffer to the parallel device. Must be less than or equal to the number of bytes in the caller-allocated write buffer.

`NumBytesWritten`

Specifies the number of bytes that were actually copied from the caller-allocated write buffer to the parallel device.

`Channel`

Not used.


## Return Value

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The caller-supplied data was successfully transferred to the device.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_<i>Xxx</i></b></dt>
</dl>
</td>
<td width="60%">
An internal operation resulted in an NTSTATUS error.

</td>
</tr>
</table>

## Remarks

To obtain a pointer to the system-supplied PPARALLEL_WRITE callback, a kernel-mode driver uses an <a href="..\parallel\ni-parallel-ioctl_internal_parclass_connect.md">IOCTL_INTERNAL_PARCLASS_CONNECT</a> request, which returns a <a href="..\parallel\ns-parallel-_parclass_information.md">PARCLASS_INFORMATION</a> structure. The <b>ParallelWrite</b> member of the PARCLASS_INFORMATION structure is a pointer to this callback.

A client can only use this routine if it has a lock on a parallel port. A client obtains a lock on a parallel port by using an <a href="..\parallel\ni-parallel-ioctl_internal_lock_port.md">IOCTL_INTERNAL_LOCK_PORT</a> request.

The PPARALLEL_WRITE callback runs in the caller's thread at the IRQL of the caller.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | parallel.h (include Parallel.h) |

## See Also

<a href="..\parallel\nc-parallel-pparallel_read.md">PPARALLEL_READ</a>



<a href="..\parallel\ni-parallel-ioctl_internal_lock_port.md">IOCTL_INTERNAL_LOCK_PORT</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PPARALLEL_WRITE function pointer%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>