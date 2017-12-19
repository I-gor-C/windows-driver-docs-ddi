---
UID: NF.ks.KsFilterAddEvent
title: KsFilterAddEvent function
author: windows-driver-content
description: The KsFilterAddEvent function adds an event to Filter's event list.
old-location: stream\ksfilteraddevent.htm
old-project: stream
ms.assetid: e93491c1-bd6d-4d89-b55f-10439b0f5eec
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: KsFilterAddEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsFilterAddEvent
req.alt-loc: ks.h
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
---

# KsFilterAddEvent function



## -description
The<b> KsFilterAddEvent</b> function adds an event to <i>Filter</i>'s event list.



## -syntax

````
void _inline KsFilterAddEvent(
  _In_ PKSFILTER      Filter,
  _In_ PKSEVENT_ENTRY EventEntry
);
````


## -parameters

### -param Filter [in]

<i>A pointer</i> to a <a href="stream.ksfilter">KSFILTER</a> structure representing the filter to which to add a specified event.


### -param EventEntry [in]

<i>A pointer</i> to an <a href="stream.ksevent_entry">KSEVENT_ENTRY</a> structure describing the event to add to <i>Filter</i>.


## -returns
None


## -remarks
This function is an inline function call to <a href="stream.ksaddevent">KsAddEvent</a>.


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
Version

</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ksaddevent">KsAddEvent</a>
</dt>
<dt>
<a href="stream.ksgenerateevents">KsGenerateEvents</a>
</dt>
<dt>
<a href="stream.ksevent_entry">KSEVENT_ENTRY</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterAddEvent function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

