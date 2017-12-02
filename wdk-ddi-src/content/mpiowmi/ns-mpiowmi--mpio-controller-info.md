---
UID: NS.mpiowmi._MPIO_CONTROLLER_INFO
title: MPIO_CONTROLLER_INFO
author: windows-driver-content
description: The MPIO_CONTROLLER_INFO structure represents a storage controller.
old-location: storage\mpio_controller_info.htm
old-project: storage
ms.assetid: 30600e86-dd35-4498-91a8-14a722b2e868
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MPIO_CONTROLLER_INFO, MPIO_CONTROLLER_INFO, *PMPIO_CONTROLLER_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mpiowmi.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_CONTROLLER_INFO
req.alt-loc: mpiowmi.h
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
---

# MPIO_CONTROLLER_INFO structure



## -description
<p>The MPIO_CONTROLLER_INFO structure represents a storage controller.</p>


## -syntax

````
typedef struct _MPIO_CONTROLLER_INFO {
  ULONG IdentifierType;
  ULONG IdentifierLength;
  UCHAR Identifier[32];
  ULONG ControllerState;
  ULONG Pad;
  WCHAR AssociatedDsm[63 + 1];
} MPIO_CONTROLLER_INFO, *PMPIO_CONTROLLER_INFO;
````


## -struct-fields
<dl>

### -field IdentifierType

<dd>
<p>An unsigned 32-bitfield that represents the identifier type for the controller.</p>
</dd>

### -field IdentifierLength

<dd>
<p>An unsigned 32-bitfield that represents the length of the controller's identifier.</p>
</dd>

### -field Identifier

<dd>
<p>A 32-byte array that contains the actual identifier (serial number) of the controller.</p>
</dd>

### -field ControllerState

<dd>
<p>An unsigned 32-bitfield that represents the controller state.</p>
</dd>

### -field Pad

<dd>
<p>Should be zero.</p>
</dd>

### -field AssociatedDsm

<dd>
<p>A string field of maximum length 63 characters. This string field returns the friendly name of the DSM that controls the devices that are exposed by this controller.</p>
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
<dt>Mpiowmi.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>