---
UID: NS.hbapiwmi._MSFC_PortEvent
title: MSFC_PortEvent
author: windows-driver-content
description: A WMI provider uses the MSFC_PortEvent structure to report port events for the indicated adapter.
old-location: storage\msfc_portevent.htm
ms.assetid: bf9e2d58-9379-4b88-9043-580a97ec7cd9
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSFC_PortEvent
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
ms.keywords: MSFC_PortEvent, MSFC_PortEvent, *PMSFC_PortEvent
req.iface: 
---

# MSFC_PortEvent structure



## -description
<p>A WMI provider uses the MSFC_PortEvent structure to report port events for the indicated adapter.</p>


## -syntax

````
typedef struct _MSFC_PortEvent {
  ULONG EventType;
  ULONG FabricPortId;
  UCHAR PortWWN[8];
} MSFC_PortEvent, *PMSFC_PortEvent;
````


## -struct-fields
<dl>

### -field <b>EventType</b>

<dd>
<p>Indicates the type of the event. The values that can be assigned to this member are defined by the <a href="https://msdn.microsoft.com/528e5eaa-aaeb-4e5b-a4b2-0f518fcd79ee">EVENT_TYPE_QUALIFIERS</a> WMI class qualifier.</p>
</dd>

### -field <b>FabricPortId</b>

<dd>
<p>Contains the fabric port ID. </p>
</dd>

### -field <b>PortWWN</b>

<dd>
<p>Contains the worldwide name that indicates the port for which the event occurred. </p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/528e5eaa-aaeb-4e5b-a4b2-0f518fcd79ee">EVENT_TYPE_QUALIFIERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MSFC_PortEvent structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
