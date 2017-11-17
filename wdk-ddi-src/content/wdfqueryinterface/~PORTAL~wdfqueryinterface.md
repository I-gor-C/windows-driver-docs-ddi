# Declarations in the wdfqueryinterface header
This header Wdfqueryinterface contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFDEVICEADDQUERYINTERFACE callback function](nc-wdfqueryinterface-pfn-wdfdeviceaddqueryinterface.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfDeviceInterfaceReferenceNoOp function](nf-wdfqueryinterface-wdfdeviceinterfacereferencenoop.md) | The WdfDeviceInterfaceReferenceNoOp method can be used for driver-defined interfaces that do not require reference counts. |
| [WDF_QUERY_INTERFACE_CONFIG_INIT function](nf-wdfqueryinterface-wdf-query-interface-config-init.md) | The WDF_QUERY_INTERFACE_CONFIG_INIT function initializes a driver's WDF_QUERY_INTERFACE_CONFIG structure. |
| [WdfDeviceInterfaceDereferenceNoOp function](nf-wdfqueryinterface-wdfdeviceinterfacedereferencenoop.md) | The WdfDeviceInterfaceDereferenceNoOp method can be used for driver-defined interfaces that do not require reference counts. |
| [WdfDeviceAddQueryInterface function](nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md) | The WdfDeviceAddQueryInterface method creates a driver-defined interface that other drivers can query and use. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_QUERY_INTERFACE_CONFIG structure](ns-wdfqueryinterface--wdf-query-interface-config.md) | The WDF_QUERY_INTERFACE_CONFIG structure describes a driver-defined interface. |

This header is used in these topics:

- [wdf](..content/_wdf)
