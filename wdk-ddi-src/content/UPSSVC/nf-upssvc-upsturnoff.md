---
UID: NF.upssvc.UPSTurnOff
title: UPSTurnOff
author: windows-driver-content
description: The UPSTurnOff function turns off the UPS unit's power outlets, after a specified delay time.
old-location: battery\upsturnoff.htm
ms.assetid: 17ae946a-e57e-48bd-9213-cf47db2cba64
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: battery
req.header: upssvc.h
req.include-header: Upssvc.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UPSTurnOff
req.alt-loc: upssvc.h
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
ms.keywords: UPSTurnOff
req.iface: 
req.product: Windows 10 or later.
---

# UPSTurnOff function



## -description
<p>The <b>UPSTurnOff</b> function turns off the UPS unit's power outlets, after a specified delay time.</p>


## -syntax

````
void UPSTurnOff(
  _In_ DWORD aTurnOffDelay
);
````


## -parameters
<dl>

### -param <i>aTurnOffDelay</i> [in]

<dd>
<p>Specifies the minimum amount of time, in seconds, to wait before turning off the UPS unit's power outlets.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The actual delay time should not be less than that specified by <i>aTurnOffDelay</i>, to ensure adequate time for the operating system to shut down. </p>

<p>The default value for <i>aTurnOffDelay </i>is 180 seconds.</p>

<p>The function must not postpone the request to turn off the power. Doing so could result in the operating system unloading the UPS service and the UPS minidriver.</p>

<p>On the other hand, the function must not turn off power from a UPS system that does not have an internal turnoff delay. Doing so will result in a premature loss of power to the computer, which can cause system corruption.</p>

<p>The actual delay time should not be less than that specified by <i>aTurnOffDelay</i>, to ensure adequate time for the operating system to shut down. </p>

<p>The default value for <i>aTurnOffDelay </i>is 180 seconds.</p>

<p>The function must not postpone the request to turn off the power. Doing so could result in the operating system unloading the UPS service and the UPS minidriver.</p>

<p>On the other hand, the function must not turn off power from a UPS system that does not have an internal turnoff delay. Doing so will result in a premature loss of power to the computer, which can cause system corruption.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Upssvc.h (include Upssvc.h)</dt>
</dl>
</td>
</tr>
</table>