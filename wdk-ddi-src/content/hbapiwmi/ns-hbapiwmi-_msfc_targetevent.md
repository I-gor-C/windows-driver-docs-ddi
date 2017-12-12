---
UID: NS.HBAPIWMI._MSFC_TARGETEVENT
title: _MSFC_TargetEvent
author: windows-driver-content
description: A WMI provider uses the MSFC_TargetEvent structure to report port events for the indicated adapter.
old-location: storage\msfc_targetevent.htm
old-project: storage
ms.assetid: e34e505c-74b1-45e4-9d9f-ba7cae111156
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _MSFC_TargetEvent, MSFC_TargetEvent, *PMSFC_TargetEvent
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
req.alt-api: MSFC_TargetEvent
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
---

# _MSFC_TargetEvent structure



## -description
A WMI provider uses the MSFC_TargetEvent structure to report port events for the indicated adapter.



## -syntax

````
typedef struct _MSFC_TargetEvent {
  ULONG EventType;
  UCHAR PortWWN[8];
  UCHAR DiscoveredPortWWN[8];
} MSFC_TargetEvent, *PMSFC_TargetEvent;
````


## -struct-fields

### -field EventType

Indicates the type of the event. The values that can be assigned to this member are defined by the <a href="storage.event_types_qualifiers">EVENT_TYPE_QUALIFIERS</a> WMI class qualifier.


### -field PortWWN

Contains a worldwide name that indicates the local port for which the event occurred. 


### -field DiscoveredPortWWN

Contains a worldwide name that indicates the remote port for which the event occurred.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="storage.event_types_qualifiers">EVENT_TYPE_QUALIFIERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MSFC_TargetEvent structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

