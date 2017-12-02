---
UID: NN.dbgeng.IDebugSystemObjects2
title: IDebugSystemObjects2
author: windows-driver-content
description: IDebugSystemObjects2 interface
old-location: debugger\idebugsystemobjects2.htm
old-project: debugger
ms.assetid: 9e354357-590b-45cf-bace-5b431f408422
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: IDebugSystemObjects2
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

# IDebugSystemObjects2 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSystemObjects2</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugsystemobjects.md">IDebugSystemObjects</a>. <b>IDebugSystemObjects2</b> also has these types of members:</p>

<p>The <b>IDebugSystemObjects2</b> interface has these methods.</p>

<p>Returns the length of time the current process has been running.</p>

<p>Returns the implicit process for the current target.</p>

<p>Returns the implicit thread for the current process.
</p>

<p>Sets the implicit process for the current target.</p>

<p>Sets the implicit thread for the current process.</p>

<p> </p>

## -members
<p>The <b>IDebugSystemObjects2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentprocessuptime">GetCurrentProcessUpTime</a>
</td>
<td align="left" width="63%">
<p>Returns the length of time the current process has been running.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getimplicitprocessdataoffset">GetImplicitProcessDataOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the implicit process for the current target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getimplicitthreaddataoffset">GetImplicitThreadDataOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the implicit thread for the current process.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setimplicitprocessdataoffset">SetImplicitProcessDataOffset</a>
</td>
<td align="left" width="63%">
<p>Sets the implicit process for the current target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setimplicitthreaddataoffset">SetImplicitThreadDataOffset</a>
</td>
<td align="left" width="63%">
<p>Sets the implicit thread for the current process.</p>
</td>
</tr>
</table><p>Returns the length of time the current process has been running.</p>

<p>Returns the implicit process for the current target.</p>

<p>Returns the implicit thread for the current process.
</p>

<p>Sets the implicit process for the current target.</p>

<p>Sets the implicit thread for the current process.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects.md">IDebugSystemObjects</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects3.md">IDebugSystemObjects3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects4.md">IDebugSystemObjects4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSystemObjects2 interface%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
