---
UID: NF:wdm.KeInitializeGuardedMutex
title: KeInitializeGuardedMutex function
author: windows-driver-content
description: The KeInitializeGuardedMutex routine initializes a guarded mutex.
old-location: kernel\keinitializeguardedmutex.htm
old-project: kernel
ms.assetid: 28d45b36-c20d-40a5-bdf9-5fb754e36e74
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: KeInitializeGuardedMutex
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Server 2003 with Service Pack 1 (SP1) and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeInitializeGuardedMutex
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
req.irql: <= APC_LEVEL
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---

# KeInitializeGuardedMutex function



## -description
The <b>KeInitializeGuardedMutex</b> routine initializes a guarded mutex. 



## -syntax

````
VOID KeInitializeGuardedMutex(
  _Out_ PKGUARDED_MUTEX Mutex
);
````


## -parameters

### -param Mutex [out]

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554235">KGUARDED_MUTEX</a> structure to initialize. The storage must be 4-byte aligned on 32-bit platforms, and 8-byte aligned on 64-bit platforms.


## -returns
None


## -remarks
Guarded mutexes must be allocated from nonpaged pool.

For more information about guarded mutexes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545716">Fast Mutexes and Guarded Mutexes</a>.


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
Available in Windows Server 2003 with Service Pack 1 (SP1) and later versions of Windows.

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
&lt;= APC_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554235">KGUARDED_MUTEX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551892">KeAcquireGuardedMutex</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeInitializeGuardedMutex routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

