---
UID: NS.netdispumdddi.MIRACAST_STATISTIC_DATA
title: MIRACAST_STATISTIC_DATA
author: windows-driver-content
description: Contains Miracast statistics data that the user-mode display driver reports to the operating system.
old-location: display\miracast_statistic_data.htm
old-project: display
ms.assetid: 94D5C260-4076-4DB7-8ED3-E0549A872FEE
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: MIRACAST_STATISTIC_DATA, MIRACAST_STATISTIC_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MIRACAST_STATISTIC_DATA
req.alt-loc: Netdispumdddi.h
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

# MIRACAST_STATISTIC_DATA structure



## -description
<p>Contains Miracast statistics data that the user-mode display driver reports to the operating system.</p>


## -syntax

````
typedef struct {
  MIRACAST_STATISTIC_TYPE StatisticType;
  union {
    struct {
      MIRACAST_CHUNK_INFO ChunkInfo;
    } EncodeComplete;
    struct {
      MIRACAST_CHUNK_ID ChunkId;
    } ChunkSent;
    struct {
      MIRACAST_PROTOCOL_EVENT Event;
    } ProtocolEvent;
  };
} MIRACAST_STATISTIC_DATA;
````


## -struct-fields
<dl>

### -field <b>StatisticType</b>

<dd>
<p>The type of statistics data from the <a href="..\netdispumdddi\ne-netdispumdddi-miracast-statistic-type.md">MIRACAST_STATISTIC_TYPE</a> enumeration.</p>
</dd>

### -field <b>EncodeComplete</b>

<dd>
<dl>

### -field <b>ChunkInfo</b>

<dd>
<p>A <a href="..\netdispumdddi\ns-netdispumdddi-miracast-chunk-info.md">MIRACAST_CHUNK_INFO</a> structure that provides info about an encode chunk that is identified by the <b>ChunkId</b> member.</p>
</dd>
</dl>
</dd>

### -field <b>ChunkSent</b>

<dd>
<dl>

### -field <b>ChunkId</b>

<dd>
<p>The identifier for this chunk, of type <a href="..\netdispumdddi\ns-netdispumdddi-miracast-chunk-id.md">MIRACAST_CHUNK_ID</a>.</p>
</dd>
</dl>
</dd>

### -field <b>ProtocolEvent</b>

<dd>
<dl>

### -field <b>Event</b>

<dd>
<p>The type of protocol event, given as a value of the <a href="..\netdispumdddi\ne-netdispumdddi-miracast-protocol-event.md">MIRACAST_PROTOCOL_EVENT</a> enumeration.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\netdispumdddi\ns-netdispumdddi-miracast-chunk-id.md">MIRACAST_CHUNK_ID</a>
</dt>
<dt>
<a href="..\netdispumdddi\ns-netdispumdddi-miracast-chunk-info.md">MIRACAST_CHUNK_INFO</a>
</dt>
<dt>
<a href="..\netdispumdddi\ne-netdispumdddi-miracast-protocol-event.md">MIRACAST_PROTOCOL_EVENT</a>
</dt>
<dt>
<a href="..\netdispumdddi\ne-netdispumdddi-miracast-statistic-type.md">MIRACAST_STATISTIC_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20MIRACAST_STATISTIC_DATA structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
