---
UID: NS.parallel._PARCLASS_INFORMATION
title: PARCLASS_INFORMATION
author: windows-driver-content
description: The PARCLASS_INFORMATION structure specifies information about a parallel port, pointers to callback routines to operate a parallel port, and pointers to callback routines to read and write to a parallel device.
old-location: parports\parclass_information.htm
old-project: parports
ms.assetid: abad8ebd-a9fc-4cfb-8495-aca4e38ee45a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PARCLASS_INFORMATION, PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
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
req.alt-api: PARCLASS_INFORMATION
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

# PARCLASS_INFORMATION structure



## -description
<p>The PARCLASS_INFORMATION structure specifies information about a parallel port, pointers to callback routines to operate a parallel port, and pointers to callback routines to read and write to a parallel device.</p>


## -syntax

````
typedef struct _PARCLASS_INFORMATION {
  PUCHAR                    Controller;
  ULONG                     SpanOfController;
  PDETERMINE_IEEE_MODES     DetermineIeeeModes;
  PNEGOTIATE_IEEE_MODE      NegotiateIeeeMode;
  PTERMINATE_IEEE_MODE      TerminateIeeeMode;
  PPARALLEL_IEEE_FWD_TO_REV IeeeFwdToRevMode;
  PPARALLEL_IEEE_REV_TO_FWD IeeeRevToFwdMode;
  PPARALLEL_READ            ParallelRead;
  PPARALLEL_WRITE           ParallelWrite;
  PVOID                     ParclassContext;
  ULONG                     HardwareCapabilities;
  ULONG                     FifoDepth;
  ULONG                     FifoWidth;
} PARCLASS_INFORMATION, *PPARCLASS_INFORMATION;
````


## -struct-fields
<dl>

### -field Controller

<dd>
<p>Specifies the base I/O address allocated to a parallel port.</p>
</dd>

### -field SpanOfController

<dd>
<p>Specifies the range in bytes of I/O address space allocated to a parallel port.</p>
</dd>

### -field DetermineIeeeModes

<dd>
<p>Pointer to the <a href="..\parallel\nc-parallel-pdetermine-ieee-modes.md">PDETERMINE_IEEE_MODES</a> callback routine that determines which IEEE protocols a parallel device supports.</p>
</dd>

### -field NegotiateIeeeMode

<dd>
<p>Pointer to the <a href="..\parallel\nc-parallel-pnegotiate-ieee-mode.md">PNEGOTIATE_IEEE_MODE</a> callback routine that negotiates the fastest protocol that the system-supplied bus driver for parallel ports supports from among those specified by the caller.</p>
</dd>

### -field TerminateIeeeMode

<dd>
<p>Pointer to the <a href="..\parallel\nc-parallel-pterminate-ieee-mode.md">PTERMINATE_IEEE_MODE</a> callback routine that terminates the current IEEE mode and sets the mode to IEEE_COMPATIBILITY.</p>
</dd>

### -field IeeeFwdToRevMode

<dd>
<p>Pointer to the <a href="..\parallel\nc-parallel-pparallel-ieee-fwd-to-rev.md">PPARALLEL_IEEE_FWD_TO_REV</a> callback routine that changes the transfer mode from forward to reverse.</p>
</dd>

### -field IeeeRevToFwdMode

<dd>
<p>Pointer to the <a href="..\parallel\nc-parallel-pparallel-ieee-rev-to-fwd.md">PPARALLEL_IEEE_REV_TO_FWD</a> callback routine that changes the transfer mode from reverse to forward.</p>
</dd>

### -field ParallelRead

<dd>
<p>Pointer to the <a href="..\parallel\nc-parallel-pparallel-read.md">PPARALLEL_READ</a> callback routine that a client can use to read from a parallel device.</p>
</dd>

### -field ParallelWrite

<dd>
<p>Pointer to the <a href="..\parallel\nc-parallel-pparallel-write.md">PPARALLEL_WRITE</a> callback routine that a client can use to write to a parallel device.</p>
</dd>

### -field ParclassContext

<dd>
<p>Pointer to the device extension of a parallel device's physical device object (<a href="wdkgloss.p#wdkgloss.pdo#wdkgloss.pdo"><i>PDO</i></a>).</p>
</dd>

### -field HardwareCapabilities

<dd>
<p>Specifies which hardware capabilities are present. <b>HardwareCapabilities</b> is a bitwise OR of one or more of the following flags:</p>
<p></p>
<dl>

### -field PPT_NO_HARDWARE_PRESENT

<dd></dd>

### -field PPT_ECP_PRESENT

<dd></dd>

### -field PPT_EPP_PRESENT 

<dd></dd>

### -field PPT_EPP_32_PRESENT

<dd>
<p>32-bit reads and writes are supported.</p>
</dd>

### -field PPT_BYTE_PRESENT

<dd></dd>

### -field PPT_BIDI_PRESENT

<dd></dd>

### -field PPT_1284_3_PRESENT

<dd></dd>
</dl>
</dd>

### -field FifoDepth

<dd>
<p>Specifies the size, in words, of the ECP FIFO. The ECP FIFO word size, in bits, is the value of <b>FifoWidth</b>.</p>
</dd>

### -field FifoWidth

<dd>
<p>Specifies the ECP FIFO word size, in bits, which is the number of bits handled in parallel.</p>
</dd>
</dl>

## -remarks
<p>A kernel-mode driver can obtain this information from the system-supplied bus driver for parallel ports using an <a href="..\parallel\ni-parallel-ioctl-internal-parclass-connect.md">IOCTL_INTERNAL_PARCLASS_CONNECT</a> request. The system-supplied bus driver for parallel ports supplies all the callback routines. </p>

<p>A client uses this information to operate a parallel port and to read and write a parallel device. The callback routines can only be used by a driver that holds a lock on the parent parallel port. A driver obtains a lock by using an <a href="..\parallel\ni-parallel-ioctl-internal-lock-port.md">IOCTL_INTERNAL_LOCK_PORT</a> request.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/c05a1a1e-308a-4b9f-af43-761c4c14d6af">Connecting to a Parallel Device</a>.</p>

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
<a href="..\parallel\ni-parallel-ioctl-internal-parclass-connect.md">IOCTL_INTERNAL_PARCLASS_CONNECT</a>
</dt>
<dt>
<a href="..\parallel\ni-parallel-ioctl-internal-lock-port.md">IOCTL_INTERNAL_LOCK_PORT</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pdetermine-ieee-modes.md">PDETERMINE_IEEE_MODES</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pnegotiate-ieee-mode.md">PNEGOTIATE_IEEE_MODE</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pparallel-ieee-fwd-to-rev.md">PPARALLEL_IEEE_FWD_TO_REV</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pparallel-ieee-rev-to-fwd.md">PPARALLEL_IEEE_REV_TO_FWD</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pparallel-read.md">PPARALLEL_READ</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pparallel-write.md">PPARALLEL_WRITE</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pterminate-ieee-mode.md">PTERMINATE_IEEE_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PARCLASS_INFORMATION structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
