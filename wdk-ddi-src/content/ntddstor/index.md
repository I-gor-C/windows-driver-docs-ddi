# Ntddstor.h header


This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Ntddstor.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [DEVICE_COPY_OFFLOAD_DESCRIPTOR structure](ns-ntddstor--device-copy-offload-descriptor.md) | Used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to describe the copy offload capabilities of a storage device. |
| [DEVICE_DATA_SET_LB_PROVISIONING_STATE structure](ns-ntddstor--device-data-set-lb-provisioning-state.md) | The DEVICE_DATA_SET_LB_PROVISIONING_STATE structure is returned by an IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES request when requesting logical block provisioning information for a data set range. |
| [DEVICE_DATA_SET_RANGE structure](ns-ntddstor--device-data-set-range.md) | The DEVICE_DATA_SET_RANGE structure specifies a block of data set ranges for the attributes for a device. |
| [DEVICE_DATA_SET_REPAIR_PARAMETERS structure](ns-ntddstor--device-data-set-repair-parameters.md) | The DEVICE_DATA_SET_REPAIR_PARAMETERS structure specifies the parameters of a storage spaces repair operation specified for a data set management action. |
| [DEVICE_DSM_NOTIFICATION_PARAMETERS structure](ns-ntddstor--device-dsm-notification-parameters.md) | The DEVICE_DSM_NOTIFICATION_PARAMETERS structure specifies the parameters for a notification action related to the data-set attributes for a device. |
| [DEVICE_DSM_OFFLOAD_READ_PARAMETERS structure](ns-ntddstor--device-dsm-offload-read-parameters.md) | The DEVICE_DSM_OFFLOAD_READ_PARAMETERS structure specifies the parameters for an offload read action related to the data-set attributes for a device. |
| [DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS structure](ns-ntddstor--device-dsm-offload-write-parameters.md) | The DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS structure specifies the parameters for an offload write action related to the data-set attributes for a device. |
| [DEVICE_LB_PROVISIONING_DESCRIPTOR structure](ns-ntddstor--device-lb-provisioning-descriptor.md) | The DEVICE_LB_PROVISIONING_DESCRIPTOR structure is one of the query result structures returned from an IOCTL_STORAGE_QUERY_PROPERTY request. This structure contains the thin provisioning capabilities for a storage device. |
| [DEVICE_MANAGE_DATA_SET_ATTRIBUTES structure](ns-ntddstor--device-manage-data-set-attributes.md) | The DEVICE_MANAGE_DATA_SET_ATTRIBUTES structure specifies a management action for the data-set attributes for a device. |
| [DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT structure](ns-ntddstor--device-manage-data-set-attributes-output.md) | The DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT structure describes output for IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES control code requests for some data set management actions. |
| [DEVICE_MEDIA_INFO structure](ns-ntddstor--device-media-info.md) | A storage class driver returns an array of DEVICE_MEDIA_INFO structures, embedded in a GET_MEDIA_TYPES structure, in response to an IOCTL_STORAGE_GET_MEDIA_TYPES_EX device-control request. |
| [DEVICE_POWER_DESCRIPTOR structure](ns-ntddstor--device-power-descriptor.md) | Used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY control code to describes the power capabilities of a storage device. |
| [DEVICE_SEEK_PENALTY_DESCRIPTOR structure](ns-ntddstor--device-seek-penalty-descriptor.md) | The DEVICE_SEEK_PENALTY_DESCRIPTOR structure is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the seek penalty descriptor data for a device. |
| [DEVICE_TRIM_DESCRIPTOR structure](ns-ntddstor--device-trim-descriptor.md) | The DEVICE_TRIM_DESCRIPTOR structure is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the trim descriptor data for a device. |
| [DEVICE_WRITE_AGGREGATION_DESCRIPTOR structure](ns-ntddstor--device-write-aggregation-descriptor.md) | Reserved for system use. |
| [GET_MEDIA_TYPES structure](ns-ntddstor--get-media-types.md) | The GET_MEDIA_TYPES structure is used in conjunction with the IOCTL_STORAGE_GET_MEDIA_TYPES_EX request to retrieve information about the types of media supported by a device. |
| [PERSISTENT_RESERVE_COMMAND structure](ns-ntddstor--persistent-reserve-command.md) | The PERSISTENT_RESERVE_COMMAND structure is used together with the IOCTL_STORAGE_PERSISTENT_RESERVE_IN and IOCTL_STORAGE_PERSISTENT_RESERVE_OUT requests to obtain and control information about persistent reservations and reservation keys that are active within a device server. |
| [STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR structure](ns-ntddstor--storage-access-alignment-descriptor.md) | The STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR structure is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the storage access alignment descriptor data for a device. |
| [STORAGE_ADAPTER_DESCRIPTOR structure](ns-ntddstor--storage-adapter-descriptor.md) | The STORAGE_ADAPTER_DESCRIPTOR structure is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the storage adapter descriptor data for a device. |
| [STORAGE_BREAK_RESERVATION_REQUEST structure](ns-ntddstor-storage-break-reservation-request.md) | The STORAGE_BREAK_RESERVATION_REQUEST structure is used in conjunction with the IOCTL_STORAGE_BREAK_RESERVATION request to free a disk resource that was previously reserved. |
| [STORAGE_BUS_RESET_REQUEST structure](ns-ntddstor--storage-bus-reset-request.md) | The STORAGE_BUS_RESET_REQUEST structure is used in conjunction with the IOCTL_STORAGE_RESET_BUS request to specify the path of the bus to be reset. |
| [STORAGE_CRYPTO_CAPABILITY structure](ns-ntddstor--storage-crypto-capability.md) | Reserved for system use. |
| [STORAGE_CRYPTO_DESCRIPTOR structure](ns-ntddstor--storage-crypto-descriptor.md) | Reserved for system use. |
| [STORAGE_DESCRIPTOR_HEADER structure](ns-ntddstor--storage-descriptor-header.md) | The STORAGE_DESCRIPTOR_HEADER structure is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the properties of a storage device or adapter. |
| [STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure](ns-ntddstor--storage-device-attributes-descriptor.md) | The STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure is used to retrieve the attributes information for a device. |
| [STORAGE_DEVICE_DESCRIPTOR structure](ns-ntddstor--storage-device-descriptor.md) | The STORAGE_DEVICE_DESCRIPTOR structure is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the storage device descriptor data for a device. |
| [STORAGE_DEVICE_ID_DESCRIPTOR structure](ns-ntddstor--storage-device-id-descriptor.md) | The STORAGE_DEVICE_ID_DESCRIPTOR structure is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the device ID descriptor data for a device. |
| [STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR structure](ns-ntddstor--storage-device-io-capability-descriptor.md) | The output buffer for the StorageDeviceIoCapabilityProperty as defined in STORAGE_PROPERTY_ID. |
| [STORAGE_DEVICE_NUMBER structure](ns-ntddstor--storage-device-number.md) | The STORAGE_DEVICE_NUMBER structure is used in conjunction with the IOCTL_STORAGE_GET_DEVICE_NUMBER request to retrieve the FILE_DEVICE_XXX device type, the device number, and, for a device that can be partitioned, the partition number assigned to a device by the driver when the device is started. |
| [STORAGE_DEVICE_POWER_CAP structure](ns-ntddstor--storage-device-power-cap.md) | This structure is used as an input and output buffer for the IOCTL_STORAGE_DEVICE_POWER_CAP. |
| [STORAGE_DEVICE_RESILIENCY_DESCRIPTOR structure](ns-ntddstor--storage-device-resiliency-descriptor.md) | Reserved for system use. |
| [STORAGE_DIAGNOSTIC_DATA structure](ns-ntddstor--storage-diagnostic-data.md) | Describes diagnostic data about the storage driver stack. The STORAGE_DIAGNOSTIC_DATA structure is provided in the output buffer of an IOCTL_STORAGE_DIAGNOSTIC request. |
| [STORAGE_DIAGNOSTIC_REQUEST structure](ns-ntddstor--storage-diagnostic-request.md) | Describes a diagnostic request about the storage driver stack. The STORAGE_DIAGNOSTIC_REQUEST structure is provided in the input buffer of an IOCTL_STORAGE_DIAGNOSTIC request. |
| [STORAGE_HOTPLUG_INFO structure](ns-ntddstor--storage-hotplug-info.md) | The STORAGE_HOTPLUG_INFO structure provides hotplug information for a device. |
| [STORAGE_HW_FIRMWARE_ACTIVATE structure](ns-ntddstor--storage-hw-firmware-activate.md) | This structure contains information about the downloaded firmware to activate. |
| [STORAGE_HW_FIRMWARE_DOWNLOAD structure](ns-ntddstor--storage-hw-firmware-download.md) | This structure contains a firmware image payload to be downloaded to the target. |
| [STORAGE_HW_FIRMWARE_INFO structure](ns-ntddstor--storage-hw-firmware-info.md) | This structure contains information about the device firmware. |
| [STORAGE_HW_FIRMWARE_INFO_QUERY structure](ns-ntddstor--storage-hw-firmware-info-query.md) | This structure contains information about the device firmware. |
| [STORAGE_HW_FIRMWARE_SLOT_INFO structure](ns-ntddstor--storage-hw-firmware-slot-info.md) | This structure contains information about a slot on a device. |
| [STORAGE_IDENTIFIER structure](ns-ntddstor--storage-identifier.md) | The STORAGE_IDENTIFIER structure represents a SCSI identification descriptor. |
| [STORAGE_LB_PROVISIONING_MAP_RESOURCES structure](ns-ntddstor--storage-lb-provisioning-map-resources.md) | The STORAGE_LB_PROVISIONING_MAP_RESOURCES structure contains, when valid, the count of available and used bytes mapped to a storage device. This structure is returned from an IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES request. |
| [STORAGE_MEDIUM_PRODUCT_TYPE_DESCRIPTOR structure](ns-ntddstor--storage-medium-product-type-descriptor.md) | Used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to describe the product type of a storage device. |
| [STORAGE_MINIPORT_DESCRIPTOR structure](ns-ntddstor--storage-miniport-descriptor.md) | Reserved for system use. |
| [STORAGE_OFFLOAD_READ_OUTPUT structure](ns-ntddstor--storage-offload-read-output.md) | The STORAGE_OFFLOAD_READ_OUTPUT structure is the output of an IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES control code request when the Action member of DEVICE_MANAGE_DATA_SET_ATTRIBUTES is set to DeviceDsmAction_OffloadRead. |
| [STORAGE_OFFLOAD_TOKEN structure](ns-ntddstor--storage-offload-token.md) | The STORAGE_OFFLOAD_TOKEN structure contains a token value that serves as a representation of a data set range within a file on a volume. This structure is used in performing offload reads and writes. |
| [STORAGE_OFFLOAD_WRITE_OUTPUT structure](ns-ntddstor--storage-offload-write-output.md) | The STORAGE_OFFLOAD_WRITE_OUTPUT structure is the output of an IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES control code request when the Action member of DEVICE_MANAGE_DATA_SET_ATTRIBUTES is set to DeviceDsmAction_OffloadWrite. |
| [STORAGE_PHYSICAL_ADAPTER_DATA structure](ns-ntddstor--storage-physical-adapter-data.md) | Specifies the physical device data of a storage adapter. |
| [STORAGE_PHYSICAL_DEVICE_DATA structure](ns-ntddstor--storage-physical-device-data.md) | Specifies the physical device data of a storage device. |
| [STORAGE_PHYSICAL_NODE_DATA structure](ns-ntddstor--storage-physical-node-data.md) | Specifies the physical device data of a storage node. |
| [STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR structure](ns-ntddstor--storage-physical-topology-descriptor.md) | Describes the physical topology of storage in a system. |
| [STORAGE_PREDICT_FAILURE structure](ns-ntddstor--storage-predict-failure.md) | The STORAGE_PREDICT_FAILURE structure is used in conjunction with IOCTL_STORAGE_PREDICT_FAILURE to report whether a device is currently predicting a failure. |
| [STORAGE_PROPERTY_QUERY structure](ns-ntddstor--storage-property-query.md) | This structure is used in conjunction with IOCTL_STORAGE_QUERY_PROPERTY to retrieve the properties of a storage device or adapter. |
| [STORAGE_PROTOCOL_COMMAND structure](ns-ntddstor--storage-protocol-command.md) | This structure is used as an input buffer when using the pass-through mechanism to issue a vendor-specific command to a storage device (via IOCTL_STORAGE_PROTOCOL_COMMAND). |
| [STORAGE_PROTOCOL_DATA_DESCRIPTOR structure](ns-ntddstor--storage-protocol-data-descriptor.md) | This structure is used in conjunction with IOCTL_STORAGE_QUERY_PROPERTY to return protocol-specific data from a storage device or adapter. |
| [STORAGE_PROTOCOL_SPECIFIC_DATA structure](ns-ntddstor--storage-protocol-specific-data.md) | Describes protocol-specific device data, provided in the input and output buffer of an IOCTL_STORAGE_QUERY_PROPERTY request. |
| [STORAGE_READ_CAPACITY structure](ns-ntddstor--storage-read-capacity.md) | The STORAGE_READ_CAPACITY contains the disk read capacity information returned from a IOCTL_STORAGE_READ_CAPACITIY request. |
| [STORAGE_SPEC_VERSION structure](ns-ntddstor--storage-spec-version.md) | Indicates the specification of the storage device. |
| [STORAGE_TEMPERATURE_DATA_DESCRIPTOR structure](ns-ntddstor--storage-temperature-data-descriptor.md) | This structure is used in conjunction with IOCTL_STORAGE_QUERY_PROPERTY to return temperature data from a storage device or adapter. |
| [STORAGE_TEMPERATURE_INFO structure](ns-ntddstor--storage-temperature-info.md) | Describes device temperature data. Returned as part of STORAGE_TEMPERATURE_DATA_DESCRIPTOR when querying for temperature data with an IOCTL_STORAGE_QUERY_PROPERTY request. |
| [STORAGE_TEMPERATURE_THRESHOLD structure](ns-ntddstor--storage-temperature-threshold.md) | This structure is used to set the over or under temperature threshold of a storage device (via IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD). |
| [STORAGE_WRITE_CACHE_PROPERTY structure](ns-ntddstor--storage-write-cache-property.md) | The STORAGE_WRITE_CACHE_PROPERTY structure is used with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve information about a device's write cache property. |
| [STORAGE_ZONE_DESCRIPTOR structure](ns-ntddstor--storage-zone-descriptor.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [STORAGE_ZONE_GROUP structure](ns-ntddstor--storage-zone-group.md) | Note  This structure is for internal use only and should not be called from your code. . |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [STORAGE_COMPONENT_HEALTH_STATUS enumeration](ne-ntddstor--storage-component-health-status.md) | Indicates the health status of a storage device. |
| [STORAGE_CRYPTO_ALGORITHM_ID enumeration](ne-ntddstor--storage-crypto-algorithm-id.md) | The STORAGE_CRYPTO_ALGORITHM_ID enum provides an output buffer for StorageAdapterCryptoProperty and PropertyStandardQuery. |
| [STORAGE_CRYPTO_KEY_SIZE enumeration](ne-ntddstor--storage-crypto-key-size.md) | The STORAGE_CRYPTO_KEY_SIZE enum returns the Size of the key in bits. |
| [STORAGE_DEVICE_FORM_FACTOR enumeration](ne-ntddstor--storage-device-form-factor.md) | Indicates the form factor of a storage device. |
| [STORAGE_DEVICE_POWER_CAP_UNITS enumeration](ne-ntddstor--storage-device-power-cap-units.md) | The units of the maximum power threshold. |
| [STORAGE_DIAGNOSTIC_LEVEL enumeration](ne-ntddstor--storage-diagnostic-level.md) | The STORAGE_DIAGNOSTIC_LEVEL enumeration specifies the target type of a storage diagnostic. |
| [STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration](ne-ntddstor--storage-diagnostic-target-type.md) | The STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration specifies the target type of a storage diagnostic. |
| [STORAGE_MEDIA_TYPE enumeration](ne-ntddstor--storage-media-type.md) | The STORAGE_MEDIA_TYPE enumeration is used in conjunction with the IOCTL_STORAGE_GET_MEDIA_TYPES_EX request to query the class driver for the types of media that a device supports. |
| [STORAGE_PROTOCOL_ATA_DATA_TYPE enumeration](ne-ntddstor--storage-protocol-ata-data-type.md) | The ATA protocol data type. |
| [STORAGE_PROTOCOL_NVME_DATA_TYPE enumeration](ne-ntddstor--storage-protocol-nvme-data-type.md) | Describes the type of NVMe protocol-specific data that's to be queried during an IOCTL_STORAGE_QUERY_PROPERTY request. |
| [STORAGE_PROTOCOL_TYPE enumeration](ne-ntddstor--storage-protocol-type.md) | This enumeration is used to define the different storage command protocols that are used between software and hardware. |
| [STORAGE_PROTOCOL_UFS_DATA_TYPE enumeration](ne-ntddstor--storage-protocol-ufs-data-type.md) | The UFS (Universal Flash Storage) data type. Describes the type of UFS specific data that's to be queried during an IOCTL_STORAGE_QUERY_PROPERTY request. |
| [STORAGE_QUERY_TYPE enumeration](ne-ntddstor--storage-query-type.md) | The STORAGE_QUERY_TYPE enumeration is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the properties of a storage device or adapter. |
| [STORAGE_ZONES_ATTRIBUTES enumeration](ne-ntddstor--storage-zones-attributes.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [STORAGE_ZONE_CONDITION enumeration](ne-ntddstor--storage-zone-condition.md) | Note  This structure is for internal use only and should not be called from your code. . |
