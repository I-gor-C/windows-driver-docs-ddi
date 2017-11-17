# Declarations in the srb header
This header Srb contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [ScsiPortWriteRegisterUchar function](nf-srb-scsiportwriteregisteruchar.md) | The ScsiPortWriteRegisterUchar routine transfers a unsigned byte value to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWriteRegisterBufferUlong function](nf-srb-scsiportwriteregisterbufferulong.md) | The ScsiPortWriteRegisterBufferUlong routine transfers a given number of ULONG values from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortFreeDeviceBase function](nf-srb-scsiportfreedevicebase.md) | The ScsiPortFreeDeviceBase routine frees a range of device I/O or memory space addresses previously mapped into the system address space with ScsiPortGetDeviceBase.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [ScsiPortWritePortBufferUchar function](nf-srb-scsiportwriteportbufferuchar.md) | The ScsiPortWritePortBufferUchar routine transfers a given number of unsigned bytes from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWritePortUlong function](nf-srb-scsiportwriteportulong.md) | The ScsiPortWritePortUlong routine transfers a ULONG value to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortUshort function](nf-srb-scsiportreadportushort.md) | The ScsiPortReadPortUshort routine reads a USHORT value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortConvertPhysicalAddressToUlong function](nf-srb-scsiportconvertphysicaladdresstoulong.md) | The ScsiPortConvertPhysicalAddressToUlong routine truncates a SCSI_PHYSICAL_ADDRESS to a ULONG.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortCompleteRequest function](nf-srb-scsiportcompleterequest.md) | The ScsiPortCompleteRequest routine completes all of the active requests for the given SCSI bus, controller, or LU, including a request being processed by the calling miniport driver routine.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [ScsiPortValidateRange function](nf-srb-scsiportvalidaterange.md) | The ScsiPortValidateRange routine indicates whether the specified access range values have already been claimed in the registry by another driver.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWriteRegisterUlong function](nf-srb-scsiportwriteregisterulong.md) | The ScsiPortWriteRegisterUlong routine transfers a ULONG value to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [SRB_STATUS function](nf-srb-srb-status.md) | TBD |
| [ScsiPortReadRegisterUlong function](nf-srb-scsiportreadregisterulong.md) | The ScsiPortReadRegisterUlong routine reads a ULONG value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortLogError function](nf-srb-scsiportlogerror.md) | The ScsiPortLogError routine logs errors to the system event log when a miniport driver or its HBA detects a SCSI error condition.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [SCSI_DECODE_BUS_TARGET function](nf-srb-scsi-decode-bus-target.md) | TBD |
| [ScsiPortGetUncachedExtension function](nf-srb-scsiportgetuncachedextension.md) | The ScsiPortGetUncachedExtension routine allocates memory that can be used by both the CPU and a bus-master HBA for DMA or for shared data.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWriteRegisterBufferUshort function](nf-srb-scsiportwriteregisterbufferushort.md) | The ScsiPortWriteRegisterBufferUshort routine transfers a given number of USHORT values from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiDebugPrint function](nf-srb-scsidebugprint.md) | The ScsiDebugPrint routine prints debug information with a level of verbosity based on global values set in the kernel debugger or set in the registry and initialized when the system boots. |
| [ScsiPortReadRegisterUchar function](nf-srb-scsiportreadregisteruchar.md) | The ScsiPortReadRegisterUchar routine reads an unsigned byte value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortConvertPhysicalAddressToULongPtr function](nf-srb-scsiportconvertphysicaladdresstoulongptr.md) | TBD |
| [ScsiPortReadRegisterBufferUshort function](nf-srb-scsiportreadregisterbufferushort.md) | The ScsiPortReadRegisterBufferUshort routine transfers a specified number of USHORT values from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortConvertPhysicalAddressToUlong function](nf-srb-scsiportconvertphysicaladdresstoulong~r1.md) | The ScsiPortConvertPhysicalAddressToUlong routine truncates a SCSI_PHYSICAL_ADDRESS to a ULONG.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortFlushDma function](nf-srb-scsiportflushdma.md) | The ScsiPortFlushDma routine flushes any data cached in the system DMA controller at the end of a transfer or terminates a system DMA transfer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortInitialize function](nf-srb-scsiportinitialize.md) | For a non-Plug and Play miniport driver, the ScsiPortInitialize routine sets up the PORT_CONFIGURATION_INFORMATION structure and calls the miniport driver's HwScsiFindAdapter routine. |
| [ScsiPortWriteRegisterBufferUchar function](nf-srb-scsiportwriteregisterbufferuchar.md) | The ScsiPortWriteRegisterBufferUchar routine transfers a given number of unsigned bytes from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWritePortBufferUshort function](nf-srb-scsiportwriteportbufferushort.md) | The ScsiPortWritePortBufferUshort routine transfers a given number of USHORT values from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortGetLogicalUnit function](nf-srb-scsiportgetlogicalunit.md) | The ScsiPortGetLogicalUnit routine returns a pointer to the miniport driver's per-LU storage area for a given peripheral.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortBufferUlong function](nf-srb-scsiportreadportbufferulong.md) | The ScsiPortReadPortBufferUlong routine transfers a given number of ULONG values from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortGetDeviceBase function](nf-srb-scsiportgetdevicebase.md) | The ScsiPortGetDeviceBase routine returns a mapped, logical base address that can be used to communicate with an HBA. |
| [ScsiPortWritePortUchar function](nf-srb-scsiportwriteportuchar.md) | The ScsiPortWritePortUchar routine transfers an unsigned byte to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortNotification function](nf-srb-scsiportnotification.md) | The ScsiPortNotification routine informs the operating system-specific port driver of certain events, such as when a miniport driver completes a request or is ready to start another SRB, as well as when the HBA indicates certain SCSI error conditions that occurred during an operation.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [ScsiPortMoveMemory function](nf-srb-scsiportmovememory.md) | The ScsiPortMoveMemory routine copies data from one location to another.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortUchar function](nf-srb-scsiportreadportuchar.md) | The ScsiPortReadPortUchar routine reads an unsigned byte value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortStallExecution function](nf-srb-scsiportstallexecution.md) | The ScsiPortStallExecution routine stalls in the miniport driver.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadRegisterBufferUchar function](nf-srb-scsiportreadregisterbufferuchar.md) | The ScsiPortReadRegisterBufferUchar routine transfers a specified number of unsigned bytes from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortBufferUshort function](nf-srb-scsiportreadportbufferushort.md) | The ScsiPortReadPortBufferUshort routine transfers a given number of USHORT values from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWritePortBufferUlong function](nf-srb-scsiportwriteportbufferulong.md) | The ScsiPortWritePortBufferUlong routine transfers a given number of ULONG values from a buffer to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortSetBusDataByOffset function](nf-srb-scsiportsetbusdatabyoffset.md) | The ScsiPortSetBusDataByOffset routine sets bus-configuration data for an adapter on a dynamically configurable I/O bus with a published, standard interface. |
| [ScsiPortWritePortUshort function](nf-srb-scsiportwriteportushort.md) | The ScsiPortWritePortUshort routine transfers a USHORT value to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [DebugPrint function](nf-srb-debugprint.md) | TBD |
| [ScsiPortGetSrb function](nf-srb-scsiportgetsrb.md) | The ScsiPortGetSrb routine returns a pointer to an active SCSI request for a particular logical unit.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadPortBufferUchar function](nf-srb-scsiportreadportbufferuchar.md) | The ScsiPortReadPortBufferUchar routine transfers a given number of unsigned byte values from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadRegisterBufferUlong function](nf-srb-scsiportreadregisterbufferulong.md) | The ScsiPortReadRegisterBufferUlong routine transfers a specified number of ULONG values from the HBA to a buffer.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortGetBusData function](nf-srb-scsiportgetbusdata.md) | The ScsiPortGetBusData routine returns bus-type-specific configuration information that a miniport driver's HwScsiFindAdapter routine might use to determine whether it supports a particular adapter on a particular I/O bus, and to configure the HBA if it does.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [ScsiPortReadPortUlong function](nf-srb-scsiportreadportulong.md) | The ScsiPortReadPortUlong routine reads a ULONG value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortGetPhysicalAddress function](nf-srb-scsiportgetphysicaladdress.md) | The ScsiPortGetPhysicalAddress routine converts a given virtual address range to a physical address range for a DMA operation.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortReadRegisterUshort function](nf-srb-scsiportreadregisterushort.md) | The ScsiPortReadRegisterUshort routine reads a USHORT value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWriteRegisterUshort function](nf-srb-scsiportwriteregisterushort.md) | The ScsiPortWriteRegisterUshort routine transfers a USHORT value to the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortIoMapTransfer function](nf-srb-scsiportiomaptransfer.md) | The ScsiPortIoMapTransfer routine sets up the system DMA controller for a miniport driver to transfer data through a subordinate HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortQuerySystemTime function](nf-srb-scsiportquerysystemtime.md) | The ScsiPortQuerySystemTime routine obtains the current system time.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [SCSI_COMBINE_BUS_TARGET function](nf-srb-scsi-combine-bus-target.md) | TBD |
| [ScsiPortConvertUlongToPhysicalAddress function](nf-srb-scsiportconvertulongtophysicaladdress.md) | The ScsiPortConvertUlongToPhysicalAddress routine extends a given ULONG address into a value of type SCSI_PHYSICAL_ADDRESS.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortGetVirtualAddress function](nf-srb-scsiportgetvirtualaddress.md) | The ScsiPortGetVirtualAddress routine returns a virtual address associated with a physical address if the physical address was obtained by a call to ScsiPortGetPhysicalAddress.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SCSI_PNP_REQUEST_BLOCK structure](ns-srb--scsi-pnp-request-block.md) | TBD |
| [SRBEX_DATA_SCSI_CDB_VAR structure](ns-srb--srbex-data-scsi-cdb-var.md) | The SRBEX_DATA_SCSI_CDB_VAR structure contains the extended SRB data for a variable length SCSI command data block (CDB). |
| [SRBEX_DATA_BIDIRECTIONAL structure](ns-srb--srbex-data-bidirectional.md) | The SRBEX_DATA_BIDIRECTIONAL structure contains the extended SRB data for bi-directional transfer commands. |
| [SRBEX_DATA_PNP structure](ns-srb--srbex-data-pnp.md) | The SRBEX_DATA_PNP structure contains the request data for an extended plug and play (PNP) SRB. |
| [SRBEX_DATA_POWER structure](ns-srb--srbex-data-power.md) | The SRBEX_DATA_POWER structure contains the request data for an extended power SRB. |
| [SCSI_SUPPORTED_CONTROL_TYPE_LIST structure](ns-srb--scsi-supported-control-type-list.md) | TBD |
| [SRBEX_DATA_SCSI_CDB32 structure](ns-srb--srbex-data-scsi-cdb32.md) | The SRBEX_DATA_SCSI_CDB32 structure contains the extended SRB data for a 32-byte SCSI command data block (CDB). |
| [SRBEX_DATA structure](ns-srb--srbex-data.md) | The SRBEX_DATA structure is the generalized format for containing extended SRB data. |
| [SRBEX_DATA_SCSI_CDB16 structure](ns-srb--srbex-data-scsi-cdb16.md) | The SRBEX_DATA_SCSI_CDB16 structure contains the extended SRB data for a 16-byte SCSI command data block (CDB). |
| [SRBEX_DATA_WMI structure](ns-srb--srbex-data-wmi.md) | The SRBEX_DATA_WMI structure contains the request data for an extended WMI SRB. |
| [HW_INITIALIZATION_DATA structure](ns-srb--hw-initialization-data.md) | TBD |
| [PORT_CONFIGURATION_INFORMATION structure](ns-srb--port-configuration-information.md) | TBD |
| [SCSI_POWER_REQUEST_BLOCK structure](ns-srb--scsi-power-request-block.md) | TBD |
| [STORAGE_REQUEST_BLOCK structure](ns-srb--storage-request-block.md) | The STORAGE_REQUEST_BLOCK is the extended format SCSI Request Block (SRB) structure. |
| [SCSI_WMI_REQUEST_BLOCK structure](ns-srb--scsi-wmi-request-block.md) | This structure is a special version of a SCSI_REQUEST_BLOCK for use with WMI commands. |
| [SRBEX_DATA_IO_INFO structure](ns-srb--srbex-data-io-info.md) | The SRBEX_DATA_IO_INFO structure contains additional information related to a read or write request in an extended SRB. |
| [STOR_DEVICE_CAPABILITIES_EX structure](ns-srb--stor-device-capabilities-ex.md) | TBD |
| [ACCESS_RANGE structure](ns-srb--access-range.md) | An ACCESS_RANGE describes a memory or I/O port range used by an HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [STORAGE_REQUEST_BLOCK_HEADER structure](ns-srb--storage-request-block-header.md) | TBD |
| [SCSI_REQUEST_BLOCK structure](ns-srb--scsi-request-block.md) | SCSI_REQUEST_BLOCK structure |
| [STOR_DEVICE_CAPABILITIES structure](ns-srb--stor-device-capabilities.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PHW_ADAPTER_CONTROL callback function](nc-srb-phw-adapter-control.md) | TBD |
| [PHW_TIMER callback function](nc-srb-phw-timer.md) | TBD |
| [PHW_FIND_ADAPTER callback function](nc-srb-phw-find-adapter.md) | TBD |
| [PHW_INITIALIZE callback function](nc-srb-phw-initialize.md) | TBD |
| [PHW_ADAPTER_STATE callback function](nc-srb-phw-adapter-state.md) | TBD |
| [PHW_DMA_STARTED callback function](nc-srb-phw-dma-started.md) | TBD |
| [PHW_RESET_BUS callback function](nc-srb-phw-reset-bus.md) | TBD |
| [PHW_INTERRUPT callback function](nc-srb-phw-interrupt.md) | TBD |
| [PHW_STARTIO callback function](nc-srb-phw-startio.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SCSI_NOTIFICATION_TYPE enumeration](ne-srb--scsi-notification-type.md) | TBD |
| [SRBEXDATATYPE enumeration](ne-srb--srbexdatatype.md) | TBD |
| [SCSI_ADAPTER_CONTROL_STATUS enumeration](ne-srb--scsi-adapter-control-status.md) | TBD |
| [PSTOR_PNP_ACTION enumeration](ne-srb-pstor-pnp-action.md) | TBD |
| [PSTOR_POWER_ACTION enumeration](ne-srb-pstor-power-action.md) | TBD |
| [SCSI_ADAPTER_CONTROL_TYPE enumeration](ne-srb--scsi-adapter-control-type.md) | TBD |
| [STOR_DEVICE_POWER_STATE enumeration](ne-srb--stor-device-power-state.md) | TBD |

This header is used in these topics:

- [Storage](..content/_Storage)
