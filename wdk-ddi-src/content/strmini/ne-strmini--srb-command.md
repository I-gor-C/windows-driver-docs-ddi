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

### -field SRB_READ_DATA

<dd>
<p>Stream-specific code that specifies to read data from hardware.</p>
</dd>

### -field SRB_WRITE_DATA

<dd>
<p>Stream-specific code that specifies to write data to the hardware.</p>
</dd>

### -field SRB_GET_STREAM_STATE

<dd>
<p>Stream-specific code that specifies to get the state of the stream.</p>
</dd>

### -field SRB_SET_STREAM_STATE

<dd>
<p>Stream-specific code that specifies to set the state of the stream.</p>
</dd>

### -field SRB_SET_STREAM_PROPERTY

<dd>
<p>Stream-specific code that specifies to set a property of the stream.</p>
</dd>

### -field SRB_GET_STREAM_PROPERTY

<dd>
<p>Stream-specific code that specifies to get a property value for the stream.</p>
</dd>

### -field SRB_OPEN_MASTER_CLOCK

<dd>
<p>Stream-specific code that indicates that the master clock is on this stream.</p>
</dd>

### -field SRB_INDICATE_MASTER_CLOCK

<dd>
<p>Stream-specific code that specifies that the handle is supplied to the master clock.</p>
</dd>

### -field SRB_UNKNOWN_STREAM_COMMAND

<dd>
<p>Stream-specific code that specifies that the IRP function is unknown to the class driver.</p>
</dd>

### -field SRB_SET_STREAM_RATE

<dd>
<p>Stream-specific code that specifies that the rate is set at which the stream should run.</p>
</dd>

### -field SRB_PROPOSE_DATA_FORMAT

<dd>
<p>Stream-specific code that specifies that a new rate is proposed, it does not change the rate.</p>
</dd>

### -field SRB_CLOSE_MASTER_CLOCK

<dd>
<p>Stream-specific code that indicates that the master clock is closed.</p>
</dd>

### -field SRB_PROPOSE_STREAM_RATE

<dd>
<p>Stream-specific code that indicates a new rate is proposed, it does not change the rate.</p>
</dd>

### -field SRB_SET_DATA_FORMAT

<dd>
<p>Stream-specific code that sets a new data format.</p>
</dd>

### -field SRB_GET_DATA_FORMAT

<dd>
<p>Stream-specific code that returns the current data format.</p>
</dd>

### -field SRB_BEGIN_FLUSH

<dd>
<p>Stream-specific code that begins the flush state.</p>
</dd>

### -field SRB_END_FLUSH

<dd>
<p>Stream-specific code that ends the flush state.</p>
</dd>

### -field SRB_GET_STREAM_INFO 

<dd>
<p>Device instance-specific code that gets the stream information structure.</p>
</dd>

### -field SRB_OPEN_STREAM

<dd>
<p>Device instance-specific code that opens the specified stream.</p>
</dd>

### -field SRB_CLOSE_STREAM

<dd>
<p>Device instance-specific code that closes the specific stream.</p>
</dd>

### -field SRB_OPEN_DEVICE_INSTANCE

<dd>
<p>Device instance-specific code that opens an instance of the device.</p>
</dd>

### -field SRB_CLOSE_DEVICE_INSTANCE

<dd>
<p>Device instance-specific code that closes an instance of the device.</p>
</dd>

### -field SRB_GET_DEVICE_PROPERTY

<dd>
<p>Device instance-specific code that gets the property of the device.</p>
</dd>

### -field SRB_SET_DEVICE_PROPERTY

<dd>
<p>Device instance-specific code that sets the property of the device.</p>
</dd>

### -field SRB_INITIALIZE_DEVICE

<dd>
<p>Device instance-specific code that initializes the device.</p>
</dd>

### -field SRB_CHANGE_POWER_STATE

<dd>
<p>Device instance-specific code that changes the power state.</p>
</dd>

### -field SRB_UNINITIALIZE_DEVICE

<dd>
<p>Device instance-specific code that uninitializes the device.</p>
</dd>

### -field SRB_UNKNOWN_DEVICE_COMMAND

<dd>
<p>Device instance-specific code that specifies that the IRP function is unknown to the class driver.</p>
</dd>

### -field SRB_PAGING_OUT_DRIVER

<dd>
<p>Device instance-specific code that indicates that the driver is to be paged out only if it is enabled in the registry. Board ints should be disabled and STATUS_SUCCESS returned.</p>
</dd>

### -field SRB_GET_DATA_INTERSECTION

<dd>
<p>Device instance-specific code that returns stream data intersection.</p>
</dd>

### -field SRB_INITIALIZATION_COMPLETE

<dd>
<p>Device instance-specific code that indicates that the initialization sequence has completed.</p>
</dd>

### -field SRB_SURPRISE_REMOVAL

<dd>
<p>Device instance-specific code that indicates a surprise removal of hardware has occurred.</p>
</dd>

### -field SRB_DEVICE_METHOD

<dd></dd>

### -field SRB_STREAM_METHOD

<dd></dd>

### -field SRB_NOTIFY_IDLE_STATE

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