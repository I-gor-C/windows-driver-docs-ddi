---
UID: NN.dbgeng.IDebugClient4
title: IDebugClient4
author: windows-driver-content
description: IDebugClient4 interface
old-location: debugger\idebugclient4.htm
old-project: debugger
ms.assetid: fcfa64f3-6cdf-4e5a-bb02-13a748fd6dda
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: DebugCreateEx
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
---

# IDebugClient4 interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugClient4</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>. <b>IDebugClient4</b> also has these types of members:

The <b>IDebugClient4</b> interface has these methods.

Registers additional files containing supporting information that will be used when opening a dump file.

Describes the files containing supporting information that were used when opening the current dump target.
(ANSI version)

Describes the files containing supporting information that were used when opening the current dump target.
(Unicode version)

Returns the number of files containing supporting information that were used when opening the current dump target.

Opens a dump file as a debugger target.

Creates a user-mode or kernel-mode crash dump file.


 

## -members
The <b>IDebugClient4</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.adddumpinformationfilewide">AddDumpInformationFileWide</a>
</td>
<td align="left" width="63%">
Registers additional files containing supporting information that will be used when opening a dump file.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getdumpfile">GetDumpFile</a>
</td>
<td align="left" width="63%">
Describes the files containing supporting information that were used when opening the current dump target.
(ANSI version)
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getdumpfilewide">GetDumpFileWide</a>
</td>
<td align="left" width="63%">
Describes the files containing supporting information that were used when opening the current dump target.
(Unicode version)
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnumberdumpfiles">GetNumberDumpFiles</a>
</td>
<td align="left" width="63%">
Returns the number of files containing supporting information that were used when opening the current dump target.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.opendumpfilewide">OpenDumpFileWide</a>
</td>
<td align="left" width="63%">
Opens a dump file as a debugger target.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writedumpfilewide">WriteDumpFileWide</a>
</td>
<td align="left" width="63%">
Creates a user-mode or kernel-mode crash dump file.

</td>
</tr>
</table>Registers additional files containing supporting information that will be used when opening a dump file.

Describes the files containing supporting information that were used when opening the current dump target.
(ANSI version)

Describes the files containing supporting information that were used when opening the current dump target.
(Unicode version)

Returns the number of files containing supporting information that were used when opening the current dump target.

Opens a dump file as a debugger target.

Creates a user-mode or kernel-mode crash dump file.


 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
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
<a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient4 interface%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>