---
UID: NF.wdm.KeInitializeThreadedDpc
title: KeInitializeThreadedDpc function
author: windows-driver-content
description: The KeInitializeThreadedDpc routine initializes a threaded DPC object, and registers a CustomThreadedDpc routine for that object.
old-location: kernel\keinitializethreadeddpc.htm
old-project: kernel
ms.assetid: ee9124db-9d92-42e1-84fa-6d3eefeaeac5
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KeInitializeThreadedDpc
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeInitializeThreadedDpc
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
req.product: Windows 10 or later.
---

# KeInitializeThreadedDpc function



## -description
The <b>KeInitializeThreadedDpc</b> routine initializes a threaded DPC object, and registers a <a href="kernel.customthreadeddpc">CustomThreadedDpc</a> routine for that object.


## -syntax

````
VOID KeInitializeThreadedDpc(
  _Out_    PRKDPC             Dpc,
  _In_     PKDEFERRED_ROUTINE DeferredRoutine,
  _In_opt_ PVOID              DeferredContext
);
````


## -parameters

### -param Dpc [out]

Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551882">KDPC</a> structure that represents the DPC object to initialize. The caller must allocate storage for the structure from resident memory.

### -param DeferredRoutine [in]

Pointer to the <a href="kernel.customthreadeddpc">CustomThreadedDpc</a> routine to associate with the DPC.

### -param DeferredContext [in, optional]

Specifies the value to pass as the <i>DeferredContext</i> parameter to <a href="kernel.customthreadeddpc">CustomThreadedDpc</a>.

## -returns
None

## -remarks
For more information about threaded DPCs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564621">Threaded DPCs</a>.

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
Available in Windows Vista and later versions of Windows.
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
Any level
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.customthreadeddpc">CustomThreadedDpc</a>
</dt>
<dt>
<a href="kernel.keinsertqueuedpc">KeInsertQueueDpc</a>
</dt>
<dt>
<a href="kernel.keremovequeuedpc">KeRemoveQueueDpc</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeInitializeThreadedDpc routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
