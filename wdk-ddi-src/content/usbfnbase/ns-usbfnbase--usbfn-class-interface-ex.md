---
UID: NS.usbfnbase._USBFN_CLASS_INTERFACE_EX
title: USBFN_CLASS_INTERFACE_EX
author: windows-driver-content
description: Describes an interface and its endpoints.
old-location: buses\usbfn_class_interface_ex.htm
old-project: usbref
ms.assetid: DEA417E7-FA4B-4F72-A03A-ECE921FC725C
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBFN_CLASS_INTERFACE_EX, USBFN_CLASS_INTERFACE_EX, *PUSBFN_CLASS_INTERFACE_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbfnbase.h
req.include-header: TBD
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBFN_CLASS_INTERFACE_EX
req.alt-loc: usbfnbase.h
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

# USBFN_CLASS_INTERFACE_EX structure



## -description
<p>Describes an interface and its endpoints.</p>


## -syntax

````
typedef struct _USBFN_CLASS_INTERFACE_EX {
  UINT8                  BaseInterfaceNumber;
  UINT8                  InterfaceCount;
  UINT8                  PipeCount;
  USBFN_PIPE_INFORMATION PipeArr[MAX_NUM_USBFN_PIPES];
} USBFN_CLASS_INTERFACE_EX, *PUSBFN_CLASS_INTERFACE_EX;
````


## -struct-fields
<dl>

### -field BaseInterfaceNumber

<dd>
<p>The index number of the interface.</p>
</dd>

### -field InterfaceCount

<dd>
<p>The number of USB interfaces contained in  the selected function.</p>
</dd>

### -field PipeCount

<dd>
<p>The number of endpoints contained in  the interface.</p>
</dd>

### -field PipeArr

<dd>
<p>An array of <a href="..\usbfnbase\ns-usbfnbase--usbfn-pipe-information.md">USBFN_PIPE_INFORMATION</a> structures that describes the endpoints in the interface.</p>
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
<dt>Usbfnbase.h (include TBD)</dt>
</dl>
</td>
</tr>
</table>