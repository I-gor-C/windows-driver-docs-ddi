---
UID: NF.ntifs.CcMdlReadComplete
title: CcMdlReadComplete
author: windows-driver-content
description: The CcMdlReadComplete routine frees the memory descriptor lists (MDL) created by CcMdlRead for a cached file.
old-location: ifsk\ccmdlreadcomplete.htm
old-project: ifsk
ms.assetid: c1525604-3aee-464d-a7f5-a6a4739a2aa4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcMdlReadComplete
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
req.alt-api: CcMdlReadComplete
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# CcMdlReadComplete function



## -description
<p>The <b>CcMdlReadComplete</b> routine frees the memory descriptor lists (MDL) created by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a> for a cached file.</p>


## -syntax

````
VOID CcMdlReadComplete(
  _In_ PFILE_OBJECT FileObject,
  _In_ PMDL         MdlChain
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>File object pointer that was passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>.</p>
</dd>

### -param <i>MdlChain</i> [in]

<dd>
<p>Address of the MDL chain returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>CcMdlReadComplete</b> frees the memory descriptor lists (MDL) created by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a> for a cached file. All physical pages that were locked down are unlocked. Any pages that were mapped are unmapped.</p>

<p>Each call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a> must be followed by a call to <b>CcMdlReadComplete</b>.</p>

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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcMdlReadComplete routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
