---
UID: NS.netdispumdddi.MIRACAST_SESSION_INFO
title: MIRACAST_SESSION_INFO
author: windows-driver-content
description: Contains info on a wireless display (Miracast) connected session.
old-location: display\miracast_session_info.htm
ms.assetid: 48F3CB86-5181-4E1E-9E7F-88FB2CD3640A
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MIRACAST_SESSION_INFO
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
ms.keywords: MIRACAST_SESSION_INFO, MIRACAST_SESSION_INFO
req.iface: 
---

# MIRACAST_SESSION_INFO structure



## -description
<p>Contains info on a wireless display (Miracast) connected session.</p>


## -syntax

````
typedef union {
  struct {
    UINT MonitorConnected  :1;
    UINT ReducedModeListDueToBandwidth  :1;
    UINT Reserved  :30;
  };
  UINT Value;
} MIRACAST_SESSION_INFO;
````


## -struct-fields
<dl>

### -field <b>MonitorConnected</b>

<dd>
<p>If set, the monitor (the source) is connected to a Miracast sink.</p>
</dd>

### -field <b>ReducedModeListDueToBandwidth</b>

<dd>
<p>If set, the user-mode driver has reduced the modes exposed to the operating system based on the current suggested encode rate.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use and should be set to zero.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>Holds a 32-bit value that identifies the Miracast connected session.</p>
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