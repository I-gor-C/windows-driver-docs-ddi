---
UID: NC.parallel.PDETERMINE_IEEE_MODES
title: PDETERMINE_IEEE_MODES
author: windows-driver-content
description: The PDETERMINE_IEEE_MODES-typed callback routine determines which IEEE 1284 protocols a parallel device supports. The system-supplied bus driver for parallel ports supplies this routine.
old-location: parports\pdetermine_ieee_modes.htm
old-project: parports
ms.assetid: 9f57337b-20b8-4aa6-a303-0972cd0c92cf
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: PDETERMINE_IEEE_MODES
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

# PDETERMINE_IEEE_MODES callback



## -description
<p>The PDETERMINE_IEEE_MODES-typed callback routine determines which IEEE 1284 protocols a parallel device supports. The system-supplied bus driver for parallel ports supplies this routine.</p>


## -prototype

````
typedef USHORT ( *PDETERMINE_IEEE_MODES)(
  _In_ PVOID Context
);
````


## -parameters
<dl>

### -param Context [in]

<dd>
<p>Pointer to a device extension of a parallel device's physical device object (<a href="wdkgloss.p#wdkgloss.pdo#wdkgloss.pdo"><i>PDO</i></a>).</p>
</dd>
</dl>

## -returns
<p>The return value indicates which protocols a parallel device supports. The return value is a bitwise OR of one or more of the following constants that represent the protocols that are supported by the system-supplied bus driver for parallel ports. The protocol constants are listed in order of decreasing data transfer rate.</p><dl>
<dd>
<p>BOUNDED_ECP</p>
</dd>
<dd>
<p>ECP_HW_NOIRQ</p>
</dd>
<dd>
<p>EPP_HW </p>
</dd>
<dd>
<p>EPP_SW</p>
</dd>
<dd>
<p>ECP_SW</p>
</dd>
<dd>
<p>IEEE_COMPATIBILITY</p>
</dd>
<dd>
<p>CENTRONICS</p>
</dd>
<dd>
<p>NONE</p>
</dd>
</dl><p>BOUNDED_ECP</p>

<p>ECP_HW_NOIRQ</p>

<p>EPP_HW </p>

<p>EPP_SW</p>

<p>ECP_SW</p>

<p>IEEE_COMPATIBILITY</p>

<p>CENTRONICS</p>

<p>NONE</p>

## -remarks
<p>To obtain a pointer to the system-supplied PDETERMINE_IEEE_MODES callback, a kernel-mode driver uses an <a href="..\parallel\ni-parallel-ioctl-internal-parclass-connect.md">IOCTL_INTERNAL_PARCLASS_CONNECT</a> request, which returns a <a href="..\parallel\ns-parallel--parclass-information.md">PARCLASS_INFORMATION</a> structure. The <b>DetermineIeeeModes</b> member of the PARCLASS_INFORMATION structure is a pointer to this callback.</p>

<p>The PDETERMINE_IEEE_MODES callback runs in the caller's thread at the IRQL of the caller.</p>

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
<a href="..\parallel\nc-parallel-pnegotiate-ieee-mode.md">PNEGOTIATE_IEEE_MODE</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pparallel-ieee-fwd-to-rev.md">PPARALLEL_IEEE_FWD_TO_REV</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PDETERMINE_IEEE_MODES function pointer%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
