---
UID: NN.dbgeng.IDebugClient3
title: IDebugClient3
author: windows-driver-content
description: IDebugClient3 interface
old-location: debugger\idebugclient3.htm
ms.assetid: 316a4d8b-4cf6-4270-8d9b-e1ede53d567d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient3
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
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
req.iface: IDebugSystemObjects4
---

# IDebugClient3 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugClient3</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff550481">IDebugClient2</a>. <b>IDebugClient3</b> also has these types of members:</p>

<p>The <b>IDebugClient3</b> interface has these methods.</p>

<p>Creates a process from a specified command line, then attaches to another user-mode process.</p>

<p>Creates a process from the specified command line.</p>

<p>Returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line.
</p>

<p> Searches for a process with a given executable file name and return its process ID.
</p>

<p> </p>

## -members
<p>The <b>IDebugClient3</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540070">CreateProcessAndAttachWide</a>
</td>
<td align="left" width="63%">
<p>Creates a process from a specified command line, then attaches to another user-mode process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540077">CreateProcessWide</a>
</td>
<td align="left" width="63%">
<p>Creates a process from the specified command line.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548250">GetRunningProcessDescriptionWide</a>
</td>
<td align="left" width="63%">
<p>Returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548260">GetRunningProcessSystemIdByExecutableNameWide</a>
</td>
<td align="left" width="63%">
<p> Searches for a process with a given executable file name and return its process ID.
</p>
</td>
</tr>
</table><p>Creates a process from a specified command line, then attaches to another user-mode process.</p>

<p>Creates a process from the specified command line.</p>

<p>Returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line.
</p>

<p> Searches for a process with a given executable file name and return its process ID.
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550481">IDebugClient2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550494">IDebugClient4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient3 interface%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
