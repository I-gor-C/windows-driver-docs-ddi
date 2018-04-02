---
UID: NF:wdbgexts.WritePhysical
title: WritePhysical function
author: windows-driver-content
description: The WritePhysical function writes to physical memory.
old-location: debugger\writephysical.htm
old-project: debugger
ms.assetid: faafaf0a-29ef-43ef-9f9a-f3b545e83f65
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: WdbgExts_Ref_4c6663a7-4fbf-4d4a-9c86-cfa51218a470.xml, WritePhysical, WritePhysical function [Windows Debugging], dbgeng/WritePhysical, debugger.writephysical
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Dbgeng.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	dbgeng.h
api_name:
-	WritePhysical
product:
- Windows
targetos: Windows
req.typenames: EXT_TDOP
req.product: Windows 10 or later.
---


# WritePhysical function
The <b>WritePhysical</b> function writes to physical memory.

## Syntax

```
void WritePhysical(
  ULONG64 address,
  PVOID   buf,
  ULONG   size,
  PULONG  sizew
);
```

## Parameters

`address`

Specifies the physical address to write.

`buf`

Specifies the address of an array of bytes to hold the data that is written.

`size`

Specifies the number of bytes to write.

`sizew`

Receives the number of bytes actually written.


## Return Value

None

## Remarks

For a WdbgExts extension, include wdbgexts.h. For a DbgEng extension, include wdbgexts.h before dbgeng.h. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | wdbgexts.h (include Wdbgexts.h, Dbgeng.h) |