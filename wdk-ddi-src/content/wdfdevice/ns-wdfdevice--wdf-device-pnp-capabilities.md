---
UID: NS.wdfdevice._WDF_DEVICE_PNP_CAPABILITIES
title: WDF_DEVICE_PNP_CAPABILITIES
author: windows-driver-content
description: The WDF_DEVICE_PNP_CAPABILITIES structure describes a device's Plug and Play capabilities.
old-location: wdf\wdf_device_pnp_capabilities.htm
ms.assetid: 0857e32e-9962-44ca-9d61-b98b09073c16
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_DEVICE_PNP_CAPABILITIES
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
req.irql: <=DISPATCH_LEVEL
ms.keywords: WDF_DEVICE_PNP_CAPABILITIES, WDF_DEVICE_PNP_CAPABILITIES, *PWDF_DEVICE_PNP_CAPABILITIES
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_PNP_CAPABILITIES structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The WDF_DEVICE_PNP_CAPABILITIES structure describes a device's Plug and Play capabilities.</p>


## -syntax

````
typedef struct _WDF_DEVICE_PNP_CAPABILITIES {
  ULONG         Size;
  WDF_TRI_STATE LockSupported;
  WDF_TRI_STATE EjectSupported;
  WDF_TRI_STATE Removable;
  WDF_TRI_STATE DockDevice;
  WDF_TRI_STATE UniqueID;
  WDF_TRI_STATE SilentInstall;
  WDF_TRI_STATE SurpriseRemovalOK;
  WDF_TRI_STATE HardwareDisabled;
  WDF_TRI_STATE NoDisplayInUI;
  ULONG         Address;
  ULONG         UINumber;
} WDF_DEVICE_PNP_CAPABILITIES, *PWDF_DEVICE_PNP_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>LockSupported</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value that indicates, if set to <b>WdfTrue</b>, that the device can be locked in its slot to prevent ejection. (This capability disables ejecting a device from its slot, not ejecting media from a device.) For more information about WDF_TRI_STATE-typed values, see the following Remarks section.  </p>
</dd>

### -field <b>EjectSupported</b>

<dd>
<p>A WDF_TRI_STATE-typed value that indicates, if set to <b>WdfTrue</b>, that the device can be ejected from its slot. (This capability enables ejecting a device from its slot, not ejecting media from a device.) </p>
</dd>

### -field <b>Removable</b>

<dd>
<p>A WDF_TRI_STATE-typed value that indicates, if set to <b>WdfTrue</b>, that the device can be removed while the system is running. If <b>Removable</b> is set to <b>WdfTrue</b> and <b>SurpriseRemovalOK</b> is set to <b>WdfFalse</b>, users should use the system's Unplug or Eject Hardware program.</p>
</dd>

### -field <b>DockDevice</b>

<dd>
<p>A WDF_TRI_STATE-typed value that indicates, if set to <b>WdfTrue</b>, that the device is a docking station.</p>
</dd>

### -field <b>UniqueID</b>

<dd>
<p>A WDF_TRI_STATE-typed value that indicates, if set to <b>WdfTrue</b>, that the device's instance ID is unique to the entire system. If <b>UniqueID</b> is set to <b>WdfFalse</b>, the instance ID is unique only to the device's bus. For more information about instance IDs, see <a href="NULL">Device Identification Strings</a>.</p>
</dd>

### -field <b>SilentInstall</b>

<dd>
<p>A WDF_TRI_STATE-typed value that indicates, if set to <b>WdfTrue</b>, that Device Manager should not display dialog boxes during installation of the device.</p>
</dd>

### -field <b>SurpriseRemovalOK</b>

<dd>
<p>A WDF_TRI_STATE-typed value that indicates, if set to <b>WdfTrue</b> (and if <b>Removable</b> is also set to <b>WdfTrue</b>), that users can remove the device without using the system's Unplug or Eject Hardware program.</p>
</dd>

### -field <b>HardwareDisabled</b>

<dd>
<p>A WDF_TRI_STATE-typed value that indicates, if set to <b>WdfTrue</b>, that the device is disabled.</p>
</dd>

### -field <b>NoDisplayInUI</b>

<dd>
<p>A WDF_TRI_STATE-typed value that indicates, if set to <b>WdfTrue</b>, that Device Manager should not display the device.</p>
</dd>

### -field <b>Address</b>

<dd>
<p>An address that indicates where the device is located on its bus. </p>
<p>The interpretation of this number is bus-specific. If the address is unknown or the bus driver does not support an address, the bus driver leaves the <b>Address</b> member at its default value of 0xFFFFFFFF (-1).</p>
<p>The following list describes the information that certain bus drivers store in the <b>Address</b> member for their child devices:</p>
<p></p>
<dl>

### -field <a id="1394"></a>1394

<dd>
<p>Does not supply an address because the addresses are volatile. Defaults to 0xFFFFFFFF. </p>
</dd>

### -field <a id="EISA"></a><a id="eisa"></a>EISA

<dd>
<p>Slot Number (0-F).</p>
</dd>

### -field <a id="IDE"></a><a id="ide"></a>IDE

<dd>
<p>For an IDE device, the address contains the target ID and LUN. For an IDE channel, the address is 0 if the channel is the primary channel or 1 if the channel is the secondary channel).</p>
</dd>

### -field <a id="ISApnp"></a><a id="isapnp"></a><a id="ISAPNP"></a>ISApnp

<dd>
<p>Does not supply an address. Defaults to 0xFFFFFFFF.</p>
</dd>

### -field <a id="PC_Card__PCMCIA_"></a><a id="pc_card__pcmcia_"></a><a id="PC_CARD__PCMCIA_"></a>PC Card (PCMCIA)

<dd>
<p>The socket number (typically 0x00 or 0x40).</p>
</dd>

### -field <a id="PCI"></a><a id="pci"></a>PCI

<dd>
<p>The device number in the high word and the function number in the low word.</p>
</dd>

### -field <a id="SCSI"></a><a id="scsi"></a>SCSI

<dd>
<p>The target ID.</p>
</dd>

### -field <a id="USB"></a><a id="usb"></a>USB

<dd>
<p>The port number.</p>
</dd>
</dl>
</dd>

### -field <b>UINumber</b>

<dd>
<p>A number that is associated with the device and can be displayed in user interfaces. This number is typically a user-perceived slot number, such as a number printed next to the slot on the board or some other number that helps the user locate the device. If <b>UINumber</b> is unknown, or if supplying a number would not assist the user in identifying the device's location, the driver sets this value to -1.</p>
</dd>
</dl>

## -remarks
<p>Several members use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a> type. For these members, a value of <b>WdfTrue</b> indicates that the device supports the capability and a value of <b>WdfFalse</b> indicates it does not. A value of <b>WdfUseDefault</b> indicates the framework will use the value that a driver lower in the stack provided. For example, if a bus driver specifies <b>WdfTrue</b> for <b>LockSupported</b> and the device's function driver specifies <b>WdfUseDefault</b>, the framework stores <b>WdfTrue</b> for the capability.</p>

<p>The WDF_DEVICE_PNP_CAPABILITIES structure is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546898">WdfDeviceSetPnpCapabilities</a>.</p>

<p>To initialize a WDF_DEVICE_PNP_CAPABILITIES structure, a driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551259">WDF_DEVICE_PNP_CAPABILITIES_INIT</a>.</p>

## -requirements
<table>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546901">WdfDeviceSetPowerCapabilities</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548802">WdfPdoInitAssignRawDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_PNP_CAPABILITIES structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
