---
UID: NF.portcls.IInterruptSync.RegisterServiceRoutine
title: IInterruptSync::RegisterServiceRoutine
author: windows-driver-content
description: The RegisterServiceRoutine method registers an interrupt service routine (ISR) that is to be called when an interrupt occurs.
old-location: audio\iinterruptsync_registerserviceroutine.htm
ms.assetid: fb0650ee-24a6-4f64-9f16-dded0ccc79cd
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IInterruptSync.RegisterServiceRoutine
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: IInterruptSync, RegisterServiceRoutine, IInterruptSync::RegisterServiceRoutine
req.iface: IInterruptSync
---

# IInterruptSync::RegisterServiceRoutine method



## -description
<p>The <code>RegisterServiceRoutine</code> method registers an interrupt service routine (ISR) that is to be called when an interrupt occurs.</p>


## -syntax

````
NTSTATUS RegisterServiceRoutine(
  [in] PINTERRUPTSYNCROUTINE Routine,
  [in] PVOID                 DynamicContext,
  [in] BOOLEAN               First
);
````


## -parameters
<dl>

### -param <i>Routine</i> [in]

<dd>
<p>Pointer to the routine that is to be called. This parameter is a function pointer of type PINTERRUPTSYNCROUTINE (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536590">IInterruptSync</a>).</p>
</dd>

### -param <i>DynamicContext</i> [in]

<dd>
<p>Specifies a context value that is passed to the routine when it is called.</p>
</dd>

### -param <i>First</i> [in]

<dd>
<p>Specifies whether the routine is added at the head or tail of the list of ISRs. If <b>TRUE</b>, the routine is added at the head of the list. If <b>FALSE</b>, it is added at the tail.</p>
</dd>
</dl>

## -returns
<p><code>RegisterServiceRoutine</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>This method adds the specified routine to the synchronization object's list of ISRs. When an interrupt occurs, the routine at the head of the list is called first, and the routine at the tail is called last.</p>

<p>This method adds the specified routine to the synchronization object's list of ISRs. When an interrupt occurs, the routine at the head of the list is called first, and the routine at the tail is called last.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>