---
UID: NF.ntifs.CcRepinBcb
title: CcRepinBcb
author: windows-driver-content
description: The CcRepinBcb routine pins a buffer control block (BCB) an additional time to prevent it from being freed by a subsequent call to CcUnpinData.
old-location: ifsk\ccrepinbcb.htm
old-project: ifsk
ms.assetid: 81c2446e-8f11-4146-8da5-17fc451c2729
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcRepinBcb
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcRepinBcb
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
req.irql: 
req.iface: 
---

# CcRepinBcb function



## -description
<p>The <b>CcRepinBcb</b> routine pins a buffer control block (BCB) an additional time to prevent it from being freed by a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539228">CcUnpinData</a>.</p>


## -syntax

````
VOID CcRepinBcb(
  _In_ PVOID Bcb
);
````


## -parameters
<dl>

### -param <i>Bcb</i> [in]

<dd>
<p>Buffer control block (BCB) pointer returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539180">CcPinRead</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff539183">CcPreparePinWrite</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>File systems call <b>CcRepinBcb</b> to preserve a BCB for write-through or error recovery. Typically a file system would do this the first time it marks a BCB as dirty while processing a write-through request, or any time that it determines that a buffer will be required for write-through.</p>

<p>Every call to <b>CcRepinBcb</b> must be matched by a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539235">CcUnpinRepinnedBcb</a>.</p>

<p>File systems call <b>CcRepinBcb</b> to preserve a BCB for write-through or error recovery. Typically a file system would do this the first time it marks a BCB as dirty while processing a write-through request, or any time that it determines that a buffer will be required for write-through.</p>

<p>Every call to <b>CcRepinBcb</b> must be matched by a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539235">CcUnpinRepinnedBcb</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539180">CcPinRead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539183">CcPreparePinWrite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539228">CcUnpinData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539235">CcUnpinRepinnedBcb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcRepinBcb routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
