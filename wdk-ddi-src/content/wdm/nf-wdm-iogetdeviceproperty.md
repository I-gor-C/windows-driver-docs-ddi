---
UID : NF:wdm.IoGetDeviceProperty
title : IoGetDeviceProperty function
author : windows-driver-content
description : The IoGetDeviceProperty routine retrieves information about a device such as configuration information and the name of its PDO.
old-location : kernel\iogetdeviceproperty.htm
old-project : kernel
ms.assetid : 8c3b7f81-ea6e-47ae-a396-58826d097f1f
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : IoGetDeviceProperty
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with Windows 2000.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IoGetDeviceProperty
req.alt-loc : NtosKrnl.exe
req.ddi-compliance : PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : PASSIVE_LEVEL
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# IoGetDeviceProperty function
The <b>IoGetDeviceProperty</b> routine retrieves information about a device such as configuration information and the name of its PDO.

## Syntax

````
NTSTATUS IoGetDeviceProperty(
  _In_      PDEVICE_OBJECT           DeviceObject,
  _In_      DEVICE_REGISTRY_PROPERTY DeviceProperty,
  _In_      ULONG                    BufferLength,
  _Out_opt_ PVOID                    PropertyBuffer,
  _Out_     PULONG                   ResultLength
);
````

## Parameters

`DeviceObject`

Pointer to the physical device object (PDO) for the device being queried.

`DeviceProperty`

Specifies the device property being requested. Must be one of the following <a href="https://msdn.microsoft.com/a17b4a88-45e8-45e7-b879-2f41b97be368">DEVICE_REGISTRY_PROPERTY</a> enumeration values:

`BufferLength`

Specifies the size, in bytes, of the caller-supplied <i>PropertyBuffer</i>.

`PropertyBuffer`

Pointer to a caller-supplied buffer to receive the property information. The buffer can be allocated from pageable memory. The type of the buffer is determined by the <i>DeviceProperty</i> (see above).

`ResultLength`

Pointer to a ULONG to receive the size of the property information returned at <i>PropertyBuffer</i>. If <b>IoGetDeviceProperty</b> returns STATUS_BUFFER_TOO_SMALL, it sets this parameter to the required buffer length.


## Return Value

<b>IoGetDeviceProperty</b> returns STATUS_SUCCESS if the call was successful. Possible error return values include the following.
<dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl>The buffer at <i>PropertyBuffer</i> was too small. <i>ResultLength</i> points to the required buffer length.
<dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl>The given <i>DeviceProperty</i> is not one of the properties handled by this routine.
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>Possibly indicates that the given <i>DeviceObject</i> was not a valid PDO pointer.

## Remarks

<b>IoGetDeviceProperty</b> retrieves device setup information from the registry. Use this routine, rather than accessing the registry directly, to insulate a driver from differences across platforms and from possible changes in the registry structure.

For many <i>DeviceProperty</i> requests, it can take two or more calls to <b>IoGetDeviceProperty</b> to determine the required <i>BufferLength</i>. The first call should use a best-guess value. If the return status is STATUS_BUFFER_TOO_SMALL, the driver should free its current buffer, allocate a buffer of the size returned in <i>ResultLength</i>, and call <b>IoGetDeviceProperty</b> again. Because some of the setup properties are dynamic, the data size can change between the time the required size is returned and driver calls this routine again. Therefore, drivers should call <b>IoGetDeviceProperty</b> inside a loop that runs until the return status is not STATUS_BUFFER_TOO_SMALL.

Function drivers that support devices on a legacy bus and a PnP bus can use the <b>DevicePropertyBusNumber</b>, <b>DevicePropertyBusTypeGuid</b>, and <b>DevicePropertyLegacyBusType</b> properties to distinguish between the buses.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** | PowerIrpDDis, HwStorPortProhibitedDDIs |

## See Also

<dl>
<dt>
<a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm-_cm_resource_list.md">CM_RESOURCE_LIST</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm-_device_removal_policy.md">DEVICE_REMOVAL_POLICY</a>
</dt>
<dt><a href="wdkgloss.g#wdkgloss.guid#wdkgloss.guid"><b>GUID</b></a></dt>
<dt>
<a href="..\wdm\ns-wdm-_io_resource_requirements_list.md">IO_RESOURCE_REQUIREMENTS_LIST</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm-_interface_type.md">INTERFACE_TYPE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoGetDeviceProperty routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>