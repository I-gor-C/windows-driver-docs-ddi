---
UID: NN.dbgeng.IDebugClient4
title: IDebugClient4
author: windows-driver-content
description: IDebugClient4 interface
old-location: debugger\idebugclient4.htm
old-project: debugger
ms.assetid: fcfa64f3-6cdf-4e5a-bb02-13a748fd6dda
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient4
req.alt-loc: dbgeng.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IDebugSystemObjects4
---

# IDebugClient4 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugClient4</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff550488">IDebugClient3</a>. <b>IDebugClient4</b> also has these types of members:</p>

<p>The <b>IDebugClient4</b> interface has these methods.</p>

<p>Registers additional files containing supporting information that will be used when opening a dump file.</p>

<p>Describes the files containing supporting information that were used when opening the current dump target.
(ANSI version)</p>

<p>Describes the files containing supporting information that were used when opening the current dump target.
(Unicode version)</p>

<p>Returns the number of files containing supporting information that were used when opening the current dump target.</p>

<p>Opens a dump file as a debugger target.</p>

<p>Creates a user-mode or kernel-mode crash dump file.
</p>

<p> </p>

## -members
<p>The <b>IDebugClient4</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537874">AddDumpInformationFileWide</a>
</td>
<td align="left" width="63%">
<p>Registers additional files containing supporting information that will be used when opening a dump file.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546586">GetDumpFile</a>
</td>
<td align="left" width="63%">
<p>Describes the files containing supporting information that were used when opening the current dump target.
(ANSI version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546590">GetDumpFileWide</a>
</td>
<td align="left" width="63%">
<p>Describes the files containing supporting information that were used when opening the current dump target.
(Unicode version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547887">GetNumberDumpFiles</a>
</td>
<td align="left" width="63%">
<p>Returns the number of files containing supporting information that were used when opening the current dump target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552324">OpenDumpFileWide</a>
</td>
<td align="left" width="63%">
<p>Opens a dump file as a debugger target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561389">WriteDumpFileWide</a>
</td>
<td align="left" width="63%">
<p>Creates a user-mode or kernel-mode crash dump file.
</p>
</td>
</tr>
</table><p>Registers additional files containing supporting information that will be used when opening a dump file.</p>

<p>Describes the files containing supporting information that were used when opening the current dump target.
(ANSI version)</p>

<p>Describes the files containing supporting information that were used when opening the current dump target.
(Unicode version)</p>

<p>Returns the number of files containing supporting information that were used when opening the current dump target.</p>

<p>Opens a dump file as a debugger target.</p>

<p>Creates a user-mode or kernel-mode crash dump file.
</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550488">IDebugClient3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient4 interface%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
