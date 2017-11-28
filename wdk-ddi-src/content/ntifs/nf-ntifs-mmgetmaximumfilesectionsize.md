---
UID: NF.ntifs.MmGetMaximumFileSectionSize
title: MmGetMaximumFileSectionSize
author: windows-driver-content
description: The MmGetMaximumFileSectionSize returns the maximum possible size of a file section for the current version of Windows.
old-location: ifsk\mmgetmaximumfilesectionsize.htm
old-project: ifsk
ms.assetid: 5B3E5B33-EFED-485A-A62A-7A54322408AC
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: MmGetMaximumFileSectionSize
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
req.alt-api: MmGetMaximumFileSectionSize
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
req.irql: <= APC_LEVEL
req.iface: 
---

# MmGetMaximumFileSectionSize function



## -description
<p>The <b>MmGetMaximumFileSectionSize</b> returns the maximum possible size of a file section for the current version of Windows.</p>


## -syntax

````
ULONGLONG MmGetMaximumFileSectionSize(void);
````


## -parameters


## -returns
<p>The maximum file section size supported by the current version of Windows.</p>

<p>The maximum file section size supported by the current version of Windows.</p>

<p>The maximum file section size supported by the current version of Windows.</p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>