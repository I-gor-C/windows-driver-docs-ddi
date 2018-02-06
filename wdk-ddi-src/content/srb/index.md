---
UID: NA:srb
ms.assetid: c0f844f9-d5bf-3401-a193-bde076ae281d
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# srb.h header



srb.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [PHW_ADAPTER_CONTROL](nc-srb-phw_adapter_control.md) | The PHW_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs. |
| [PHW_ADAPTER_STATE](nc-srb-phw_adapter_state.md) | The PHW_INITIALIZE routine prototype declares a routine that saves or restores the state of the miniport driver's HBA. |
| [PHW_DMA_STARTED](nc-srb-phw_dma_started.md) | The PHW_DMA_STARTED routine prototype declares a SCSI miniport driver routine that starts DMA for subordinate DMA device. |
| [PHW_FIND_ADAPTER](nc-srb-phw_find_adapter.md) | The PHW_FIND_ADAPTER prototype declares a routine that uses supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter. |
| [PHW_INITIALIZE](nc-srb-phw_initialize.md) | The PHW_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs. |
| [PHW_INTERRUPT](nc-srb-phw_interrupt.md) | The PHW_INTERRUPT routine prototype declares the miniport driver's interrupt handler routine. |
| [PHW_RESET_BUS](nc-srb-phw_reset_bus.md) | The PHW_RESET_BUS prototype declares a routine that resets the indicated SCSI bus. |
| [PHW_STARTIO](nc-srb-phw_startio.md) | The PHW_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs. |
| [PHW_TIMER](nc-srb-phw_timer.md) | The PHW_TIMER routine prototype declares a SCSI miniport driver's timer routine. |
| [ScsiDebugPrint](nf-srb-scsidebugprint.md) | The ScsiDebugPrint routine prints debug information with a level of verbosity based on global values set in the kernel debugger or set in the registry and initialized when the system boots. |
| [ScsiPortCompleteRequest](nf-srb-scsiportcompleterequest.md) | The ScsiPortCompleteRequest routine completes all of the active requests for the given SCSI bus, controller, or LU, including a request being processed by the calling miniport driver routine.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [ScsiPortConvertPhysicalAddressToUlong](nf-srb-scsiportconvertphysicaladdresstoulong.md) | The ScsiPortConvertPhysicalAddressToUlong routine truncates a SCSI_PHYSICAL_ADDRESS to a ULONG.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortConvertUlongToPhysicalAddress](nf-srb-scsiportconvertulongtophysicaladdress.md) | The ScsiPortConvertUlongToPhysicalAddress routine extends a given ULONG address into a value of type SCSI_PHYSICAL_ADDRESS.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortFlushDma](nf-srb-scsiportflushdma.md) | The ScsiPortFlushDma routine flushes any data cached in the system DMA controller at the end of a transfer or terminates a system DMA transfer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortFreeDeviceBase](nf-srb-scsiportfreedevicebase.md) | The ScsiPortFreeDeviceBase routine frees a range of device I/O or memory space addresses previously mapped into the system address space with ScsiPortGetDeviceBase.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [ScsiPortGetBusData](nf-srb-scsiportgetbusdata.md) | The ScsiPortGetBusData routine returns bus-type-specific configuration information that a miniport driver's HwScsiFindAdapter routine might use to determine whether it supports a particular adapter on a particular I/O bus, and to configure the HBA if it does.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [ScsiPortGetDeviceBase](nf-srb-scsiportgetdevicebase.md) | The ScsiPortGetDeviceBase routine returns a mapped, logical base address that can be used to communicate with an HBA. |
| [ScsiPortGetLogicalUnit](nf-srb-scsiportgetlogicalunit.md) | The ScsiPortGetLogicalUnit routine returns a pointer to the miniport driver's per-LU storage area for a given peripheral.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortGetPhysicalAddress](nf-srb-scsiportgetphysicaladdress.md) | The ScsiPortGetPhysicalAddress routine converts a given virtual address range to a physical address range for a DMA operation.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortGetSrb](nf-srb-scsiportgetsrb.md) | The ScsiPortGetSrb routine returns a pointer to an active SCSI request for a particular logical unit.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortGetUncachedExtension](nf-srb-scsiportgetuncachedextension.md) | The ScsiPortGetUncachedExtension routine allocates memory that can be used by both the CPU and a bus-master HBA for DMA or for shared data.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortGetVirtualAddress](nf-srb-scsiportgetvirtualaddress.md) | The ScsiPortGetVirtualAddress routine returns a virtual address associated with a physical address if the physical address was obtained by a call to ScsiPortGetPhysicalAddress.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [ScsiPortInitialize](nf-srb-scsiportinitialize.md) | For a non-Plug and Play miniport driver, the ScsiPortInitialize routine sets up the PORT_CONFIGURATION_INFORMATION structure and calls the miniport driver's HwScsiFindAdapter routine. |
| [ScsiPortIoMapTransfer](nf-srb-scsiportiomaptransfer.md) | The ScsiPortIoMapTransfer routine sets up the system DMA controller for a miniport driver to transfer data through a subordinate HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortLogError](nf-srb-scsiportlogerror.md) | The ScsiPortLogError routine logs errors to the system event log when a miniport driver or its HBA detects a SCSI error condition.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortMoveMemory](nf-srb-scsiportmovememory.md) | The ScsiPortMoveMemory routine copies data from one location to another.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortNotification](nf-srb-scsiportnotification.md) | The ScsiPortNotification routine informs the operating system-specific port driver of certain events, such as when a miniport driver completes a request or is ready to start another SRB, as well as when the HBA indicates certain SCSI error conditions that occurred during an operation.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [ScsiPortQuerySystemTime](nf-srb-scsiportquerysystemtime.md) | The ScsiPortQuerySystemTime routine obtains the current system time.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortBufferUchar](nf-srb-scsiportreadportbufferuchar.md) | The ScsiPortReadPortBufferUchar routine transfers a given number of unsigned byte values from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortBufferUlong](nf-srb-scsiportreadportbufferulong.md) | The ScsiPortReadPortBufferUlong routine transfers a given number of ULONG values from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortBufferUshort](nf-srb-scsiportreadportbufferushort.md) | The ScsiPortReadPortBufferUshort routine transfers a given number of USHORT values from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortUchar](nf-srb-scsiportreadportuchar.md) | The ScsiPortReadPortUchar routine reads an unsigned byte value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortUlong](nf-srb-scsiportreadportulong.md) | The ScsiPortReadPortUlong routine reads a ULONG value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortUshort](nf-srb-scsiportreadportushort.md) | The ScsiPortReadPortUshort routine reads a USHORT value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadRegisterBufferUchar](nf-srb-scsiportreadregisterbufferuchar.md) | The ScsiPortReadRegisterBufferUchar routine transfers a specified number of unsigned bytes from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadRegisterBufferUlong](nf-srb-scsiportreadregisterbufferulong.md) | The ScsiPortReadRegisterBufferUlong routine transfers a specified number of ULONG values from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadRegisterBufferUshort](nf-srb-scsiportreadregisterbufferushort.md) | The ScsiPortReadRegisterBufferUshort routine transfers a specified number of USHORT values from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadRegisterUchar](nf-srb-scsiportreadregisteruchar.md) | The ScsiPortReadRegisterUchar routine reads an unsigned byte value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadRegisterUlong](nf-srb-scsiportreadregisterulong.md) | The ScsiPortReadRegisterUlong routine reads a ULONG value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadRegisterUshort](nf-srb-scsiportreadregisterushort.md) | The ScsiPortReadRegisterUshort routine reads a USHORT value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortSetBusDataByOffset](nf-srb-scsiportsetbusdatabyoffset.md) | The ScsiPortSetBusDataByOffset routine sets bus-configuration data for an adapter on a dynamically configurable I/O bus with a published, standard interface. |
| [ScsiPortStallExecution](nf-srb-scsiportstallexecution.md) | The ScsiPortStallExecution routine stalls in the miniport driver.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortValidateRange](nf-srb-scsiportvalidaterange.md) | The ScsiPortValidateRange routine indicates whether the specified access range values have already been claimed in the registry by another driver.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWritePortBufferUchar](nf-srb-scsiportwriteportbufferuchar.md) | The ScsiPortWritePortBufferUchar routine transfers a given number of unsigned bytes from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWritePortBufferUlong](nf-srb-scsiportwriteportbufferulong.md) | The ScsiPortWritePortBufferUlong routine transfers a given number of ULONG values from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWritePortBufferUshort](nf-srb-scsiportwriteportbufferushort.md) | The ScsiPortWritePortBufferUshort routine transfers a given number of USHORT values from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWritePortUchar](nf-srb-scsiportwriteportuchar.md) | The ScsiPortWritePortUchar routine transfers an unsigned byte to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWritePortUlong](nf-srb-scsiportwriteportulong.md) | The ScsiPortWritePortUlong routine transfers a ULONG value to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWritePortUshort](nf-srb-scsiportwriteportushort.md) | The ScsiPortWritePortUshort routine transfers a USHORT value to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWriteRegisterBufferUchar](nf-srb-scsiportwriteregisterbufferuchar.md) | The ScsiPortWriteRegisterBufferUchar routine transfers a given number of unsigned bytes from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWriteRegisterBufferUlong](nf-srb-scsiportwriteregisterbufferulong.md) | The ScsiPortWriteRegisterBufferUlong routine transfers a given number of ULONG values from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWriteRegisterBufferUshort](nf-srb-scsiportwriteregisterbufferushort.md) | The ScsiPortWriteRegisterBufferUshort routine transfers a given number of USHORT values from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWriteRegisterUchar](nf-srb-scsiportwriteregisteruchar.md) | The ScsiPortWriteRegisterUchar routine transfers a unsigned byte value to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWriteRegisterUlong](nf-srb-scsiportwriteregisterulong.md) | The ScsiPortWriteRegisterUlong routine transfers a ULONG value to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWriteRegisterUshort](nf-srb-scsiportwriteregisterushort.md) | The ScsiPortWriteRegisterUshort routine transfers a USHORT value to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |



## Structures
| Title | Description |
| ---- |:---- |
| [_ACCESS_RANGE](ns-srb-_access_range.md) | An ACCESS_RANGE describes a memory or I/O port range used by an HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [_HW_INITIALIZATION_DATA](ns-srb-_hw_initialization_data.md) | Each SCSI miniport driver's DriverEntry routine must initialize with zeros and, then, fill in the relevant HW_INITIALIZATION_DATA (SCSI) information for the OS-specific port driver.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [_PORT_CONFIGURATION_INFORMATION](ns-srb-_port_configuration_information.md) | PORT_CONFIGURATION_INFORMATION (SCSI) contains configuration information for an HBA. |
| [_SCSI_REQUEST_BLOCK](ns-srb-_scsi_request_block.md) | SCSI_REQUEST_BLOCK structure |
| [_SCSI_WMI_REQUEST_BLOCK](ns-srb-_scsi_wmi_request_block.md) | This structure is a special version of a SCSI_REQUEST_BLOCK for use with WMI commands. |
| [_SRBEX_DATA](ns-srb-_srbex_data.md) | The SRBEX_DATA structure is the generalized format for containing extended SRB data. |
| [_SRBEX_DATA_BIDIRECTIONAL](ns-srb-_srbex_data_bidirectional.md) | The SRBEX_DATA_BIDIRECTIONAL structure contains the extended SRB data for bi-directional transfer commands. |
| [_SRBEX_DATA_IO_INFO](ns-srb-_srbex_data_io_info.md) | The SRBEX_DATA_IO_INFO structure contains additional information related to a read or write request in an extended SRB. |
| [_SRBEX_DATA_PNP](ns-srb-_srbex_data_pnp.md) | The SRBEX_DATA_PNP structure contains the request data for an extended plug and play (PNP) SRB. |
| [_SRBEX_DATA_POWER](ns-srb-_srbex_data_power.md) | The SRBEX_DATA_POWER structure contains the request data for an extended power SRB. |
| [_SRBEX_DATA_SCSI_CDB_VAR](ns-srb-_srbex_data_scsi_cdb_var.md) | The SRBEX_DATA_SCSI_CDB_VAR structure contains the extended SRB data for a variable length SCSI command data block (CDB). |
| [_SRBEX_DATA_SCSI_CDB16](ns-srb-_srbex_data_scsi_cdb16.md) | The SRBEX_DATA_SCSI_CDB16 structure contains the extended SRB data for a 16-byte SCSI command data block (CDB). |
| [_SRBEX_DATA_SCSI_CDB32](ns-srb-_srbex_data_scsi_cdb32.md) | The SRBEX_DATA_SCSI_CDB32 structure contains the extended SRB data for a 32-byte SCSI command data block (CDB). |
| [_SRBEX_DATA_WMI](ns-srb-_srbex_data_wmi.md) | The SRBEX_DATA_WMI structure contains the request data for an extended WMI SRB. |
| [_STORAGE_REQUEST_BLOCK](ns-srb-_storage_request_block.md) | The STORAGE_REQUEST_BLOCK is the extended format SCSI Request Block (SRB) structure. |