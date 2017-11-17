# Declarations in the storport header
This header Storport contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [TRACK_INFORMATION2 structure](ns-storport--track-information2.md) | TBD |
| [STOR_POFX_FSTATE_CONTEXT structure](ns-storport--stor-pofx-fstate-context.md) | TBD |
| [PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA structure](ns-storport--physical-element-status-parameter-data.md) | TBD |
| [STOR_POFX_PERF_STATE structure](ns-storport--stor-pofx-perf-state.md) | TBD |
| [MODE_PARAMETER_HEADER10 structure](ns-storport--mode-parameter-header10.md) | TBD |
| [SCSI_SUPPORTED_CONTROL_TYPE_LIST structure](ns-storport--scsi-supported-control-type-list.md) | TBD |
| [MODE_CONTROL_PAGE structure](ns-storport--mode-control-page.md) | TBD |
| [PRT_PARAMETER_DATA structure](ns-storport-prt-parameter-data.md) | The RT_PARAMETER_DATA structure contains the parameter data for the report timestamp command. |
| [SRBEX_DATA_SCSI_CDB32 structure](ns-storport--srbex-data-scsi-cdb32.md) | The SRBEX_DATA_SCSI_CDB32 structure contains the extended SRB data for a 32-byte SCSI command data block (CDB). |
| [STOR_POFX_PERF_STATE_CONTEXT structure](ns-storport--stor-pofx-perf-state-context.md) | TBD |
| [VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure](ns-storport--vpd-zoned-block-device-characteristics-page.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [STOR_SYSTEM_POWER_HINTS structure](ns-storport--stor-system-power-hints.md) | TBD |
| [NOTIFICATION_MEDIA_STATUS structure](ns-storport--notification-media-status.md) | TBD |
| [STOR_POFX_COMPONENT_PERF_SET structure](ns-storport--stor-pofx-component-perf-set.md) | TBD |
| [AUDIO_OUTPUT structure](ns-storport--audio-output.md) | TBD |
| [STOR_RICH_DEVICE_DESCRIPTION structure](ns-storport--stor-rich-device-description.md) | The STOR_RICH_DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA (direct memory access) adapter. |
| [SRBEX_DATA_SCSI_CDB_VAR structure](ns-storport--srbex-data-scsi-cdb-var.md) | The SRBEX_DATA_SCSI_CDB_VAR structure contains the extended SRB data for a variable length SCSI command data block (CDB). |
| [SCSI_EXTENDED_MESSAGE structure](ns-storport--scsi-extended-message.md) | TBD |
| [STOR_LOCK_HANDLE structure](ns-storport--stor-lock-handle.md) | TBD |
| [PPRI_RESERVATION_DESCRIPTOR structure](ns-storport-ppri-reservation-descriptor.md) | The PRI_RESERVATION_DESCRIPTOR structure is used to construct the PRI_RESERVATION_LIST structure that is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS. |
| [PERFORMANCE_DESCRIPTOR structure](ns-storport--performance-descriptor.md) | TBD |
| [SES_CONFIGURATION_DIAGNOSTIC_PAGE structure](ns-storport--ses-configuration-diagnostic-page.md) | TBD. |
| [VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure](ns-storport--vpd-block-device-characteristics-page.md) | TBD |
| [HW_INITIALIZATION_DATA structure](ns-storport--hw-initialization-data.md) | TBD |
| [STOR_DEVICE_CAPABILITIES structure](ns-storport--stor-device-capabilities.md) | The STOR_DEVICE_CAPABILITIES structure reports device capabilities to the Storport driver in response to a capabilities query in a SCSI request block (SRB) with a function of SRB_FUNCTION_PNP. |
| [TRACK_INFORMATION3 structure](ns-storport--track-information3.md) | TBD |
| [STOR_POWER_CONTROL_HEADER structure](ns-storport--stor-power-control-header.md) | TBD |
| [PORT_OUTPUT structure](ns-storport--port-output.md) | TBD |
| [SCSI_SENSE_DESCRIPTOR_INFORMATION structure](ns-storport--scsi-sense-descriptor-information.md) | TBD |
| [LBA_STATUS_DESCRIPTOR structure](ns-storport--lba-status-descriptor.md) | TBD |
| [SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN structure](ns-storport--scsi-sense-descriptor-ata-status-return.md) | TBD |
| [MODE_PARM_READ_WRITE structure](ns-storport--mode-parm-read-write.md) | TBD |
| [SENSE_DATA structure](ns-storport--sense-data~r1.md) | TBD |
| [SES_PHY_DESCRIPTOR structure](ns-storport--ses-phy-descriptor.md) | TBD |
| [SES_SAS_SLOT_INFORMATION structure](ns-storport--ses-sas-slot-information.md) | TBD |
| [CDB structure](ns-storport--cdb.md) | TBD |
| [FORMAT_DESCRIPTOR structure](ns-storport--format-descriptor.md) | TBD |
| [SRBEX_DATA_BIDIRECTIONAL structure](ns-storport--srbex-data-bidirectional.md) | The SRBEX_DATA_BIDIRECTIONAL structure contains the extended SRB data for bi-directional transfer commands. |
| [STOR_SLIST_HEADER structure](ns-storport--stor-slist-header.md) | TBD |
| [STOR_POFX_ACTIVE_CONTEXT structure](ns-storport--stor-pofx-active-context.md) | TBD |
| [VPD_BLOCK_LIMITS_PAGE structure](ns-storport--vpd-block-limits-page.md) | TBD |
| [PRECEIVE_TOKEN_INFORMATION_HEADER structure](ns-storport-preceive-token-information-header.md) | TBD |
| [MODE_CACHING_PAGE_EX structure](ns-storport--mode-caching-page-ex.md) | TBD |
| [STORAGE_REQUEST_BLOCK_HEADER structure](ns-storport--storage-request-block-header.md) | TBD |
| [MODE_FLEXIBLE_DISK_PAGE structure](ns-storport--mode-flexible-disk-page.md) | TBD |
| [SES_DIAGNOSTIC_PAGE structure](ns-storport--ses-diagnostic-page.md) | TBD |
| [SCSI_REQUEST_BLOCK structure](ns-storport--scsi-request-block.md) | TBD |
| [NOTIFICATION_BUSY_STATUS structure](ns-storport--notification-busy-status.md) | TBD |
| [STOR_UC_DEVICE_USAGE structure](ns-storport--stor-uc-device-usage.md) | TBD |
| [MODE_CACHING_PAGE structure](ns-storport--mode-caching-page.md) | TBD |
| [STORPORT_TELEMETRY_EVENT structure](ns-storport--storport-telemetry-event.md) | The STORPORT_TELEMETRY_EVENT structure describes the miniport telemetry data payload. |
| [STOR_REQUEST_INFO_V1 structure](ns-storport--stor-request-info-v1.md) | TBD |
| [STOR_SLIST_ENTRY structure](ns-storport--stor-slist-entry.md) | TBD |
| [VPD_MEDIA_SERIAL_NUMBER_PAGE structure](ns-storport--vpd-media-serial-number-page.md) | TBD |
| [MEMORY_REGION structure](ns-storport--memory-region.md) | The MEMORY_REGION structure describes a region of physically contiguous memory. |
| [STOR_CRYPTO_CAPABILITIES_DATA structure](ns-storport--stor-crypto-capabilities-data.md) | Reserved for system use. |
| [PPOPULATE_TOKEN_HEADER structure](ns-storport-ppopulate-token-header.md) | TBD |
| [CDVD_REPORT_AGID_DATA structure](ns-storport--cdvd-report-agid-data.md) | TBD |
| [VPD_IDENTIFICATION_DESCRIPTOR structure](ns-storport--vpd-identification-descriptor.md) | TBD |
| [UNMAP_LIST_HEADER structure](ns-storport--unmap-list-header.md) | TBD |
| [HW_INITIALIZATION_DATA structure](ns-storport--hw-initialization-data~r1.md) | TBD |
| [CDVD_CAPABILITIES_PAGE structure](ns-storport--cdvd-capabilities-page.md) | TBD |
| [SENSE_DATA structure](ns-storport--sense-data.md) | TBD |
| [SLOT_TABLE_INFORMATION structure](ns-storport--slot-table-information.md) | TBD |
| [VPD_IDENTIFICATION_PAGE structure](ns-storport--vpd-identification-page.md) | TBD |
| [FOUR_BYTE structure](ns-storport--four-byte.md) | TBD |
| [MODE_READ_RECOVERY_PAGE structure](ns-storport--mode-read-recovery-page.md) | TBD |
| [STOR_CRYPTO_OPERATION_INSERT_KEY structure](ns-storport--stor-crypto-operation-insert-key.md) | Reserved for system use. |
| [SCSI_WMI_REQUEST_BLOCK structure](ns-storport--scsi-wmi-request-block.md) | This structure is a special version of a SCSI_REQUEST_BLOCK for use with WMI commands. |
| [OVERWRITE_PARAMETER_LIST structure](ns-storport--overwrite-parameter-list.md) | TBD |
| [STOR_UNICODE_STRING structure](ns-storport--stor-unicode-string.md) | TBD |
| [STOR_DPC structure](ns-storport--stor-dpc.md) | The STOR_DPC structure is an opaque structure that represents a DPC object. Do not set the members of this structure directly. |
| [TRACK_INFORMATION structure](ns-storport--track-information.md) | TBD |
| [STOR_SERIAL_NUMBER structure](ns-storport--stor-serial-number.md) | TBD |
| [STOR_POFX_DEVICE_V3 structure](ns-storport--stor-pofx-device-v3.md) | The STOR_POFX_DEVICE_V3 structure describes the power attributes of a storage device to the power management framework (PoFx). |
| [SES_ADDITIONAL_ELEMENT_STATUS_DIAGNOSTIC_PAGE structure](ns-storport--ses-additional-element-status-diagnostic-page.md) | TBD |
| [VPD_SUPPORTED_PAGES_PAGE structure](ns-storport--vpd-supported-pages-page.md) | TBD |
| [MODE_PARAMETER_HEADER structure](ns-storport--mode-parameter-header.md) | TBD |
| [MODE_RIGID_GEOMETRY_PAGE structure](ns-storport--mode-rigid-geometry-page.md) | TBD |
| [TAPE_POSITION_DATA structure](ns-storport--tape-position-data.md) | TBD |
| [PHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR structure](ns-storport--physical-element-status-data-descriptor.md) | TBD |
| [MODE_READ_WRITE_RECOVERY_PAGE structure](ns-storport--mode-read-write-recovery-page.md) | TBD |
| [POWER_CONDITION_PAGE structure](ns-storport--power-condition-page.md) | TBD |
| [FORMATTED_CAPACITY_DESCRIPTOR structure](ns-storport--formatted-capacity-descriptor.md) | TBD |
| [HeaderX64 structure](ns-storport-headerx64.md) | TBD |
| [PERF_CONFIGURATION_DATA structure](ns-storport--perf-configuration-data.md) | The PERF_CONFIGURATION_DATA structure describes the performance optimizations that are supported by the StorPortInitializePerfOpts routine. |
| [STOR_POFX_DEVICE_V2 structure](ns-storport--stor-pofx-device-v2.md) | The STOR_POFX_DEVICE_V2 structure describes the power attributes of a storage device to the power management framework (PoFx). |
| [SUPPORTED_SECURITY_PROTOCOLS_PARAMETER_DATA structure](ns-storport--supported-security-protocols-parameter-data.md) | TBD |
| [UNMAP_BLOCK_DESCRIPTOR structure](ns-storport--unmap-block-descriptor.md) | TBD |
| [SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND structure](ns-storport--scsi-sense-descriptor-block-command.md) | TBD |
| [SES_CONTROL_DESCRIPTOR structure](ns-storport--ses-control-descriptor.md) | TBD |
| [LOG_PAGE structure](ns-storport--log-page.md) | TBD |
| [NOTIFICATION_OPERATIONAL_STATUS structure](ns-storport--notification-operational-status.md) | TBD |
| [STOR_ADAPTER_CONTROL_POWER structure](ns-storport--stor-adapter-control-power.md) | TBD |
| [SCSI_PNP_REQUEST_BLOCK structure](ns-storport--scsi-pnp-request-block.md) | TheSCSI_PNP_REQUEST_BLOCK structure is a special version of a SCSI_REQUEST_BLOCK that is used for plug and play (PNP) requests.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [STOR_POFX_COMPONENT structure](ns-storport--stor-pofx-component.md) | The STOR_POFX_COMPONENT structure describes the power state attributes of a storage device component. |
| [MINIPORT_DUMP_POINTERS structure](ns-storport--miniport-dump-pointers.md) | A Storport miniport driver uses this structure to support the SCSI_REQUEST_BLOCK (SRB) function code SRB_FUNCTION_DUMP_POINTERS. |
| [READ_CAPACITY16_DATA structure](ns-storport--read-capacity16-data.md) | TBD |
| [SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure](ns-storport--ses-download-microcode-control-diagnostic-page.md) | The SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process. |
| [CDVD_FEATURE_SET_PAGE structure](ns-storport--cdvd-feature-set-page.md) | TBD |
| [STOR_RPMB_CAPABILITIES_DATA structure](ns-storport--stor-rpmb-capabilities-data.md) | TBD |
| [SES_ENCLOSURE_DESCRIPTOR structure](ns-storport--ses-enclosure-descriptor.md) | TBD |
| [Header16 structure](ns-storport-header16.md) | TBD |
| [SES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR structure](ns-storport--ses-additional-element-status-descriptor.md) | TBD |
| [LUN_LIST structure](ns-storport--lun-list.md) | TBD |
| [MODE_MRW_PAGE structure](ns-storport--mode-mrw-page.md) | TBD |
| [STORAGE_REQUEST_BLOCK structure](ns-storport--storage-request-block.md) | The STORAGE_REQUEST_BLOCK is the extended format SCSI Request Block (SRB) structure. |
| [PWRITE_USING_TOKEN_HEADER structure](ns-storport-pwrite-using-token-header.md) | TBD |
| [OPC_TABLE_ENTRY structure](ns-storport--opc-table-entry.md) | TBD |
| [STOR_SCATTER_GATHER_LIST structure](ns-storport--stor-scatter-gather-list.md) | The STOR_SCATTER_GATHER_LIST structure is used in conjunction with the StorPortGetScatterGatherList routine to retrieve the scatter/gather list for a SCSI request block (SRB). |
| [STOR_ADDR_BTL8 structure](ns-storport--stor-addr-btl8.md) | The STOR_ADDR_BTL8 address structure contains the addressing information for an 8-bit Bus-Target-LUN (BTL8) address. |
| [STOR_POFX_COMPONENT_IDLE_STATE structure](ns-storport--stor-pofx-component-idle-state.md) | The STOR_POFX_COMPONENT_IDLE_STATE structure specifies the attributes of an functional power state (F-state) of a component in a storage device. |
| [NOTIFICATION_POWER_STATUS structure](ns-storport--notification-power-status.md) | TBD |
| [READ_DVD_STRUCTURES_HEADER structure](ns-storport--read-dvd-structures-header.md) | TBD |
| [STOR_POFX_DEVICE structure](ns-storport--stor-pofx-device.md) | The STOR_POFX_DEVICE structure describes the power attributes of a storage device to the power management framework (PoFx). |
| [INQUIRYDATA structure](ns-storport--inquirydata~r1.md) | TBD |
| [PRECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER structure](ns-storport-preceive-token-information-response-header.md) | TBD |
| [STOR_POFX_COMPONENT_V2 structure](ns-storport--stor-pofx-component-v2.md) | The STOR_POFX_COMPONENT_V2 structure describes the power state attributes of a storage device component. |
| [TWO_BYTE structure](ns-storport--two-byte.md) | TBD |
| [SCSI_POWER_REQUEST_BLOCK structure](ns-storport--scsi-power-request-block.md) | The SCSI_POWER_REQUEST_BLOCK structure is a special version of a SCSI_REQUEST_BLOCK that is used for power management requests.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [SRBEX_DATA_SCSI_CDB16 structure](ns-storport--srbex-data-scsi-cdb16.md) | The SRBEX_DATA_SCSI_CDB16 structure contains the extended SRB data for a 16-byte SCSI command data block (CDB). |
| [READ_CAPACITY_DATA structure](ns-storport--read-capacity-data.md) | TBD |
| [STOR_SCATTER_GATHER_ELEMENT structure](ns-storport--stor-scatter-gather-element.md) | The STOR_SCATTER_GATHER_ELEMENT structure is used with STOR_SCATTER_GATHER_LIST to build a list of scatter/gather elements. |
| [CDVD_KEY_DATA structure](ns-storport--cdvd-key-data.md) | TBD |
| [SES_PROTOCOL_INFORMATION structure](ns-storport--ses-protocol-information.md) | TBD |
| [NOTIFICATION_EVENT_STATUS_HEADER structure](ns-storport--notification-event-status-header.md) | TBD |
| [PORT_CONFIGURATION_INFORMATION structure](ns-storport--port-configuration-information.md) | The PORT_CONFIGURATION_INFORMATION contains configuration information for a host bus adapter (HBA). |
| [SCSI_SENSE_DESCRIPTOR_HEADER structure](ns-storport--scsi-sense-descriptor-header.md) | TBD |
| [LBA_STATUS_LIST_HEADER structure](ns-storport--lba-status-list-header.md) | TBD |
| [SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE structure](ns-storport--ses-download-microcode-status-diagnostic-page.md) | The Download Microcode Status diagnostic page includes information about the status of one or more download microcode operations. |
| [SES_TYPE_DESCRIPTOR_HEADER structure](ns-storport--ses-type-descriptor-header.md) | TBD |
| [MODE_INFO_EXCEPTIONS structure](ns-storport--mode-info-exceptions.md) | TBD |
| [DISC_INFORMATION structure](ns-storport--disc-information.md) | TBD |
| [STOR_POFX_POWER_REQUIRED_CONTEXT structure](ns-storport--stor-pofx-power-required-context.md) | TBD |
| [MODE_FORMAT_PAGE structure](ns-storport--mode-format-page.md) | TBD |
| [LOG_PARAMETER structure](ns-storport--log-parameter.md) | TBD |
| [STARTIO_PERFORMANCE_PARAMETERS structure](ns-storport--startio-performance-parameters.md) | The STARTIO_PERFORMANCE_PARAMETERS structure describes the performance parameters that are returned to the miniport driver by the StorPortGetStartIoPerfParams routine. |
| [STOR_DEVICE_CAPABILITIES_EX structure](ns-storport--stor-device-capabilities-ex.md) | The STOR_DEVICE_CAPABILITIES_EX structure reports device capabilities to the Storport driver in response to a capabilities query in a SCSI request block (SRB) with a function of SRB_FUNCTION_PNP. |
| [DESCRIPTOR_SENSE_DATA structure](ns-storport--descriptor-sense-data.md) | TBD |
| [DATA_BLOCK_HEADER structure](ns-storport--data-block-header.md) | TBD |
| [LOG_PARAMETER_HEADER structure](ns-storport--log-parameter-header.md) | TBD |
| [SRBEX_DATA_PNP structure](ns-storport--srbex-data-pnp.md) | The SRBEX_DATA_PNP structure contains the request data for an extended plug and play (PNP) SRB. |
| [CDAUDIO_CONTROL_PAGE structure](ns-storport--cdaudio-control-page.md) | TBD |
| [STOR_CRYPTO_CAPABILITY structure](ns-storport--stor-crypto-capability.md) | Reserved for system use. |
| [FORMATTED_CAPACITY_LIST structure](ns-storport--formatted-capacity-list.md) | TBD |
| [NOTIFICATION_MULTI_HOST_STATUS structure](ns-storport--notification-multi-host-status.md) | TBD |
| [SES_STATUS_DIAGNOSTIC_PAGE structure](ns-storport--ses-status-diagnostic-page.md) | TBD |
| [VIRTUAL_HW_INITIALIZATION_DATA structure](ns-storport--virtual-hw-initialization-data.md) | The VIRTUAL_HW_INITIALIZATION_DATA structure contains information particular to each virtual miniport driver. |
| [CDB32 structure](ns-storport--cdb32.md) | TBD |
| [MINIPORT_MAPPINGS structure](ns-storport--miniport-mappings.md) | TBD |
| [STOR_REQUEST_INFO_V2 structure](ns-storport--stor-request-info-v2.md) | TBD |
| [READ_BLOCK_LIMITS structure](ns-storport--read-block-limits.md) | TBD |
| [Header8 structure](ns-storport-header8.md) | TBD |
| [SES_CONTROL_DIAGNOSTIC_PAGE structure](ns-storport--ses-control-diagnostic-page.md) | TBD |
| [SRBEX_DATA structure](ns-storport--srbex-data.md) | The SRBEX_DATA structure is the generalized format for containing extended SRB data. |
| [STOR_MAX_OPERATIONAL_POWER structure](ns-storport--stor-max-operational-power.md) | TBD |
| [CDVD_REPORT_ASF_DATA structure](ns-storport--cdvd-report-asf-data.md) | TBD |
| [DISK_INFORMATION structure](ns-storport--disk-information.md) | TBD |
| [MODE_DISCONNECT_PAGE structure](ns-storport--mode-disconnect-page.md) | TBD |
| [STOR_CRYPTO_KEY_INFO structure](ns-storport--stor-crypto-key-info.md) | Reserved for system use. |
| [CDDA_OUTPUT_PORT structure](ns-storport--cdda-output-port.md) | TBD |
| [MESSAGE_INTERRUPT_INFORMATION structure](ns-storport--message-interrupt-information.md) | The MESSAGE_INTERRUPT_INFORMATION structure describes a message signaled interrupt (MSI). |
| [STOR_POFX_POWER_CONTROL structure](ns-storport--stor-pofx-power-control.md) | TBD |
| [STOR_POFX_UNIT_POWER_INFO structure](ns-storport--stor-pofx-unit-power-info.md) | TBD |
| [PPRO_PARAMETER_LIST structure](ns-storport-ppro-parameter-list.md) | The PRO_PARAMETER_LIST structure is sent in a Persistent Reserve Out command to a device server. |
| [STOR_FILTER_RESOURCE_REQUIREMENTS structure](ns-storport--stor-filter-resource-requirements.md) | TBD |
| [CDVD_KEY_HEADER structure](ns-storport--cdvd-key-header.md) | TBD |
| [VPD_THIRD_PARTY_COPY_PAGE structure](ns-storport--vpd-third-party-copy-page.md) | TBD |
| [INQUIRYDATA structure](ns-storport--inquirydata.md) | TBD |
| [NOTIFICATION_EXTERNAL_STATUS structure](ns-storport--notification-external-status.md) | TBD |
| [STOR_UNIT_ATTRIBUTES structure](ns-storport--stor-unit-attributes.md) | The STOR_UNIT_ATTRIBUTES structure contains bitfields indicating attribute support for a storage device unit. |
| [LOG_PAGE_LOGICAL_BLOCK_PROVISIONING structure](ns-storport--log-page-logical-block-provisioning.md) | TBD |
| [FORMAT_LIST_HEADER structure](ns-storport--format-list-header.md) | TBD |
| [ACCESS_RANGE structure](ns-storport--access-range.md) | TBD |
| [CDVD_INACTIVITY_TIMEOUT_PAGE structure](ns-storport--cdvd-inactivity-timeout-page.md) | TBD |
| [SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure](ns-storport--ses-download-microcode-status-descriptor.md) | The SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure specifies the status and additional status of a download microcode. |
| [STOR_POWER_SETTING_INFO structure](ns-storport--stor-power-setting-info.md) | TBD |
| [STOR_UNIT_CONTROL_POWER structure](ns-storport--stor-unit-control-power.md) | TBD |
| [SRBEX_DATA_POWER structure](ns-storport--srbex-data-power.md) | The SRBEX_DATA_POWER structure contains the request data for an extended power SRB. |
| [MODE_CDROM_WRITE_PARAMETERS_PAGE structure](ns-storport--mode-cdrom-write-parameters-page.md) | TBD |
| [PBLOCK_DEVICE_TOKEN_DESCRIPTOR structure](ns-storport-pblock-device-token-descriptor.md) | TBD |
| [PPRI_REGISTRATION_LIST structure](ns-storport-ppri-registration-list.md) | The PRI_REGISTRATION_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_KEYS. |
| [CDVD_TITLE_KEY_HEADER structure](ns-storport--cdvd-title-key-header.md) | TBD |
| [ZONE_DESCRIPTIOR structure](ns-storport--zone-descriptior.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [STOR_RICH_DEVICE_DESCRIPTION_V2 structure](ns-storport--stor-rich-device-description-v2.md) | TBD |
| [PBLOCK_DEVICE_RANGE_DESCRIPTOR structure](ns-storport-pblock-device-range-descriptor.md) | TBD |
| [SENSE_DATA_EX structure](ns-storport--sense-data-ex.md) | TBD |
| [VPD_LOGICAL_BLOCK_PROVISIONING_PAGE structure](ns-storport--vpd-logical-block-provisioning-page.md) | TBD |
| [SES_STATUS_DESCRIPTOR structure](ns-storport--ses-status-descriptor.md) | TBD |
| [STOR_LOG_EVENT_DETAILS structure](ns-storport--stor-log-event-details.md) | The STOR_LOG_EVENT_DETAILS structure provides details pertaining to Storport-specific error log events and system log events. |
| [REPORT_ZONES_DATA structure](ns-storport--report-zones-data.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [SRBEX_DATA_WMI structure](ns-storport--srbex-data-wmi.md) | The SRBEX_DATA_WMI structure contains the request data for an extended WMI SRB. |
| [READ_BUFFER_CAPACITY_DATA structure](ns-storport--read-buffer-capacity-data.md) | TBD |
| [VPD_ATA_INFORMATION_PAGE structure](ns-storport--vpd-ata-information-page.md) | TBD |
| [PPRI_RESERVATION_LIST structure](ns-storport-ppri-reservation-list.md) | The PRI_RESERVATION_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS. |
| [VPD_SERIAL_NUMBER_PAGE structure](ns-storport--vpd-serial-number-page.md) | TBD |
| [STORPORT_EXTENDED_FUNCTIONS structure](ns-storport--storport-extended-functions.md) | TBD |
| [READ_CAPACITY_DATA_EX structure](ns-storport--read-capacity-data-ex.md) | TBD |
| [LOG_PARAMETER_THRESHOLD_RESOURCE_COUNT structure](ns-storport--log-parameter-threshold-resource-count.md) | TBD |
| [MODE_CDROM_WRITE_PARAMETERS_PAGE2 structure](ns-storport--mode-cdrom-write-parameters-page2.md) | TBD |
| [STOR_ADDRESS structure](ns-storport--stor-address.md) | A general structure for holding a storage device address. |
| [PST_PARAMETER_DATA structure](ns-storport-pst-parameter-data.md) | The ST_PARAMETER_DATA structure contains the parameter list for the set timestamp command. |
| [STOR_LIST_ENTRY structure](ns-storport--stor-list-entry.md) | A STOR_LIST_ENTRY structure describes an entry in a doubly linked list or serves as the header for such a list. |
| [MECHANICAL_STATUS_INFORMATION_HEADER structure](ns-storport--mechanical-status-information-header.md) | TBD |
| [SRBEX_DATA_IO_INFO structure](ns-storport--srbex-data-io-info.md) | The SRBEX_DATA_IO_INFO structure contains additional information related to a read or write request in an extended SRB. |
| [WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR structure](ns-storport--windows-block-device-token-limits-descriptor.md) | TBD |
| [EIGHT_BYTE structure](ns-storport--eight-byte.md) | TBD |
| [CDVD_CHALLENGE_KEY_DATA structure](ns-storport--cdvd-challenge-key-data.md) | TBD |
| [STARTIO_PERFORMANCE_PARAMETERS_V2 structure](ns-storport--startio-performance-parameters-v2.md) | TBD |
| [DPC_BUFFER structure](ns-storport--dpc-buffer.md) | TBD |
| [MODE_PARAMETER_BLOCK structure](ns-storport--mode-parameter-block.md) | TBD |
| [MECHANICAL_STATUS structure](ns-storport--mechanical-status.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [StorPortReadRegisterBufferUlong64 function](nf-storport-storportreadregisterbufferulong64.md) | This StorPortReadRegisterBufferUlong64 routine reads a number of ULONG64 values from the specified 64-bit register address into a buffer. |
| [StorPortReadPortUchar function](nf-storport-storportreadportuchar.md) | The StorPortReadPortUchar routine reads a value from a specified port address |
| [StorPortSetUnitAttributes function](nf-storport-storportsetunitattributes.md) | The StorPortSetUnitAttributes routine registers the power attributes of a storage unit device with the Storport driver. |
| [StorPortFreeTimer function](nf-storport-storportfreetimer.md) | Frees a Storport timer context object previously created by the StorPortInitializeTimer routine. |
| [StorPortReadRegisterUshort function](nf-storport-storportreadregisterushort~r1.md) | The StorPortReadRegisterUshort routine reads a value from a specified register address. |
| [IsSenseDataCurrentError function](nf-storport-issensedatacurrenterror.md) | TBD |
| [StorPortInitializeSpinlock function](nf-storport-storportinitializespinlock.md) | The StorPortInitializeSpinLock routine initializes a variable of type STOR_KSPIN_LOCK. |
| [StorPortWriteRegisterUshort function](nf-storport-storportwriteregisterushort~r1.md) | The StorPortWriteRegisterUshort routine transfers a ULONG value to the indicated HBA register address. |
| [StorPortStallExecution function](nf-storport-storportstallexecution.md) | The StorPortStallExecution routine stalls the miniport driver. |
| [StorPortFreeDeviceBase function](nf-storport-storportfreedevicebase.md) | StorPortFreeDeviceBase frees a range of device I/O memory that was mapped by StorPortGetDeviceBase. |
| [ScsiPortReadPortBufferUlong function](nf-storport-scsiportreadportbufferulong.md) | TBD |
| [ScsiPortWriteRegisterBufferUlong function](nf-storport-scsiportwriteregisterbufferulong.md) | TBD |
| [StorPortSetPowerSettingNotificationGuids function](nf-storport-storportsetpowersettingnotificationguids.md) | The StorPortSetPowerSettingNotificationGuids routine enables a miniport to receive power setting notifications. The miniport registers an array of GUIDs which identify the power settings to receive power change notifications for. |
| [StorPortInterlockedFlushSList function](nf-storport-storportinterlockedflushslist.md) | Removes all items from a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system. |
| [StorPortGetPhysicalAddress function](nf-storport-storportgetphysicaladdress.md) | The StorPortGetPhysicalAddress routine converts a given virtual address range to a physical address range for a DMA operation. |
| [StorPortDeviceReady function](nf-storport-storportdeviceready.md) | The StorPortDeviceReady routine notifies the port driver that the indicated logical unit is ready to handle new requests. |
| [StorPortEtwEvent8 function](nf-storport-storportetwevent8.md) | The StorPortEtwEvent8 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log eight general purpose ETW parameters. The ETW parameters are expressed as eight name-value pairs. |
| [StorPortAllocatePool function](nf-storport-storportallocatepool.md) | The StorPortAllocatePool routine allocates a block of non-contiguous, non-paged pool memory. |
| [StorPortQuerySystemTime function](nf-storport-storportquerysystemtime.md) | The StoriPortQuerySystemTime routine obtains the current system time. |
| [StorPortWriteRegisterBufferUlong64 function](nf-storport-storportwriteregisterbufferulong64.md) | This StorPortWriteRegisterBufferUlong64 routine writes a number of ULONG64 values from a the specified 64-bit register address. |
| [StorPortPropagateIrpExtension function](nf-storport-storportpropagateirpextension.md) | TBD |
| [StorPortGetLogicalProcessorRelationship function](nf-storport-storportgetlogicalprocessorrelationship.md) | The StorPortGetLogicalProcessorRelationship routine returns relationship information for one or more specified types. |
| [ScsiPortReadPortUlong function](nf-storport-scsiportreadportulong.md) | TBD |
| [StorPortRequestTimer function](nf-storport-storportrequesttimer.md) | Schedules a callback event for a Storport timer context object. |
| [StorPortGetMSIInfo function](nf-storport-storportgetmsiinfo.md) | The StorPortGetMSIInfo routine retrieves the message signaled interrupt (MSI) information for the specified message. |
| [StorPortBuildScatterGatherList function](nf-storport-storportbuildscattergatherlist.md) | The StorPortBuildScatterGatherList routine creates a scatter/gather list for the specified data buffer. |
| [StorPortWritePortUlong function](nf-storport-storportwriteportulong~r1.md) | The StorPortWritePortUlong routine writes a value to a specified register address. |
| [StorPortRegistryRead function](nf-storport-storportregistryread.md) | The StorPortRegistryRead routine reads the registry data for the indicated device and value. |
| [StorPortFreeContiguousMemorySpecifyCache function](nf-storport-storportfreecontiguousmemoryspecifycache.md) | The StorPortFreeContiguousMemorySpecifyCache routine deallocates a range of noncached memory in the nonpaged portion of the system address space. |
| [StorPortWriteRegisterBufferUshort function](nf-storport-storportwriteregisterbufferushort.md) | The StorPortWriteRegisterBufferUshort routine transfers a given number of USHORT values from a buffer to the HBA. |
| [ScsiValidateBlockCommandSenseDescriptor function](nf-storport-scsivalidateblockcommandsensedescriptor.md) | TBD |
| [StorPortInitializeRpmb function](nf-storport-storportinitializerpmb.md) | TBD |
| [StorPortReadPortBufferUshort function](nf-storport-storportreadportbufferushort~r1.md) | The StorPortReadPortBufferUshort routine reads a value from a specified port address. |
| [StorPortPause function](nf-storport-storportpause.md) | The StorPortPause routine pauses an adapter for the specified period of time. |
| [StorPortReadPortBufferUchar function](nf-storport-storportreadportbufferuchar.md) | The StorPortReadPortBufferUchar routine reads a value from a specified port address |
| [StorPortWritePortBufferUshort function](nf-storport-storportwriteportbufferushort~r1.md) | The StorPortWritePortBufferUshort routine writes a value to a specified register address. |
| [StorPortReadRegisterBufferUlong function](nf-storport-storportreadregisterbufferulong~r1.md) | The StorPortReadRegisterBufferUlong routine reads a value from a specified register address. |
| [StorPortGetGroupAffinity function](nf-storport-storportgetgroupaffinity.md) | The StorPortGetGroupAffinity routine constructs a mask of the active processors in a requested group. |
| [StorPortRegistryWrite function](nf-storport-storportregistrywrite.md) | The StorPortRegistryWrite routine is called by the miniport driver to convert the registry data contained in a specified buffer from ASCII to Unicode and to then write the data to the miniport driver's per-HBA storage area. |
| [StorPortGetSystemPortNumber function](nf-storport-storportgetsystemportnumber.md) | The StorPortGetSystemPortNumber routine retrieves the system assigned port number for a storage adapter. |
| [ScsiPortReadRegisterUchar function](nf-storport-scsiportreadregisteruchar.md) | TBD |
| [StorPortGetMessageInterruptInformation function](nf-storport-storportgetmessageinterruptinformation.md) | TBD |
| [StorPortDebugPrint function](nf-storport-storportdebugprint.md) | The StorPortDebugPrint routine prints a debug string to the kernel debugger, if the debugger is attached. |
| [ScsiPortWritePortBufferUlong function](nf-storport-scsiportwriteportbufferulong.md) | TBD |
| [ScsiPortReadPortUchar function](nf-storport-scsiportreadportuchar.md) | TBD |
| [StorPortWriteRegisterUlong function](nf-storport-storportwriteregisterulong~r1.md) | The StorPortWriteRegisterUlong routine transfers a ULONG value to the indicated HBA register address. |
| [StorPortStateChangeDetected function](nf-storport-storportstatechangedetected.md) | Notifies the Storport port driver of a state change for a logical unit number (LUN), host bus adapter (HBA) port, or target device. |
| [REVERSE_BYTES_8 function](nf-storport-reverse-bytes-8.md) | TBD |
| [StorPortPoFxSetPerfState function](nf-storport-storportpofxsetperfstate.md) | TBD |
| [StorPortReadRegisterBufferUshort function](nf-storport-storportreadregisterbufferushort.md) | The StorPortReadRegisterBufferUshort routine reads a value from a specified register address. |
| [StorPortResumeDevice function](nf-storport-storportresumedevice.md) | The StorPortResumeDevice routine resumes a previously paused logical unit. |
| [StorPortGetScatterGatherList function](nf-storport-storportgetscattergatherlist.md) | The StorPortGetScatterGatherList routine retrieves the associated scatter/gather list for the specified SCSI request block (SRB). |
| [ScsiPortWriteRegisterBufferUshort function](nf-storport-scsiportwriteregisterbufferushort.md) | TBD |
| [ScsiPortWriteRegisterUlong function](nf-storport-scsiportwriteregisterulong.md) | TBD |
| [StorPortReadPortUlong function](nf-storport-storportreadportulong.md) | The StorPortReadPortUlong routine reads a value from a specified port address. |
| [ScsiPortWritePortBufferUchar function](nf-storport-scsiportwriteportbufferuchar.md) | TBD |
| [ScsiPortWritePortUshort function](nf-storport-scsiportwriteportushort.md) | TBD |
| [ScsiPortWritePortUchar function](nf-storport-scsiportwriteportuchar.md) | TBD |
| [StorPortBuildMdlForNonPagedPool function](nf-storport-storportbuildmdlfornonpagedpool.md) | The StorPortBuildMdlForNonPagedPool routine updates the MDL to describe the associated non-paged memory. |
| [StorPortReleaseMSISpinLock function](nf-storport-storportreleasemsispinlock.md) | The StorPortReleaseMSISpinLock routine releases a previously acquired message signaled interrupt (MSI) spin lock for the specified message. |
| [StorPortInitializeDpc function](nf-storport-storportinitializedpc.md) | The StorPortInitializeDpc routine initializes a StorPort DPC. |
| [StorPortLogTelemetry function](nf-storport-storportlogtelemetry.md) | The StorPortLogTelemetry routine logs a miniport telemetry event to help diagnose or collect any useful information. |
| [StorPortPoFxSetComponentLatency function](nf-storport-storportpofxsetcomponentlatency.md) | The StorPortPoFxSetComponentLatency routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified storage device component. |
| [StorPortCompleteRequest function](nf-storport-storportcompleterequest.md) | The StorPortCompleteRequest routine completes all outstanding requests setting the SRB status value to SrbStatus. |
| [StorPortReadPortBufferUlong function](nf-storport-storportreadportbufferulong~r1.md) | The StorPortReadPortBufferUlong routine reads a value from a specified port address. |
| [StorPortInitialize function](nf-storport-storportinitialize.md) | The StorPortInitilize routine initializes the port driver parameters and extension data. StorPortInitilize also saves the adapter information provided from the miniport driver. |
| [WHICH_BIT function](nf-storport-which-bit.md) | TBD |
| [StorPortGetD3ColdSupport function](nf-storport-storportgetd3coldsupport.md) | TBD |
| [StorPortGetProcessorIndexFromNumber function](nf-storport-storportgetprocessorindexfromnumber.md) | TBD |
| [StorPortFreeWorker function](nf-storport-storportfreeworker.md) | Frees a Storport work item previously allocated by the StorPortInitializeWorker routine. |
| [StorPortReadPortBufferUlong function](nf-storport-storportreadportbufferulong.md) | The StorPortReadPortBufferUlong routine reads a value from a specified port address. |
| [StorPortWritePortBufferUchar function](nf-storport-storportwriteportbufferuchar~r1.md) | The StorPortWritePortBufferUchar routine writes a value to a specified register address. |
| [RTL_CONTAINS_FIELD function](nf-storport-rtl-contains-field.md) | TBD |
| [StorPortWritePortUshort function](nf-storport-storportwriteportushort~r1.md) | The StorPortWritePortUshort routine writes a value to a specified register address. |
| [StorPortInterlockedRemoveHeadList function](nf-storport-storportinterlockedremoveheadlist.md) | The StorPortInterlockedRemoveHeadList routine removes an entry from the beginning of a doubly linked list of STOR_LIST_ENTRY structures. |
| [StorPortGetHighestNodeNumber function](nf-storport-storportgethighestnodenumber.md) | The StorPortGetHighestNodeNumber routine returns the largest possible node number on the system. |
| [StorPortReadRegisterUlong function](nf-storport-storportreadregisterulong~r1.md) | The StorPortReadRegisterUlong routine reads a value from a specified register address. |
| [StorPortGetRequestCryptoInfo function](nf-storport-storportgetrequestcryptoinfo.md) | Reserved for system use. |
| [StorPortPoFxPowerControl function](nf-storport-storportpofxpowercontrol.md) | The StorPortPoFxPowerControl routine sends a power control request to the power management framework (PoFx) to forward to the power engine plug-in (PEP). |
| [StorPortReadRegisterBufferUchar function](nf-storport-storportreadregisterbufferuchar~r1.md) | The StorPortReadRegisterBufferUchar routine reads a value from a specified register address. |
| [StorPortInitializeCryptoEngine function](nf-storport-storportinitializecryptoengine.md) | Reserved for system use. |
| [StorPortWritePortUchar function](nf-storport-storportwriteportuchar~r1.md) | The StorPortWritePortUchar routine writes a value to a specified register address. |
| [StorPortAcquireSpinLock function](nf-storport-storportacquirespinlock.md) | The StorPortAcquireSpinLock routine acquires the specified spin lock. |
| [StorPortUpdateAdapterMaxIO function](nf-storport-storportupdateadaptermaxio.md) | This function can be called by a miniport to update the maximum IO's supported by an adapter. This function is valid during HwInitialize/HwPassiveInitRoutine callback and has effect only during adapter initialization. |
| [StorPortCopyMemory function](nf-storport-storportcopymemory.md) | TBD |
| [StorPortReadRegisterUchar function](nf-storport-storportreadregisteruchar~r1.md) | The StorPortReadRegisterUchar routine reads a value from a specified register address. |
| [StorPortInitializeWorker function](nf-storport-storportinitializeworker.md) | Creates a new Storport work item that runs in a system worker thread. |
| [ScsiPortWriteRegisterBufferUchar function](nf-storport-scsiportwriteregisterbufferuchar.md) | TBD |
| [StorPortWriteRegisterUchar function](nf-storport-storportwriteregisteruchar~r1.md) | The StorPortWriteRegisterBufferUshort routine transfers a given number of character values from a buffer to the indicated HBA register address. |
| [DebugPrint function](nf-storport-debugprint.md) | TBD |
| [StorPortInitializeListHead function](nf-storport-storportinitializelisthead.md) | The StorPortInitializeListHead routine initializes a STOR_LIST_ENTRY structure that represents the head of a doubly linked list. |
| [REVERSE_SHORT function](nf-storport-reverse-short.md) | TBD |
| [StorPortPoFxSetIdleTimeout function](nf-storport-storportpofxsetidletimeout.md) | TBD |
| [StorPortGetDataInBufferSystemAddress function](nf-storport-storportgetdatainbuffersystemaddress.md) | Returns the system address for the input data buffer of a SCSI request block (SRB). |
| [IsDescriptorSenseDataFormat function](nf-storport-isdescriptorsensedataformat.md) | TBD |
| [REVERSE_BYTES_6 function](nf-storport-reverse-bytes-6.md) | TBD |
| [StorPortReady function](nf-storport-storportready.md) | The StorPortReady routine notifies the port driver that the adapter is no longer busy. |
| [ScsiPortReadPortUshort function](nf-storport-scsiportreadportushort.md) | TBD |
| [StorPortGetPfns function](nf-storport-storportgetpfns.md) | The StorPortGetPfns routine can be called when a miniport needs to retreive PFNs associated with a MDL for a SRB. |
| [StorPortAllocateMdl function](nf-storport-storportallocatemdl.md) | The StorPortAllocateMdl routine allocates an MDL to describe the given non-paged pool memory. |
| [StorPortReadRegisterUlong64 function](nf-storport-storportreadregisterulong64.md) | The StorPortReadRegisterUlong64 routine reads a 64-bit value from a specified 64-bit register address. |
| [REVERSE_LONG function](nf-storport-reverse-long.md) | TBD |
| [StorPortResume function](nf-storport-storportresume.md) | The StorPortResume routine resumes a paused adapter. |
| [StorPortInterlockedPopEntrySList function](nf-storport-storportinterlockedpopentryslist.md) | Removes an item from the front of a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system. Syntax. |
| [StorPortQueryDepthSList function](nf-storport-storportquerydepthslist.md) | Retrieves the number of entries in a Storport managed singly linked list. |
| [ScsiGetFixedSenseKeyAndCodes function](nf-storport-scsigetfixedsensekeyandcodes.md) | TBD |
| [ScsiConvertToFixedSenseFormat function](nf-storport-scsiconverttofixedsenseformat.md) | TBD |
| [StorPortGetSystemAddress function](nf-storport-storportgetsystemaddress.md) | The StorPortGetSystemAddress routine returns a virtual address in system space for the data buffer of the specified SCSI request block (SRB). |
| [StorPortFreeHostMemoryBuffer function](nf-storport-storportfreehostmemorybuffer.md) | The StorPortFreeHostMemoryBuffer routine frees the physically contiguous memory that was allocated to be used for a Host Memory Buffer (HMB). |
| [FIELD_OFFSET function](nf-storport-field-offset.md) | TBD |
| [SRB_STATUS function](nf-storport-srb-status.md) | TBD |
| [StorPortWritePortBufferUchar function](nf-storport-storportwriteportbufferuchar.md) | The StorPortWritePortBufferUchar routine writes a value to a specified register address. |
| [StorPortRegistryReadAdapterKey function](nf-storport-storportregistryreadadapterkey.md) | The StorPortRegistryReadAdapterKey routine is called by the miniport driver to read the hardware or device registry adapter keys located in registry at HKLM/CurrentControlSet/Enum/&lt;Instance path&gt;/DeviceParameters/... |
| [ScsiGetDescriptorSenseKeyAndCodes function](nf-storport-scsigetdescriptorsensekeyandcodes.md) | TBD |
| [IsSenseDataDeferredError function](nf-storport-issensedatadeferrederror.md) | TBD |
| [ScsiGetTotalSenseByteCountIndicated function](nf-storport-scsigettotalsensebytecountindicated.md) | TBD |
| [StorPortLogSystemEvent function](nf-storport-storportlogsystemevent.md) | The StorPortLogSystemEvent routine gives miniport drivers full access to the capabilities of the Windows kernel event facility, enabling miniport drivers to create event log entries that are truly useful in troubleshooting storage issues. |
| [StorPortGetActiveNodeCount function](nf-storport-storportgetactivenodecount.md) | The StorPortGetActiveNodeCount routine returns the number of nodes that are present in the system. |
| [StorPortReadRegisterUlong function](nf-storport-storportreadregisterulong.md) | The StorPortReadRegisterUlong routine reads a value from a specified register address. |
| [ScsiGetNextSenseDescriptorByType function](nf-storport-scsigetnextsensedescriptorbytype.md) | TBD |
| [StorPortWriteRegisterUchar function](nf-storport-storportwriteregisteruchar.md) | The StorPortWriteRegisterBufferUshort routine transfers a given number of character values from a buffer to the indicated HBA register address. |
| [StorPortGetDataInBufferMdl function](nf-storport-storportgetdatainbuffermdl.md) | Returns an MDL associated with the input data buffer of a SCSI request block (SRB). |
| [StorPortIsDeviceOperationAllowed function](nf-storport-storportisdeviceoperationallowed.md) | A miniport driver can call the StorPortIsDeviceOperationAllowedminiport routine to determine if operations for a certain device management class are allowed. |
| [StorPortGetActivityIdSrb function](nf-storport-storportgetactivityidsrb.md) | Retrieves the Event Tracing for Windows (ETW) activity ID associated with a request block. |
| [StorPortWritePortUchar function](nf-storport-storportwriteportuchar.md) | The StorPortWritePortUchar routine writes a value to a specified register address. |
| [ScsiPortWritePortBufferUshort function](nf-storport-scsiportwriteportbufferushort.md) | TBD |
| [StorPortConvertPhysicalAddressToULong64 function](nf-storport-storportconvertphysicaladdresstoulong64.md) | TBD |
| [StorPortSetAdapterBusType function](nf-storport-storportsetadapterbustype.md) | Used to adjust the BusType of the adapter depending on its current configuration. |
| [StorPortConvertUlongToPhysicalAddress function](nf-storport-storportconvertulongtophysicaladdress.md) | The StorPortConvertUlongToPhysicalAddress routine converts an unsigned long address into a physical address. |
| [StorPortPoFxActivateComponent function](nf-storport-storportpofxactivatecomponent.md) | The StorPortPoFxActivateComponent routine increments the activation reference count on the specified component of a storage device. |
| [StorPortWriteRegisterUlong64 function](nf-storport-storportwriteregisterulong64.md) | This StorPortWriteRegisterUlong64 routine writes a ULONG64 value to the specified register address. |
| [StorPortGetLogicalUnit function](nf-storport-storportgetlogicalunit.md) | The StorPortGetLogicalUnit routine returns a pointer to the miniport driver's per-logical-unit storage area. |
| [StorPortBusy function](nf-storport-storportbusy.md) | The StorPortBusy routine notifies the port driver that the adapter is currently busy, handling outstanding requests. |
| [StorPortAsyncNotificationDetected function](nf-storport-storportasyncnotificationdetected.md) | A storage miniport driver calls StorPortAsyncNotificationDetected to notify the Storport driver of a storage device status change event. |
| [ScsiPortReadRegisterUshort function](nf-storport-scsiportreadregisterushort.md) | TBD |
| [ScsiValidateInformationSenseDescriptor function](nf-storport-scsivalidateinformationsensedescriptor.md) | TBD |
| [SCSI_DECODE_BUS_TARGET function](nf-storport-scsi-decode-bus-target.md) | TBD |
| [ScsiPortReadPortBufferUshort function](nf-storport-scsiportreadportbufferushort.md) | TBD |
| [StorPortReadPortBufferUshort function](nf-storport-storportreadportbufferushort.md) | The StorPortReadPortBufferUshort routine reads a value from a specified port address. |
| [StorPortAllocateRegistryBuffer function](nf-storport-storportallocateregistrybuffer.md) | The StorPortAllocateRegistryBuffer routine is called by the miniport driver to allocate a buffer that can be used to read and write registry data. |
| [StorPortReadPortUshort function](nf-storport-storportreadportushort~r1.md) | The StorPortReadPortUshort routine reads a value from a specified port address. |
| [StorPortQueryPerformanceCounter function](nf-storport-storportqueryperformancecounter.md) | The current system performance counter value is queried is returned by the StorPortQueryPerformanceCounter routine. |
| [StorPortSetDeviceQueueDepth function](nf-storport-storportsetdevicequeuedepth.md) | The StorPortSetDeviceQueueDepth routine sets the maximum depth of the device queue for the indicated device. |
| [StorPortGetActiveGroupCount function](nf-storport-storportgetactivegroupcount.md) | The StorPortGetActiveGroupCount routine returns the number of processor groups that are present in the system. |
| [StorPortGetVirtualAddress function](nf-storport-storportgetvirtualaddress.md) | The StorPortGetVirtualAddress routine obtains a virtual address that maps to the indicated physical address. |
| [StorPortReadPortUshort function](nf-storport-storportreadportushort.md) | The StorPortReadPortUshort routine reads a value from a specified port address. |
| [StorPortEtwEvent2 function](nf-storport-storportetwevent2.md) | The StorPortEtwEvent2 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log two general purpose ETW parameters. The ETW parameters are expressed as two name-value pairs. |
| [ScsiPortReadRegisterBufferUchar function](nf-storport-scsiportreadregisterbufferuchar.md) | TBD |
| [StorPortEtwEvent4 function](nf-storport-storportetwevent4.md) | The StorPortEtwEvent4 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log four general purpose ETW parameters. The ETW parameters are expressed as four name-value pairs. |
| [StorPortWriteRegisterBufferUchar function](nf-storport-storportwriteregisterbufferuchar.md) | The StorPortWriteRegisterBufferUchar routine transfers a given number of unsigned bytes from a buffer to the HBA. |
| [StorPortPauseDevice function](nf-storport-storportpausedevice.md) | The StorPortPauseDevice routine pauses a specific logical unit device for the specified period of time. |
| [StorPortFlushDataBufferMdl function](nf-storport-storportflushdatabuffermdl.md) | TBD |
| [StorPortGetDeviceObjects function](nf-storport-storportgetdeviceobjects.md) | The StorPortGetDeviceObjects routine returns the device objects that are associated with the adapter device stack. |
| [StorPortReadPortBufferUchar function](nf-storport-storportreadportbufferuchar~r1.md) | The StorPortReadPortBufferUchar routine reads a value from a specified port address |
| [StorPortReadRegisterBufferUshort function](nf-storport-storportreadregisterbufferushort~r1.md) | The StorPortReadRegisterBufferUshort routine reads a value from a specified register address. |
| [StorPortPoFxSetComponentResidency function](nf-storport-storportpofxsetcomponentresidency.md) | The StorPortPoFxSetComponentResidency routine sets the estimated time for how long a storage device component is likely to remain idle after the component enters the idle condition. |
| [StorPortGetDeviceBase function](nf-storport-storportgetdevicebase.md) | The StorPortGetDeviceBase routine maps an I/O address to system address space. |
| [StorPortInvokeAcpiMethod function](nf-storport-storportinvokeacpimethod.md) | The StorPortInvokeAcpiMethod routine executes an ACPI method for a storage device. |
| [StorPortSetBusDataByOffset function](nf-storport-storportsetbusdatabyoffset.md) | The StorPortSetBusDataByOffset routine writes bus-specific configuration information. |
| [StorPortFreePool function](nf-storport-storportfreepool.md) | The StorPortFreePool routine frees a block of memory that was previously allocated by a call to the StorPortAllocatePool routine. |
| [StorPortPoFxRegisterPerfStates function](nf-storport-storportpofxregisterperfstates.md) | TBD |
| [StorPortWritePortBufferUshort function](nf-storport-storportwriteportbufferushort.md) | The StorPortWritePortBufferUshort routine writes a value to a specified register address. |
| [StorPortWriteRegisterBufferUlong function](nf-storport-storportwriteregisterbufferulong.md) | The StorPortWriteRegisterBufferUlong routine transfers a given number of ULONG values from a buffer to the HBA. |
| [StorPortInitializePerfOpts function](nf-storport-storportinitializeperfopts.md) | The StorPortInitializePerfOpts function initializes the performance optimizations that both the miniport driver and the Storport driver support using a PERF_CONFIGURATION_DATA structure. |
| [StorPortPutScatterGatherList function](nf-storport-storportputscattergatherlist.md) | The StorPortPutScatterGatherList routine releases any resources associated with a scatter/gather list that was previously created by a call to the StorPortBuildScatterGatherList routine. |
| [StorPortInterlockedInsertHeadList function](nf-storport-storportinterlockedinsertheadlist.md) | The StorPortInterlockedInsertHeadList routine atomically inserts an entry at the beginning of a doubly linked list of STOR_LIST_ENTRY structures. |
| [IsSenseDataFormatValueValid function](nf-storport-issensedataformatvaluevalid.md) | TBD |
| [StorPortGetRequestInfo function](nf-storport-storportgetrequestinfo.md) | The StorPortGetRequestInfo routine retrieves the IO request information associated with a SCSI request block (SRB) and returns it in a STOR_REQUEST_INFO structure. |
| [StorPortPoFxIdleComponent function](nf-storport-storportpofxidlecomponent.md) | The StorPortPoFxIdleComponent routine decrements the activation reference count of a specified component of a storage device. |
| [StorPortGetStartIoPerfParams function](nf-storport-storportgetstartioperfparams.md) | The StorPortGetStartIoPerfParams routine places the performance parameters for a given I/O request in a STARTIO_PERFORMANCE_PARAMETERS structure. |
| [ScsiPortWriteRegisterUchar function](nf-storport-scsiportwriteregisteruchar.md) | TBD |
| [StorPortAcquireMSISpinLock function](nf-storport-storportacquiremsispinlock.md) | The StorPortAcquireMSISpinLock routine acquires the message signaled interrupt (MSI) spin lock that is associated with the specified message. |
| [StorPortFreeRegistryBuffer function](nf-storport-storportfreeregistrybuffer.md) | The StorPortFreeRegistryBuffer routine frees the buffer that was allocated for storing registry data. |
| [StorPortWritePortUshort function](nf-storport-storportwriteportushort.md) | The StorPortWritePortUshort routine writes a value to a specified register address. |
| [StorPortWritePortBufferUlong function](nf-storport-storportwriteportbufferulong.md) | The StorPortWritePortBufferUlong routine writes a value to a specified register address. |
| [ScsiPortReadRegisterUlong function](nf-storport-scsiportreadregisterulong.md) | TBD |
| [StorPortGetBusData function](nf-storport-storportgetbusdata.md) | The StorPortGetBusData routine retrieves the bus-specific configuration information necessary to initialize the HBA. |
| [REVERSE_BYTES_2 function](nf-storport-reverse-bytes-2.md) | TBD |
| [StorPortReadRegisterBufferUchar function](nf-storport-storportreadregisterbufferuchar.md) | The StorPortReadRegisterBufferUchar routine reads a value from a specified register address. |
| [ScsiGetSenseKeyAndCodes function](nf-storport-scsigetsensekeyandcodes.md) | TBD |
| [StorPortInterlockedPushEntrySList function](nf-storport-storportinterlockedpushentryslist.md) | Inserts an item at the front of a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system. |
| [StorPortWriteRegisterBufferUchar function](nf-storport-storportwriteregisterbufferuchar~r1.md) | The StorPortWriteRegisterBufferUchar routine transfers a given number of unsigned bytes from a buffer to the HBA. |
| [StorPortRegistryWriteAdapterKey function](nf-storport-storportregistrywriteadapterkey.md) | The StorPortRegistryWriteAdapterKey routine is called by the miniport driver to write the hardware or device registry adapter keys located in registry at HKLM/CurrentControlSet/Enum/&lt;Instance path&gt;/DeviceParameters/... |
| [RTL_SIZEOF_THROUGH_FIELD function](nf-storport-rtl-sizeof-through-field.md) | TBD |
| [StorPortWriteRegisterUlong function](nf-storport-storportwriteregisterulong.md) | The StorPortWriteRegisterUlong routine transfers a ULONG value to the indicated HBA register address. |
| [StorPortReadPortUlong function](nf-storport-storportreadportulong~r1.md) | The StorPortReadPortUlong routine reads a value from a specified port address. |
| [ScsiPortWritePortUlong function](nf-storport-scsiportwriteportulong.md) | TBD |
| [StorPortNotification function](nf-storport-storportnotification.md) | The miniport driver uses the StorPortNotification routine to notify the Storport driver of certain events and conditions. |
| [StorPortCompleteServiceIrp function](nf-storport-storportcompleteserviceirp.md) | The StorPortCompleteServiceIrp routine is called by a Storport virtual miniport driver when it needs to complete a request that it received in its HwStorProcessServiceRequest callback routine. |
| [StorPortIssueDpc function](nf-storport-storportissuedpc.md) | The StorPortIssueDpc routine issues a deferred procedure call (DPC). |
| [StorPortWriteRegisterBufferUlong function](nf-storport-storportwriteregisterbufferulong~r1.md) | The StorPortWriteRegisterBufferUlong routine transfers a given number of ULONG values from a buffer to the HBA. |
| [StorPortInterlockedInsertTailList function](nf-storport-storportinterlockedinserttaillist.md) | The StorPortInterlockedInsertTailList routine atomically inserts an entry at the end of a doubly linked list of STOR_LIST_ENTRY structures. |
| [ScsiGetSenseDescriptor function](nf-storport-scsigetsensedescriptor.md) | TBD |
| [StorPortInitializeTimer function](nf-storport-storportinitializetimer.md) | Creates a Storport timer context object. |
| [StorPortAllocateHostMemoryBuffer function](nf-storport-storportallocatehostmemorybuffer.md) | This function allocates one or more ranges of physically contiguous memory to be used as a Host Memory Buffer (HMB). |
| [StorPortConvertPhysicalAddressToUlong function](nf-storport-storportconvertphysicaladdresstoulong~r1.md) | TBD |
| [ScsiGetSenseDescriptorLength function](nf-storport-scsigetsensedescriptorlength.md) | TBD |
| [StorPortFreeMdl function](nf-storport-storportfreemdl.md) | The StorPortFreeMdl routine frees a memory descriptor list (MDL) describing non-paged pool memory. |
| [StorPortReadPortUchar function](nf-storport-storportreadportuchar~r1.md) | The StorPortReadPortUchar routine reads a value from a specified port address |
| [ScsiPortReadRegisterBufferUshort function](nf-storport-scsiportreadregisterbufferushort.md) | TBD |
| [StorPortValidateRange function](nf-storport-storportvalidaterange.md) | The StorPortValidateRange routine determines whether a specified range of I/O addresses is in use by another adapter. This routine is obsolete in Windows NT 4.0 and later operating systems. |
| [StorPortSynchronizeAccess function](nf-storport-storportsynchronizeaccess.md) | The StorPortSynchronizeAccess routine provides synchronized access to a miniport driver's device extension. |
| [RtlZeroMemory function](nf-storport-rtlzeromemory.md) | TBD |
| [ScsiGetSenseErrorCode function](nf-storport-scsigetsenseerrorcode.md) | TBD |
| [StorPortMarkDumpMemory function](nf-storport-storportmarkdumpmemory.md) | A miniport should mark memory used for the dump file or the hibernation file. |
| [StorPortConvertPhysicalAddressToUlong function](nf-storport-storportconvertphysicaladdresstoulong.md) | TBD |
| [ScsiPortWriteRegisterUshort function](nf-storport-scsiportwriteregisterushort.md) | TBD |
| [StorPortWriteRegisterBufferUshort function](nf-storport-storportwriteregisterbufferushort~r1.md) | The StorPortWriteRegisterBufferUshort routine transfers a given number of USHORT values from a buffer to the HBA. |
| [SCSI_COMBINE_BUS_TARGET function](nf-storport-scsi-combine-bus-target.md) | TBD |
| [ScsiPortReadPortBufferUchar function](nf-storport-scsiportreadportbufferuchar.md) | TBD |
| [StorPortInitializePoFxPower function](nf-storport-storportinitializepofxpower.md) | A miniport driver calls StorPortInitializePoFxPower to register a storage device with the power management framework (PoFx). |
| [REVERSE_BYTES_4 function](nf-storport-reverse-bytes-4.md) | TBD |
| [StorPortGetNodeAffinity function](nf-storport-storportgetnodeaffinity.md) | The StorPortGetNodeAffinity routine constructs a mask of the active processors in a requested non-uniform memory access (NUMA) node. |
| [StorPortIsCurrentOsInstallationUpgrade function](nf-storport-storportiscurrentosinstallationupgrade.md) | The StorPortIsCurrentOsInstallationUpgrade routine checks if the current installation of Windows is an upgrade from a previous version or not. |
| [StorPortDeviceBusy function](nf-storport-storportdevicebusy.md) | The StorPortDeviceBusy routine notifies the port driver that the specified logical unit is currently busy, handling outstanding requests. |
| [StorPortExtendedFunction function](nf-storport-storportextendedfunction.md) | TBD |
| [StorPortWritePortUlong function](nf-storport-storportwriteportulong.md) | The StorPortWritePortUlong routine writes a value to a specified register address. |
| [StorPortReleaseSpinLock function](nf-storport-storportreleasespinlock.md) | The StorPortReleaseSpinLock routine releases a spinlock acquired by StorPortAcquireSpinLock. |
| [StorPortGetDataInBufferScatterGatherList function](nf-storport-storportgetdatainbufferscattergatherlist.md) | Returns the scatter-gather list associated with the input data buffer of a SCSI request block (SRB). |
| [StorPortGetOriginalMdl function](nf-storport-storportgetoriginalmdl.md) | The StorPortGetOriginalMdl routine returns the MDL associated with the given SRB. |
| [StorPortLogError function](nf-storport-storportlogerror.md) | The StorPortLogError routine notifies the port driver that an error occurred. |
| [StorPortQueueWorkItem function](nf-storport-storportqueueworkitem.md) | Schedules a Storport work item to execute within the context of a system worker thread. |
| [IsFixedSenseDataFormat function](nf-storport-isfixedsensedataformat.md) | TBD |
| [StorPortReadRegisterUshort function](nf-storport-storportreadregisterushort.md) | The StorPortReadRegisterUshort routine reads a value from a specified register address. |
| [StorPortAllocateContiguousMemorySpecifyCacheNode function](nf-storport-storportallocatecontiguousmemoryspecifycachenode.md) | The StorPortAllocateContiguousMemorySpecifyCacheNode routine allocates a range of physically contiguous noncached, nonpaged memory. |
| [StorPortGetUncachedExtension function](nf-storport-storportgetuncachedextension.md) | The StorPortGetUncachedExtension routine allocates an uncached common buffer to be shared by the CPU and the device. |
| [REVERSE_LONGLONG function](nf-storport-reverse-longlong.md) | TBD |
| [StorPortEnablePassiveInitialization function](nf-storport-storportenablepassiveinitialization.md) | The StorPortEnablePassiveInitialization routine enables the miniport's HwStorPassiveInitializeRoutine callback routine to execute at PASSIVE_LEVEL during miniport initialization. |
| [RTL_FIELD_SIZE function](nf-storport-rtl-field-size.md) | TBD |
| [StorPortGetCurrentProcessorNumber function](nf-storport-storportgetcurrentprocessornumber.md) | The StorPortGetCurrentProcessorNumber routine retrieves the current processor number from the kernel. |
| [StorPortWritePortBufferUlong function](nf-storport-storportwriteportbufferulong~r1.md) | The StorPortWritePortBufferUlong routine writes a value to a specified register address. |
| [ScsiPortReadRegisterBufferUlong function](nf-storport-scsiportreadregisterbufferulong.md) | TBD |
| [StorPortInitializeSListHead function](nf-storport-storportinitializeslisthead.md) | Initializes the head of a Storport managed singly linked list. |
| [StorPortReadRegisterUchar function](nf-storport-storportreadregisteruchar.md) | The StorPortReadRegisterUchar routine reads a value from a specified register address. |
| [StorPortReadRegisterBufferUlong function](nf-storport-storportreadregisterbufferulong.md) | The StorPortReadRegisterBufferUlong routine reads a value from a specified register address. |
| [StorPortMoveMemory function](nf-storport-storportmovememory.md) | The StorPortMoveMemory routine copies memory from one buffer to another. |
| [StorPortWriteRegisterUshort function](nf-storport-storportwriteregisterushort.md) | The StorPortWriteRegisterUshort routine transfers a ULONG value to the indicated HBA register address. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [STOR_DEVICE_POWER_STATE enumeration](ne-storport--stor-device-power-state.md) | The STOR_DEVICE_POWER_STATE enumerator specifies a device power state. |
| [STOR_EVENT_ASSOCIATION_ENUM enumeration](ne-storport--stor-event-association-enum.md) | The STOR_EVENT_ASSOCIATION_ENUM enumerator specifies the type of device that is associated with an event. |
| [SCSI_ADAPTER_CONTROL_STATUS enumeration](ne-storport--scsi-adapter-control-status.md) | TBD |
| [STOR_SPINLOCK enumeration](ne-storport--stor-spinlock.md) | The STOR_SPINLOCK enumeration is used to specify the type of a spinlock. |
| [SCSI_NOTIFICATION_TYPE enumeration](ne-storport--scsi-notification-type.md) | TBD |
| [SRBEXDATATYPE enumeration](ne-storport--srbexdatatype.md) | TBD |
| [INTERRUPT_SYNCHRONIZATION_MODE enumeration](ne-storport--interrupt-synchronization-mode.md) | The INTERRUPT_SYNCHRONIZATION_MODE enumerator specifies the interrupt synchronization mode. |
| [STOR_CRYPTO_ALGORITHM_ID enumeration](ne-storport--stor-crypto-algorithm-id.md) | TBD |
| [SES_ELEMENT_TYPE enumeration](ne-storport--ses-element-type.md) | TBD |
| [STOR_CRYPTO_KEY_SIZE enumeration](ne-storport--stor-crypto-key-size.md) | TBD |
| [VPD_ASSOCIATION enumeration](ne-storport--vpd-association.md) | TBD |
| [STOR_POFX_PERF_STATE_UNIT enumeration](ne-storport--stor-pofx-perf-state-unit.md) | TBD |
| [VPD_CODE_SET enumeration](ne-storport--vpd-code-set.md) | TBD |
| [SCSI_ADAPTER_CONTROL_TYPE enumeration](ne-storport--scsi-adapter-control-type.md) | TBD |
| [STOR_CRYPTO_OPERATION_TYPE enumeration](ne-storport--stor-crypto-operation-type.md) | TBD |
| [SCSI_UC_DEVICE_USAGE_TYPE enumeration](ne-storport--scsi-uc-device-usage-type.md) | TBD |
| [SES_ELEMENT_STATE enumeration](ne-storport--ses-element-state.md) | TBD |
| [STORPORT_FUNCTION_CODE enumeration](ne-storport--storport-function-code.md) | TBD |
| [SCSI_UNIT_CONTROL_TYPE enumeration](ne-storport--scsi-unit-control-type.md) | TBD |
| [STOR_IO_PRIORITY_HINT enumeration](ne-storport--stor-io-priority-hint.md) | TBD |
| [TRANSFER_COUNT_UNITS enumeration](ne-storport--transfer-count-units.md) | TBD |
| [SES_DOWNLOAD_MICROCODE_STATE enumeration](ne-storport--ses-download-microcode-state.md) | TBD. |
| [STOR_POFX_PERF_STATE_TYPE enumeration](ne-storport--stor-pofx-perf-state-type.md) | TBD |
| [PSTOR_PNP_ACTION enumeration](ne-storport-pstor-pnp-action.md) | TBD |
| [STOR_SYNCHRONIZATION_MODEL enumeration](ne-storport--stor-synchronization-model.md) | TBD |
| [PSTOR_POWER_ACTION enumeration](ne-storport-pstor-power-action.md) | The STOR_POWER_ACTION enumerator indicates the power state that the system is about to enter during a power transition. |
| [STOR_RPMB_FRAME_TYPE enumeration](ne-storport--stor-rpmb-frame-type.md) | TBD |
| [VPD_IDENTIFIER_TYPE enumeration](ne-storport--vpd-identifier-type.md) | TBD |
| [SCSI_UNIT_CONTROL_STATUS enumeration](ne-storport--scsi-unit-control-status.md) | TBD |
| [RAID_SYSTEM_POWER enumeration](ne-storport--raid-system-power.md) | TBD |
| [STORPORT_ETW_EVENT_OPCODE enumeration](ne-storport--storport-etw-event-opcode.md) | TBD |
| [OPERATION_STATUS enumeration](ne-storport--operation-status.md) | TBD |
| [STORPORT_ETW_LEVEL enumeration](ne-storport--storport-etw-level.md) | TBD |
| [GETSGSTATUS enumeration](ne-storport--getsgstatus.md) | TBD |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_SCSI_MINIPORT_ENABLE_DISABLE_AUTOSAVE IOCTL](ni-storport-ioctl-scsi-miniport-enable-disable-autosave.md) | TBD |
| [IOCTL_SCSI_MINIPORT_READ_SMART_ATTRIBS IOCTL](ni-storport-ioctl-scsi-miniport-read-smart-attribs.md) | TBD |
| [IOCTL_SCSI_EXECUTE_OUT IOCTL](ni-storport-ioctl-scsi-execute-out.md) | TBD |
| [IOCTL_SCSI_MINIPORT_NOT_QUORUM_CAPABLE IOCTL](ni-storport-ioctl-scsi-miniport-not-quorum-capable.md) | TBD |
| [IOCTL_SCSI_EXECUTE_NONE IOCTL](ni-storport-ioctl-scsi-execute-none.md) | TBD |
| [IOCTL_SCSI_MINIPORT_RETURN_STATUS IOCTL](ni-storport-ioctl-scsi-miniport-return-status.md) | TBD |
| [IOCTL_SCSI_MINIPORT_READ_SMART_LOG IOCTL](ni-storport-ioctl-scsi-miniport-read-smart-log.md) | TBD |
| [IOCTL_SCSI_MINIPORT_IDENTIFY IOCTL](ni-storport-ioctl-scsi-miniport-identify.md) | TBD |
| [IOCTL_SCSI_MINIPORT_DSM_GENERAL IOCTL](ni-storport-ioctl-scsi-miniport-dsm-general.md) | TBD |
| [IOCTL_SCSI_MINIPORT_DSM IOCTL](ni-storport-ioctl-scsi-miniport-dsm.md) | TBD |
| [IOCTL_SCSI_MINIPORT_WRITE_SMART_LOG IOCTL](ni-storport-ioctl-scsi-miniport-write-smart-log.md) | TBD |
| [IOCTL_SCSI_EXECUTE_IN IOCTL](ni-storport-ioctl-scsi-execute-in.md) | TBD |
| [IOCTL_SCSI_MINIPORT_DISABLE_SMART IOCTL](ni-storport-ioctl-scsi-miniport-disable-smart.md) | TBD |
| [IOCTL_SCSI_MINIPORT_SMART_VERSION IOCTL](ni-storport-ioctl-scsi-miniport-smart-version.md) | TBD |
| [IOCTL_SCSI_MINIPORT_ENABLE_DISABLE_AUTO_OFFLINE IOCTL](ni-storport-ioctl-scsi-miniport-enable-disable-auto-offline.md) | TBD |
| [IOCTL_SCSI_MINIPORT_SAVE_ATTRIBUTE_VALUES IOCTL](ni-storport-ioctl-scsi-miniport-save-attribute-values.md) | TBD |
| [IOCTL_SCSI_MINIPORT_ENABLE_SMART IOCTL](ni-storport-ioctl-scsi-miniport-enable-smart.md) | TBD |
| [IOCTL_SCSI_MINIPORT_EXECUTE_OFFLINE_DIAGS IOCTL](ni-storport-ioctl-scsi-miniport-execute-offline-diags.md) | TBD |
| [IOCTL_SCSI_MINIPORT_NOT_CLUSTER_CAPABLE IOCTL](ni-storport-ioctl-scsi-miniport-not-cluster-capable.md) | TBD |
| [IOCTL_SCSI_MINIPORT_READ_SMART_THRESHOLDS IOCTL](ni-storport-ioctl-scsi-miniport-read-smart-thresholds.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PStorPortAcquireMSISpinLock callback function](nc-storport-pstorportacquiremsispinlock.md) | TBD |
| [PStorPortCompleteServiceIrp callback function](nc-storport-pstorportcompleteserviceirp.md) | TBD |
| [PStorPortGetMessageInterruptInformation callback function](nc-storport-pstorportgetmessageinterruptinformation.md) | TBD |
| [PStorPortReleaseMSISpinLock callback function](nc-storport-pstorportreleasemsispinlock.md) | TBD |
| [PStorPortAllocatePool callback function](nc-storport-pstorportallocatepool.md) | TBD |
| [PStorPortPutScatterGatherList callback function](nc-storport-pstorportputscattergatherlist.md) | TBD |
| [PStorPortBuildScatterGatherList callback function](nc-storport-pstorportbuildscattergatherlist.md) | TBD |
| [PStorPortGetSystemAddress callback function](nc-storport-pstorportgetsystemaddress.md) | TBD |
| [PStorPortFreePool callback function](nc-storport-pstorportfreepool.md) | TBD |
| [PStorPortGetOriginalMdl callback function](nc-storport-pstorportgetoriginalmdl.md) | TBD |

This header is used in these topics:

- [Storage](..content/_Storage)
