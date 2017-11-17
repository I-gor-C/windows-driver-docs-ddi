---
UID: NF.wdfdevice.WDF_PNPPOWER_EVENT_CALLBACKS_INIT
title: WDF_PNPPOWER_EVENT_CALLBACKS_INIT
author: windows-driver-content
description: The WDF_PNPPOWER_EVENT_CALLBACKS_INIT function initializes a driver's WDF_PNPPOWER_EVENT_CALLBACKS structure.
old-location: wdf\wdf_pnppower_event_callbacks_init.htm
ms.assetid: f84e200b-542d-4885-a091-9e311b4ab697
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_PNPPOWER_EVENT_CALLBACKS_INIT
req.alt-loc: wdfdevice.h
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
ms.keywords: WDF_PNPPOWER_EVENT_CALLBACKS_INIT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_PNPPOWER_EVENT_CALLBACKS_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_PNPPOWER_EVENT_CALLBACKS_INIT</b> function initializes a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552416">WDF_PNPPOWER_EVENT_CALLBACKS</a> structure.</p>


## -syntax

````
VOID WDF_PNPPOWER_EVENT_CALLBACKS_INIT(
  _Out_ PWDF_PNPPOWER_EVENT_CALLBACKS Callbacks
);
````


## -parameters
<dl>

### -param <i>Callbacks</i> [out]

<dd>
<p>A pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552416">WDF_PNPPOWER_EVENT_CALLBACKS</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_PNPPOWER_EVENT_CALLBACKS_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff552416">WDF_PNPPOWER_EVENT_CALLBACKS</a> structure and sets the structure's <b>Size</b> member.</p>

<p>For a code example that uses <b>WDF_PNPPOWER_EVENT_CALLBACKS_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546135">WdfDeviceInitSetPnpPowerEventCallbacks</a>.</p>

<p>The <b>WDF_PNPPOWER_EVENT_CALLBACKS_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff552416">WDF_PNPPOWER_EVENT_CALLBACKS</a> structure and sets the structure's <b>Size</b> member.</p>

<p>For a code example that uses <b>WDF_PNPPOWER_EVENT_CALLBACKS_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546135">WdfDeviceInitSetPnpPowerEventCallbacks</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>