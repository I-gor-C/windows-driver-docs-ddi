---
UID: NF.wdm.IoReleaseRemoveLock
title: IoReleaseRemoveLock
author: windows-driver-content
description: The IoReleaseRemoveLock routine releases a remove lock acquired with a previous call to IoAcquireRemoveLock.
old-location: kernel\ioreleaseremovelock.htm
ms.assetid: 75cf8262-8cb4-428e-b18e-b80121c6390e
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoReleaseRemoveLock
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: RemoveLock, RemoveLockCheck, RemoveLockForward, RemoveLockForward2, RemoveLockForwardDeviceControl, RemoveLockForwardDeviceControl2, RemoveLockForwardDeviceControlInternal, RemoveLockForwardDeviceControlInternal2, RemoveLockForwardRead, RemoveLockForwardRead2, RemoveLockForwardWrite, RemoveLockForwardWrite2, RemoveLockMnRemove, RemoveLockMnRemove2, RemoveLockMnSurpriseRemove, RemoveLockQueryMnRemove, RemoveLockRelease2, RemoveLockReleaseCleanup, RemoveLockReleaseClose, RemoveLockReleaseCreate, RemoveLockReleaseDeviceControl, RemoveLockReleaseInternalDeviceControl, RemoveLockReleasePnp, RemoveLockReleasePower, RemoveLockReleaseRead, RemoveLockReleaseShutdown, RemoveLockReleaseSystemControl, RemoveLockReleaseWrite
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
ms.keywords: IoReleaseRemoveLock
req.iface: 
req.product: Windows 10 or later.
---

# IoReleaseRemoveLock function



## -description
<p>The <b>IoReleaseRemoveLock</b> routine releases a remove lock acquired with a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548204">IoAcquireRemoveLock</a>.</p>


## -syntax

````
VOID IoReleaseRemoveLock(
  _In_ PIO_REMOVE_LOCK RemoveLock,
  _In_ PVOID           Tag
);
````


## -parameters
<dl>

### -param <i>RemoveLock</i> [in]

<dd>
<p>Pointer to an <b>IO_REMOVE_LOCK</b> structure that the caller passed to a previous call to <b>IoAcquireRemoveLock</b>. </p>
</dd>

### -param <i>Tag</i> [in]

<dd>
<p>Pointer to a caller-supplied tag that was passed to a previous call to <b>IoAcquireRemoveLock</b>. </p>
<p>If a driver specified a <i>Tag</i> when it acquired the lock, the driver must specify the same <i>Tag</i> when releasing the lock. If the tags do not match, this routine asserts on a checked build.</p>
<p>If the call to <b>IoAcquireRemoveLock</b> did not specify a <i>Tag</i>, then this parameter is <b>NULL</b>.</p>
<p>The I/O system only uses this parameter on checked builds. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver calls <b>IoReleaseRemoveLock</b> when it has completed the I/O operation for which it called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548204">IoAcquireRemoveLock</a>.</p>

<p>For I/O operations (including power and PnP IRPs) that set an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine, a driver should call <b>IoReleaseRemoveLock</b> in the <i>IoCompletion</i> routine, after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>.</p>

<p>For I/O operations that do not set an <i>IoCompletion</i> routine, a driver should call <b>IoReleaseRemoveLock</b> after passing the current IRP to the next-lower driver, but before exiting the dispatch routine.</p>

<p>Each call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548204">IoAcquireRemoveLock</a> must have a corresponding call to <b>IoReleaseRemoveLock</b>. </p>

<p><b>IoReleaseRemoveLock</b> decrements the count of outstanding acquisitions of the remove lock. If the count goes to zero and the driver has received an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a> request, <b>IoReleaseRemoveLock</b> sets an internal event. When a driver is ready to delete a device object, it calls a similar routine, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549567">IoReleaseRemoveLockAndWait</a>. The driver makes this call only in its dispatch code for an <b>IRP_MN_REMOVE_DEVICE</b> request. The <b>IoReleaseRemoveLockAndWait</b> routine does not return until <b>IoReleaseRemoveLock</b> sets the event that indicates the acquisition count is zero. After <b>IoReleaseRemoveLockAndWait</b> returns, the driver can safely detach and delete the device object.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565504">Using Remove Locks</a>. </p>

<p>A driver calls <b>IoReleaseRemoveLock</b> when it has completed the I/O operation for which it called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548204">IoAcquireRemoveLock</a>.</p>

<p>For I/O operations (including power and PnP IRPs) that set an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine, a driver should call <b>IoReleaseRemoveLock</b> in the <i>IoCompletion</i> routine, after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>.</p>

<p>For I/O operations that do not set an <i>IoCompletion</i> routine, a driver should call <b>IoReleaseRemoveLock</b> after passing the current IRP to the next-lower driver, but before exiting the dispatch routine.</p>

<p>Each call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548204">IoAcquireRemoveLock</a> must have a corresponding call to <b>IoReleaseRemoveLock</b>. </p>

<p><b>IoReleaseRemoveLock</b> decrements the count of outstanding acquisitions of the remove lock. If the count goes to zero and the driver has received an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a> request, <b>IoReleaseRemoveLock</b> sets an internal event. When a driver is ready to delete a device object, it calls a similar routine, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549567">IoReleaseRemoveLockAndWait</a>. The driver makes this call only in its dispatch code for an <b>IRP_MN_REMOVE_DEVICE</b> request. The <b>IoReleaseRemoveLockAndWait</b> routine does not return until <b>IoReleaseRemoveLock</b> sets the event that indicates the acquisition count is zero. After <b>IoReleaseRemoveLockAndWait</b> returns, the driver can safely detach and delete the device object.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565504">Using Remove Locks</a>. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975206">RemoveLock</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975207">RemoveLockCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975208">RemoveLockForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975209">RemoveLockForward2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975210">RemoveLockForwardDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975211">RemoveLockForwardDeviceControl2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975212">RemoveLockForwardDeviceControlInternal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975213">RemoveLockForwardDeviceControlInternal2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975214">RemoveLockForwardRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975215">RemoveLockForwardRead2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975216">RemoveLockForwardWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975217">RemoveLockForwardWrite2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975232">RemoveLockMnRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975233">RemoveLockMnRemove2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975234">RemoveLockMnSurpriseRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975235">RemoveLockQueryMnRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975236">RemoveLockRelease2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975237">RemoveLockReleaseCleanup</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975238">RemoveLockReleaseClose</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975239">RemoveLockReleaseCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975240">RemoveLockReleaseDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975241">RemoveLockReleaseInternalDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975242">RemoveLockReleasePnp</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975243">RemoveLockReleasePower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975244">RemoveLockReleaseRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975245">RemoveLockReleaseShutdown</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975246">RemoveLockReleaseSystemControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975247">RemoveLockReleaseWrite</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548204">IoAcquireRemoveLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549324">IoInitializeRemoveLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549567">IoReleaseRemoveLockAndWait</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoReleaseRemoveLock routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
