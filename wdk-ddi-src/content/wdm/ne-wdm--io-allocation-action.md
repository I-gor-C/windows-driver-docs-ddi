---
UID: NE.wdm._IO_ALLOCATION_ACTION
title: IO_ALLOCATION_ACTION
author: windows-driver-content
description: The IO_ALLOCATION_ACTION enumerated type is used to specify return values for AdapterControl and ControllerControl routines.
old-location: kernel\io_allocation_action.htm
old-project: kernel
ms.assetid: 245d35a1-e877-4446-a0da-e50ece3656b1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
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
req.alt-api: IO_ALLOCATION_ACTION
req.alt-loc: Wdm.h
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
req.iface: 
req.product: Windows 10 or later.
---

# IO_ALLOCATION_ACTION enumeration



## -description
<p>The <b>IO_ALLOCATION_ACTION</b> enumerated type is used to specify return values for <a href="kernel.adaptercontrol">AdapterControl</a> and <a href="..\wdm\nc-wdm-driver-control.md">ControllerControl</a> routines.</p>


## -syntax

````
typedef enum _IO_ALLOCATION_ACTION { 
  KeepObject                     = 1,
  DeallocateObject               = 2,
  DeallocateObjectKeepRegisters  = 3
} IO_ALLOCATION_ACTION, *PIO_ALLOCATION_ACTION;
````


## -enum-fields
<dl>

### -field KeepObject

<dd>
<p>Indicates that you want the driver to retain ownership of the adapter or controller object.</p>
</dd>

### -field DeallocateObject

<dd>
<p>Indicates that you do not want the driver to retain ownership of the adapter or controller object.</p>
</dd>

### -field DeallocateObjectKeepRegisters

<dd>
<p><u>For adapter objects only.</u> Indicates that you do not want the driver to retain ownership of the adapter object, but you do want the driver to retain ownership of the allocated map registers. </p>
</dd>
</dl>

## -remarks
<p>If an <i>AdapterControl</i> or <i>ControllerControl</i> routine completes an IRP, or if it can set up an operation (such as a disk seek) for a target device object that could be overlapped with an operation for another device object, it should return <b>DeallocateObject</b>.</p>

<p>If a driver uses packet-based bus-master DMA, its <i>AdapterControl</i> routine should return <b>DeallocateObjectKeepRegisters</b>.</p>

<p>Otherwise, the driver should return <b>KeepObject</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>