---
UID: NN.dbgeng.IDebugDataSpaces3
title: IDebugDataSpaces3
author: windows-driver-content
description: IDebugDataSpaces3 interface
old-location: debugger\idebugdataspaces3.htm
old-project: debugger
ms.assetid: a5da1ed0-c4e6-4ab8-b581-64bc7d0519f2
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
req.alt-api: IDebugDataSpaces3
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

# IDebugDataSpaces3 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugDataSpaces3</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff550531">IDebugDataSpaces2</a>. <b>IDebugDataSpaces3</b> also has these types of members:</p>

<p>The <b>IDebugDataSpaces3</b> interface has these methods.</p>

<p>Releases the resources used by the specified enumeration.</p>

<p>Returns the GUID for the next block of tagged data in the enumeration.
</p>

<p>Returns the NT headers for the specified image loaded in the target.
</p>

<p>Reads the tagged data that might be associated with a debugger session.
</p>

<p>Initializes a enumeration over the tagged data associated with a debugger session.
</p>

<p> </p>

## -members
<p>The <b>IDebugDataSpaces3</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542978">EndEnumTagged</a>
</td>
<td align="left" width="63%">
<p>Releases the resources used by the specified enumeration.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547874">GetNextTagged</a>
</td>
<td align="left" width="63%">
<p>Returns the GUID for the next block of tagged data in the enumeration.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553544">ReadImageNtHeaders</a>
</td>
<td align="left" width="63%">
<p>Returns the NT headers for the specified image loaded in the target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554336">ReadTagged</a>
</td>
<td align="left" width="63%">
<p>Reads the tagged data that might be associated with a debugger session.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558801">StartEnumTagged</a>
</td>
<td align="left" width="63%">
<p>Initializes a enumeration over the tagged data associated with a debugger session.
</p>
</td>
</tr>
</table><p>Releases the resources used by the specified enumeration.</p>

<p>Returns the GUID for the next block of tagged data in the enumeration.
</p>

<p>Returns the NT headers for the specified image loaded in the target.
</p>

<p>Reads the tagged data that might be associated with a debugger session.
</p>

<p>Initializes a enumeration over the tagged data associated with a debugger session.
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550528">IDebugDataSpaces</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550531">IDebugDataSpaces2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550546">IDebugDataSpaces4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces3 interface%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
