---
UID: NS.iddcx.IDARG_IN_SWAPCHAINSETDEVICE
title: IDARG_IN_SWAPCHAINSETDEVICE
author: windows-driver-content
description: Gives information about the device that will process the swap chain.
old-location: display\idarg_in_swapchainsetdevice.htm
old-project: display
ms.assetid: afd52391-5b18-4b86-9d35-2d9ed3e20256
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_IN_SWAPCHAINSETDEVICE,
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
req.alt-api: IDARG_IN_SWAPCHAINSETDEVICE
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

# IDARG_IN_SWAPCHAINSETDEVICE structure



## -description
<p>
                 Gives information about the device that will process the swap chain.</p>


## -syntax

````
typedef struct IDARG_IN_SWAPCHAINSETDEVICE {
  IDXGIDevice* pDevice;
} IDARG_IN_SWAPCHAINSETDEVICE, *IDARG_IN_SWAPCHAINSETDEVICE;
````


## -struct-fields
<dl>

### -field pDevice

<dd>
<p>
                     The DXGI device used to process swap chain frames.
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