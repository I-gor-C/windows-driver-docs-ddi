---
UID: NS.parallel._PARALLEL_PORT_INFORMATION
title: PARALLEL_PORT_INFORMATION
author: windows-driver-content
description: The PARALLEL_PORT_INFORMATION structure specifies information about the resources assigned to a parallel port, the capabilities of the parallel port, and pointers to callback routines that a kernel-mode driver can use to operate the parallel port.
old-location: parports\parallel_port_information.htm
old-project: parports
ms.assetid: 9f170425-2c65-469e-adae-e845b11b9c8e
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: PARALLEL_PORT_INFORMATION, PARALLEL_PORT_INFORMATION, *PPARALLEL_PORT_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: parallel.h
req.include-header: Parallel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PARALLEL_PORT_INFORMATION
req.alt-loc: parallel.h
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
req.iface: 
---

# PARALLEL_PORT_INFORMATION structure



## -description
<p>The PARALLEL_PORT_INFORMATION structure specifies information about the resources assigned to a parallel port, the capabilities of the parallel port, and pointers to callback routines that a kernel-mode driver can use to operate the parallel port.</p>


## -syntax

````
typedef struct _PARALLEL_PORT_INFORMATION {
  PHYSICAL_ADDRESS                OriginalController;
  PUCHAR                          Controller;
  ULONG                           SpanOfController;
  PPARALLEL_TRY_ALLOCATE_ROUTINE  TryAllocatePort;
  PPARALLEL_FREE_ROUTINE          FreePort;
  PPARALLEL_QUERY_WAITERS_ROUTINE QueryNumWaiters;
  PVOID                           Context;
} PARALLEL_PORT_INFORMATION, *PPARALLEL_PORT_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>OriginalController</b>

<dd>
<p>Specifies the bus relative base I/O address of the parallel port registers. </p>
</dd>

### -field <b>Controller</b>

<dd>
<p>Pointer to the system-mapped base I/O location of the parallel port registers.</p>
</dd>

### -field <b>SpanOfController</b>

<dd>
<p>Specifies the size, in bytes, of the I/O space, allocated to the parallel port.</p>
</dd>

### -field <b>TryAllocatePort</b>

<dd>
<p>Pointer to the system-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff544550">PPARALLEL_TRY_ALLOCATE_ROUTINE</a> callback that a kernel-mode driver can use to attempt to allocate the parallel port.</p>
</dd>

### -field <b>FreePort</b>

<dd>
<p>Pointer to the system-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff544509">PPARALLEL_FREE_ROUTINE</a> callback that a kernel-mode driver can use to free the parallel port. </p>
</dd>

### -field <b>QueryNumWaiters</b>

<dd>
<p>Pointer to the system-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff544532">PPARALLEL_QUERY_WAITERS_ROUTINE</a> callback that a kernel-mode driver can use to determine the number of requests on the work queue of the parallel port.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>Pointer to the device extension of parallel port.</p>
</dd>
</dl>

## -remarks
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a> request from the Plug and Play manager passes a translated resource list that contains the port information in a PARALLEL_PORT_INFORMATION structure. The system-supplied function driver for parallel ports saves the information in the extension of the parallel port and returns the information in response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544002">IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO</a> request.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/d8ae2296-05b6-419a-93cc-00fcb12d41fe">Obtaining Information About a ParallelPort</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Parallel.h (include Parallel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543996">IOCTL_INTERNAL_GET_MORE_PARALLEL_PORT_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543997">IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544002">IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544207">MORE_PARALLEL_PORT_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544299">PARALLEL_PNP_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544509">PPARALLEL_FREE_ROUTINE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544532">PPARALLEL_QUERY_WAITERS_ROUTINE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544550">PPARALLEL_TRY_ALLOCATE_ROUTINE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PARALLEL_PORT_INFORMATION structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
