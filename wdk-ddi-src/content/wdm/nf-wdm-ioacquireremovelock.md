---
UID: NF.wdm.IoAcquireRemoveLock
title: IoAcquireRemoveLock macro
author: windows-driver-content
description: The IoAcquireRemoveLock routine increments the count for a remove lock, indicating that the associated device object should not be detached from the device stack or deleted.
old-location: kernel\ioacquireremovelock.htm
old-project: kernel
ms.assetid: 46398050-7f06-4d64-8b27-12e529884cb2
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
      <a href="kernel.ioinitializeremovelock">IoInitializeRemoveLock</a>.


### -param Tag [in, optional]

Optionally points to a caller-supplied tag that identifies this instance of acquiring the remove lock. For 
       example, a driver Dispatch routine typically sets this parameter to a pointer to the IRP the routine is 
       processing.

If a driver specifies a <i>Tag</i> on a call to 
       <b>IoAcquireRemoveLock</b>, the driver must supply the same 
       <i>Tag</i> in the corresponding call to 
       <a href="kernel.ioreleaseremovelock">IoReleaseRemoveLock</a>.

The <i>Tag</i> does not have to be unique, but should be something meaningful during 
       debugging.

The I/O system uses this parameter on checked builds only.


## -remarks
A driver must initialize a remove lock with a call to 
     <a href="kernel.ioinitializeremovelock">IoInitializeRemoveLock</a> before using the 
     lock.

A driver must call <a href="kernel.ioreleaseremovelock">IoReleaseRemoveLock</a> to 
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
<a href="devtest.wdm_completerequeststatuscheck">CompleteRequestStatusCheck</a>, <a href="devtest.wdm_markdevicepower">MarkDevicePower</a>, <a href="devtest.wdm_markpower">MarkPower</a>, <a href="devtest.wdm_markpowerdown">MarkPowerDown</a>, <a href="devtest.wdm_markqueryrelations">MarkQueryRelations</a>, <a href="devtest.wdm_markstartdevice">MarkStartDevice</a>, <a href="devtest.wdm_multremovelock">MultRemoveLock</a>, <a href="devtest.wdm_nsremovelockmnremove">NsRemoveLockMnRemove</a>, <a href="devtest.wdm_nsremovelockmnsurpriseremove">NsRemoveLockMnSurpriseRemove</a>, <a href="devtest.wdm_nsremovelockquerymnremove">NsRemoveLockQueryMnRemove</a>, <a href="devtest.wdm_powerdownallocate">PowerDownAllocate</a>, <a href="devtest.wdm_powerdownfail">PowerDownFail</a>, <a href="devtest.wdm_powerupfail">PowerUpFail</a>, <a href="devtest.wdm_removelock">RemoveLock</a>, <a href="devtest.wdm_removelockcheck">RemoveLockCheck</a>, <a href="devtest.wdm_removelockforward">RemoveLockForward</a>, <a href="devtest.wdm_removelockforward2">RemoveLockForward2</a>, <a href="devtest.wdm_removelockforwarddevicecontrol">RemoveLockForwardDeviceControl</a>, <a href="devtest.wdm_removelockforwarddevicecontrol2">RemoveLockForwardDeviceControl2</a>, <a href="devtest.wdm_removelockforwarddevicecontrolinternal">RemoveLockForwardDeviceControlInternal</a>, <a href="devtest.wdm_removelockforwarddevicecontrolinternal2">RemoveLockForwardDeviceControlInternal2</a>, <a href="devtest.wdm_removelockforwardread">RemoveLockForwardRead</a>, <a href="devtest.wdm_removelockforwardread2">RemoveLockForwardRead2</a>, <a href="devtest.wdm_removelockforwardwrite">RemoveLockForwardWrite</a>, <a href="devtest.wdm_removelockforwardwrite2">RemoveLockForwardWrite2</a>, <a href="devtest.wdm_removelockmnremove">RemoveLockMnRemove</a>, <a href="devtest.wdm_removelockmnremove2">RemoveLockMnRemove2</a>, <a href="devtest.wdm_removelockmnsurpriseremove">RemoveLockMnSurpriseRemove</a>, <a href="devtest.wdm_removelockquerymnremove">RemoveLockQueryMnRemove</a>, <a href="devtest.wdm_removelockrelease2">RemoveLockRelease2</a>, <a href="devtest.wdm_removelockreleasecleanup">RemoveLockReleaseCleanup</a>, <a href="devtest.wdm_removelockreleaseclose">RemoveLockReleaseClose</a>, <a href="devtest.wdm_removelockreleasecreate">RemoveLockReleaseCreate</a>, <a href="devtest.wdm_removelockreleasedevicecontrol">RemoveLockReleaseDeviceControl</a>, <a href="devtest.wdm_removelockreleaseinternaldevicecontrol">RemoveLockReleaseInternalDeviceControl</a>, <a href="devtest.wdm_removelockreleasepnp">RemoveLockReleasePnp</a>, <a href="devtest.wdm_removelockreleasepower">RemoveLockReleasePower</a>, <a href="devtest.wdm_removelockreleaseread">RemoveLockReleaseRead</a>, <a href="devtest.wdm_removelockreleaseshutdown">RemoveLockReleaseShutdown</a>, <a href="devtest.wdm_removelockreleasesystemcontrol">RemoveLockReleaseSystemControl</a>, <a href="devtest.wdm_removelockreleasewrite">RemoveLockReleaseWrite</a>, <a href="devtest.wdm_wmiforward">WmiForward</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioinitializeremovelock">IoInitializeRemoveLock</a>
</dt>
<dt>
<a href="kernel.ioreleaseremovelock">IoReleaseRemoveLock</a>
</dt>
<dt>
<a href="kernel.ioreleaseremovelockandwait">IoReleaseRemoveLockAndWait</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoAcquireRemoveLock routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

