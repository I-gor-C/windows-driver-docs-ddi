---
UID: NN.dbgeng.IDebugEventContextCallbacks
title: IDebugEventContextCallbacks
author: windows-driver-content
description: This interface supports event context callbacks and replaces the use of the IDebugClient::SetEventCallbacks method.
old-location: debugger\idebugeventcontextcallbacks.htm
old-project: debugger
ms.assetid: F4FAA5C9-B7D9-43B6-8B1D-CA790522900C
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
req.alt-api: IDebugEventContextCallbacks
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

# IDebugEventContextCallbacks interface



## -description
This interface supports event context callbacks and replaces the use of the <a href="debugger.seteventcallbacks">IDebugClient::SetEventCallbacks</a> method.
Set this interface on a debugger client by using the <a href="debugger.idebugclient6_seteventcontextcallbacks">IDebugClient6::SetEventContextCallbacks</a> method.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugEventContextCallbacks</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface but does not have additional members.

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
<a href="debugger.seteventcallbacks">IDebugClient::SetEventCallbacks</a>
</dt>
<dt>
<a href="debugger.idebugclient6_seteventcontextcallbacks">IDebugClient6::SetEventContextCallbacks</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugEventContextCallbacks interface%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
