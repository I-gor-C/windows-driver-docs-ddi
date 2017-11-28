# Pcivirt.h header


This header is used by unknown technology.

Pcivirt.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [READ_WRITE_MITIGATED_REGISTER callback](nc-pcivirt-read-write-mitigated-register.md) | Reads or writes to mitigated address spaces. |
| [SRIOV_GET_DEVICE_LOCATION callback](nc-pcivirt-sriov-get-device-location.md) | Retrieves information about the current location of the PCI device on the bus, such as PCI Segment, Bus, Device and Function number. |
| [SRIOV_GET_RESOURCE_FOR_BAR callback](nc-pcivirt-sriov-get-resource-for-bar.md) | Gets the translated resource for a specific Base Address Register (BAR). |
| [SRIOV_GET_VENDOR_AND_DEVICE_IDS callback](nc-pcivirt-sriov-get-vendor-and-device-ids.md) | Supplies the Vendor and Device ID for a PCI Express SR-IOV Virtual Function (VF) to be used for generating a more generic Plug and Play ID for the VF. These IDs cannot be read directly from the VF’s configuration space. |
| [SRIOV_QUERY_LUID callback](nc-pcivirt-sriov-query-luid.md) | Gets the local unique identifier of the SR-IOV device. |
| [SRIOV_QUERY_LUID_VF callback](nc-pcivirt-sriov-query-luid-vf.md) | Gets the PCI Express SR-IOV Virtual Function (VF) given a unique identifier. |
| [SRIOV_QUERY_PROBED_BARS callback](nc-pcivirt-sriov-query-probed-bars.md) | Queries the data read from the physical function's (PF) base address registers (BARs) if the value -1 were written to them first. |
| [SRIOV_QUERY_PROBED_BARS_2 callback](nc-pcivirt-sriov-query-probed-bars-2.md) | Queries the data read from the specified PCI Express SR-IOV Virtual Function (VF) base address registers (BARs) if the value -1 were written to them first. |
| [SRIOV_QUERY_VF_LUID callback](nc-pcivirt-sriov-query-vf-luid.md) | Gets the local unique identifier of the PCI Express SR-IOV Virtual Function (VF). |
| [SRIOV_READ_BLOCK callback](nc-pcivirt-sriov-read-block.md) | Reads data from the specified configuration block of a PCI Express SR-IOV Virtual Function (VF). |
| [SRIOV_READ_CONFIG callback](nc-pcivirt-sriov-read-config.md) | Reads data from the configuration space of the specified PCI Express SR-IOV Virtual Function (VF). |
| [SRIOV_RESET_FUNCTION callback](nc-pcivirt-sriov-reset-function.md) | Resets the specified PCI Express SR-IOV Virtual Function (VF). |
| [SRIOV_SET_POWER_STATE callback](nc-pcivirt-sriov-set-power-state.md) | Sets the power state of the specified PCI Express SR-IOV Virtual Function (VF). |
| [SRIOV_WRITE_BLOCK callback](nc-pcivirt-sriov-write-block.md) | Writes data to the specified configuration block of a PCI Express SR-IOV Virtual Function (VF). |
| [SRIOV_WRITE_CONFIG callback](nc-pcivirt-sriov-write-config.md) | Writes configuration data to a PCI Express SR-IOV Virtual Function (VF). |

## Structures

| Title   | Description   |
| ---- |:---- |
| [MITIGABLE_DEVICE_INTERFACE structure](ns-pcivirt--mitigable-device-interface.md) | Stores function pointers to callback functions implemented by the physical function (PF) driver for the mitigable device interface. |
| [SRIOV_DEVICE_INTERFACE_STANDARD structure](ns-pcivirt--sriov-device-interface-standard.md) | Stores function pointers to callback functions implemented by the physical function (PF) driver in the device stack for the of the SR-IOV device. |
| [SRIOV_DEVICE_INTERFACE_STANDARD_2 structure](ns-pcivirt--sriov-device-interface-standard-2.md) | Stores function pointers to callback functions implemented by the physical function (PF) driver in the device stack for the of the SR-IOV device. This is an extended version of SRIOV_DEVICE_INTERFACE_STANDARD. |
| [SRIOV_INVALIDATE_BLOCK structure](ns-pcivirt--sriov-invalidate-block.md) | Contains the configuration block information. This structure is used in a IOCTL_SRIOV_INVALIDATE_BLOCK request. |
| [SRIOV_MITIGATED_RANGES_INPUT structure](ns-pcivirt--sriov-mitigated-ranges-input.md) | This structure is the input buffer in the IOCTL_SRIOV_QUERY_MITIGATED_RANGES request to get the specific ranges on which intercepts must be placed. |
| [SRIOV_MITIGATED_RANGES_OUTPUT structure](ns-pcivirt--sriov-mitigated-ranges-output.md) | This structure is the output buffer received by the IOCTL_SRIOV_QUERY_MITIGATED_RANGES request to get the specific ranges on which intercepts must be placed. |
| [SRIOV_MITIGATED_RANGE_COUNT_INPUT structure](ns-pcivirt--sriov-mitigated-range-count-input.md) | This structure is used as an input buffer to the IOCTL_SRIOV_QUERY_MITIGATED_RANGE_COUNT request to determine the ranges of memory-mapped I/O space that must be mitigated. |
| [SRIOV_MITIGATED_RANGE_COUNT_OUTPUT structure](ns-pcivirt--sriov-mitigated-range-count-output.md) | This structures is the output buffer received by the IOCTL_SRIOV_QUERY_MITIGATED_RANGE_COUNT request that contains an array of ranges of memory-mapped I/O space that must be mitigated. |
| [SRIOV_MITIGATED_RANGE_UPDATE_INPUT structure](ns-pcivirt--sriov-mitigated-range-update-input.md) | This structure is used as an input buffer to the IOCTL_SRIOV_MITIGATED_RANGE_UPDATE request to indicate the virtual function (VF) whose memory-mapped I/O space that must be mitigated. |
| [SRIOV_MITIGATED_RANGE_UPDATE_OUTPUT structure](ns-pcivirt--sriov-mitigated-range-update-output.md) | This structures is the output buffer received by the IOCTL_SRIOV_MITIGATED_RANGE_UPDATE request that indicates the virtual function (VF) whose memory-mapped I/O space was mitigated. |
| [SRIOV_PNP_EVENT_COMPLETE structure](ns-pcivirt--sriov-pnp-event-complete.md) | Stores the status for an event that the SR-IOV Physical Function (PF) driver should set for Plug and Play even completion. This structure is used in the input buffer of the IOCTL_SRIOV_EVENT_COMPLETE request. |
| [SRIOV_PROXY_QUERY_LUID_OUTPUT structure](ns-pcivirt--sriov-proxy-query-luid-output.md) | Stores the local unique identifier of the SR_IOV device implementing the interface. This structure is the output buffer for the IOCTL_SRIOV_PROXY_QUERY_LUID request. |
| [VPCI_PNP_ID structure](ns-pcivirt--vpci-pnp-id.md) | Stores the PnP identifiers for a virtual PCI device. For example strings, see Identifiers for PCI Devices. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_SRIOV_ATTACH IOCTL](ni-pcivirt-ioctl-sriov-attach.md) | The request indicates that the virtualization stack wants to register for Plug and Play events received by the SR-IOV device. |
| [IOCTL_SRIOV_DETACH IOCTL](ni-pcivirt-ioctl-sriov-detach.md) | The request indicates that the virtualization stack wants to unregister for Plug and Play events (previously registered through the IOCTL_SRIOV_ATTACH request). |
| [IOCTL_SRIOV_EVENT_COMPLETE IOCTL](ni-pcivirt-ioctl-sriov-event-complete.md) | The request indicates that the virtualization stack or the SR-IOV device received one of the events listed in SRIOV_PF_EVENT. |
| [IOCTL_SRIOV_INVALIDATE_BLOCK IOCTL](ni-pcivirt-ioctl-sriov-invalidate-block.md) | The IOCTL_SRIOV_INVALIDATE_BLOCK request indicates that the virtualization stack wants to reset the contents of the specified configuration block. |
| [IOCTL_SRIOV_MITIGATED_RANGE_UPDATE IOCTL](ni-pcivirt-ioctl-sriov-mitigated-range-update.md) | The IOCTL_SRIOV_MITIGATED_RANGE_UPDATE request indicates that the virtualization stack wants to update to the mitigation ranges. |
| [IOCTL_SRIOV_NOTIFICATION IOCTL](ni-pcivirt-ioctl-sriov-notification.md) | The request indicates that the virtualization stack wants to be notified when one of the events listed in SRIOV_PF_EVENT occurs. |
| [IOCTL_SRIOV_PROXY_QUERY_LUID IOCTL](ni-pcivirt-ioctl-sriov-proxy-query-luid.md) | This request supplies the local unique identifier of the SR_IOV device implementing the interface. |
| [IOCTL_SRIOV_QUERY_MITIGATED_RANGES IOCTL](ni-pcivirt-ioctl-sriov-query-mitigated-ranges.md) | The request determines the specific ranges on which intercepts must be placed. |
| [IOCTL_SRIOV_QUERY_MITIGATED_RANGE_COUNT IOCTL](ni-pcivirt-ioctl-sriov-query-mitigated-range-count.md) | The request determines the ranges of memory-mapped I/O space that must mitigated. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [SRIOV_PF_EVENT enumeration](ne-pcivirt--sriov-pf-event.md) | Defines event values for the SR-IOV device. |
