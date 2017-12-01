---
UID: NE.strmini._SRB_COMMAND
title: SRB_COMMAND
author: windows-driver-content
description: .
old-location: stream\srb_command.htm
old-project: stream
ms.assetid: 2A72D3B5-286A-4C20-AFEC-77EDCDD56B6A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: strmini.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRB_COMMAND
req.alt-loc: Strmini.h
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

# SRB_COMMAND enumeration



## -description
<p></p>


## -syntax

````
typedef enum _SRB_COMMAND { 
  SRB_READ_DATA,
  SRB_WRITE_DATA,
  SRB_GET_STREAM_STATE,
  SRB_SET_STREAM_STATE,
  SRB_SET_STREAM_PROPERTY,
  SRB_GET_STREAM_PROPERTY,
  SRB_OPEN_MASTER_CLOCK,
  SRB_INDICATE_MASTER_CLOCK,
  SRB_UNKNOWN_STREAM_COMMAND,
  SRB_SET_STREAM_RATE,
  SRB_PROPOSE_DATA_FORMAT,
  SRB_CLOSE_MASTER_CLOCK,
  SRB_PROPOSE_STREAM_RATE,
  SRB_SET_DATA_FORMAT,
  SRB_GET_DATA_FORMAT,
  SRB_BEGIN_FLUSH,
  SRB_END_FLUSH,
  SRB_GET_STREAM_INFO          = 0x100,
  SRB_OPEN_STREAM,
  SRB_CLOSE_STREAM,
  SRB_OPEN_DEVICE_INSTANCE,
  SRB_CLOSE_DEVICE_INSTANCE,
  SRB_GET_DEVICE_PROPERTY,
  SRB_SET_DEVICE_PROPERTY,
  SRB_INITIALIZE_DEVICE,
  SRB_CHANGE_POWER_STATE,
  SRB_UNINITIALIZE_DEVICE,
  SRB_UNKNOWN_DEVICE_COMMAND,
  SRB_PAGING_OUT_DRIVER,
  SRB_GET_DATA_INTERSECTION,
  SRB_INITIALIZATION_COMPLETE,
  SRB_SURPRISE_REMOVAL,
#if (NTDDI_VERSION >= NTDDI_WINXP)
  SRB_DEVICE_METHOD,
  SRB_STREAM_METHOD,
#if ( (NTDDI_VERSION >= NTDDI_WINXPSP2) && (NTDDI_VERSION < NTDDI_WS03) ) || (NTDDI_VERSION >= NTDDI_WS03SP1)


  SRB_NOTIFY_IDLE_STATE
#endif 

#endif } SRB_COMMAND;
````


## -enum-fields
<dl>

### -field <a id="SRB_READ_DATA"></a><a id="srb_read_data"></a><b>SRB_READ_DATA</b>

<dd>
<p>Stream-specific code that specifies to read data from hardware.</p>
</dd>

### -field <a id="SRB_WRITE_DATA"></a><a id="srb_write_data"></a><b>SRB_WRITE_DATA</b>

<dd>
<p>Stream-specific code that specifies to write data to the hardware.</p>
</dd>

### -field <a id="SRB_GET_STREAM_STATE"></a><a id="srb_get_stream_state"></a><b>SRB_GET_STREAM_STATE</b>

<dd>
<p>Stream-specific code that specifies to get the state of the stream.</p>
</dd>

### -field <a id="SRB_SET_STREAM_STATE"></a><a id="srb_set_stream_state"></a><b>SRB_SET_STREAM_STATE</b>

<dd>
<p>Stream-specific code that specifies to set the state of the stream.</p>
</dd>

### -field <a id="SRB_SET_STREAM_PROPERTY"></a><a id="srb_set_stream_property"></a><b>SRB_SET_STREAM_PROPERTY</b>

<dd>
<p>Stream-specific code that specifies to set a property of the stream.</p>
</dd>

### -field <a id="SRB_GET_STREAM_PROPERTY"></a><a id="srb_get_stream_property"></a><b>SRB_GET_STREAM_PROPERTY</b>

<dd>
<p>Stream-specific code that specifies to get a property value for the stream.</p>
</dd>

### -field <a id="SRB_OPEN_MASTER_CLOCK"></a><a id="srb_open_master_clock"></a><b>SRB_OPEN_MASTER_CLOCK</b>

<dd>
<p>Stream-specific code that indicates that the master clock is on this stream.</p>
</dd>

### -field <a id="SRB_INDICATE_MASTER_CLOCK"></a><a id="srb_indicate_master_clock"></a><b>SRB_INDICATE_MASTER_CLOCK</b>

<dd>
<p>Stream-specific code that specifies that the handle is supplied to the master clock.</p>
</dd>

### -field <a id="SRB_UNKNOWN_STREAM_COMMAND"></a><a id="srb_unknown_stream_command"></a><b>SRB_UNKNOWN_STREAM_COMMAND</b>

<dd>
<p>Stream-specific code that specifies that the IRP function is unknown to the class driver.</p>
</dd>

### -field <a id="SRB_SET_STREAM_RATE"></a><a id="srb_set_stream_rate"></a><b>SRB_SET_STREAM_RATE</b>

<dd>
<p>Stream-specific code that specifies that the rate is set at which the stream should run.</p>
</dd>

### -field <a id="SRB_PROPOSE_DATA_FORMAT"></a><a id="srb_propose_data_format"></a><b>SRB_PROPOSE_DATA_FORMAT</b>

<dd>
<p>Stream-specific code that specifies that a new rate is proposed, it does not change the rate.</p>
</dd>

### -field <a id="SRB_CLOSE_MASTER_CLOCK"></a><a id="srb_close_master_clock"></a><b>SRB_CLOSE_MASTER_CLOCK</b>

<dd>
<p>Stream-specific code that indicates that the master clock is closed.</p>
</dd>

### -field <a id="SRB_PROPOSE_STREAM_RATE"></a><a id="srb_propose_stream_rate"></a><b>SRB_PROPOSE_STREAM_RATE</b>

<dd>
<p>Stream-specific code that indicates a new rate is proposed, it does not change the rate.</p>
</dd>

### -field <a id="SRB_SET_DATA_FORMAT"></a><a id="srb_set_data_format"></a><b>SRB_SET_DATA_FORMAT</b>

<dd>
<p>Stream-specific code that sets a new data format.</p>
</dd>

### -field <a id="SRB_GET_DATA_FORMAT"></a><a id="srb_get_data_format"></a><b>SRB_GET_DATA_FORMAT</b>

<dd>
<p>Stream-specific code that returns the current data format.</p>
</dd>

### -field <a id="SRB_BEGIN_FLUSH"></a><a id="srb_begin_flush"></a><b>SRB_BEGIN_FLUSH</b>

<dd>
<p>Stream-specific code that begins the flush state.</p>
</dd>

### -field <a id="SRB_END_FLUSH"></a><a id="srb_end_flush"></a><b>SRB_END_FLUSH</b>

<dd>
<p>Stream-specific code that ends the flush state.</p>
</dd>

### -field <a id="SRB_GET_STREAM_INFO_"></a><a id="srb_get_stream_info_"></a><b>SRB_GET_STREAM_INFO </b>

<dd>
<p>Device instance-specific code that gets the stream information structure.</p>
</dd>

### -field <a id="SRB_OPEN_STREAM"></a><a id="srb_open_stream"></a><b>SRB_OPEN_STREAM</b>

<dd>
<p>Device instance-specific code that opens the specified stream.</p>
</dd>

### -field <a id="SRB_CLOSE_STREAM"></a><a id="srb_close_stream"></a><b>SRB_CLOSE_STREAM</b>

<dd>
<p>Device instance-specific code that closes the specific stream.</p>
</dd>

### -field <a id="SRB_OPEN_DEVICE_INSTANCE"></a><a id="srb_open_device_instance"></a><b>SRB_OPEN_DEVICE_INSTANCE</b>

<dd>
<p>Device instance-specific code that opens an instance of the device.</p>
</dd>

### -field <a id="SRB_CLOSE_DEVICE_INSTANCE"></a><a id="srb_close_device_instance"></a><b>SRB_CLOSE_DEVICE_INSTANCE</b>

<dd>
<p>Device instance-specific code that closes an instance of the device.</p>
</dd>

### -field <a id="SRB_GET_DEVICE_PROPERTY"></a><a id="srb_get_device_property"></a><b>SRB_GET_DEVICE_PROPERTY</b>

<dd>
<p>Device instance-specific code that gets the property of the device.</p>
</dd>

### -field <a id="SRB_SET_DEVICE_PROPERTY"></a><a id="srb_set_device_property"></a><b>SRB_SET_DEVICE_PROPERTY</b>

<dd>
<p>Device instance-specific code that sets the property of the device.</p>
</dd>

### -field <a id="SRB_INITIALIZE_DEVICE"></a><a id="srb_initialize_device"></a><b>SRB_INITIALIZE_DEVICE</b>

<dd>
<p>Device instance-specific code that initializes the device.</p>
</dd>

### -field <a id="SRB_CHANGE_POWER_STATE"></a><a id="srb_change_power_state"></a><b>SRB_CHANGE_POWER_STATE</b>

<dd>
<p>Device instance-specific code that changes the power state.</p>
</dd>

### -field <a id="SRB_UNINITIALIZE_DEVICE"></a><a id="srb_uninitialize_device"></a><b>SRB_UNINITIALIZE_DEVICE</b>

<dd>
<p>Device instance-specific code that uninitializes the device.</p>
</dd>

### -field <a id="SRB_UNKNOWN_DEVICE_COMMAND"></a><a id="srb_unknown_device_command"></a><b>SRB_UNKNOWN_DEVICE_COMMAND</b>

<dd>
<p>Device instance-specific code that specifies that the IRP function is unknown to the class driver.</p>
</dd>

### -field <a id="SRB_PAGING_OUT_DRIVER"></a><a id="srb_paging_out_driver"></a><b>SRB_PAGING_OUT_DRIVER</b>

<dd>
<p>Device instance-specific code that indicates that the driver is to be paged out only if it is enabled in the registry. Board ints should be disabled and STATUS_SUCCESS returned.</p>
</dd>

### -field <a id="SRB_GET_DATA_INTERSECTION"></a><a id="srb_get_data_intersection"></a><b>SRB_GET_DATA_INTERSECTION</b>

<dd>
<p>Device instance-specific code that returns stream data intersection.</p>
</dd>

### -field <a id="SRB_INITIALIZATION_COMPLETE"></a><a id="srb_initialization_complete"></a><b>SRB_INITIALIZATION_COMPLETE</b>

<dd>
<p>Device instance-specific code that indicates that the initialization sequence has completed.</p>
</dd>

### -field <a id="SRB_SURPRISE_REMOVAL"></a><a id="srb_surprise_removal"></a><b>SRB_SURPRISE_REMOVAL</b>

<dd>
<p>Device instance-specific code that indicates a surprise removal of hardware has occurred.</p>
</dd>

### -field <a id="SRB_DEVICE_METHOD"></a><a id="srb_device_method"></a><b>SRB_DEVICE_METHOD</b>

<dd></dd>

### -field <a id="SRB_STREAM_METHOD"></a><a id="srb_stream_method"></a><b>SRB_STREAM_METHOD</b>

<dd></dd>

### -field <a id="SRB_NOTIFY_IDLE_STATE"></a><a id="srb_notify_idle_state"></a><b>SRB_NOTIFY_IDLE_STATE</b>

<dd>
<p>Device instance-specific code that specifies to call on first open and last close.</p>
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
<dt>Strmini.h</dt>
</dl>
</td>
</tr>
</table>