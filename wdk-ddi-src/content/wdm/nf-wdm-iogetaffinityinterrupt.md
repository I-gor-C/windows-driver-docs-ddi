---
UID: NF.wdm.IoGetAffinityInterrupt
title: IoGetAffinityInterrupt
author: windows-driver-content
description: For more information, see the WdmlibIoGetAffinityInterrupt function.#define IoGetAffinityInterrupt WdmlibIoGetAffinityInterrupt
old-location: kernel\iogetaffinityinterrupt.htm
old-project: kernel
ms.assetid: aec1ace6-9945-4e7a-b0f6-81591670ecfe
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoGetAffinityInterrupt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoGetAffinityInterrupt,WdmlibIoGetAffinityInterrupt
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

# IoGetAffinityInterrupt function



## -description
<p>For more information, see the <a href="..\iointex\nf-iointex-wdmlibiogetaffinityinterrupt.md">WdmlibIoGetAffinityInterrupt</a> function.</p>
<p><code>#define IoGetAffinityInterrupt WdmlibIoGetAffinityInterrupt</code></p>


## -syntax

````
NTSTATUS IoGetAffinityInterrupt(
  _In_  PKINTERRUPT     InterruptObject,
  _Out_ PGROUP_AFFINITY GroupAffinity
);
````


## -parameters
<dl>

### -param <i>InterruptObject</i> [in]

<dd>
<p>For more information, see the <a href="..\iointex\nf-iointex-wdmlibiogetaffinityinterrupt.md">WdmlibIoGetAffinityInterrupt</a> function.</p>
</dd>

### -param <i>GroupAffinity</i> [out]

<dd>
<p>For more information, see the <a href="..\iointex\nf-iointex-wdmlibiogetaffinityinterrupt.md">WdmlibIoGetAffinityInterrupt</a> function.</p>
</dd>
</dl>

## -returns
<p>For more information, see the <a href="..\iointex\nf-iointex-wdmlibiogetaffinityinterrupt.md">WdmlibIoGetAffinityInterrupt</a> function.</p>

## -remarks


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
<p>Available in Windows 7 and later versions of Windows.</p>
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
<a href="..\iointex\nf-iointex-wdmlibiogetaffinityinterrupt.md">WdmlibIoGetAffinityInterrupt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoGetAffinityInterrupt routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
