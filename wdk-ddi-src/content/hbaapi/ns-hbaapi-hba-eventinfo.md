---
UID: NS.hbaapi.HBA_EventInfo
title: HBA_EventInfo
author: windows-driver-content
description: The HBA_EventInfo structure contains information about an event of the indicated type.
old-location: storage\hba_eventinfo.htm
old-project: storage
ms.assetid: fc6b73ac-f86c-4978-9d71-9bd8398c116b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_EventInfo, HBA_EVENTINFO, *PHBA_EVENTINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_EVENTINFO
req.alt-loc: hbaapi.h
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

# HBA_EventInfo structure



## -description
<p>The HBA_EventInfo structure contains information about an event of the indicated type.</p>


## -syntax

````
typedef struct HBA_EventInfo {
  HBA_UINT32 EventCode;
  union {
    HBA_LINK_EVENTINFO Link_EventInfo;
    HBA_RSCN_EVENTINFO RSCN_EventInfo;
    HBA_PTY_EVENTINFO  Pty_EventInfo;
  } Event;
} HBA_EVENTINFO, *PHBA_EVENTINFO;
````


## -struct-fields
<dl>

### -field <b>EventCode</b>

<dd>
<p>Contains a code indicating the type of event. The following table lists the values that this member can have:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>HBA_EVENT_LIP_OCCURRED</p>
</td>
<td>
<p>A loop initialization primitive event occurred.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_EVENT_LINK_UP</p>
</td>
<td>
<p>A link up event occurred. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_EVENT_LINK_DOWN</p>
</td>
<td>
<p>A link down event occurred. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_EVENT_LIP_RESET_OCCURRED</p>
</td>
<td>
<p>A loop initialization primitive resest event occurred.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_EVENT_RSCN</p>
</td>
<td>
<p>An RSCN event occurred.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_EVENT_PROPRIETARY</p>
</td>
<td>
<p>A proprietary event occurred. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Event</b>

<dd>
<dl>

### -field <b>Link_EventInfo</b>

<dd>
<p>Contains a structure of type <a href="..\hbaapi\ns-hbaapi-hba-link-eventinfo.md">HBA_Link_EventInfo</a> that holds information associated with a link event. </p>
</dd>

### -field <b>RSCN_EventInfo</b>

<dd>
<p>Contains a structure of type <a href="..\hbaapi\ns-hbaapi-hba-rscn-eventinfo.md">HBA_RSCN_EventInfo</a> that holds information associated with a link event.</p>
</dd>

### -field <b>Pty_EventInfo</b>

<dd>
<p>Contains a structure of type <a href="..\hbaapi\ns-hbaapi-hba-pty-eventinfo.md">HBA_Pty_EventInfo</a> that holds information associated with a link event.</p>
</dd>
</dl>
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
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hbaapi\ns-hbaapi-hba-link-eventinfo.md">HBA_Link_EventInfo</a>
</dt>
<dt>
<a href="..\hbaapi\ns-hbaapi-hba-pty-eventinfo.md">HBA_Pty_EventInfo</a>
</dt>
<dt>
<a href="..\hbaapi\ns-hbaapi-hba-rscn-eventinfo.md">HBA_RSCN_EventInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_EventInfo structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
