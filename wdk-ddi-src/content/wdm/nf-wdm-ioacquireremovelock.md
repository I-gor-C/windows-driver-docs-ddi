---
UID: NF:wdm.IoAcquireRemoveLock
title: IoAcquireRemoveLock macro
author: windows-driver-content
description: The IoAcquireRemoveLock routine increments the count for a remove lock, indicating that the associated device object should not be detached from the device stack or deleted.
old-location: kernel\ioacquireremovelock.htm
old-project: kernel
ms.assetid: 46398050-7f06-4d64-8b27-12e529884cb2
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: IoAcquireRemoveLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoAcquireRemoveLock
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: CompleteRequestStatusCheck, MarkDevicePower, MarkPower, MarkPowerDown, MarkQueryRelations, MarkStartDevice, MultRemoveLock, NsRemoveLockMnRemove, NsRemoveLockMnSurpriseRemove, NsRemoveLockQueryMnRemove, PowerDownAllocate, PowerDownFail, PowerUpFail, RemoveLock, RemoveLockCheck, RemoveLockForward, RemoveLockForward2, RemoveLockForwardDeviceControl, RemoveLockForwardDeviceControl2, RemoveLockForwardDeviceControlInternal, RemoveLockForwardDeviceControlInternal2, RemoveLockForwardRead, RemoveLockForwardRead2, RemoveLockForwardWrite, RemoveLockForwardWrite2, RemoveLockMnRemove, RemoveLockMnRemove2, RemoveLockMnSurpriseRemove, RemoveLockQueryMnRemove, RemoveLockRelease2, RemoveLockReleaseCleanup, RemoveLockReleaseClose, RemoveLockReleaseCreate, RemoveLockReleaseDeviceControl, RemoveLockReleaseInternalDeviceControl, RemoveLockReleasePnp, RemoveLockReleasePower, RemoveLockReleaseRead, RemoveLockReleaseShutdown, RemoveLockReleaseSystemControl, RemoveLockReleaseWrite, WmiForward
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---

# IoAcquireRemoveLock macro



## -description
The <b>IoAcquireRemoveLock</b> routine increments the count for a remove lock, 
   indicating that the associated device object should not be detached from the device stack or deleted.



## -syntax

````
NTSTATUS IoAcquireRemoveLock(
  _In_     PIO_REMOVE_LOCK RemoveLock,
  _In_opt_ PVOID           Tag
);
````


## -parameters

### -param RemoveLock [in]

Pointer to an <b>IO_REMOVE_LOCK</b> structure that the caller initialized with a 
      previous call to 
      <a href="..\wdm\nf-wdm-ioinitializeremovelock.md">IoInitializeRemoveLock</a>.


### -param Tag [in, optional]

Optionally points to a caller-supplied tag that identifies this instance of acquiring the remove lock. For 
       example, a driver Dispatch routine typically sets this parameter to a pointer to the IRP the routine is 
       processing.

If a driver specifies a <i>Tag</i> on a call to 
       <b>IoAcquireRemoveLock</b>, the driver must supply the same 
       <i>Tag</i> in the corresponding call to 
       <a href="..\wdm\nf-wdm-ioreleaseremovelock.md">IoReleaseRemoveLock</a>.

The <i>Tag</i> does not have to be unique, but should be something meaningful during 
       debugging.

The I/O system uses this parameter on checked builds only.


## -remarks
A driver must initialize a remove lock with a call to 
     <a href="..\wdm\nf-wdm-ioinitializeremovelock.md">IoInitializeRemoveLock</a> before using the 
     lock.

A driver must call <a href="..\wdm\nf-wdm-ioreleaseremovelock.md">IoReleaseRemoveLock</a> to 
     release the lock when it is no longer needed.

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565504">Using Remove Locks</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975144">CompleteRequestStatusCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975187">MarkDevicePower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975188">MarkPower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975189">MarkPowerDown</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975190">MarkQueryRelations</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975191">MarkStartDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975192">MultRemoveLock</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/jj157235">NsRemoveLockMnRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/jj157236">NsRemoveLockMnSurpriseRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/jj157237">NsRemoveLockQueryMnRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975201">PowerDownAllocate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975203">PowerDownFail</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975205">PowerUpFail</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975206">RemoveLock</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975207">RemoveLockCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975208">RemoveLockForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975209">RemoveLockForward2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975210">RemoveLockForwardDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975211">RemoveLockForwardDeviceControl2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975212">RemoveLockForwardDeviceControlInternal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975213">RemoveLockForwardDeviceControlInternal2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975214">RemoveLockForwardRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975215">RemoveLockForwardRead2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975216">RemoveLockForwardWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975217">RemoveLockForwardWrite2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975232">RemoveLockMnRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975233">RemoveLockMnRemove2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975234">RemoveLockMnSurpriseRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975235">RemoveLockQueryMnRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975236">RemoveLockRelease2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975237">RemoveLockReleaseCleanup</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975238">RemoveLockReleaseClose</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975239">RemoveLockReleaseCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975240">RemoveLockReleaseDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975241">RemoveLockReleaseInternalDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975242">RemoveLockReleasePnp</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975243">RemoveLockReleasePower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975244">RemoveLockReleaseRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975245">RemoveLockReleaseShutdown</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975246">RemoveLockReleaseSystemControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975247">RemoveLockReleaseWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556175">WmiForward</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-ioinitializeremovelock.md">IoInitializeRemoveLock</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-ioreleaseremovelock.md">IoReleaseRemoveLock</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-ioreleaseremovelockandwait.md">IoReleaseRemoveLockAndWait</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoAcquireRemoveLock routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

