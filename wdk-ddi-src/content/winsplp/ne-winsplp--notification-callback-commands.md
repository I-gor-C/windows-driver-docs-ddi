---
UID: NE.winsplp._NOTIFICATION_CALLBACK_COMMANDS
title: NOTIFICATION_CALLBACK_COMMANDS
author: windows-driver-content
description: TBD.
old-location: print\notification_callback_commands.htm
ms.assetid: D93D09AE-B0B8-4682-BBBA-1EEC952A733D
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
req.alt-api: NOTIFICATION_CALLBACK_COMMANDS
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

# NOTIFICATION_CALLBACK_COMMANDS enumeration



## -description
<p>TBD</p>


## -syntax

````
typedef enum _NOTIFICATION_CALLBACK_COMMANDS { 
  NOTIFICATION_COMMAND_NOTIFY,
  NOTIFICATION_COMMAND_CONTEXT_ACQUIRE,
  NOTIFICATION_COMMAND_CONTEXT_RELEASE
} NOTIFICATION_CALLBACK_COMMANDS;
````


## -enum-fields
<dl>

### -field <a id="NOTIFICATION_COMMAND_NOTIFY"></a><a id="notification_command_notify"></a><b>NOTIFICATION_COMMAND_NOTIFY</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="NOTIFICATION_COMMAND_CONTEXT_ACQUIRE"></a><a id="notification_command_context_acquire"></a><b>NOTIFICATION_COMMAND_CONTEXT_ACQUIRE</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="NOTIFICATION_COMMAND_CONTEXT_RELEASE"></a><a id="notification_command_context_release"></a><b>NOTIFICATION_COMMAND_CONTEXT_RELEASE</b>

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