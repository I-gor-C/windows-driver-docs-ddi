---
UID: NF.wdm.KeInitializeDpc
title: KeInitializeDpc
author: windows-driver-content
description: The KeInitializeDpc routine initializes a DPC object, and registers a CustomDpc routine for that object.
old-location: kernel\keinitializedpc.htm
old-project: kernel
ms.assetid: 5dd82086-d39c-4ebc-9e2a-73ef504f873c
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeInitializeDpc
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
req.alt-api: KeInitializeDpc
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
req.iface: 
req.product: Windows 10 or later.
---

# KeInitializeDpc function



## -description
<p>The <b>KeInitializeDpc</b> routine initializes a DPC object, and registers a <a href="https://msdn.microsoft.com/library/windows/hardware/ff542972">CustomDpc</a> routine for that object.</p>


## -syntax

````
VOID KeInitializeDpc(
  _Out_    PRKDPC             Dpc,
  _In_     PKDEFERRED_ROUTINE DeferredRoutine,
  _In_opt_ PVOID              DeferredContext
);
````


## -parameters
<dl>

### -param <i>Dpc</i> [out]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551882">KDPC</a> structure that represents the DPC object to initialize. The caller must allocate storage for the structure from resident memory.</p>
</dd>

### -param <i>DeferredRoutine</i> [in]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542972">CustomDpc</a> routine to associate with the DPC.</p>
</dd>

### -param <i>DeferredContext</i> [in, optional]

<dd>
<p>Specifies the value to pass as the <i>DeferredContext</i> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff542972">CustomDpc</a>. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The caller can queue an initialized DPC with <a href="https://msdn.microsoft.com/library/windows/hardware/ff552185">KeInsertQueueDpc</a>. The caller also can set up a timer object associated with the initialized DPC object and queue the DPC with <a href="https://msdn.microsoft.com/library/windows/hardware/ff553286">KeSetTimer</a>.</p>

<p>Storage for the DPC object must be resident: in the device extension of a driver-created device object, in the controller extension of a driver-created controller object, or in nonpaged pool allocated by the caller.</p>

<p>The caller can queue an initialized DPC with <a href="https://msdn.microsoft.com/library/windows/hardware/ff552185">KeInsertQueueDpc</a>. The caller also can set up a timer object associated with the initialized DPC object and queue the DPC with <a href="https://msdn.microsoft.com/library/windows/hardware/ff553286">KeSetTimer</a>.</p>

<p>Storage for the DPC object must be resident: in the device extension of a driver-created device object, in the controller extension of a driver-created controller object, or in nonpaged pool allocated by the caller.</p>

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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542972">CustomDpc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552185">KeInsertQueueDpc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553169">KeRemoveQueueDpc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553286">KeSetTimer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeInitializeDpc routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
