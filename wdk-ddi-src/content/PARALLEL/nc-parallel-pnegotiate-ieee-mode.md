---
UID: NC.parallel.PNEGOTIATE_IEEE_MODE
title: PNEGOTIATE_IEEE_MODE
author: windows-driver-content
description: The PNEGOTIATE_IEEE_MODE-typed callback routine selects the fastest forward and reverse protocols that the system-supplied bus driver for parallel ports supports from among those specified by the caller.
old-location: parports\pnegotiate_ieee_mode.htm
ms.assetid: 2cf3564e-10aa-49bb-9b94-abd987870196
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: parports
req.header: parallel.h
req.include-header: Parallel.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PNEGOTIATE_IEEE_MODE
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
ms.keywords: RegisterOpRegionHandler
req.iface: 
---

# PNEGOTIATE_IEEE_MODE callback



## -description
<p>The PNEGOTIATE_IEEE_MODE-typed callback routine selects the fastest forward and reverse protocols that the system-supplied bus driver for parallel ports supports from among those specified by the caller. The system-supplied bus driver for parallel ports supplies this routine.</p>


## -prototype

````
typedef NTSTATUS  ( *PNEGOTIATE_IEEE_MODE)(
  _In_ PVOID           Context,
  _In_ USHORT          ModeMaskFwd,
  _In_ USHORT          ModeMaskRev,
  _In_ PARALLEL_SAFETY ModeSafety,
  _In_ BOOLEAN         IsForward
);
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>Pointer to the device extension of a parallel device's physical device object (<a href="wdkgloss.p#wdkgloss.pdo#wdkgloss.pdo"><i>PDO</i></a>).</p>
</dd>

### -param <i>ModeMaskFwd</i> [in]

<dd>
<p>Specifies the forward protocols. <i>ModeMaskFwd</i> is a bitwise OR of the constants that represent the protocols that the parallel port bus driver supports. For the forward and reverse protocol values, see the protocol constants defined in <i>ntddpar.h</i> (from NONE to ECP_ANY).</p>
</dd>

### -param <i>ModeMaskRev</i> [in]

<dd>
<p>Specifies the reverse protocols. <i>ModeMaskRev </i>is a bitwise OR of the constants that represent the protocols that the parallel port bus driver supports.</p>
</dd>

### -param <i>ModeSafety</i> [in]

<dd>
<p>Specifies the safety mode. Must be set to the SAFE_MODE enumeration value of the PARALLEL_SAFETY enumeration type:</p>
<pre class="syntax" xml:space="preserve"><code>typedef enum {
  SAFE_MODE,
  UNSAFE_MODE
} PARALLEL_SAFETY;</code></pre>
</dd>

### -param <i>IsForward</i> [in]

<dd>
<p>Specifies whether to connect the forward or the reverse protocol that the routine negotiates. If <i>IsForward</i> is <b>TRUE</b>, the forward protocol is connected. Otherwise, the reverse protocol is connected.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESSFUL</b></dt>
</dl><p>The IEEE mode was successfully negotiated.</p><dl>
<dt><b>STATUS_DEVICE_PROTOCOL_ERROR</b></dt>
</dl><p>An IEEE mode is already set on the device.</p><dl>
<dt><b>STATUS_<i>Xxx</i></b></dt>
</dl><p>An internal operation resulted in an NTSTATUS error.</p>

<p> </p>

## -remarks
<p>To obtain a pointer to the system-supplied PNEGOTIATE_IEEE_MODE callback, a kernel-mode driver uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544040">IOCTL_INTERNAL_PARCLASS_CONNECT</a> request, which returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure. The <b>NegotiateIeeeMode</b> member of the PARCLASS_INFORMATION structure is a pointer to this callback.</p>

<p>The PNEGOTIATE_IEEE_MODE callback runs in the caller's thread at the IRQL of the caller.</p>

<p>To obtain a pointer to the system-supplied PNEGOTIATE_IEEE_MODE callback, a kernel-mode driver uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544040">IOCTL_INTERNAL_PARCLASS_CONNECT</a> request, which returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure. The <b>NegotiateIeeeMode</b> member of the PARCLASS_INFORMATION structure is a pointer to this callback.</p>

<p>The PNEGOTIATE_IEEE_MODE callback runs in the caller's thread at the IRQL of the caller.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543975">IOCTL_IEEE1284_GET_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543978">IOCTL_IEEE1284_NEGOTIATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544061">IOCTL_PAR_GET_DEFAULT_MODES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544365">PDETERMINE_IEEE_MODES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544524">PPARALLEL_IEEE_FWD_TO_REV</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544528">PPARALLEL_IEEE_REV_TO_FWD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544773">PTERMINATE_IEEE_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PNEGOTIATE_IEEE_MODE function pointer%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
