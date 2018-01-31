---
UID : NA:ntddscsi
ms.assetid : 77408c2c-0fca-30f4-a739-547207f848ef
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# ntddscsi.h header



ntddscsi.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_ATA_PASS_THROUGH](ni-ntddscsi-ioctl_ata_pass_through.md) | Allows an application to send almost any ATA command to a target device, with the following restrictions:\_If a class driver for the target type of device exists, the application must send the request to the class driver. |
| [IOCTL_ATA_PASS_THROUGH_DIRECT](ni-ntddscsi-ioctl_ata_pass_through_direct.md) | Allows an application to send almost any ATA command to a target device, with the following restrictions:\_If a class driver for the target type of device exists, the application must send the request to the class driver. |
| [IOCTL_MINIPORT_PROCESS_SERVICE_IRP](ni-ntddscsi-ioctl_miniport_process_service_irp.md) | This IOCTL is used by a user-mode application or kernel-mode driver that requires notification when something of interest happens in the virtual miniport. |
| [IOCTL_MPIO_PASS_THROUGH_PATH](ni-ntddscsi-ioctl_mpio_pass_through_path.md) | This I/O control code allows an application or kernel driver to send a SCSI command to a designated real LUN. |
| [IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT](ni-ntddscsi-ioctl_mpio_pass_through_path_direct.md) | This I/O control code allows an application or kernel driver to send a SCSI command to a designated real LUN. |
| [IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX](ni-ntddscsi-ioctl_mpio_pass_through_path_direct_ex.md) | The IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX control code request is the extended version of the IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT request. This request provides support for bidirectional data transfers and allows a command data block (CDB) &gt; 16 bytes. |
| [IOCTL_MPIO_PASS_THROUGH_PATH_EX](ni-ntddscsi-ioctl_mpio_pass_through_path_ex.md) | The IOCTL_MPIO_PASS_THROUGH_PATH_EX control code request is the extended version of the IOCTL_MPIO_PASS_THROUGH_PATH request. This request provides support for bidirectional data transfers and allows a command data block (CDB) &gt; 16 bytes. |
| [IOCTL_SCSI_GET_ADDRESS](ni-ntddscsi-ioctl_scsi_get_address.md) | Returns the address information, such as the target ID (TID) and the logical unit number (LUN) of a particular SCSI target. |
| [IOCTL_SCSI_GET_CAPABILITIES](ni-ntddscsi-ioctl_scsi_get_capabilities.md) | Returns the capabilities and limitations of the underlying SCSI HBA. |
| [IOCTL_SCSI_GET_INQUIRY_DATA](ni-ntddscsi-ioctl_scsi_get_inquiry_data.md) | Returns the SCSI inquiry data for all devices on a given SCSI host bus adapter (HBA). |
| [IOCTL_SCSI_MINIPORT](ni-ntddscsi-ioctl_scsi_miniport.md) | Sends a special control function to an HBA-specific miniport driver. |
| [IOCTL_SCSI_MINIPORT_DIAGNOSTIC](ni-ntddscsi-ioctl_scsi_miniport_diagnostic.md) | The IOCTL_SCSI_MINIPORT_DIAGNOSTIC control code is use to perform a diagnostic request to the Miniport. |
| [IOCTL_SCSI_MINIPORT_HYBRID](ni-ntddscsi-ioctl_scsi_miniport_hybrid.md) | The IOCTL_SCSI_MINIPORT_HYBRID control code sends a hybrid disk control request to an HBA-specific miniport driver. |
| [IOCTL_SCSI_MINIPORT_NVCACHE](ni-ntddscsi-ioctl_scsi_miniport_nvcache.md) | The NV Cache Management operations that are defined here can be invoked by user-mode application code running with administrator privileges, using DeviceIoControl and the IOCTL_SCSI_MINIPORT control code. |
| [IOCTL_SCSI_PASS_THROUGH](ni-ntddscsi-ioctl_scsi_pass_through.md) | Allows an application to send almost any SCSI command to a target device, with the following restrictions:Multitarget commands, such as COPY, are not allowed.Bidirectional data transfer operations are not supported.If a class driver for the target type of device exists, the request must be sent to that class driver. Thus, an application can send this request directly to the system port driver for a target logical unit (LU) only if there is no class driver for the type of device that is connected to that LU. The system port driver does not check to determine if a device has been claimed by a class driver before it processes a pass-through request. Therefore, if an application bypasses a class driver that has claimed a device and sends a pass-through request for that device directly to the port driver, a conflict for control of the device can occur between the class driver and the application. If a pass-through request is sent to an adapter device object and if it originates from user mode and targets an LU that is claimed by a class driver, Storport fails the request with STATUS_INVALID_DEVICE_REQUEST. If the request is sent to an LU device object, originates in kernel mode, or targets an unclaimed LU, it is passed to the miniport driver.This request cannot be used if the CDB might require the underlying miniport driver to access memory directly. If the caller's CDB might require direct access to memory, use IOCTL_SCSI_PASS_THROUGH_DIRECT instead. Applications must not attempt to send a pass-through request asynchronously. All pass-through requests must be synchronous. Applications do not require administrative privileges to send a pass-through request to a device, but they must have read/write access to the device. The calling application creates the SCSI command descriptor block, which can include a request for request-sense data if a CHECK CONDITION occurs. IOCTL_SCSI_PASS_THROUGH is a buffered device control request. To bypass buffering in system memory, callers should use IOCTL_SCSI_PASS_THROUGH_DIRECT. When handling an IOCTL_SCSI_PASS_THROUGH_DIRECT request, the system locks down the buffer in user memory and the device accesses this memory directly. This request is typically used for transferring small amounts of data (&lt;16K).Applications can send this request by means of an IRP_MJ_DEVICE_CONTROL request.Storage class drivers set the minor IRP number to IRP_MN_SCSI_CLASS to indicate that the request has been processed by a storage class driver. |
| [IOCTL_SCSI_PASS_THROUGH_DIRECT](ni-ntddscsi-ioctl_scsi_pass_through_direct.md) | Allows an application to send almost any SCSI command to a target device, with the following restrictions:Multitarget commands, such as COPY, are not allowed.Bidirectional data transfer operations are not supported.If a class driver for the target type of device exists, the request must be sent to that class driver. Thus, an application can send this request directly to the system port driver for a target logical unit only if there is no class driver for the type of device connected to that LU.This request must be made if the input CDB might require the underlying miniport driver to access memory directly.The calling application creates the SCSI command descriptor block, which can include a request for request-sense data if a CHECK CONDITION occurs. If the CDB requests a data transfer operation, the caller must set up an adapter device aligned buffer from which or into which the miniport driver can transfer data directly. This request is typically used for transferring larger amounts of data (&gt;16K).Applications can send this request by means of an IRP_MJ_DEVICE_CONTROL request. Storage class drivers set the minor IRP number to IRP_MN_SCSI_CLASS to indicate that the request has been processed by a storage class driver. |
| [IOCTL_SCSI_PASS_THROUGH_DIRECT_EX](ni-ntddscsi-ioctl_scsi_pass_through_direct_ex.md) | The IOCTL_SCSI_PASS_THROUGH_DIRECT_EX control code request is the extended version of the IOCTL_SCSI_PASS_THROUGH_DIRECT request. This request provides support for bidirectional data transfers and allows a command data block (CDB) &gt; 16 bytes. |
| [IOCTL_SCSI_PASS_THROUGH_EX](ni-ntddscsi-ioctl_scsi_pass_through_ex.md) | The IOCTL_SCSI_PASS_THROUGH_EX control code request is the extended version of the IOCTL_SCSI_PASS_THROUGH request. This request provides support for bidirectional data transfers and allows a command data block (CDB) &gt; 16 bytes. |
| [IOCTL_SCSI_RESCAN_BUS](ni-ntddscsi-ioctl_scsi_rescan_bus.md) | Rescans the LUNs on the bus(es). |




## Structures
| Title | Description |
| ---- |:---- |
| [_ATA_PASS_THROUGH_DIRECT](ns-ntddscsi-_ata_pass_through_direct.md) | The ATA_PASS_THROUGH_DIRECT structure is used in conjunction with an IOCTL_ATA_PASS_THROUGH_DIRECT request to instruct the port driver to send an embedded ATA command to the target device. |
| [_ATA_PASS_THROUGH_EX](ns-ntddscsi-_ata_pass_through_ex.md) | The ATA_PASS_THROUGH_EX structure is used in conjunction with an IOCTL_ATA_PASS_THROUGH request to instruct the port driver to send an embedded ATA command to the target device. |
| [_HYBRID_INFORMATION](ns-ntddscsi-_hybrid_information.md) | The HYBRID_INFORMATION structure contains hybrid disk capability information. |
| [_IO_SCSI_CAPABILITIES](ns-ntddscsi-_io_scsi_capabilities.md) | The IO_SCSI_CAPABILITIES structure is used in conjunction with the IOCTL_SCSI_GET_CAPABILITIES request to retrieve the capabilities and limitations of the underlying SCSI host adapter.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [_MPIO_PASS_THROUGH_PATH](ns-ntddscsi-_mpio_pass_through_path.md) | The MPIO_PASS_THROUGH_PATH structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH request to instruct the port driver to send an embedded SCSI command to the target device. |
| [_MPIO_PASS_THROUGH_PATH_DIRECT](ns-ntddscsi-_mpio_pass_through_path_direct.md) | The MPIO_PASS_THROUGH_PATH_DIRECT structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT request to instruct the port driver to send an embedded SCSI command to the target device. |
| [_MPIO_PASS_THROUGH_PATH_DIRECT_EX](ns-ntddscsi-_mpio_pass_through_path_direct_ex.md) | The MPIO_PASS_THROUGH_PATH_DIRECT_EX structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [_MPIO_PASS_THROUGH_PATH_EX](ns-ntddscsi-_mpio_pass_through_path_ex.md) | The MPIO_PASS_THROUGH_PATH_EX structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [_NV_FEATURE_PARAMETER](ns-ntddscsi-_nv_feature_parameter.md) | The NV_FEATURE_PARAMETER structure is used in conjunction with the IOCTL_SCSI_MINIPORT_NVCACHE request to get NV Cache Manager feature support information from the device. |
| [_NVCACHE_REQUEST_BLOCK](ns-ntddscsi-_nvcache_request_block.md) | The NVCACHE_REQUEST_BLOCK structure is used in conjunction with the IOCTL_SCSI_MINIPORT request to manage hybrid-hard disk drive (H-HDD) devices (for example, Microsoft ReadyDrive technology). |
| [_SCSI_ADAPTER_BUS_INFO](ns-ntddscsi-_scsi_adapter_bus_info.md) | The SCSI_ADAPTER_BUS_INFO structure is used in conjunction with the IOCTL_SCSI_GET_INQUIRY_DATA request to retrieve the SCSI inquiry data for all devices on a given SCSI bus. |
| [_SCSI_ADDRESS](ns-ntddscsi-_scsi_address.md) | The SCSI_ADDRESS structure is used in conjunction with the IOCTL_SCSI_GET_ADDRESS request to retrieve the address information, such as the target ID (TID) and the logical unit number (LUN) of a particular SCSI target. |
| [_SCSI_BUS_DATA](ns-ntddscsi-_scsi_bus_data.md) | The SCSI_BUS_DATA structure is used in conjunction with the IOCTL_SCSI_GET_INQUIRY_DATA request and the SCSI_ADAPTER_BUS_INFO structure to retrieve the SCSI inquiry data for all devices on a given SCSI bus. |
| [_SCSI_INQUIRY_DATA](ns-ntddscsi-_scsi_inquiry_data.md) | The SCSI_INQUIRY_DATA structure is used in conjunction with the IOCTL_SCSI_GET_INQUIRY_DATA request to retrieve the SCSI inquiry data for all devices on a given SCSI bus. |
| [_SCSI_PASS_THROUGH](ns-ntddscsi-_scsi_pass_through.md) | The SCSI_PASS_THROUGH structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH request to instruct the port driver to send an embedded SCSI command to the target device. |
| [_SCSI_PASS_THROUGH_DIRECT](ns-ntddscsi-_scsi_pass_through_direct.md) | The SCSI_PASS_THROUGH_DIRECT structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH_DIRECT request to instruct the port driver to send an embedded SCSI command to the target device. |
| [_SCSI_PASS_THROUGH_DIRECT_EX](ns-ntddscsi-_scsi_pass_through_direct_ex.md) | The SCSI_PASS_THROUGH_DIRECT_EX structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH_DIRECT_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [_SCSI_PASS_THROUGH_EX](ns-ntddscsi-_scsi_pass_through_ex.md) | The SCSI_PASS_THROUGH_EX structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [_SRB_IO_CONTROL](ns-ntddscsi-_srb_io_control.md) | SRB_IO_CONTROL structure |
| [_STORAGE_DIAGNOSTIC_MP_REQUEST](ns-ntddscsi-_storage_diagnostic_mp_request.md) | Describes a diagnostic request to Miniport. The STORAGE_DIAGNOSTIC_MP_REQUEST structure is provided in the input/output buffer of an IOCTL_SCSI_MINIPORT_DIAGNOSTIC request. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_MP_STORAGE_DIAGNOSTIC_LEVEL](ne-ntddscsi-_mp_storage_diagnostic_level.md) | The MP_STORAGE_DIAGNOSTIC_LEVEL enumeration allows the caller to control what kinds of data the provider should return. |
| [_MP_STORAGE_DIAGNOSTIC_TARGET_TYPE](ne-ntddscsi-_mp_storage_diagnostic_target_type.md) | The MP_STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration specifies the target type of a storage diagnostic. |