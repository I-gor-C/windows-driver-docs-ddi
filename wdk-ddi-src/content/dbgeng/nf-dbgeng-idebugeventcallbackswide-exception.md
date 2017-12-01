---
UID: NF.dbgeng.IDebugEventCallbacksWide.Exception
title: IDebugEventCallbacksWide::Exception
author: windows-driver-content
description: The Exception callback method is called by the engine when an exceptiondebugging event occurs in the target.
old-location: debugger\idebugeventcallbackswide_exception.htm
old-project: debugger
ms.assetid: 02f5bec1-f2d2-4b72-bd9e-b30315c334da
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugEventCallbacksWide, Exception, IDebugEventCallbacksWide::Exception
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugEventCallbacksWide.Exception
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
req.iface: IDebugEventCallbacksWide
---

# IDebugEventCallbacksWide::Exception method



## -description
<p>The <b>Exception</b> callback method is called by the engine when an <a href="wdkgloss.e#wdkgloss.exception#wdkgloss.exception"><i>exception</i></a>debugging event occurs in the target.</p>


## -syntax

````
HRESULT Exception(
  [in] PEXCEPTION_RECORD64 Exception,
  [in] ULONG               FirstChance
);
````


## -parameters
<dl>

### -param <i>Exception</i> [in]

<dd>
<p>Specifies the nature of the exception.  EXCEPTION_RECORD64 is defined in Winnt.h.</p>
</dd>

### -param <i>FirstChance</i> [in]

<dd>
<p>Specifies whether this exception has been previously encountered.  A nonzero value means that this is the first time the exception has been encountered ("first chance").  A zero value means that the exception has already been offered to all possible handlers, and each one declined to handle it ("second chance").</p>
</dd>
</dl>

## -returns
<p>This method returns a <a href="debugger.debug_status_xxx">DEBUG_STATUS_XXX</a> value, which indicates how the execution of the target should proceed after the engine processes this event.  For details on how the engine treats this value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.</p>

## -remarks
<p>This method is only called by the engine if the DEBUG_EVENT_EXCEPTION flag is set in the mask returned by <a href="debugger.idebugeventcallbackswide_getinterestmask">IDebugEventCallbacksWide::GetInterestMask</a>.</p>

<p>Because the structure that <i>Exception</i> points to might be deleted after this method returns, implementations of <b>IDebugEventCallbacksWide</b> should not access this structure after returning.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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