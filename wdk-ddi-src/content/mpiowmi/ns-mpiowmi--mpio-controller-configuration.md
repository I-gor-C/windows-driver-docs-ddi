---
UID: NS.mpiowmi._MPIO_CONTROLLER_CONFIGURATION
title: MPIO_CONTROLLER_CONFIGURATION
author: windows-driver-content
description: The MPIO_CONTROLLER_CONFIGURATION structure provides a top-level view of the storage controllers and the targets that are connected to them in the system.
old-location: storage\mpio_controller_configuration.htm
old-project: storage
ms.assetid: af608197-fa2b-474f-aa87-eb933a57b8cc
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MPIO_CONTROLLER_CONFIGURATION, MPIO_CONTROLLER_CONFIGURATION, *PMPIO_CONTROLLER_CONFIGURATION
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
req.alt-api: MPIO_CONTROLLER_CONFIGURATION
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

# MPIO_CONTROLLER_CONFIGURATION structure



## -description
<p>The MPIO_CONTROLLER_CONFIGURATION structure provides a top-level view of the storage controllers and the targets that are connected to them in the system.</p>


## -syntax

````
typedef struct _MPIO_CONTROLLER_CONFIGURATION {
  ULONG                NumberControllers;
  MPIO_CONTROLLER_INFO ControllerInfo[1];
} MPIO_CONTROLLER_CONFIGURATION, *PMPIO_CONTROLLER_CONFIGURATION;
````


## -struct-fields
<dl>

### -field <b>NumberControllers</b>

<dd>
<p>An unsigned 32-bitfield that represents the total number of controllers on the system that are known to MPIO.</p>
</dd>

### -field <b>ControllerInfo</b>

<dd>
<p>An array with information about all the controllers and all targets in the system. The number of elements of the array is given by <i>NumberControllers</i> and each element of the array is an instance of an MPIO_CONTROLLER_INFO structure.</p>
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