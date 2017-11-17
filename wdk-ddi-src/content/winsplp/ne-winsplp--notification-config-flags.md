---
UID: NE.winsplp._NOTIFICATION_CONFIG_FLAGS
title: NOTIFICATION_CONFIG_FLAGS
author: windows-driver-content
description: TBD.
old-location: print\notification_config_flags.htm
ms.assetid: B53AB706-D780-4E29-A531-51D3A9041D24
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: print
req.header: winsplp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NOTIFICATION_CONFIG_FLAGS
req.alt-loc: 
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
ms.keywords: GdiStartPageEMF
req.iface: 
req.product: Windows 10 or later.
---

# NOTIFICATION_CONFIG_FLAGS enumeration



## -description
<p>TBD</p>


## -syntax

````
typedef enum _NOTIFICATION_CONFIG_FLAGS { 
  NOTIFICATION_CONFIG_CREATE_EVENT       = 1 << 0,
  NOTIFICATION_CONFIG_REGISTER_CALLBACK  = 1 << 1,
  NOTIFICATION_CONFIG_EVENT_TRIGGER      = 1 << 2,
  NOTIFICATION_CONFIG_ASYNC_CHANNEL      = 1 << 3
} NOTIFICATION_CONFIG_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="NOTIFICATION_CONFIG_CREATE_EVENT"></a><a id="notification_config_create_event"></a><b>NOTIFICATION_CONFIG_CREATE_EVENT</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="NOTIFICATION_CONFIG_REGISTER_CALLBACK"></a><a id="notification_config_register_callback"></a><b>NOTIFICATION_CONFIG_REGISTER_CALLBACK</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="NOTIFICATION_CONFIG_EVENT_TRIGGER"></a><a id="notification_config_event_trigger"></a><b>NOTIFICATION_CONFIG_EVENT_TRIGGER</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="NOTIFICATION_CONFIG_ASYNC_CHANNEL"></a><a id="notification_config_async_channel"></a><b>NOTIFICATION_CONFIG_ASYNC_CHANNEL</b>

<dd>
<p>TBD</p>
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
<dt>Winsplp.h</dt>
</dl>
</td>
</tr>
</table>