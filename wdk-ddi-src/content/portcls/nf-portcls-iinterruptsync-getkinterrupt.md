---
UID: NF.portcls.IInterruptSync.GetKInterrupt
title: IInterruptSync::GetKInterrupt
author: windows-driver-content
description: The GetKInterrupt method gets a WDM interrupt object from a port-class synchronization object.
old-location: audio\iinterruptsync_getkinterrupt.htm
old-project: audio
ms.assetid: 045c509b-852d-405c-9615-8a2f351bf8c7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IInterruptSync, GetKInterrupt, IInterruptSync::GetKInterrupt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IInterruptSync.GetKInterrupt
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
req.irql: Any level
req.iface: IInterruptSync
---

# IInterruptSync::GetKInterrupt method



## -description
<p>The <code>GetKInterrupt</code> method gets a WDM interrupt object from a port-class synchronization object.</p>


## -syntax

````
PKINTERRUPT GetKInterrupt(
    None
);
````


## -parameters
<dl>

### -param None 

<dd></dd>
</dl>

## -returns
<p><code>GetKInterrupt</code> returns a pointer to a WDM interrupt object.</p>

## -remarks
<p>The PKINTERRUPT pointer is one of the two parameters that are passed to every interrupt service routine (see <a href="kernel.interruptservice">InterruptService</a>). Every <b>IInterruptSync</b> object has an associated PKINTERRUPT pointer. It points to the associated kernel interrupt object, which is opaque.</p>

<p>A driver typically calls <code>GetKInterrupt</code> only if it needs to obtain this pointer so that it can call <a href="..\wdm\nf-wdm-kesynchronizeexecution.md">KeSynchronizeExecution</a> directly.</p>

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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iinterruptsync.md">IInterruptSync</a>
</dt>
<dt>
<a href="kernel.interruptservice">InterruptService</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kesynchronizeexecution.md">KeSynchronizeExecution</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IInterruptSync::GetKInterrupt method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
