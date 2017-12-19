---
UID: NF.dbgeng.IDebugControl3.GetCurrentEventIndex
title: IDebugControl3::GetCurrentEventIndex method
author: windows-driver-content
description: The GetCurrentEventIndex method returns the index of the current event within the current list of events for the current target, if such a list exists.
old-location: debugger\getcurrenteventindex.htm
old-project: Debugger
ms.assetid: 148cf294-0410-4704-93ce-338529a214ad
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugControl3, IDebugControl3::GetCurrentEventIndex, GetCurrentEventIndex
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl3.GetCurrentEventIndex
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

# IDebugControl3::GetCurrentEventIndex method



## -description
The <b>GetCurrentEventIndex</b> method returns the index of the current event within the current list of events for the current target, if such a list exists.



## -syntax

````
HRESULT GetCurrentEventIndex(
  [out] PULONG Index
);
````


## -parameters

### -param Index [out]

Receives the index of the current event in the target.  The index will be a number between zero and one less than the number of events returned by <a href="debugger.getnumberevents">GetNumberEvents</a>.  The index of the first event is zero.


## -returns
This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

 


## -remarks
Targets that do not have fixed sets of events will always return zero to <i>Index</i>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="debugger.getnumberevents">GetNumberEvents</a>
</dt>
<dt>
<a href="debugger.setnexteventindex">SetNextEventIndex</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugControl3::GetCurrentEventIndex method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

