---
UID: NC.d3dkmddi.DXGKCB_POWERRUNTIMECONTROLREQUEST
title: DXGKCB_POWERRUNTIMECONTROLREQUEST
author: windows-driver-content
description: Called by the display miniport driver to exchange information with the Power Engine Plug-in (PEP).
old-location: display\dxgkcbpowerruntimecontrolrequest.htm
old-project: display
ms.assetid: 28984c89-a1d9-4720-8c4c-2b2ce34e0899
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkCbPowerRuntimeControlRequest
req.alt-loc: D3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# DXGKCB_POWERRUNTIMECONTROLREQUEST callback



## -description
<p>Called by the display miniport driver to exchange information with the Power Engine Plug-in (PEP).</p>


## -prototype

````
DXGKCB_POWERRUNTIMECONTROLREQUEST DxgkCbPowerRuntimeControlRequest;

NTSTATUS APIENTRY CALLBACK* DxgkCbPowerRuntimeControlRequest(
  _In_      const HANDLE  hAdapter,
  _In_            LPCGUID PowerControlCode,
  _In_opt_        PVOID   InBuffer,
  _In_            SIZE_T  InBufferSize,
  _Out_opt_       PVOID   OutBuffer,
  _In_            SIZE_T  OutBufferSize,
  _Out_opt_       PSIZE_T BytesReturned
)
{ ... }
````


## -parameters
<dl>

### -param <i>hAdapter</i> [in]

<dd>
<p>A handle to the display adapter. The display miniport driver receives the handle from the <b>DeviceHandle</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560942">DXGKRNL_INTERFACE</a> structure in a call to its <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a> function.</p>
</dd>

### -param <i>PowerControlCode</i> [in]

<dd>
<p>A pointer to a GUID that defines the meaning of the display miniport driver's control request. For more information, see Remarks.</p>
</dd>

### -param <i>InBuffer</i> [in, optional]

<dd>
<p>An optional pointer to an input buffer.</p>
</dd>

### -param <i>InBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the buffer that <i>InBuffer</i> points to.</p>
</dd>

### -param <i>OutBuffer</i> [out, optional]

<dd>
<p>An optional pointer to an output buffer.</p>
</dd>

### -param <i>OutBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the buffer that <i>OutBuffer</i> points to.</p>
</dd>

### -param <i>BytesReturned</i> [out, optional]

<dd>
<p>An optional pointer to a buffer that contains the number of bytes that are written by the PEP to the output buffer.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if it succeeds. Otherwise, it returns one of the error codes defined in Ntstatus.h.</p>

## -remarks
<p>Although the driver can use any GUID in the <i>PowerControlCode</i> parameter, the following GUIDs that are defined in D3dkmddi.h are recommended. By using these GUIDs, the display port driver can issue Event Tracing for Windows (ETW) events, which are useful to profile driver performance issues.<p></p>
<dl>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE_UP"></a><a id="guid_dxgkddi_power_voltage_up"></a>GUID_DXGKDDI_POWER_VOLTAGE_UP</dt>
<dd>
<p>Increase the voltage.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE_DOWN"></a><a id="guid_dxgkddi_power_voltage_down"></a>GUID_DXGKDDI_POWER_VOLTAGE_DOWN</dt>
<dd>
<p>Decrease the voltage.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE"></a><a id="guid_dxgkddi_power_voltage"></a>GUID_DXGKDDI_POWER_VOLTAGE</dt>
<dd>
<p>Change the voltage, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK_UP"></a><a id="guid_dxgkddi_power_clock_up"></a>GUID_DXGKDDI_POWER_CLOCK_UP</dt>
<dd>
<p>Increase the clock setting.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK_DOWN"></a><a id="guid_dxgkddi_power_clock_down"></a>GUID_DXGKDDI_POWER_CLOCK_DOWN</dt>
<dd>
<p>Decrease the clock setting.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK"></a><a id="guid_dxgkddi_power_clock"></a>GUID_DXGKDDI_POWER_CLOCK</dt>
<dd>
<p>Change the clock setting, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH_UP"></a><a id="guid_dxgkddi_power_bandwidth_up"></a>GUID_DXGKDDI_POWER_BANDWIDTH_UP</dt>
<dd>
<p>Increase the bandwidth.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH_DOWN"></a><a id="guid_dxgkddi_power_bandwidth_down"></a>GUID_DXGKDDI_POWER_BANDWIDTH_DOWN</dt>
<dd>
<p>Decrease the bandwidth.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH"></a><a id="guid_dxgkddi_power_bandwidth"></a>GUID_DXGKDDI_POWER_BANDWIDTH</dt>
<dd>
<p>Change the bandwidth, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
</dl>
</p>

<p></p><dl>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE_UP"></a><a id="guid_dxgkddi_power_voltage_up"></a>GUID_DXGKDDI_POWER_VOLTAGE_UP</dt>
<dd>
<p>Increase the voltage.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE_DOWN"></a><a id="guid_dxgkddi_power_voltage_down"></a>GUID_DXGKDDI_POWER_VOLTAGE_DOWN</dt>
<dd>
<p>Decrease the voltage.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE"></a><a id="guid_dxgkddi_power_voltage"></a>GUID_DXGKDDI_POWER_VOLTAGE</dt>
<dd>
<p>Change the voltage, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK_UP"></a><a id="guid_dxgkddi_power_clock_up"></a>GUID_DXGKDDI_POWER_CLOCK_UP</dt>
<dd>
<p>Increase the clock setting.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK_DOWN"></a><a id="guid_dxgkddi_power_clock_down"></a>GUID_DXGKDDI_POWER_CLOCK_DOWN</dt>
<dd>
<p>Decrease the clock setting.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK"></a><a id="guid_dxgkddi_power_clock"></a>GUID_DXGKDDI_POWER_CLOCK</dt>
<dd>
<p>Change the clock setting, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH_UP"></a><a id="guid_dxgkddi_power_bandwidth_up"></a>GUID_DXGKDDI_POWER_BANDWIDTH_UP</dt>
<dd>
<p>Increase the bandwidth.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH_DOWN"></a><a id="guid_dxgkddi_power_bandwidth_down"></a>GUID_DXGKDDI_POWER_BANDWIDTH_DOWN</dt>
<dd>
<p>Decrease the bandwidth.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH"></a><a id="guid_dxgkddi_power_bandwidth"></a>GUID_DXGKDDI_POWER_BANDWIDTH</dt>
<dd>
<p>Change the bandwidth, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
</dl><p>Increase the voltage.</p>

<p>Decrease the voltage.</p>

<p>Change the voltage, but the driver doesn't know if the change is an increase or decrease.</p>

<p>Increase the clock setting.</p>

<p>Decrease the clock setting.</p>

<p>Change the clock setting, but the driver doesn't know if the change is an increase or decrease.</p>

<p>Increase the bandwidth.</p>

<p>Decrease the bandwidth.</p>

<p>Change the bandwidth, but the driver doesn't know if the change is an increase or decrease.</p>

<p>These GUIDs do not imply that there is any communication protocol between the display miniport driver and the PEP, nor do they imply that there are any restrictions on the values that can be passed between the display miniport driver and the PEP.</p>

<p>Although the driver can use any GUID in the <i>PowerControlCode</i> parameter, the following GUIDs that are defined in D3dkmddi.h are recommended. By using these GUIDs, the display port driver can issue Event Tracing for Windows (ETW) events, which are useful to profile driver performance issues.<p></p>
<dl>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE_UP"></a><a id="guid_dxgkddi_power_voltage_up"></a>GUID_DXGKDDI_POWER_VOLTAGE_UP</dt>
<dd>
<p>Increase the voltage.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE_DOWN"></a><a id="guid_dxgkddi_power_voltage_down"></a>GUID_DXGKDDI_POWER_VOLTAGE_DOWN</dt>
<dd>
<p>Decrease the voltage.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE"></a><a id="guid_dxgkddi_power_voltage"></a>GUID_DXGKDDI_POWER_VOLTAGE</dt>
<dd>
<p>Change the voltage, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK_UP"></a><a id="guid_dxgkddi_power_clock_up"></a>GUID_DXGKDDI_POWER_CLOCK_UP</dt>
<dd>
<p>Increase the clock setting.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK_DOWN"></a><a id="guid_dxgkddi_power_clock_down"></a>GUID_DXGKDDI_POWER_CLOCK_DOWN</dt>
<dd>
<p>Decrease the clock setting.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK"></a><a id="guid_dxgkddi_power_clock"></a>GUID_DXGKDDI_POWER_CLOCK</dt>
<dd>
<p>Change the clock setting, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH_UP"></a><a id="guid_dxgkddi_power_bandwidth_up"></a>GUID_DXGKDDI_POWER_BANDWIDTH_UP</dt>
<dd>
<p>Increase the bandwidth.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH_DOWN"></a><a id="guid_dxgkddi_power_bandwidth_down"></a>GUID_DXGKDDI_POWER_BANDWIDTH_DOWN</dt>
<dd>
<p>Decrease the bandwidth.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH"></a><a id="guid_dxgkddi_power_bandwidth"></a>GUID_DXGKDDI_POWER_BANDWIDTH</dt>
<dd>
<p>Change the bandwidth, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
</dl>
</p>

<p></p><dl>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE_UP"></a><a id="guid_dxgkddi_power_voltage_up"></a>GUID_DXGKDDI_POWER_VOLTAGE_UP</dt>
<dd>
<p>Increase the voltage.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE_DOWN"></a><a id="guid_dxgkddi_power_voltage_down"></a>GUID_DXGKDDI_POWER_VOLTAGE_DOWN</dt>
<dd>
<p>Decrease the voltage.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_VOLTAGE"></a><a id="guid_dxgkddi_power_voltage"></a>GUID_DXGKDDI_POWER_VOLTAGE</dt>
<dd>
<p>Change the voltage, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK_UP"></a><a id="guid_dxgkddi_power_clock_up"></a>GUID_DXGKDDI_POWER_CLOCK_UP</dt>
<dd>
<p>Increase the clock setting.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK_DOWN"></a><a id="guid_dxgkddi_power_clock_down"></a>GUID_DXGKDDI_POWER_CLOCK_DOWN</dt>
<dd>
<p>Decrease the clock setting.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_CLOCK"></a><a id="guid_dxgkddi_power_clock"></a>GUID_DXGKDDI_POWER_CLOCK</dt>
<dd>
<p>Change the clock setting, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH_UP"></a><a id="guid_dxgkddi_power_bandwidth_up"></a>GUID_DXGKDDI_POWER_BANDWIDTH_UP</dt>
<dd>
<p>Increase the bandwidth.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH_DOWN"></a><a id="guid_dxgkddi_power_bandwidth_down"></a>GUID_DXGKDDI_POWER_BANDWIDTH_DOWN</dt>
<dd>
<p>Decrease the bandwidth.</p>
</dd>
<dt><a id="GUID_DXGKDDI_POWER_BANDWIDTH"></a><a id="guid_dxgkddi_power_bandwidth"></a>GUID_DXGKDDI_POWER_BANDWIDTH</dt>
<dd>
<p>Change the bandwidth, but the driver doesn't know if the change is an increase or decrease.</p>
</dd>
</dl><p>Increase the voltage.</p>

<p>Decrease the voltage.</p>

<p>Change the voltage, but the driver doesn't know if the change is an increase or decrease.</p>

<p>Increase the clock setting.</p>

<p>Decrease the clock setting.</p>

<p>Change the clock setting, but the driver doesn't know if the change is an increase or decrease.</p>

<p>Increase the bandwidth.</p>

<p>Decrease the bandwidth.</p>

<p>Change the bandwidth, but the driver doesn't know if the change is an increase or decrease.</p>

<p>These GUIDs do not imply that there is any communication protocol between the display miniport driver and the PEP, nor do they imply that there are any restrictions on the values that can be passed between the display miniport driver and the PEP.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-setpowercomponentactive.md">DxgkCbSetPowerComponentActive</a>
</dt>
<dt>
<a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560942">DXGKRNL_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_POWERRUNTIMECONTROLREQUEST callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
