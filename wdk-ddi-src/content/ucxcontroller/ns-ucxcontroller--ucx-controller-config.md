---
UID: NS.ucxcontroller._UCX_CONTROLLER_CONFIG
title: UCX_CONTROLLER_CONFIG
author: windows-driver-content
description: This structure configuration data for a USB controller.
old-location: buses\_ucx_controller_config.htm
old-project: usbref
ms.assetid: 9A4249B6-BFC2-42B4-BBA6-094BD78C98DE
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_CONTROLLER_CONFIG, UCX_CONTROLLER_CONFIG, *PUCX_CONTROLLER_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxcontroller.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_CONTROLLER_CONFIG
req.alt-loc: Ucxcontroller.h
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

# UCX_CONTROLLER_CONFIG structure



## -description
<p>This structure configuration data for a USB controller.</p>


## -syntax

````
typedef struct _UCX_CONTROLLER_CONFIG {
   ULONG                                                                   Size;
  ULONG                                                                    NumberOfPresentedDeviceMgmtEvtCallbacks;
  PFN_UCX_CONTROLLER_QUERY_USB_CAPABILITY                                  EvtControllerQueryUsbCapability;
  HANDLE                                                                   Reserved1;
  PFN_UCX_CONTROLLER_GET_CURRENT_FRAMENUMBER                               EvtControllerGetCurrentFrameNumber;
  PFN_UCX_CONTROLLER_USBDEVICE_ADD                                         EvtControllerUsbDeviceAdd;
  PFN_UCX_CONTROLLER_RESET                                                 EvtControllerReset;
  HANDLE                                                                   Reserved2;
  HANDLE                                                                   Reserved3;
  HANDLE                                                                   Reserved4;
  UCX_CONTROLLER_PARENT_BUS_TYPE                                           ParentBusType;
  UCX_CONTROLLER_PCI_INFORMATION                                           PciDeviceInfo;
  UCX_CONTROLLER_ACPI_INFORMATION                                          AcpiDeviceInfo;
  UCHAR                                                                    DeviceDescription[MAX_GENERIC_USB_CONTROLLER_NAME_SIZE];
  UNICODE_STRING                                                           ManufacturerNameString;
  UNICODE_STRING                                                           ModelNameString;
  UNICODE_STRING                                                           ModelNumberString;
      PFN_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS                     EvtControllerGetTransportCharacteristics;
      PFN_UCX_CONTROLLER_SET_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION EvtControllerSetTransportCharacteristicsChangeNotification;
  HANDLE                                                                   Reserved5;
  HANDLE                                                                   Reserved6;
  HANDLE                                                                   Reserved7;
} UCX_CONTROLLER_CONFIG, *P_UCX_CONTROLLER_CONFIG;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field NumberOfPresentedDeviceMgmtEvtCallbacks

<dd>
<p>The number of device event callback functions provided by this structure.</p>
</dd>

### -field EvtControllerQueryUsbCapability

<dd>
<p>A pointer to an <a href="..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-query-usb-capability.md">EVT_UCX_CONTROLLER_QUERY_USB_CAPABILITY</a> callback function.</p>
</dd>

### -field Reserved1

<dd>
<p>Do not use.</p>
</dd>

### -field EvtControllerGetCurrentFrameNumber

<dd>
<p>A pointer to an <a href="..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-get-current-framenumber.md">EVT_UCX_CONTROLLER_GET_CURRENT_FRAMENUMBER</a> call back function.</p>
</dd>

### -field EvtControllerUsbDeviceAdd

<dd>
<p>A pointer to an <a href="..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-usbdevice-add.md">EVT_UCX_CONTROLLER_USBDEVICE_ADD</a> callback function.</p>
</dd>

### -field EvtControllerReset

<dd>
<p>A pointer to an <a href="..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-reset.md">EVT_UCX_CONTROLLER_RESET</a> callback function.</p>
</dd>

### -field Reserved2

<dd>
<p>Do not use.</p>
</dd>

### -field Reserved3

<dd>
<p>Do not use.</p>
</dd>

### -field Reserved4

<dd>
<p>Do not use.</p>
</dd>

### -field ParentBusType

<dd>
<p>The parent bus type of the USB controller.</p>
</dd>

### -field PciDeviceInfo

<dd>
<p>Information about the PCI USB controller (if present).</p>
</dd>

### -field AcpiDeviceInfo

<dd>
<p>Information about the advanced configuration and power interface (ACPI) USB controller (if present).</p>
</dd>

### -field DeviceDescription

<dd>
<p>A description for the device.</p>
</dd>

### -field ManufacturerNameString

<dd>
<p>String containing the manufacturer name.</p>
</dd>

### -field ModelNameString

<dd>
<p>String containing the model name of the controller hardware.</p>
</dd>

### -field ModelNumberString

<dd>
<p>String containing the model number of the controller hardware.</p>
</dd>

### -field EvtControllerGetTransportCharacteristics

<dd>
<p>A pointer to an <a href="..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-get-transport-characteristics.md">EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS</a> callback function.</p>
</dd>

### -field EvtControllerSetTransportCharacteristicsChangeNotification

<dd>
<p>A pointer to an <a href="..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-set-transport-characteristics-change-notification.md">EVT_UCX_CONTROLLER_SET_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION</a> callback function.</p>
</dd>

### -field Reserved5

<dd>
<p>Do not use.</p>
</dd>

### -field Reserved6

<dd>
<p>Do not use.</p>
</dd>

### -field Reserved7

<dd>
<p>Do not use.</p>
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
<dt>Ucxcontroller.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>