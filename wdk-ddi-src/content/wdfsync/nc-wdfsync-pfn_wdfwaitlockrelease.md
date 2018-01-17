---
UID: NC:wdfsync.PFN_WDFWAITLOCKRELEASE
title: PFN_WDFWAITLOCKRELEASE function
author: windows-driver-content
description: The WdfWaitLockRelease method releases a specified wait lock.
old-location: wdf\wdfwaitlockrelease.htm
old-project: wdf
ms.assetid: f7fb070b-fea4-48d9-8f89-1c01af183ef0
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: PFN_WDFWAITLOCKRELEASE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfsync.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfWaitLockRelease
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, WdfWaitlock, WdfWaitlockRelease
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.typenames: WDF_REQUEST_SEND_OPTIONS, *PWDF_REQUEST_SEND_OPTIONS
req.product: Windows 10 or later.
---

# PFN_WDFWAITLOCKRELEASE function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfWaitLockRelease</b> method releases a specified wait lock.



## -syntax

````
VOID WdfWaitLockRelease(
  _In_ WDFWAITLOCK Lock
);
````


## -parameters

### -param Lock [in]

A handle to a framework wait-lock object, obtained by a previous call to <a href="..\wdfsync\nf-wdfsync-wdfwaitlockcreate.md">WdfWaitLockCreate</a>.


## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
The <b>WdfWaitLockRelease</b> method releases a wait lock that the driver acquired by a previous call to <a href="..\wdfsync\nf-wdfsync-wdfwaitlockacquire.md">WdfWaitLockAcquire</a>.

For more information about wait locks, see <a href="wdf.synchronization_techniques_for_wdf_drivers">Synchronization Techniques for Framework-Based Drivers</a>.

For a code example that uses <b>WdfWaitLockRelease</b>, see <a href="..\wdfsync\nf-wdfsync-wdfwaitlockacquire.md">WdfWaitLockAcquire</a>.


## -see-also
<dl>
<dt>
<a href="..\wdfsync\nf-wdfsync-wdfwaitlockacquire.md">WdfWaitLockAcquire</a>
</dt>
<dt>
<a href="..\wdfsync\nf-wdfsync-wdfwaitlockcreate.md">WdfWaitLockCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWaitLockRelease method%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

