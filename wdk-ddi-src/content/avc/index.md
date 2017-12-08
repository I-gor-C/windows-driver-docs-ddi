# Avc.h header


This header is used by Streaming media devices. For more information, see
- [Streaming media devices](../_stream/index.md)

Avc.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PFNAVCINTERSECTHANDLER callback](nc-avc-pfnavcintersecthandler.md) | The AV/C intersect handler determines if the data ranges are compatible. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [AVCCONNECTINFO structure](ns-avc--avcconnectinfo.md) | The AVCCONNECTINFO structure is used to initialize a subunit driver and establish pin connections. |
| [AVCPRECONNECTINFO structure](ns-avc--avcpreconnectinfo.md) | The AVCPRECONNECTINFO structure is used to initialize a subunit driver and establish pin connections. |
| [AVC_COMMAND_IRB structure](ns-avc--avc-command-irb.md) | The AVC_COMMAND_IRB structure defines a structure that contains an AV/C command and response pair. |
| [AVC_EXT_PLUG_COUNTS structure](ns-avc--avc-ext-plug-counts.md) | The AVC_EXT_PLUG_COUNTS structure describes the number of external plugs on the subunit. |
| [AVC_IRB structure](ns-avc--avc-irb.md) | The AVC_IRB structure is an I/O Request Block (IRB) header structure where a function number is stored. |
| [AVC_MULTIFUNC_IRB structure](ns-avc--avc-multifunc-irb.md) | The AVC_MULTIFUNC_IRB structure contains other AV/C related structures in a union. |
| [AVC_PEER_DO_LIST structure](ns-avc--avc-peer-do-list.md) | The AVC_PEER_DO_LIST describes all nonvirtual (peer) instances of avc.sys. |
| [AVC_PEER_DO_LOCATOR structure](ns-avc--avc-peer-do-locator.md) | The AVC_PEER_DO_LOCATOR describes nonvirtual (peer) instances of avc.sys. |
| [AVC_PIN_COUNT structure](ns-avc--avc-pin-count.md) | The AVC_PIN_COUNT structure specifies the number of pins on an AV/C subunit device. |
| [AVC_PIN_DESCRIPTOR structure](ns-avc--avc-pin-descriptor.md) | The AVC_PIN_DESCRIPTOR structure describes a pin on an AV/C subunit device. |
| [AVC_PIN_ID structure](ns-avc--avc-pin-id.md) | The AVC_PIN_ID structure describes a pin on a subunit. |
| [AVC_PRECONNECT_INFO structure](ns-avc--avc-preconnect-info.md) | The AVC_PRECONNECT_INFO structure specifies the preconnection information for the specified pin ID (zero-based offset) on an AV/C subunit device. |
| [AVC_SETCONNECT_INFO structure](ns-avc--avc-setconnect-info.md) | The AVC_SETCONNECT_INFO structure is used to initialize a subunit driver and establish pin connections. |
| [AVC_SUBUNIT_ADDR_SPEC structure](ns-avc--avc-subunit-addr-spec.md) | The AVC_SUBUNIT_ADDR_SPEC structure is used with virtual instances of avc.sys to describe virtual subunit addresses. |
| [AVC_SUBUNIT_INFO_BLOCK structure](ns-avc--avc-subunit-info-block.md) | The AVC_SUBUNIT_INFO_BLOCK structure describes subunit information. |
| [AVC_UNIQUE_ID structure](ns-avc--avc-unique-id.md) | The AVC_UNIQUE_ID describe the unique ID of the AV/C unit. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_AVC_BUS_RESET IOCTL](ni-avc-ioctl-avc-bus-reset.md) | The IOCTL_AVC_BUS_RESET I/O control code allows the caller to complete any previous IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO and IOCTL_AVC_REMOVE_VIRTUAL_SUBUNIT_INFO control requests that did not use the AVC_SUBUNIT_ADDR_TRIGGERBUSRESET flag. |
| [IOCTL_AVC_CLASS IOCTL](ni-avc-ioctl-avc-class.md) | The IOCTL_AVC_CLASS I/O control code is supported only from kernel mode, using the IRP_MJ_INTERNAL_DEVICE_CONTROL dispatch.Avc.sys supports two device interfaces, depending upon the type of instance (peer or virtual). |
| [IOCTL_AVC_REMOVE_VIRTUAL_SUBUNIT_INFO IOCTL](ni-avc-ioctl-avc-remove-virtual-subunit-info.md) | The IOCTL_AVC_REMOVE_VIRTUAL_SUBUNIT_INFO I/O control code controls the enumeration of virtual subunits. |
| [IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO IOCTL](ni-avc-ioctl-avc-update-virtual-subunit-info.md) | The IOCTL_AVC_UPDATE_VIRTUAL_SUBUNIT_INFO I/O control code controls the enumeration of virtual subunits. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [KSPIN_FLAG_AVC enumeration](ne-avc--kspin-flag-avc.md) | The KSPIN_FLAG_AVC enumeration type is used for connection management and in the AVC_FUNCTION_GET_CONNECTINFO function code. |
