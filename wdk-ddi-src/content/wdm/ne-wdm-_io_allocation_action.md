---
UID: NE:wdm._IO_ALLOCATION_ACTION
title: "_IO_ALLOCATION_ACTION"
author: windows-driver-content
description: The IO_ALLOCATION_ACTION enumerated type is used to specify return values for AdapterControl and ControllerControl routines.
old-location: kernel\io_allocation_action.htm
old-project: kernel
ms.assetid: 245d35a1-e877-4446-a0da-e50ece3656b1
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: DeallocateObject, sysenum_26c04e01-0e17-4f1b-93c9-b9ad8d9ca4d5.xml, DeallocateObjectKeepRegisters, kernel.io_allocation_action, wdm/IO_ALLOCATION_ACTION, wdm/DeallocateObject, wdm/DeallocateObjectKeepRegisters, PIO_ALLOCATION_ACTION, _IO_ALLOCATION_ACTION, *PIO_ALLOCATION_ACTION, wdm/KeepObject, PIO_ALLOCATION_ACTION enumeration pointer [Kernel-Mode Driver Architecture], wdm/PIO_ALLOCATION_ACTION, KeepObject, IO_ALLOCATION_ACTION, IO_ALLOCATION_ACTION enumeration [Kernel-Mode Driver Architecture]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Windows
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Wdm.h
apiname:
-	IO_ALLOCATION_ACTION
product: Windows
targetos: Windows
req.typenames: IO_ALLOCATION_ACTION, *PIO_ALLOCATION_ACTION
req.product: Windows 10 or later.
---

# _IO_ALLOCATION_ACTION Enumeration
The <b>IO_ALLOCATION_ACTION</b> enumerated type is used to specify return values for <a href="..\wdm\nc-wdm-driver_control.md">AdapterControl</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff542049">ControllerControl</a> routines.

## Syntax
````
typedef enum _IO_ALLOCATION_ACTION { 
  KeepObject                     = 1,
  DeallocateObject               = 2,
  DeallocateObjectKeepRegisters  = 3
} IO_ALLOCATION_ACTION, *PIO_ALLOCATION_ACTION;
````

## Constants

<table>
            
                <tr>
                    <td>DeallocateObject</td>
                    <td>Indicates that you do not want the driver to retain ownership of the adapter or controller object.</td>
                </tr>
            
                <tr>
                    <td>DeallocateObjectKeepRegisters</td>
                    <td><u>For adapter objects only.</u> Indicates that you do not want the driver to retain ownership of the adapter object, but you do want the driver to retain ownership of the allocated map registers.</td>
                </tr>
            
                <tr>
                    <td>KeepObject</td>
                    <td>Indicates that you want the driver to retain ownership of the adapter or controller object.</td>
                </tr>
</table>

    ## Remarks

        If an <i>AdapterControl</i> or <i>ControllerControl</i> routine completes an IRP, or if it can set up an operation (such as a disk seek) for a target device object that could be overlapped with an operation for another device object, it should return <b>DeallocateObject</b>.

If a driver uses packet-based bus-master DMA, its <i>AdapterControl</i> routine should return <b>DeallocateObjectKeepRegisters</b>.

Otherwise, the driver should return <b>KeepObject</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h) |