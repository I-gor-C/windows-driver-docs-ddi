---
UID: NF.sensorscx.SensorsCxSensorDataReady
title: SensorsCxSensorDataReady
author: windows-driver-content
description: This function notifies the class extension that the driver has retrieved data.
old-location: sensors\sensorscxsensordataready.htm
old-project: sensors
ms.assetid: 9F01D093-226E-4CB4-8085-812115EBA671
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: SensorsCxSensorDataReady
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: sensorscx.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SensorsCxSensorDataReady
req.alt-loc: SensorsCx.h
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

# SensorsCxSensorDataReady function



## -description
<p>This function notifies the class extension that the driver has retrieved data.</p>


## -syntax

````
FORCEINLINE NTSTATUS SensorsCxSensorDataReady(
  _In_ SENSOROBJECT            Sensor,
  _In_ PSENSOR_COLLECTION_LIST pSensorData
);
````


## -parameters
<dl>

### -param <i>Sensor</i> [in]

<dd>
<p>A reference to a sensor object.</p>
</dd>

### -param <i>pSensorData</i> [in]

<dd>
<p>A list of <a href="https://msdn.microsoft.com/library/windows/hardware/dn946698">Sensor properties</a>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn957092">SENSOR_COLLECTION_LIST</a>.</p>
</dd>
</dl>

## -returns
<p>This function returns NTSTATUS with different values. Some values that may be returned are the following:</p>

<p>STATUS_SUCCESS is returned if the function completes successfully.</p>

<p>STATUS_UNSUCCESSFUL is returned if the function does not complete successfully.</p>

<p>STATUS_INVALID_PARAMETER is returned if any of the _In_ parameters are NULL.</p>

## -remarks
<p>This function is implemented by the class extension and the driver must call it. Note that when batch latency expires for sensor drivers
    that support data batching, <b>SensorsCxSensorDataReady</b> is called repeatedly until all the batched data samples are delivered to the client.
    For more information about the callback function related to  batch latency, see <a href="https://msdn.microsoft.com/library/windows/hardware/mt219125">EvtSensorSetBatchLatency</a>.
</p>

<p>This function is implemented by the class extension and the driver must call it. Note that when batch latency expires for sensor drivers
    that support data batching, <b>SensorsCxSensorDataReady</b> is called repeatedly until all the batched data samples are delivered to the client.
    For more information about the callback function related to  batch latency, see <a href="https://msdn.microsoft.com/library/windows/hardware/mt219125">EvtSensorSetBatchLatency</a>.
</p>

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
<dt>SensorsCx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt219125">EvtSensorSetBatchLatency</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957092">SENSOR_COLLECTION_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn946698">Sensor properties</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20SensorsCxSensorDataReady function%20 RELEASE:%20(11/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
