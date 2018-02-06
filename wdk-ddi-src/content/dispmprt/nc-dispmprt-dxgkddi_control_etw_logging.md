---
UID: NC:dispmprt.DXGKDDI_CONTROL_ETW_LOGGING
title: DXGKDDI_CONTROL_ETW_LOGGING
author: windows-driver-content
description: The DxgkDdiControlEtwLogging function enables or disables Event Tracing for Windows (ETW) event logging.
old-location: display\dxgkddicontroletwlogging.htm
old-project: display
ms.assetid: c94a43bb-19d0-4894-80b0-885562fefea5
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.dxgkddicontroletwlogging, DxgkDdiControlEtwLogging callback function [Display Devices], DxgkDdiControlEtwLogging, DXGKDDI_CONTROL_ETW_LOGGING, DXGKDDI_CONTROL_ETW_LOGGING, dispmprt/DxgkDdiControlEtwLogging, DmFunctions_87548564-6b7b-431b-b68c-202af84deefc.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	dispmprt.h
apiname:
-	DxgkDdiControlEtwLogging
product: Windows
targetos: Windows
req.typenames: SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
---


# DXGKDDI_CONTROL_ETW_LOGGING function
The <i>DxgkDdiControlEtwLogging </i>function enables or disables Event Tracing for Windows (ETW) event logging.

## Syntax

```
DXGKDDI_CONTROL_ETW_LOGGING DxgkddiControlEtwLogging;

void DxgkddiControlEtwLogging(
  IN_BOOLEAN Enable,
  IN_ULONG Flags,
  IN_UCHAR Level
)
{...}
```

## Parameters

`Enable`

A Boolean value that indicates whether <i>DxgkDdiControlEtwLogging </i>enables or disables ETW event logging. <b>TRUE</b> indicates that it enables and <b>FALSE</b> indicates that it disables.

`Flags`

A valid bitwise OR of values. Currently, no flags are defined.

`Level`

A value that indicates the level of event logging.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | dispmprt.h (include Dispmprt.h) |
| **IRQL** | PASSIVE_LEVEL |