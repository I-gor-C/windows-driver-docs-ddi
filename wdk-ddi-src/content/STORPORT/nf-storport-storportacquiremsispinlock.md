---
UID: NF.storport.StorPortAcquireMSISpinLock
title: StorPortAcquireMSISpinLock
author: windows-driver-content
description: The StorPortAcquireMSISpinLock routine acquires the message signaled interrupt (MSI) spin lock that is associated with the specified message.
old-location: storage\storportacquiremsispinlock.htm
ms.assetid: 8aa5a8a6-2024-4b3e-a500-5a484d937a62
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
req.alt-api: StorPortAcquireMSISpinLock
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
ms.keywords: StorPortAcquireMSISpinLock
req.iface: 
req.product: Windows 10 or later.
---

# StorPortAcquireMSISpinLock function



## -description
<p>The <b>StorPortAcquireMSISpinLock</b> routine acquires the message signaled interrupt (MSI) spin lock that is associated with the specified message. </p>


## -syntax

````
ULONG StorPortAcquireMSISpinLock(
  _In_ PVOID  HwDeviceExtension,
  _In_ ULONG  MessageID,
  _In_ PULONG OldIrql
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
<p>The identifier of the message whose spin lock the caller acquires.</p>
</dd>

### -param <i>OldIrql</i> [in]

<dd>
<p>A pointer to the storage for the original IRQL value to be used in a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff567494">StorPortReleaseMSISpinLock</a>.</p>
</dd>
</dl>

## -returns
<p><b>StorPortAcquireMSISpinLock</b> returns one of the following values:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the spin lock was acquired successfully.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>HwDeviceExtension</i> was <b>NULL</b>.</p>

<p> </p>

## -remarks
<p>A miniport driver calls the <b>StorPortAcquireMSISpinLock</b> routine to acquire the MSI spin lock for a particular message. To release the spin lock, the miniport driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567494">StorPortReleaseMSISpinLock</a> routine. This routine is used by a miniport drivers to acquire a  the MSI spin lock for an individual message only when the <b>InterruptSynchronizationMode</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a> structure is set to <b>InterruptSynchronizePerMessage</b>.</p>

<p>When a miniport needs to synchronize with all messages, it can use one call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff567025">StorPortAcquireSpinLock</a> which will acquire a lock for each message in the proper order.</p>

<p>A miniport driver calls the <b>StorPortAcquireMSISpinLock</b> routine to acquire the MSI spin lock for a particular message. To release the spin lock, the miniport driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567494">StorPortReleaseMSISpinLock</a> routine. This routine is used by a miniport drivers to acquire a  the MSI spin lock for an individual message only when the <b>InterruptSynchronizationMode</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a> structure is set to <b>InterruptSynchronizePerMessage</b>.</p>

<p>When a miniport needs to synchronize with all messages, it can use one call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff567025">StorPortAcquireSpinLock</a> which will acquire a lock for each message in the proper order.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567025">StorPortAcquireSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567494">StorPortReleaseMSISpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortAcquireMSISpinLock routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
