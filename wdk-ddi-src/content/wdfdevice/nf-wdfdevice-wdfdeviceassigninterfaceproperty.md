---
UID: NF.wdfdevice.WdfDeviceAssignInterfaceProperty
title: WdfDeviceAssignInterfaceProperty function
author: windows-driver-content
description: The WdfDeviceAssignInterfaceProperty method modifies the current value of a device interface property.
old-location: wdf\wdfdeviceassigninterfaceproperty.htm
old-project: wdf
ms.assetid: 49608EE6-1666-4430-AD22-9627EEF6F223
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDeviceAssignInterfaceProperty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WdfDeviceAssignInterfaceProperty
req.alt-loc: WUDFx02000.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WUDFx02000.lib
req.dll: WUDFx02000.dll; TBD
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceAssignInterfaceProperty function



## -description
<p class="CCE_Message">[Applies to UMDF only]
The <b>WdfDeviceAssignInterfaceProperty</b> method modifies the current value of a <a href="https://msdn.microsoft.com/43aa0ce6-a06b-43e4-a213-300554391ae0">device interface property</a>.


## -syntax

````
NTSTATUS WdfDeviceAssignInterfaceProperty(
  _In_     WDFDEVICE                           Device,
  _In_     PWDF_DEVICE_INTERFACE_PROPERTY_DATA PropertyData,
  _In_     DEVPROPTYPE                         Type,
  _In_     ULONG                               BufferLength,
  _In_opt_ PVOID                               PropertyBuffer
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.

### -param PropertyData [in]

A pointer to <a href="wdf.wdf_device_interface_property_data">WDF_DEVICE_INTERFACE_PROPERTY_DATA</a> structure.

### -param Type [in]

A <b>DEVPROPTYPE</b>-typed value that specifies the type of the data that is provided in <i>PropertyBuffer</i>.

### -param BufferLength [in]

Specifies the length, in bytes, of the buffer that <i>PropertyBuffer</i> points to.

### -param PropertyBuffer [in, optional]

A pointer to the device interface property data. Set this parameter to <b>NULL</b> to delete the specified property.

## -returns
If the <b>WdfDeviceAssignInterfaceProperty</b> method encounters no errors, it returns STATUS_SUCCESS. Additional return values include:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>One of the parameters is incorrect.

 

The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

## -remarks
For information about related methods, see <a href="wdf.accessing_the_unified_device_property_model">Accessing the Unified Device Property Model</a>.

The following code example initializes a <a href="wdf.wdf_device_interface_property_data">WDF_DEVICE_INTERFACE_PROPERTY_DATA</a> structure and then calls <b>WdfDeviceAssignInterfaceProperty</b>.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum support
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version
</th>
<td width="70%">
2.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.dll; </dt>
<dt>TBD</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_device_interface_property_data">WDF_DEVICE_INTERFACE_PROPERTY_DATA</a>
</dt>
<dt>
<a href="wdf.wdf_device_interface_property_data_init">WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT</a>
</dt>
<dt>
<a href="wdf.wdfdeviceallocandqueryinterfaceproperty">WdfDeviceAllocAndQueryInterfaceProperty</a>
</dt>
<dt>
<a href="wdf.wdfdevicequeryinterfaceproperty">WdfDeviceQueryInterfaceProperty</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceAssignInterfaceProperty method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
