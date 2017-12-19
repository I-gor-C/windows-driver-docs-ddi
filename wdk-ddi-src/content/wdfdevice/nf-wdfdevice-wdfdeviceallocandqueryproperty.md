---
UID: NF.wdfdevice.WdfDeviceAllocAndQueryProperty
title: WdfDeviceAllocAndQueryProperty function
author: windows-driver-content
description: The WdfDeviceAllocAndQueryProperty method allocates a buffer and retrieves a specified device property.
old-location: wdf\wdfdeviceallocandqueryproperty.htm
old-project: wdf
ms.assetid: f921fee7-e2c0-4e0f-a78b-d2dff8af97a2
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDeviceAllocAndQueryProperty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceAllocAndQueryProperty
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceAllocAndQueryProperty function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDeviceAllocAndQueryProperty</b> method allocates a buffer and retrieves a specified device property.



## -syntax

````
NTSTATUS WdfDeviceAllocAndQueryProperty(
  _In_     WDFDEVICE                Device,
  _In_     DEVICE_REGISTRY_PROPERTY DeviceProperty,
  _In_     POOL_TYPE                PoolType,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES   PropertyMemoryAttributes,
  _Out_    WDFMEMORY                *PropertyMemory
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.


### -param DeviceProperty [in]

A <a href="kernel.device_registry_property">DEVICE_REGISTRY_PROPERTY</a>-typed enumerator that identifies the device property to be retrieved.


### -param PoolType [in]

A <a href="kernel.pool_type">POOL_TYPE</a>-typed enumerator that specifies the type of memory to be allocated.


### -param PropertyMemoryAttributes [in, optional]

A pointer to a caller-allocated <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that describes object attributes for the memory object that the function will allocate. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.


### -param PropertyMemory [out]

A pointer to a WDFMEMORY-typed location that receives a handle to a framework memory object. 


## -returns
If the operation succeeds, <b>WdfDeviceAllocAndQueryProperty</b> returns STATUS_SUCCESS. Additional return values include:
<dl>
<dt><b>STATUS_INVALID_PARAMETER or STATUS_INVALID_PARAMETER_2</b></dt>
</dl>The specified <i>DeviceProperty</i> value is invalid.

<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>The device's drivers have not yet reported the device's properties.

 

The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A bug check occurs if the driver supplies an invalid object handle.


## -remarks
The <b>WdfDeviceAllocAndQueryProperty</b> method determines the amount of memory that is necessary to hold the requested device property. It allocates enough memory to hold the data, and returns a handle to a framework memory object that describes the allocated memory. To access the data, your driver can call <a href="wdf.wdfmemorygetbuffer">WdfMemoryGetBuffer</a>. 

Alternatively, you can use <a href="wdf.wdfdeviceallocandquerypropertyex">WdfDeviceAllocAndQueryPropertyEx</a> to access device properties that are exposed through the Unified Property Model.

The following code example initializes a <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure with attributes for the framework memory object that the framework will create for the requested property. Then, the example calls <b>WdfDeviceAllocAndQueryProperty</b> to obtain the <b>DevicePropertyPhysicalDeviceObjectName</b> property. After <b>WdfDeviceAllocAndQueryProperty</b> returns, the driver can call <a href="wdf.wdfmemorygetbuffer">WdfMemoryGetBuffer</a> to obtain a pointer to the buffer that contains the name string.


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
Minimum KMDF version

</th>
<td width="70%">
1.0

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
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdevicequeryproperty">WdfDeviceQueryProperty</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceAllocAndQueryProperty method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

