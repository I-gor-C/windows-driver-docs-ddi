---
UID: NS.hbapiwmi._GetEventBuffer_OUT
title: GetEventBuffer_OUT
author: windows-driver-content
description: The GetEventBuffer_OUT structure is used to report the output parameter data of the GetEventBuffer WMI method to the WMI client.
old-location: storage\geteventbuffer_out.htm
old-project: storage
ms.assetid: 1ba41017-8c4b-49eb-b0ec-8e58c2673314
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetEventBuffer_OUT, GetEventBuffer_OUT, *PGetEventBuffer_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetEventBuffer_OUT
req.alt-loc: hbapiwmi.h
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
---

# GetEventBuffer_OUT structure



## -description
<p>The GetEventBuffer_OUT structure is used to report the output parameter data of the <a href="storage.geteventbuffer">GetEventBuffer</a> WMI method to the WMI client.</p>


## -syntax

````
typedef struct _GetEventBuffer_OUT {
  ULONG            HBAStatus;
  ULONG            EventCount;
  MSFC_EventBuffer Events[1];
} GetEventBuffer_OUT, *PGetEventBuffer_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>Contains a value associated with the WMI class qualifier <a href="storage.hba_status">HBA_STATUS</a> that indicates the result of an HBA query operation. </p>
</dd>

### -field <b>EventCount</b>

<dd>
<p>Indicates the number of events in <b>Events</b> that were retrieved by the <a href="storage.geteventbuffer">GetEventBuffer</a> WMI method.</p>
</dd>

### -field <b>Events</b>

<dd>
<p>Contains an array of type <a href="..\hbapiwmi\ns-hbapiwmi--msfc-eventbuffer.md">MSFC_EventBuffer</a> that contains the next events in the HBA's event queue.</p>
</dd>
</dl>

## -remarks
<p>The <a href="storage.geteventbuffer">GetEventBuffer</a> method retrieves the next events in the HBA's event queue. </p>

<p>The WMI tool suite generates a declaration of the GetEventBuffer_OUT structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbaadaptermethods_wmi_class">MSFC_HBAAdapterMethods WMI Class</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.geteventbuffer">GetEventBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GetEventBuffer_OUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
