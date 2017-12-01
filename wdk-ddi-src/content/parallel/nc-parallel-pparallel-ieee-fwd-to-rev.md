---
UID: NC.parallel.PPARALLEL_IEEE_FWD_TO_REV
title: PPARALLEL_IEEE_FWD_TO_REV
author: windows-driver-content
description: The PPARALLEL_IEEE_FWD_TO_REV-typed callback routine changes the transfer mode from forward to reverse. The system-supplied bus driver for parallel ports supplies this routine.
old-location: parports\pparallel_ieee_fwd_to_rev.htm
old-project: parports
ms.assetid: cb7e01e3-7aff-436c-af82-bc7716d2fe1f
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: RegisterOpRegionHandler
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
req.alt-api: PPARALLEL_IEEE_FWD_TO_REV
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

# PPARALLEL_IEEE_FWD_TO_REV callback



## -description
<p>The PPARALLEL_IEEE_FWD_TO_REV-typed callback routine changes the transfer mode from forward to reverse. The system-supplied bus driver for parallel ports supplies this routine.</p>


## -prototype

````
typedef NTSTATUS ( *PPARALLEL_IEEE_FWD_TO_REV)(
  _In_ PVOID Context
);
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>Pointer to a device extension of a parallel device's physical device object (<a href="wdkgloss.p#wdkgloss.pdo#wdkgloss.pdo"><i>PDO</i></a>).</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The transfer mode was changed from forward to reverse.</p><dl>
<dt><b>STATUS_<i>Xxx</i></b></dt>
</dl><p>An internal operation resulted in an NTSTATUS error.</p>

<p> </p>

## -remarks
<p>To obtain a pointer to the system-supplied PPARALLEL_IEEE_FWD_TO_REV callback, a kernel-mode driver uses an <a href="..\parallel\ni-parallel-ioctl-internal-parclass-connect.md">IOCTL_INTERNAL_PARCLASS_CONNECT</a> request, which returns a <a href="..\parallel\ns-parallel--parclass-information.md">PARCLASS_INFORMATION</a> structure. The <b>IeeeFwdToRevMode</b> member of the PARCLASS_INFORMATION structure is a pointer to this callback.</p>

<p>If the device is connected and in the reverse mode, the PPARALLEL_IEEE_FWD_TO_REV callback returns without further processing. Otherwise, the callback puts the parallel device into reverse mode and connects a previously negotiated reverse protocol. The <a href="..\parallel\nc-parallel-pnegotiate-ieee-mode.md">PNEGOTIATE_IEEE_MODE</a> callback can be used to negotiate the reverse protocol.</p>

<p>The PPARALLEL_IEEE_FWD_TO_REV callback runs in the caller's thread at the caller's IRQL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<a href="..\ntddpar\ni-ntddpar-ioctl-ieee1284-get-mode.md">IOCTL_IEEE1284_GET_MODE</a>
</dt>
<dt>
<a href="..\ntddpar\ni-ntddpar-ioctl-ieee1284-negotiate.md">IOCTL_IEEE1284_NEGOTIATE</a>
</dt>
<dt>
<a href="..\ntddpar\ni-ntddpar-ioctl-par-get-default-modes.md">IOCTL_PAR_GET_DEFAULT_MODES</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pdetermine-ieee-modes.md">PDETERMINE_IEEE_MODES</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pnegotiate-ieee-mode.md">PNEGOTIATE_IEEE_MODE</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pparallel-ieee-rev-to-fwd.md">PPARALLEL_IEEE_REV_TO_FWD</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pterminate-ieee-mode.md">PTERMINATE_IEEE_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PPARALLEL_IEEE_FWD_TO_REV function pointer%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
