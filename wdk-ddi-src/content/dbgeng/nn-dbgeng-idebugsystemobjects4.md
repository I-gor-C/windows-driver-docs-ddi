---
UID: NN.dbgeng.IDebugSystemObjects4
title: IDebugSystemObjects4
author: windows-driver-content
description: IDebugSystemObjects4 interface
old-location: debugger\idebugsystemobjects4.htm
old-project: debugger
ms.assetid: 075143eb-03c4-41b2-b419-4618ed103843
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
req.alt-api: IDebugSystemObjects4,IDebugSystemObjects4.GetCurrentSystemServerNameWide
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

# IDebugSystemObjects4 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSystemObjects4</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff550892">IDebugSystemObjects3</a>. <b>IDebugSystemObjects4</b> also has these types of members:</p>

<p>The <b>IDebugSystemObjects4</b> interface has these methods.</p>

<p>Returns the name of executable file loaded in the current process.</p>

<p></p>

<p> </p>

## -members
<p>The <b>IDebugSystemObjects4</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545804">GetCurrentProcessExecutableNameWide</a>
</td>
<td align="left" width="63%">
<p>Returns the name of executable file loaded in the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetCurrentSystemServerNameWide</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
</table><p>Returns the name of executable file loaded in the current process.</p>

<p></p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550875">IDebugSystemObjects</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550885">IDebugSystemObjects2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550892">IDebugSystemObjects3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSystemObjects4 interface%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
