---
UID: NF.wdm.ExReleaseResourceForThreadLite
title: ExReleaseResourceForThreadLite function
author: windows-driver-content
description: The ExReleaseResourceForThreadLite routine releases the input resource of the indicated thread.
old-location: kernel\exreleaseresourceforthreadlite.htm
old-project: kernel
ms.assetid: 840e7f50-644c-49b9-a40b-d504e19b0db2
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: ExReleaseResourceForThreadLite
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExReleaseResourceForThreadLite
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: ExclusiveResourceAccess, WithinCriticalRegion, HwStorPortProhibitedDDIs, WithinCriticalRegion(storport)
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

# ExReleaseResourceForThreadLite function



## -description
The <b>ExReleaseResourceForThreadLite</b> routine releases the input resource of the indicated thread.



## -syntax

````
VOID ExReleaseResourceForThreadLite(
  _Inout_ PERESOURCE       Resource,
  _In_    ERESOURCE_THREAD ResourceThreadId
);
````


## -parameters

### -param Resource [in, out]

A pointer to the resource to release.


### -param ResourceThreadId [in]

Identifies the thread that originally acquired the resource. If this is not the currently executing thread, the caller must have transferred ownership of the resource by calling the <a href="kernel.exsetresourceownerpointerex">ExSetResourceOwnerPointerEx</a> routine first on the thread that originally acquired the resource.


## -returns
None


## -remarks
If this is not the currently executing thread, the caller must have transferred ownership of the resource by calling the <a href="kernel.exsetresourceownerpointerex">ExSetResourceOwnerPointerEx</a> routine first on the thread that originally acquired the resource. This is to ensure that thread A does not get terminated or deleted before thread B has a chance to release the resource.

Unless the caller is running in a system thread, the caller must explicitly disable the delivery of normal kernel APCs before calling this routine. This requirement prevents threads from being suspended while they manipulate or hold a resource. The caller can disable normal kernel APC delivery by calling the <a href="kernel.keentercriticalregion">KeEnterCriticalRegion</a> routine. Delivery must remain disabled until the resource is released, at which point it can be reenabled by calling the <a href="kernel.keleavecriticalregion">KeLeaveCriticalRegion</a> routine. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543219">Disabling APCs</a>.

This requirement does not apply to calls made to <b>ExReleaseResourceForThreadLite</b> from a system thread. A caller running in a system thread does not need to explicitly disable APCs before calling this routine.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
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
<a href="devtest.wdm_exclusiveresourceaccess">ExclusiveResourceAccess</a>, <a href="devtest.wdm_withincriticalregion">WithinCriticalRegion</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_withincriticalregion">WithinCriticalRegion(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exacquireresourceexclusivelite">ExAcquireResourceExclusiveLite</a>
</dt>
<dt>
<a href="kernel.exacquireresourcesharedlite">ExAcquireResourceSharedLite</a>
</dt>
<dt>
<a href="kernel.exacquiresharedstarveexclusive">ExAcquireSharedStarveExclusive</a>
</dt>
<dt>
<a href="kernel.exacquiresharedwaitforexclusive">ExAcquireSharedWaitForExclusive</a>
</dt>
<dt>
<a href="kernel.exgetcurrentresourcethread">ExGetCurrentResourceThread</a>
</dt>
<dt>
<a href="kernel.exinitializeresourcelite">ExInitializeResourceLite</a>
</dt>
<dt>
<a href="kernel.exreinitializeresourcelite">ExReinitializeResourceLite</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExReleaseResourceForThreadLite routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

