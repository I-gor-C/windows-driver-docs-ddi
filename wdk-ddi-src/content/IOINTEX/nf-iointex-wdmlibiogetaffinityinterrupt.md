---
UID: NF.iointex.WdmlibIoGetAffinityInterrupt
title: WdmlibIoGetAffinityInterrupt
author: windows-driver-content
description: The WdmlibIoGetAffinityInterrupt function gets the group affinity of an interrupt object.
old-location: kernel\wdmlibiogetaffinityinterrupt.htm
ms.assetid: E9E80EB4-C20B-4025-957B-32DC6FAE7F38
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: iointex.h
req.include-header: Iointex.h, Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WdmlibIoGetAffinityInterrupt,IoGetAffinityInterrupt
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
ms.keywords: WdmlibIoGetAffinityInterrupt
req.iface: 
---

# WdmlibIoGetAffinityInterrupt function



## -description
<p>The <b>WdmlibIoGetAffinityInterrupt</b> function gets the group affinity of an interrupt object. </p>


## -syntax

````
NTSTATUS WdmlibIoGetAffinityInterrupt(
  _In_  PKINTERRUPT     InterruptObject,
  _Out_ PGROUP_AFFINITY GroupAffinity
);
````


## -parameters
<dl>

### -param <i>InterruptObject</i> [in]

<dd>
<p>A pointer to an interrupt object. This parameter points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554237">KINTERRUPT</a> structure that represents a registration by a driver to receive device interrupts. The structure is opaque. The caller obtained this pointer value in a previous call to the <a href="https://msdn.microsoft.com/172598B1-C486-489F-98F0-382EB8139A08">WdmlibIoConnectInterruptEx</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a> routine.</p>
</dd>

### -param <i>GroupAffinity</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer into which the routine writes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a> structure that specifies the group affinity of the interrupt object that <i>InterruptObject</i> points to. This buffer must be large enough to contain the structure.</p>
</dd>
</dl>

## -returns
<p><b>WdmlibIoGetAffinityInterrupt</b> returns STATUS_SUCCESS if the call is successful. Possible error return values include the following:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>InterruptObject</i> parameter does not point to a valid interrupt object. </p>

<p> </p>

## -remarks
<p>A kernel-mode driver calls this routine to get the set of logical processors on which the driver's registered interrupt service routine (ISR) can receive device interrupts. This set of processors is described by a <b>GROUP_AFFINITY</b> structure, which specifies a group number and an affinity mask. All the processors that are assigned to a particular ISR registration must belong to the same group.</p>

<p>The driver registered the ISR in a previous call to the <a href="https://msdn.microsoft.com/172598B1-C486-489F-98F0-382EB8139A08">WdmlibIoConnectInterruptEx</a> or <b>IoConnectInterrupt</b> routine.</p>

<p>In Windows 7, <a href="https://msdn.microsoft.com/172598B1-C486-489F-98F0-382EB8139A08">WdmlibIoConnectInterruptEx</a> and <b>IoConnectInterrupt</b> assign device interrupts only to logical processors in group 0. This is by default. A driver can specify a different interrupt affinity for its device in an INF file or in its response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550874">IRP_MN_FILTER_RESOURCE_REQUIREMENTS</a> request. For more information about how to change the interrupt affinity, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=147914">Supporting Systems That Have More Than 64 Processors</a> white paper on the  WHDC website.</p>

<p>A kernel-mode driver calls this routine to get the set of logical processors on which the driver's registered interrupt service routine (ISR) can receive device interrupts. This set of processors is described by a <b>GROUP_AFFINITY</b> structure, which specifies a group number and an affinity mask. All the processors that are assigned to a particular ISR registration must belong to the same group.</p>

<p>The driver registered the ISR in a previous call to the <a href="https://msdn.microsoft.com/172598B1-C486-489F-98F0-382EB8139A08">WdmlibIoConnectInterruptEx</a> or <b>IoConnectInterrupt</b> routine.</p>

<p>In Windows 7, <a href="https://msdn.microsoft.com/172598B1-C486-489F-98F0-382EB8139A08">WdmlibIoConnectInterruptEx</a> and <b>IoConnectInterrupt</b> assign device interrupts only to logical processors in group 0. This is by default. A driver can specify a different interrupt affinity for its device in an INF file or in its response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550874">IRP_MN_FILTER_RESOURCE_REQUIREMENTS</a> request. For more information about how to change the interrupt affinity, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=147914">Supporting Systems That Have More Than 64 Processors</a> white paper on the  WHDC website.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iointex.h (include Iointex.h, Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/172598B1-C486-489F-98F0-382EB8139A08">WdmlibIoConnectInterruptEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550874">IRP_MN_FILTER_RESOURCE_REQUIREMENTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554237">KINTERRUPT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20WdmlibIoGetAffinityInterrupt function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
