---
UID: NF.storport.StorPortReleaseMSISpinLock
title: StorPortReleaseMSISpinLock
author: windows-driver-content
description: The StorPortReleaseMSISpinLock routine releases a previously acquired message signaled interrupt (MSI) spin lock for the specified message.
old-location: storage\storportreleasemsispinlock.htm
ms.assetid: 5a2cf757-9dca-4717-a775-834a22c02a12
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortReleaseMSISpinLock
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
ms.keywords: StorPortReleaseMSISpinLock
req.iface: 
req.product: Windows 10 or later.
---

# StorPortReleaseMSISpinLock function



## -description
<p>The <b>StorPortReleaseMSISpinLock</b> routine releases a previously acquired message signaled interrupt (MSI) spin lock for the specified message. </p>


## -syntax

````
ULONG StorPortReleaseMSISpinLock(
  _In_ PVOID HwDeviceExtension,
  _In_ ULONG MessageID,
  _In_ ULONG OldIrql
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>MessageID</i> [in]

<dd>
<p>The identifier of the message.</p>
</dd>

### -param <i>OldIrql</i> [in]

<dd>
<p>The IRQL that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567023">StorPortAcquireMSISpinLock</a> routine returned when the miniport driver acquired the spin lock.</p>
</dd>
</dl>

## -returns
<p>StorPortReleaseMSISpinLock returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the spin lock was released successfully.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>HwDeviceExtension was <b>NULL</b>.</p>

<p> </p>

## -remarks
<p>Miniport drivers are not required to acquire MSI spin locks for messages unless the <b>InterruptSynchronizePerMessage</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a> structure indicates a synchronization mode of <b>InterruptSynchronizationMode</b>.</p>

<p>Miniport drivers are not required to acquire MSI spin locks for messages unless the <b>InterruptSynchronizePerMessage</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a> structure indicates a synchronization mode of <b>InterruptSynchronizationMode</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This routine is available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567023">StorPortAcquireMSISpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortReleaseMSISpinLock routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
