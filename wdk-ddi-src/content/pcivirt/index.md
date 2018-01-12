---
UID: NA:pcivirt
---

# Pcivirt.h header

## -description

This header is used by PCI. For more information, see
- [PCI](../_PCI/index.md)

Pcivirt.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_MITIGABLE_DEVICE_INTERFACE structure](ns-pcivirt-_mitigable_device_interface.md) | Stores function pointers to callback functions implemented by the physical function (PF) driver for the mitigable device interface. |
| [_SRIOV_DEVICE_INTERFACE_STANDARD structure](ns-pcivirt-_sriov_device_interface_standard.md) | Stores function pointers to callback functions implemented by the physical function (PF) driver in the device stack for the of the SR-IOV device. |
| [_SRIOV_DEVICE_INTERFACE_STANDARD_2 structure](ns-pcivirt-_sriov_device_interface_standard_2.md) | Stores function pointers to callback functions implemented by the physical function (PF) driver in the device stack for the of the SR-IOV device. This is an extended version of SRIOV_DEVICE_INTERFACE_STANDARD. |
| [_SRIOV_INVALIDATE_BLOCK structure](ns-pcivirt-_sriov_invalidate_block.md) | Contains the configuration block information. This structure is used in a IOCTL_SRIOV_INVALIDATE_BLOCK request. |
| [_SRIOV_MITIGATED_RANGES_INPUT structure](ns-pcivirt-_sriov_mitigated_ranges_input.md) | This structure is the input buffer in the IOCTL_SRIOV_QUERY_MITIGATED_RANGES request to get the specific ranges on which intercepts must be placed. |
| [_SRIOV_MITIGATED_RANGES_OUTPUT structure](ns-pcivirt-_sriov_mitigated_ranges_output.md) | This structure is the output buffer received by the IOCTL_SRIOV_QUERY_MITIGATED_RANGES request to get the specific ranges on which intercepts must be placed. |
| [_SRIOV_MITIGATED_RANGE_COUNT_INPUT structure](ns-pcivirt-_sriov_mitigated_range_count_input.md) | This structure is used as an input buffer to the IOCTL_SRIOV_QUERY_MITIGATED_RANGE_COUNT request to determine the ranges of memory-mapped I/O space that must be mitigated. |
| [_SRIOV_MITIGATED_RANGE_COUNT_OUTPUT structure](ns-pcivirt-_sriov_mitigated_range_count_output.md) | This structures is the output buffer received by the IOCTL_SRIOV_QUERY_MITIGATED_RANGE_COUNT request that contains an array of ranges of memory-mapped I/O space that must be mitigated. |
| [_SRIOV_MITIGATED_RANGE_UPDATE_INPUT structure](ns-pcivirt-_sriov_mitigated_range_update_input.md) | This structure is used as an input buffer to the IOCTL_SRIOV_MITIGATED_RANGE_UPDATE request to indicate the virtual function (VF) whose memory-mapped I/O space that must be mitigated. |
| [_SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT structure](ns-pcivirt-_sriov_mitigated_range_update_output.md) | This structures is the output buffer received by the IOCTL_SRIOV_MITIGATED_RANGE_UPDATE request that indicates the virtual function (VF) whose memory-mapped I/O space was mitigated. |
| [_SRIOV_PNP_EVENT_COMPLETE structure](ns-pcivirt-_sriov_pnp_event_complete.md) | Stores the status for an event that the SR-IOV Physical Function (PF) driver should set for Plug and Play even completion. This structure is used in the input buffer of the IOCTL_SRIOV_EVENT_COMPLETE request. |
| [_SRIOV_PROXY_QUERY_LUID_OUTPUT structure](ns-pcivirt-_sriov_proxy_query_luid_output.md) | Stores the local unique identifier of the SR_IOV device implementing the interface. This structure is the output buffer for the IOCTL_SRIOV_PROXY_QUERY_LUID request. |
| [_VPCI_PNP_ID structure](ns-pcivirt-_vpci_pnp_id.md) | Stores the PnP identifiers for a virtual PCI device. For example strings, see Identifiers for PCI Devices. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_SRIOV_ATTACH IOCTL](ni-pcivirt-ioctl_sriov_attach.md) | The request indicates that the virtualization stack wants to register for Plug and Play events received by the SR-IOV device. |
| [IOCTL_SRIOV_DETACH IOCTL](ni-pcivirt-ioctl_sriov_detach.md) | The request indicates that the virtualization stack wants to unregister for Plug and Play events (previously registered through the IOCTL_SRIOV_ATTACH request). |
| [IOCTL_SRIOV_EVENT_COMPLETE IOCTL](ni-pcivirt-ioctl_sriov_event_complete.md) | The request indicates that the virtualization stack or the SR-IOV device received one of the events listed in SRIOV_PF_EVENT. |
| [IOCTL_SRIOV_INVALIDATE_BLOCK IOCTL](ni-pcivirt-ioctl_sriov_invalidate_block.md) | The IOCTL_SRIOV_INVALIDATE_BLOCK request indicates that the virtualization stack wants to reset the contents of the specified configuration block. |
| [IOCTL_SRIOV_MITIGATED_RANGE_UPDATE IOCTL](ni-pcivirt-ioctl_sriov_mitigated_range_update.md) | The IOCTL_SRIOV_MITIGATED_RANGE_UPDATE request indicates that the virtualization stack wants to update to the mitigation ranges. |
| [IOCTL_SRIOV_NOTIFICATION IOCTL](ni-pcivirt-ioctl_sriov_notification.md) | The request indicates that the virtualization stack wants to be notified when one of the events listed in SRIOV_PF_EVENT occurs. |
| [IOCTL_SRIOV_PROXY_QUERY_LUID IOCTL](ni-pcivirt-ioctl_sriov_proxy_query_luid.md) | This request supplies the local unique identifier of the SR_IOV device implementing the interface. |
| [IOCTL_SRIOV_QUERY_MITIGATED_RANGES IOCTL](ni-pcivirt-ioctl_sriov_query_mitigated_ranges.md) | The request determines the specific ranges on which intercepts must be placed. |
| [IOCTL_SRIOV_QUERY_MITIGATED_RANGE_COUNT IOCTL](ni-pcivirt-ioctl_sriov_query_mitigated_range_count.md) | The request determines the ranges of memory-mapped I/O space that must mitigated. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_SRIOV_PF_EVENT enumeration](ne-pcivirt-_sriov_pf_event.md) | Defines event values for the SR-IOV device. |
