---
UID : NA:wdfqueryinterface
ms.assetid : f1e1f714-ecee-3288-bb22-75c85c09b214
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# wdfqueryinterface.h header



wdfqueryinterface.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [WDF_QUERY_INTERFACE_CONFIG_INIT](nf-wdfqueryinterface-wdf_query_interface_config_init.md) | The WDF_QUERY_INTERFACE_CONFIG_INIT function initializes a driver's WDF_QUERY_INTERFACE_CONFIG structure. |
| [WdfDeviceAddQueryInterface](nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md) | The WdfDeviceAddQueryInterface method creates a driver-defined interface that other drivers can query and use. |
| [WdfDeviceInterfaceDereferenceNoOp](nf-wdfqueryinterface-wdfdeviceinterfacedereferencenoop.md) | The WdfDeviceInterfaceDereferenceNoOp method can be used for driver-defined interfaces that do not require reference counts. |
| [WdfDeviceInterfaceReferenceNoOp](nf-wdfqueryinterface-wdfdeviceinterfacereferencenoop.md) | The WdfDeviceInterfaceReferenceNoOp method can be used for driver-defined interfaces that do not require reference counts. |



## Structures
| Title | Description |
| ---- |:---- |
| [_WDF_QUERY_INTERFACE_CONFIG](ns-wdfqueryinterface-_wdf_query_interface_config.md) | The WDF_QUERY_INTERFACE_CONFIG structure describes a driver-defined interface. |