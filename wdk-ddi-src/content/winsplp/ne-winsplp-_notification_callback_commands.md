---
UID : NE:winsplp._NOTIFICATION_CALLBACK_COMMANDS
title : "_NOTIFICATION_CALLBACK_COMMANDS"
author : windows-driver-content
description : "."
old-location : print\notification_callback_commands.htm
old-project : print
ms.assetid : D93D09AE-B0B8-4682-BBBA-1EEC952A733D
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : print.notification_callback_commands, NOTIFICATION_COMMAND_CONTEXT_RELEASE, winsplp/NOTIFICATION_CALLBACK_COMMANDS, NOTIFICATION_CALLBACK_COMMANDS, winsplp/NOTIFICATION_COMMAND_NOTIFY, NOTIFICATION_COMMAND_CONTEXT_ACQUIRE, NOTIFICATION_COMMAND_NOTIFY, _NOTIFICATION_CALLBACK_COMMANDS, winsplp/NOTIFICATION_COMMAND_CONTEXT_RELEASE, NOTIFICATION_CALLBACK_COMMANDS enumeration [Print Devices], winsplp/NOTIFICATION_COMMAND_CONTEXT_ACQUIRE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : winsplp.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : NOTIFICATION_CALLBACK_COMMANDS
req.product : Windows 10 or later.
---

# _NOTIFICATION_CALLBACK_COMMANDS Enumeration


## Syntax
````
typedef enum _NOTIFICATION_CALLBACK_COMMANDS { 
  NOTIFICATION_COMMAND_NOTIFY,
  NOTIFICATION_COMMAND_CONTEXT_ACQUIRE,
  NOTIFICATION_COMMAND_CONTEXT_RELEASE
} NOTIFICATION_CALLBACK_COMMANDS;
````

## Constants

<table>

<tr>
<td>NOTIFICATION_COMMAND_CONTEXT_ACQUIRE</td>
<td></td>
</tr>

<tr>
<td>NOTIFICATION_COMMAND_CONTEXT_RELEASE</td>
<td></td>
</tr>

<tr>
<td>NOTIFICATION_COMMAND_NOTIFY</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | winsplp.h |