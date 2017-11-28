---
UID: NF.umdprovider.UMDEtwUnregister~r1
title: UMDEtwUnregister
author: windows-driver-content
description: Unregisters the event trace provider. Call this function before the user-mode driver is unloaded. After this function is called, the driver should not make any other calls to log events.
old-location: display\umdetwunregister.htm
old-project: display
ms.assetid: 19ab8771-2a86-469a-98e4-3d295a458b90
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: UMDEtwUnregister
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: umdprovider.h
req.include-header: Umdprovider.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UMDEtwUnregister
req.alt-loc: umdprovider.h
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
req.iface: 
req.product: Windows 10 or later.
---

# UMDEtwUnregister function



## -description
<p>Unregisters the event trace provider. Call this function before the user-mode driver is unloaded. After this function is called, the driver should not make any other calls to log events.</p>


## -syntax

````
void UMDEtwUnregister(void);
````


## -parameters


## -returns
<p>This function does not return a value.</p>

<p>This function does not return a value.</p>

<p>This function does not return a value.</p>

## -remarks
<p><b>UMDEtwUnregister</b> is defined inline in Umdprovider.h as:</p>

<p>The <a href="etw.eventunregister_func">EventUnregister</a> function is  described in the <a href="events.windows_events">Windows Events</a> documentation.</p>

<p><b>UMDEtwUnregister</b> is defined inline in Umdprovider.h as:</p>

<p>The <a href="etw.eventunregister_func">EventUnregister</a> function is  described in the <a href="events.windows_events">Windows Events</a> documentation.</p>

<p><b>UMDEtwUnregister</b> is defined inline in Umdprovider.h as:</p>

<p>The <a href="etw.eventunregister_func">EventUnregister</a> function is  described in the <a href="events.windows_events">Windows Events</a> documentation.</p>

<p><b>UMDEtwUnregister</b> is defined inline in Umdprovider.h as:</p>

<p>The <a href="etw.eventunregister_func">EventUnregister</a> function is  described in the <a href="events.windows_events">Windows Events</a> documentation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<dt>Umdprovider.h (include Umdprovider.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj542439">UMDEtwRegister</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20UMDEtwUnregister function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
