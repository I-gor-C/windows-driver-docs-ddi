---
UID: NC.sercx.EVT_SERCX_TRANSMIT_CANCEL
title: EVT_SERCX_TRANSMIT_CANCEL
author: windows-driver-content
description: The EvtSerCxTransmitCancel event callback function notifies the serial controller driver that the pending transmit request is canceled.
old-location: serports\evtsercxtransmitcancel.htm
old-project: serports
ms.assetid: 7922A3BD-8829-42A3-9F94-3C26F1262626
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SENSOR_VALUE_PAIR, SENSOR_VALUE_PAIR, *PSENSOR_VALUE_PAIR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: sercx.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EvtSerCxTransmitCancel
req.alt-loc: 1.0\Sercx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Called at IRQL <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_SERCX_TRANSMIT_CANCEL callback



## -description
<p>The <i>EvtSerCxTransmitCancel</i> event callback function notifies the serial controller driver that the pending transmit request is canceled.</p>


## -prototype

````
EVT_SERCX_TRANSMIT_CANCEL EvtSerCxTransmitCancel;

VOID EvtSerCxTransmitCancel(
  _In_ WDFDEVICE Device
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A WDFDEVICE handle to the framework device object that represents the serial controller.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The serial framework extension (SerCx) calls this function to inform the serial controller driver that the current transmit request has been canceled.  If the driver has an outstanding transmit operation in progress, the driver should cancel this operation and call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406715">SerCxProgressTransmit</a> method to report the cancellation. In the <b>SerCxProgressTransmit</b> call, set <i>BytesTransmitted</i> to the number of bytes transmitted before the operation was canceled, and set <i>TransmitStatus</i> to <b>SerCxStatusCancelled</b>.</p>

<p>To register an <i>EvtSerCxTransmitCancel</i> callback function, the driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406711">SerCxInitialize</a> method.</p>

<p>The function type for this callback is declared in Sercx.h, as follows.</p>

<p>To define an <i>EvtSerCxTransmitCancel</i> callback function that is named <code>MyEvtSerCxTransmitCancel</code>, you must first provide a function declaration that <a href="NULL">Static Driver Verifier</a> (SDV) and other verification tools require, as follows.</p>

<p>Then, implement your callback function as follows.</p>

<p>For more information about SDV requirements for function declarations, see <a href="https://msdn.microsoft.com/73a408ba-0219-4fde-8dad-ca330e4e67c3">Declaring Functions Using Function Role Types for KMDF Drivers</a>.</p>

<p>The serial framework extension (SerCx) calls this function to inform the serial controller driver that the current transmit request has been canceled.  If the driver has an outstanding transmit operation in progress, the driver should cancel this operation and call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406715">SerCxProgressTransmit</a> method to report the cancellation. In the <b>SerCxProgressTransmit</b> call, set <i>BytesTransmitted</i> to the number of bytes transmitted before the operation was canceled, and set <i>TransmitStatus</i> to <b>SerCxStatusCancelled</b>.</p>

<p>To register an <i>EvtSerCxTransmitCancel</i> callback function, the driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406711">SerCxInitialize</a> method.</p>

<p>The function type for this callback is declared in Sercx.h, as follows.</p>

<p>To define an <i>EvtSerCxTransmitCancel</i> callback function that is named <code>MyEvtSerCxTransmitCancel</code>, you must first provide a function declaration that <a href="NULL">Static Driver Verifier</a> (SDV) and other verification tools require, as follows.</p>

<p>Then, implement your callback function as follows.</p>

<p>For more information about SDV requirements for function declarations, see <a href="https://msdn.microsoft.com/73a408ba-0219-4fde-8dad-ca330e4e67c3">Declaring Functions Using Function Role Types for KMDF Drivers</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1.0\Sercx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Called at IRQL &lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>