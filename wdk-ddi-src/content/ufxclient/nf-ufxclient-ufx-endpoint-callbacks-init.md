---
UID: NF.ufxclient.UFX_ENDPOINT_CALLBACKS_INIT
title: UFX_ENDPOINT_CALLBACKS_INIT
author: windows-driver-content
description: The UFX_ENDPOINT_CALLBACKS_INIT macro initializes the UFX_ENDPOINT_CALLBACKS structure.
old-location: buses\ufx_endpoint_callbacks_init.htm
old-project: usbref
ms.assetid: 10EB0C86-915F-4C24-ADBE-1D8E8DD8ECB6
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UFX_ENDPOINT_CALLBACKS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ufxclient.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFX_ENDPOINT_CALLBACKS_INIT
req.alt-loc: ufxclient.h
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

# UFX_ENDPOINT_CALLBACKS_INIT function



## -description
<p>The <b>UFX_ENDPOINT_CALLBACKS_INIT</b> macro initializes the <a href="..\ufxclient\ns-ufxclient--ufx-endpoint-callbacks.md">UFX_ENDPOINT_CALLBACKS</a> structure.<div class="alert"><b>Note</b>  <p class="note">Note that there are currently no endpoint callback functions defined in the <a href="..\ufxclient\ns-ufxclient--ufx-endpoint-callbacks.md">UFX_ENDPOINT_CALLBACKS</a> structure. </p>
</div>
<div> </div>
</p>


## -syntax

````
FORCEINLINE void UFX_ENDPOINT_CALLBACKS_INIT(
  _Out_ PUFX_DEVICE_CALLBACKS Callbacks
);
````


## -parameters
<dl>

### -param Callbacks [out]

<dd>
<p>A pointer to the <a href="..\ufxclient\ns-ufxclient--ufx-endpoint-callbacks.md">UFX_ENDPOINT_CALLBACKS</a> structure.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>The <b>UFX_ENDPOINT_CALLBACKS_INIT</b> macro will set all fields of the <a href="..\ufxclient\ns-ufxclient--ufx-endpoint-callbacks.md">UFX_ENDPOINT_CALLBACKS</a> structure to zero and set the size field appropriately.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufxclient.h</dt>
</dl>
</td>
</tr>
</table>