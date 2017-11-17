---
UID: NL.dbgeng.DebugBaseEventCallbacksWide
title: DebugBaseEventCallbacksWide
author: windows-driver-content
description: The DebugBaseEventCallbacksWide class provides a base implementation of the IDebugEventCallbacksWide interface.
old-location: debugger\debugbaseeventcallbackswide.htm
ms.assetid: 38AD8472-1BA3-42EA-99CE-E91098A5B334
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
req.alt-api: DebugBaseEventCallbacksWide
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

# DebugBaseEventCallbacksWide interface



## -description
<p>The <b>DebugBaseEventCallbacksWide</b> class provides a base implementation
of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550563">IDebugEventCallbacksWide</a> interface.  </p>
<p>A program can derive an event callbacks class from <b>DebugBaseEventCallbacksWide</b> and implement
only the methods needed. </p>
<p>Be careful to implement <a href="https://msdn.microsoft.com/b1e62ae3-4a3d-42db-b7fe-87d1a7e0b438">GetInterestMask</a> appropriately.</p>


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550563">IDebugEventCallbacksWide</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b1e62ae3-4a3d-42db-b7fe-87d1a7e0b438">GetInterestMask</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20DebugBaseEventCallbacksWide class%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
