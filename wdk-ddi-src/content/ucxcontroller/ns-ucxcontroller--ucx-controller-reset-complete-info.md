---
UID: NS.ucxcontroller._UCX_CONTROLLER_RESET_COMPLETE_INFO
title: UCX_CONTROLLER_RESET_COMPLETE_INFO
author: windows-driver-content
description: Contains information about the operation to reset the controller. This is used by the client driver in its EVT_UCX_CONTROLLER_RESET callback function.
old-location: buses\_ucx_controller_reset_complete_info.htm
old-project: usbref
ms.assetid: 72935645-0567-4FC9-962C-3E823C08D001
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_CONTROLLER_RESET_COMPLETE_INFO, UCX_CONTROLLER_RESET_COMPLETE_INFO, *PUCX_CONTROLLER_RESET_COMPLETE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxcontroller.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_CONTROLLER_RESET_COMPLETE_INFO
req.alt-loc: Ucxcontroller.h
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

# UCX_CONTROLLER_RESET_COMPLETE_INFO structure



## -description
<p>Contains information about the operation to reset the controller. This is used by the client driver in its <a href="buses.evt_ucx_controller_reset">EVT_UCX_CONTROLLER_RESET</a> callback function.</p>


## -syntax

````
typedef struct _UCX_CONTROLLER_RESET_COMPLETE_INFO {
  ULONG                Size;
  UCX_CONTROLLER_STATE UcxControllerState;
  BOOLEAN              UcxCoordinated;
} UCX_CONTROLLER_RESET_COMPLETE_INFO, *P_UCX_CONTROLLER_RESET_COMPLETE_INFO;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field <b>UcxControllerState</b>

<dd>
<p>The UCX controller state after reset. </p>
</dd>

### -field <b>UcxCoordinated</b>

<dd>
<p>Indicates if the reset was coordinated with UCX (TRUE) or not (FALSE).</p>
</dd>
</dl>

## -remarks
<p>This structure is populated by a call to <a href="buses._ucxcontrollerresetcomplete">UcxControllerResetComplete</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucxcontroller.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>