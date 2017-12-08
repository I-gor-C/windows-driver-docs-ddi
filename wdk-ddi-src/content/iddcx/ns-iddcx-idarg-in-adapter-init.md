---
UID: NS.iddcx.IDARG_IN_ADAPTER_INIT
title: IDARG_IN_ADAPTER_INIT
author: windows-driver-content
description: Initializes an adapter that will be hosted on a WDF device.
old-location: display\idarg_in_adapter_init.htm
old-project: display
ms.assetid: 2db324c8-69b1-4497-b6a7-76047baeca19
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_IN_ADAPTER_INIT,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDARG_IN_ADAPTER_INIT
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDARG_IN_ADAPTER_INIT structure



## -description
<p>
                 Initializes an adapter that will be hosted on a WDF device.
             </p>


## -syntax

````
typedef struct IDARG_IN_ADAPTER_INIT {
  WDFDEVICE              WdfDevice;
  IDDCX_ADAPTER_CAPS*    pCaps;
  PWDF_OBJECT_ATTRIBUTES ObjectAttributes;
} IDARG_IN_ADAPTER_INIT, *IDARG_IN_ADAPTER_INIT;
````


## -struct-fields
<dl>

### -field WdfDevice

<dd>
<p>
                     The WDF device that will be hosting this WDDM adapter object.
                 </p>
</dd>

### -field pCaps

<dd>
<p>
                     [in] A reference  to the capabilities of the adapter.
                 </p>
</dd>

### -field ObjectAttributes

<dd>
<p>
                     [in][optional] Object attributes that are used to initialize the WDF adapter object.
                 </p>
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>