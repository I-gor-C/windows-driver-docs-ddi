---
UID: NF.wdfdevice.WdfDeviceAllocAndQueryInterfaceProperty
title: WdfDeviceAllocAndQueryInterfaceProperty
author: windows-driver-content
description: The WdfDeviceAllocAndQueryInterfaceProperty method allocates a buffer and retrieves a specified device interface property.
old-location: wdf\wdfdeviceallocandqueryinterfaceproperty.htm
old-project: wdf
ms.assetid: 40516E83-892C-4538-B452-DAB0F5ACBB25
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDeviceAllocAndQueryInterfaceProperty
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
req.alt-api: WdfDeviceAllocAndQueryInterfaceProperty
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceAllocAndQueryInterfaceProperty function



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>WdfDeviceAllocAndQueryInterfaceProperty</b> method  allocates a buffer and retrieves a specified device interface property.</p>


## -syntax

````
NTSTATUS WdfDeviceAllocAndQueryInterfaceProperty(
  _In_     WDFDEVICE                           Device,
  _In_     PWDF_DEVICE_INTERFACE_PROPERTY_DATA PropertyData,
  _In_     POOL_TYPE                           PoolType,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES              PropertyMemoryAttributes,
  _Out_    WDFMEMORY                           PropertyMemory,
  _Out_    PDEVPROPTYPE                        Type
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>PropertyData</i> [in]

<dd>
<p>A pointer to a <a href="..\wdfdevice\ns-wdfdevice--wdf-device-interface-property-data.md">WDF_DEVICE_INTERFACE_PROPERTY_DATA</a> structure that identifies the device interface property to be retrieved.</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>A <b>POOL_TYPE</b>-typed enumerator that specifies the type of memory to be allocated.</p>
</dd>

### -param <i>PropertyMemoryAttributes</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that describes object attributes for the memory object that the function will allocate. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>PropertyMemory</i> [out]

<dd>
<p>A pointer to a <b>WDFMEMORY</b>-typed location that receives a handle to a framework memory object.

</p>
</dd>

### -param <i>Type</i> [out]

<dd>
<p>A pointer to a <b>DEVPROPTYPE</b>-typed variable that, on return,  identifies the type of property data contained in <i>PropertyMemory</i>.</p>
</dd>
</dl>

## -returns
<p>If the <b>WdfDeviceAllocAndQueryInterfaceProperty</b> method encounters no errors, it returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameters is incorrect.</p>

<p> </p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>The <b>WdfDeviceAllocAndQueryInterfaceProperty</b> method determines the amount of memory that is necessary to hold the requested device interface property. It allocates enough memory to hold the data, and returns a handle to a framework memory object that describes the allocated memory. To access the data, your driver can call <a href="..\wdfmemory\nf-wdfmemory-wdfmemorygetbuffer.md">WdfMemoryGetBuffer</a>. </p>

<p>For information about related methods, see <a href="wdf.accessing_the_unified_device_property_model">Accessing the Unified Device Property Model</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\ns-wdfdevice--wdf-device-interface-property-data.md">WDF_DEVICE_INTERFACE_PROPERTY_DATA</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdf-device-interface-property-data-init.md">WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdeviceassigninterfaceproperty.md">WdfDeviceAssignInterfaceProperty</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicequeryinterfaceproperty.md">WdfDeviceQueryInterfaceProperty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceAllocAndQueryInterfaceProperty method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
