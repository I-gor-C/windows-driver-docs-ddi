---
UID: NE.winsplp._NOTIFICATION_CALLBACK_COMMANDS
title: NOTIFICATION_CALLBACK_COMMANDS
author: windows-driver-content
description: .
old-location: print\notification_callback_commands.htm
old-project: print
ms.assetid: D93D09AE-B0B8-4682-BBBA-1EEC952A733D
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: SCARD_IO_REQUEST, SCARD_IO_REQUEST, *PSCARD_IO_REQUEST, *LPSCARD_IO_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: winsplp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NOTIFICATION_CALLBACK_COMMANDS
req.alt-loc: Winsplp.h
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

# NOTIFICATION_CALLBACK_COMMANDS enumeration



## -description
<p></p>


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

### -field NOTIFICATION_COMMAND_NOTIFY

<dd></dd>

### -field NOTIFICATION_COMMAND_CONTEXT_ACQUIRE

<dd></dd>

### -field NOTIFICATION_COMMAND_CONTEXT_RELEASE

<dd></dd>
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