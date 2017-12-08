---
UID: NF.wdm.ExInitializeResourceLite
title: ExInitializeResourceLite function
author: windows-driver-content
description: The ExInitializeResourceLite routine initializes a resource variable.
old-location: kernel\exinitializeresourcelite.htm
old-project: kernel
ms.assetid: be18a6e6-863d-4a0c-9bcd-a36ace0b54fe
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: ExInitializeResourceLite
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
req.alt-api: ExInitializeResourceLite
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: HwStorPortProhibitedDDIs
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

# ExInitializeResourceLite function



## -description
The <b>ExInitializeResourceLite</b> routine initializes a resource variable. 


## -syntax

````
NTSTATUS ExInitializeResourceLite(
  _Out_ PERESOURCE Resource
);
````


## -parameters

### -param Resource [out]

A pointer to the caller-supplied storage, which must be at least <b>sizeof</b>(<b>ERESOURCE</b>), for the resource variable being initialized. The storage must be 4-byte aligned on 32-bit platforms, and 8-byte aligned on 64-bit platforms.

## -returns
<b>ExInitializeResourceLite</b> returns STATUS_SUCCESS.

## -remarks
The storage for <b>ERESOURCE</b> must be allocated from nonpaged pool.

The resource variable can be used for synchronization by a set of threads. Although the caller provides the storage for the resource variable, the <b>ERESOURCE</b> structure is opaque: that is, its members are reserved for system use.

Call <b>ExDeleteResourceLite</b> before freeing the memory for the resource.

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
<a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
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
<a href="kernel.exconvertexclusivetosharedlite">ExConvertExclusiveToSharedLite</a>
</dt>
<dt>
<a href="kernel.exdeleteresourcelite">ExDeleteResourceLite</a>
</dt>
<dt>
<a href="kernel.exisresourceacquiredexclusivelite">ExIsResourceAcquiredExclusiveLite</a>
</dt>
<dt>
<a href="kernel.exisresourceacquiredsharedlite">ExIsResourceAcquiredSharedLite</a>
</dt>
<dt>
<a href="kernel.exreinitializeresourcelite">ExReinitializeResourceLite</a>
</dt>
<dt>
<a href="kernel.exreleaseresourceforthreadlite">ExReleaseResourceForThreadLite</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExInitializeResourceLite routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
