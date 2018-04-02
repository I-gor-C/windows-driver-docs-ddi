---
UID: NC:ntdd8042.PI8042_KEYBOARD_INITIALIZATION_ROUTINE
title: PI8042_KEYBOARD_INITIALIZATION_ROUTINE
author: windows-driver-content
description: A PI8042_KEYBOARD_INITIALIZATION_ROUTINE-typed callback routine supplements the default initialization of a keyboard device by I8042prt.
old-location: hid\pi8042_keyboard_initialization_routine.htm
old-project: hid
ms.assetid: bc1c82f0-f68c-433c-87f0-16c687d18557
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: KeyboardInitializationRoutine, KeyboardInitializationRoutine callback function [Human Input Devices], PI8042_KEYBOARD_INITIALIZATION_ROUTINE, hid.pi8042_keyboard_initialization_routine, i8042ref_4bc54efc-bd3d-4091-a8c7-64631d187d20.xml, ntdd8042/KeyboardInitializationRoutine
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntdd8042.h
req.include-header: Ntdd8042.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	ntdd8042.h
api_name:
-	KeyboardInitializationRoutine
product:
- Windows
targetos: Windows
req.typenames: MSFC_VirtualFibrePortAttributes, *PMSFC_VirtualFibrePortAttributes
---


# PI8042_KEYBOARD_INITIALIZATION_ROUTINE callback function
A PI8042_KEYBOARD_INITIALIZATION_ROUTINE-typed callback routine supplements the default initialization of a keyboard device by I8042prt.

## Syntax

```
PI8042_KEYBOARD_INITIALIZATION_ROUTINE Pi8042KeyboardInitializationRoutine;

NTSTATUS Pi8042KeyboardInitializationRoutine(
  PVOID InitializationContext,
  PVOID SynchFuncContext,
  PI8042_SYNCH_READ_PORT ReadPort,
  PI8042_SYNCH_WRITE_PORT WritePort,
  PBOOLEAN TurnTranslationOn
)
{...}
```

## Parameters

`InitializationContext`

Pointer to the filter device object of the driver that supplies the callback.

`SynchFuncContext`

Pointer to the context for the callbacks that are pointed to by <i>ReadPort</i> and <i>Writeport.</i>

`ReadPort`

Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543272">PI8042_SYNCH_READ_PORT</a> callback that reads from the port.

`WritePort`

Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543276">PI8042_SYNCH_WRITE_PORT</a> callback that writes to the port.

`TurnTranslationOn`

Specifies whether to turn translation on or off. If <i>TranslationOn</i> is <b>TRUE</b>, translation is turned on; otherwise, translation is turned off.


## Return Value

A PI8042_KEYBOARD_INITIALIZATION_ROUTINE callback returns an appropriate NTSTATUS code.

## Remarks

An upper-level keyboard filter driver can provide a PI8042_KEYBOARD_INITIALIZATION_ROUTINE callback.

If an upper-level keyboard filter driver supplies an initialization callback, I8042prt calls the filter initialization callback when I8042prt initializes the keyboard. Default keyboard initialization includes the following operations: reset the keyboard, set the typematic rate and delay, and set the light-emitting diodes (LED).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ntdd8042.h (include Ntdd8042.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543272">PI8042_SYNCH_READ_PORT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543276">PI8042_SYNCH_WRITE_PORT</a>