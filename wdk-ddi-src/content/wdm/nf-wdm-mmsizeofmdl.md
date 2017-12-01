---
UID: NF.wdm.MmSizeOfMdl
title: MmSizeOfMdl
author: windows-driver-content
description: The MmSizeOfMdl routine returns the number of bytes to allocate for an MDL describing a given address range.
old-location: kernel\mmsizeofmdl.htm
old-project: kernel
ms.assetid: 83e7d4be-df76-4dc8-a8e2-91d279127ef1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: MmSizeOfMdl
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
req.alt-api: MmSizeOfMdl
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

# MmSizeOfMdl function



## -description
<p>The <b>MmSizeOfMdl</b> routine returns the number of bytes to allocate for an MDL describing a given address range.</p>


## -syntax

````
SIZE_T MmSizeOfMdl(
  _In_ PVOID  Base,
  _In_ SIZE_T Length
);
````


## -parameters
<dl>

### -param <i>Base</i> [in]

<dd>
<p>Pointer to the base virtual address for the range. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Supplies the size, in bytes, of the range. </p>
</dd>
</dl>

## -returns
<p><b>MmSizeOfMdl</b> returns the number of bytes required to contain the MDL. </p>

## -remarks
<p>Memory for the MDL itself must be allocated from nonpaged pool. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554500">MmCreateMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554568">MmInitializeMdl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmSizeOfMdl routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
