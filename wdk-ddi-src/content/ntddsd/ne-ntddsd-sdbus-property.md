---
UID: NE.ntddsd.SDBUS_PROPERTY
title: SDBUS_PROPERTY
author: windows-driver-content
description: The SDBUS_PROPERTY enumeration lists the properties of a Secure Digital (SD) card that an SD device driver can set with an SD request.
old-location: sd\sdbus_property.htm
old-project: SD
ms.assetid: 22301feb-2c6b-43ac-b7e8-c10f2e8e4d62
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: STORAGE_DIAGNOSTIC_MP_REQUEST, STORAGE_DIAGNOSTIC_MP_REQUEST, *PSTORAGE_DIAGNOSTIC_MP_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddsd.h
req.include-header: Ntddsd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SDBUS_PROPERTY
req.alt-loc: ntddsd.h
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
---

# SDBUS_PROPERTY enumeration



## -description
<p>The SDBUS_PROPERTY enumeration lists the properties of a Secure Digital (SD) card that an SD device driver can set with an SD request.</p>


## -syntax

````
typedef enum  { 
  SDP_MEDIA_CHANGECOUNT      = 0,
  SDP_MEDIA_STATE            = 1,
  SDP_WRITE_PROTECTED        = 2,
  SDP_FUNCTION_NUMBER        = 3,
  SDP_FUNCTION_TYPE          = 4,
  SDP_BUS_DRIVER_VERSION     = 5,
  SDP_BUS_WIDTH              = 6,
  SDP_BUS_CLOCK              = 7,
  SDP_BUS_INTERFACE_CONTROL  = 8,
  SDP_HOST_BLOCK_LENGTH      = 9,
  SDP_FUNCTION_BLOCK_LENGTH  = 10,
  SDP_FN0_BLOCK_LENGTH       = 11,
  SDP_FUNCTION_INT_ENABLE    = 12
} SDBUS_PROPERTY;
````


## -enum-fields
<dl>

### -field <a id="SDP_MEDIA_CHANGECOUNT"></a><a id="sdp_media_changecount"></a><b>SDP_MEDIA_CHANGECOUNT</b>

<dd>
<p>Indicates that the operation applies to the media change count property. This property includes 4 bytes of data (ULONG) that describe SD storage functions. This property is read-only. </p>
</dd>

### -field <a id="SDP_MEDIA_STATE"></a><a id="sdp_media_state"></a><b>SDP_MEDIA_STATE</b>

<dd>
<p>Indicates that the operation applies to the media state property. Provided for compatibility with SD storage-only host controllers. Valid only for SD storage functions. For a list of valid media states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff537944">SDPROP_MEDIA_STATE</a><u>.</u> This property is read-only. </p>
</dd>

### -field <a id="SDP_WRITE_PROTECTED"></a><a id="sdp_write_protected"></a><b>SDP_WRITE_PROTECTED</b>

<dd>
<p>Indicates that the operation applies to the write-protected property and the state of the WriteProtect switch on the SD card. This property is read-only.</p>
</dd>

### -field <a id="SDP_FUNCTION_NUMBER"></a><a id="sdp_function_number"></a><b>SDP_FUNCTION_NUMBER</b>

<dd>
<p>Indicates that the operation applies to the function number property. This property is read-only.</p>
</dd>

### -field <a id="SDP_FUNCTION_TYPE"></a><a id="sdp_function_type"></a><b>SDP_FUNCTION_TYPE</b>

<dd>
<p>v2.0 SDBUS_FUNCTION_TYPE</p>
</dd>

### -field <a id="SDP_BUS_DRIVER_VERSION"></a><a id="sdp_bus_driver_version"></a><b>SDP_BUS_DRIVER_VERSION</b>

<dd>
<p>Indicates that the operation applies to the driver version property. This property is read-only. This property is only supported in version 2.0 or later of the driver.</p>
</dd>

### -field <a id="SDP_BUS_WIDTH"></a><a id="sdp_bus_width"></a><b>SDP_BUS_WIDTH</b>

<dd>
<p>Indicates that the operation applies to the bus width property. The value of this property is either 1 or 4. This property is only supported in version 2.0 or later of the driver.</p>
</dd>

### -field <a id="SDP_BUS_CLOCK"></a><a id="sdp_bus_clock"></a><b>SDP_BUS_CLOCK</b>

<dd>
<p>Indicates that the operation applies to the bus clock speed property. The value of this property is in KHz. This property is only supported in version 2.0 or later of the driver.</p>
</dd>

### -field <a id="SDP_BUS_INTERFACE_CONTROL"></a><a id="sdp_bus_interface_control"></a><b>SDP_BUS_INTERFACE_CONTROL</b>

<dd>
<p>Indicates that the operation applies to the SDIO bus interface control property.This property is corresponding to CCCR[7], which is defined in the <i>Secure Digital I/O (SDIO) Card Specification</i>. For setting bus width, SDP_BUS_WIDTH should be used to synchronize the memory function of a combination card. This property is only supported in version 2.0 or later of the driver.</p>
</dd>

### -field <a id="SDP_HOST_BLOCK_LENGTH"></a><a id="sdp_host_block_length"></a><b>SDP_HOST_BLOCK_LENGTH</b>

<dd>
<p>Indicates that the operation applies to the host block length property, which is the maximum block length that is supported by the controller. This property is read-only. This property is only supported in version 2.0 or later of the driver.</p>
</dd>

### -field <a id="SDP_FUNCTION_BLOCK_LENGTH"></a><a id="sdp_function_block_length"></a><b>SDP_FUNCTION_BLOCK_LENGTH</b>

<dd>
<p>Indicates that the operation applies to the SDIO function block length property. This property is only supported in version 2.0 or later of the driver.</p>
</dd>

### -field <a id="SDP_FN0_BLOCK_LENGTH"></a><a id="sdp_fn0_block_length"></a><b>SDP_FN0_BLOCK_LENGTH</b>

<dd>
<p>Indicates that the operation applies to the SDIO function zero block length property. This property is shared by all functions of the SDIO card. This property is only supported in version 2.0 or later of the driver.</p>
</dd>

### -field <a id="SDP_FUNCTION_INT_ENABLE"></a><a id="sdp_function_int_enable"></a><b>SDP_FUNCTION_INT_ENABLE</b>

<dd>
<p>Indicates that the operation applies to the SDIO function interrupt enable property. It is a Boolean-type property and only applies to the current function. This property is only supported in version 2.0 or later of the driver.</p>
</dd>
</dl>

## -remarks
<p>To read or set a property on an SD device, a device driver must do the following:</p>

<p>Set the <b>RequestFunction</b> member of <a href="https://msdn.microsoft.com/09b30bf0-fe85-4ad5-bd3e-113ed3a093ac">SDBUS_REQUEST_PACKET</a> to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff538012">SD_REQUEST_FUNCTION</a> enumeration value of either SDRF_GET_PROPERTY or SDRF_SET_PROPERTY.</p>

<p>Set the <b>Property</b> member of SDBUS_REQUEST_PACKET to the SDBUS_PROPERTY enumeration value that specifies the property to read or change.</p>

<p>Send the request to the bus driver by passing the initialized SDBUS_REQUEST_PACKET structure to either <a href="https://msdn.microsoft.com/library/windows/hardware/ff537909">SdBusSubmitRequest</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff537914">SdBusSubmitRequestAsync</a>.</p>

<p>To read or set a property on an SD device, a device driver must do the following:</p>

<p>Set the <b>RequestFunction</b> member of <a href="https://msdn.microsoft.com/09b30bf0-fe85-4ad5-bd3e-113ed3a093ac">SDBUS_REQUEST_PACKET</a> to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff538012">SD_REQUEST_FUNCTION</a> enumeration value of either SDRF_GET_PROPERTY or SDRF_SET_PROPERTY.</p>

<p>Set the <b>Property</b> member of SDBUS_REQUEST_PACKET to the SDBUS_PROPERTY enumeration value that specifies the property to read or change.</p>

<p>Send the request to the bus driver by passing the initialized SDBUS_REQUEST_PACKET structure to either <a href="https://msdn.microsoft.com/library/windows/hardware/ff537909">SdBusSubmitRequest</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff537914">SdBusSubmitRequestAsync</a>.</p>

<p>To read or set a property on an SD device, a device driver must do the following:</p>

<p>Set the <b>RequestFunction</b> member of <a href="https://msdn.microsoft.com/09b30bf0-fe85-4ad5-bd3e-113ed3a093ac">SDBUS_REQUEST_PACKET</a> to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff538012">SD_REQUEST_FUNCTION</a> enumeration value of either SDRF_GET_PROPERTY or SDRF_SET_PROPERTY.</p>

<p>Set the <b>Property</b> member of SDBUS_REQUEST_PACKET to the SDBUS_PROPERTY enumeration value that specifies the property to read or change.</p>

<p>Send the request to the bus driver by passing the initialized SDBUS_REQUEST_PACKET structure to either <a href="https://msdn.microsoft.com/library/windows/hardware/ff537909">SdBusSubmitRequest</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff537914">SdBusSubmitRequestAsync</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddsd.h (include Ntddsd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538012">SD_REQUEST_FUNCTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/09b30bf0-fe85-4ad5-bd3e-113ed3a093ac">SDBUS_REQUEST_PACKET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537909">SdBusSubmitRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537914">SdBusSubmitRequestAsync</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SD\buses]:%20SDBUS_PROPERTY enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
