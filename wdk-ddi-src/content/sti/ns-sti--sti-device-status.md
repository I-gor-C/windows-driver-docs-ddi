---
UID: NS.sti._STI_DEVICE_STATUS
title: STI_DEVICE_STATUS
author: windows-driver-content
description: The STI_DEVICE_STATUS structure is used as a parameter to the IStiDevice::GetStatus and IStiUSD::GetStatus methods.
old-location: image\sti_device_status.htm
old-project: image
ms.assetid: 40104e1f-b936-430b-9e8c-28738579f4c7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: STI_DEVICE_STATUS, STI_DEVICE_STATUS, *PSTI_DEVICE_STATUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: sti.h
req.include-header: Sti.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STI_DEVICE_STATUS
req.alt-loc: sti.h
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
req.iface: IStiDevice
req.product: Windows 10 or later.
---

# STI_DEVICE_STATUS structure



## -description
<p>The STI_DEVICE_STATUS structure is used as a parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543752">IStiDevice::GetStatus</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543823">IStiUSD::GetStatus</a> methods.</p>


## -syntax

````
typedef struct _STI_DEVICE_STATUS {
  DWORD dwSize;
  DWORD StatusMask;
  DWORD dwOnlineState;
  DWORD dwHardwareStatusCode;
  DWORD dwEventHandlingState;
  DWORD dwPollingInterval;
} STI_DEVICE_STATUS, *PSTI_DEVICE_STATUS;
````


## -struct-fields
<dl>

### -field <b>dwSize</b>

<dd>
<p>Caller-supplied size, in bytes, of the STI_DEVICE_STATUS structure.</p>
</dd>

### -field <b>StatusMask</b>

<dd>
<p>One or more caller-supplied bit flags, indicating the type of status information being requested. The following flags are defined:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>STI_DEVSTATUS_EVENTS_STATE</p>
</td>
<td>
<p>The driver should fill in the <b>dwEventHandlingState</b> member.</p>
</td>
</tr>
<tr>
<td>
<p>STI_DEVSTATUS_ONLINE_STATE </p>
</td>
<td>
<p>The driver should fill in the <b>dwOnlineState</b> member.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwOnlineState</b>

<dd>
<p>Bit flags indicating the device's current status. The following flags are defined in <i>Sti.h</i>.</p>
<p>Currently use of STI_ONLINESTATE_OPERATIONAL is required, while use of all other flags is optional. (Currently, STI_ONLINESTATE_OPERATIONAL is the only flag that the still image server checks.)</p>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_BUSY"></a><a id="sti_onlinestate_busy"></a>STI_ONLINESTATE_BUSY

<dd>
<p>The device is busy.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_ERROR"></a><a id="sti_onlinestate_error"></a>STI_ONLINESTATE_ERROR

<dd>
<p>The device has reported an error.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_INITIALIZING"></a><a id="sti_onlinestate_initializing"></a>STI_ONLINESTATE_INITIALIZING

<dd>
<p>The device is being initialized.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_IO_ACTIVE"></a><a id="sti_onlinestate_io_active"></a>STI_ONLINESTATE_IO_ACTIVE

<dd>
<p>The device is active but not accepting commands.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_OFFLINE"></a><a id="sti_onlinestate_offline"></a>STI_ONLINESTATE_OFFLINE

<dd>
<p>The device is off-line.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_OPERATIONAL"></a><a id="sti_onlinestate_operational"></a>STI_ONLINESTATE_OPERATIONAL

<dd>
<p>The device is online and ready. If set, Control Panel indicates the device is ready. Otherwise, it indicates the device is off-line.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_PAPER_JAM"></a><a id="sti_onlinestate_paper_jam"></a>STI_ONLINESTATE_PAPER_JAM

<dd>
<p>The device has reported a paper jam.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_PAPER_PROBLEM"></a><a id="sti_onlinestate_paper_problem"></a>STI_ONLINESTATE_PAPER_PROBLEM

<dd>
<p>The device has reported an unspecified paper problem.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_PAUSED"></a><a id="sti_onlinestate_paused"></a>STI_ONLINESTATE_PAUSED

<dd>
<p>The device is paused.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_PENDING"></a><a id="sti_onlinestate_pending"></a>STI_ONLINESTATE_PENDING

<dd>
<p>I/O operations are pending.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_POWER_SAVE"></a><a id="sti_onlinestate_power_save"></a>STI_ONLINESTATE_POWER_SAVE

<dd>
<p>The device is in power save mode.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_TRANSFERRING"></a><a id="sti_onlinestate_transferring"></a>STI_ONLINESTATE_TRANSFERRING

<dd>
<p>The device is transferring data.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_USER_INTERVENTION"></a><a id="sti_onlinestate_user_intervention"></a>STI_ONLINESTATE_USER_INTERVENTION

<dd>
<p>The device requires user intervention.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_ONLINESTATE_WARMING_UP"></a><a id="sti_onlinestate_warming_up"></a>STI_ONLINESTATE_WARMING_UP

<dd>
<p>The device is warming up.</p>
</dd>
</dl>
</dd>

### -field <b>dwHardwareStatusCode</b>

<dd>
<p>Optional device-specific, vendor-defined value.</p>
</dd>

### -field <b>dwEventHandlingState</b>

<dd>
<p>Contains bit flags indicating event status. The following flags are defined in <i>Sti.h</i>.</p>
<p></p>
<dl>

### -field <a id="STI_EVENTHANDLING_ENABLED"></a><a id="sti_eventhandling_enabled"></a>STI_EVENTHANDLING_ENABLED

<dd>
<p><i>Not used</i>.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_EVENTHANDLING_PENDING"></a><a id="sti_eventhandling_pending"></a>STI_EVENTHANDLING_PENDING

<dd>
<p>A device event has occurred.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_EVENTHANDLING_POLLING"></a><a id="sti_eventhandling_polling"></a>STI_EVENTHANDLING_POLLING

<dd>
<p><i>Not used</i>.</p>
</dd>
</dl>
</dd>

### -field <b>dwPollingInterval</b>

<dd>
<p>Time value, in milliseconds, indicating how often the device should be polled, if polling is required.</p>
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
<dt>Sti.h (include Sti.h)</dt>
</dl>
</td>
</tr>
</table>